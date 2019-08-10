import os


def set_env(key_path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path


def get_firestore_client(key_path):
    from google.cloud import firestore
    set_env(key_path)
    db = firestore.Client()
    return db


def get_vision_client(key_path):
    from google.cloud import vision
    set_env(key_path)
    client = vision.ImageAnnotatorClient()
    return client
