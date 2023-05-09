class BasicConfig:
    USER_DB = 'postgres'
    PASS_DB = 'Castillo105.dct'
    URL_DB = 'localhost'
    NAME_DB = 'panaderia'
    FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI = FULL_URL_DB
    DEBUG = True
    SECRET_KEY = "secretKey19"
    BCRYPT_LOG_ROUNDS = 13