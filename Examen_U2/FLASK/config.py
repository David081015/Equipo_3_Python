class BasicConfig:
    USER_DB = 'postgres'
    PASS_DB = 'Castillo105.dct'
    URL_DB = 'localhost'
    NAME_DB = 'flask_eu2'
    FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI = FULL_URL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "llave_secreta"