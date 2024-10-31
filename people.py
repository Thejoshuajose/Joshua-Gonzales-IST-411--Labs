MONGO_DBNAME = 'dbGonzales'
ITEM_METHODS = ['GET','PATCH','PUT','DELETE']
RESOURCE_METHODS = ['GET','POST','DELETE']
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'
STRICT_JSON = True


schema = {
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
    },
    'role': {
        'type': 'list',
        'allowed': ["author", "contributor", "copy"],
    },
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        },
    },
    'born': {
        'type': 'datetime',
    },
}

people = {

    'item_title': 'person',

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },

    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': schema
}

DOMAIN = {
    'people': people,
    'log': {
        'schema': {
            'activity_id': {
                'type': 'string',
                'required': True
            },
            'activity_description': {
                'type': 'string',
                'minlength': 10,
                'maxlength': 200,
                'required': True
            },
            'date': {
                'type': 'string',
                'required': True
            },
            'time': {
                'type': 'string',
                'required': True
            }
        }
    }
}
