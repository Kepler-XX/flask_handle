class Config(object):

    DEBUG = False

    MYSQL_FOR_DB = {
        "DATABASE_HOST": "106.14.206.19",
        "DATABASE_PORT": 3306,
        "DATABASE_USER": "root",
        "DATABASE_PASSWORD": "123456",
        "DATABASE_DB": "kepler",
        "DATABASE_CHARSET": "utf8"
    }

    ES_FOR_SEARCH = {
        "ES_HOST": "",
        "ES_PORT": 9200,
        "ES_INDEX": "",
        "ES_TYPE": ""
    }

    REDIS_FOR_CACHE = {
        "REDIS_HOST": "",
        "REDIS_PORT": 6379,
        "REDIS_DB": 8,
        "REDIS_PASSWORD": ""
    }

    MONGO_FOR_DB = {
        "MONGO_HOST": "",
        "MONGO_PORT": 19060,
        "MONGO_DB": "",
    }


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


configs = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}


