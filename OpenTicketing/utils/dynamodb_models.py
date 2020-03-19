# Copyright belong to Diego Navaro at https://gist.github.com/dnmellen/de4eb3ae72b3d60637ccabad77a1f964

"""
@python_2_unicode_compatible
class YourModel(DynamoDBMapperMixin, UUIDModel):

    DYNAMO_DB_TABLE = 'yourdynamotable'
    DYNAMO_DB_FIELDS = [
        'dynamo_field_1', 'dynamo_field2'
    ]
    
    # Your usual Django fields below...

How to use it
You need to create your DynamoDB tables first
Create your model using DynamoDBMapperMixin like in YourModel
No need to make any django migrations
Defined fields have autocompletion in manage.py shell
DYNAMO_DB_FIELDS will behave like a @property. You can do things like:
obj = YourModel()
obj.dynamo_field_1 = 50  # it stores Decimal(50) (nothing is saved to DynamoDB yet)
obj.dynamo_field_2 = "Hello world"
obj.dynamo_field_2  # Returns "Hello world", still not saved to DynamoDB
obj.save()  # All modifications in dynamo fields are actually performed
del obj.dynamo_field_2  # Deletes dynamo_field2 field in DynamoDB table
obj.save()
"""

import uuid
import boto3
from decimal import Decimal
from functools import partial
from django.db import models
from django.conf import settings


class UUIDModel(models.Model):
    """
    Basic abstract model for the rest of the models of the app
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["created_at"]


if not settings.AWS_DYNAMODB_REGION_NAME:
    dynamodb = None
elif settings.AWS_DYNAMODB_REGION_NAME == 'local':

    dynamodb = boto3.resource(
        'dynamodb',
        region_name='eu-west-1',
        aws_access_key_id='foo',
        aws_secret_access_key='bar',
        endpoint_url='http://{}:{}'.format(
            settings.LOCAL_DYNAMODB_HOST, settings.LOCAL_DYNAMODB_PORT
        )
    )
else:
    dynamodb = boto3.resource(
        'dynamodb',
        region_name=settings.AWS_DYNAMODB_REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )


class DynamoDBMapperMixin(object):
    """
    Mixin that maps a schema to DynamoDB
    """

    # This schema should be filled on the models using this mixin
    DYNAMO_DB_TABLE = None
    DYNAMO_DB_FIELDS = []

    def _get_dynamo_item(self, **kwargs):
        """
        Gets the item from DynamoDB
        Id in DynamoDB will be the same id as in Django model
        """
        try:
            self._cached_dynamodb_item = self._cached_dynamodb_item or self.dynamodb_table.get_item(Key={'id': str(self.id)}, **kwargs)['Item']
            return self._cached_dynamodb_item
        except KeyError:
            if self.dynamodb_table.put_item(Item={'id': str(self.id)}):
                return self._get_dynamo_item(**kwargs)

    def _get_dynamo_field_value(self, field):
        try:
            return self._get_dynamo_item()[field]
        except KeyError:
            return None

    def _update_dynamo_field_value(self, field, value):
        # Cast digits to Decimal
        if type(value) in (int, float):
            value = Decimal(value)

        self._dynamodb_update_actions[field] = {'Value': value, 'Action': 'PUT'}
        setattr(self, '_' + field, value)  # Sets a cached value for the current instance

    def _delete_dynamo_field_value(self, field):
        self._dynamodb_update_actions[field] = {'Action': 'DELETE'}
        setattr(self, '_' + field, None)  # Sets a cached value for the current instance

    def clear_dynamodb_local_cache(self):
        for field in self.DYNAMO_DB_FIELDS:
            if hasattr(self, '_' + field):
                delattr(self, '_' + field)
        self._dynamodb_update_actions = {}
        self._cached_dynamodb_item = {}

    def __getattr__(self, name):
        if name in self.DYNAMO_DB_FIELDS:
            if hasattr(self, '_' + name):
                return getattr(self, '_' + name)
            else:
                return self._dynamodb_getters[name]()
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        if name in self.DYNAMO_DB_FIELDS:
            return self._dynamodb_setters[name](value=value)
        else:
            return super(DynamoDBMapperMixin, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name in self.DYNAMO_DB_FIELDS:
            return self._dynamodb_deleters[name]()
        else:
            return super(DynamoDBMapperMixin, self).__delattr__(name)
    
    def __dir__(self):
        """
        Overrides __dir__ for autocompletion!
        """
        return super(DynamoDBMapperMixin, self).__dir__() + self.DYNAMO_DB_FIELDS

    def __init__(self, *args, **kwargs):
        # Get DynamoDB table instance
        self.dynamodb_table = dynamodb.Table(self.DYNAMO_DB_TABLE)

        # Cached dynamodb item
        self._cached_dynamodb_item = {}

        # Update actions storage: Actions will be performed on save() call
        self._dynamodb_update_actions = {}

        # Store getters & setters
        self._dynamodb_getters = {}
        self._dynamodb_setters = {}
        self._dynamodb_deleters = {}

        # Create getters & setters for Dynamo DB fields
        for field in self.DYNAMO_DB_FIELDS:
            self._dynamodb_getters[field] = partial(self._get_dynamo_field_value, field=field)
            self._dynamodb_setters[field] = partial(self._update_dynamo_field_value, field=field)
            self._dynamodb_deleters[field] = partial(self._delete_dynamo_field_value, field=field)

        return super(DynamoDBMapperMixin, self).__init__(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.dynamodb_table.delete_item(Key={'id': str(self.id)})
        return super(DynamoDBMapperMixin, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(DynamoDBMapperMixin, self).save(*args, **kwargs)

        # Perform update item in dynamodb if needed
        if self._dynamodb_update_actions:
            self.dynamodb_table.update_item(
                Key={'id': str(self.id)},
                AttributeUpdates=self._dynamodb_update_actions,
            )
            self.clear_dynamodb_local_cache()


