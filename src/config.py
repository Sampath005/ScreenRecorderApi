# /src/config.py
import json
import os
from dotenv import load_dotenv, find_dotenv
import boto3
from botocore.exceptions import ClientError

load_dotenv(find_dotenv())


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class Testing(object):
    """
    Development environment configuration
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Retrieving SecretKey and EmailPassword
# DEV = Development()

app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}

