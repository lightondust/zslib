import os
from google.cloud import firestore


def set_env(key_path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path


class BaseDatabase(object):

    def __init__(self, key_path):
        self.key_path = key_path
        self.db = self.get_client()

        self.res_cursor = None

    def get_client(self):
        set_env(self.key_path)
        db = firestore.Client()
        return db

    def read_from_cursor(self, record_no):
        res = self.iter_n_items(self.res_cursor, record_no)
        return [r.to_dict() for r in res]

    def read_data(self, collection, document):
        ref = self.db.collection(collection).document(document)
        return ref.get().to_dict()

    def read_from_collection(self, collection, read_no=10, if_read=True):
        self.res_cursor = self.db.collection(collection).stream()
        if if_read:
            return self.read_from_cursor(read_no)

    def create_document(self, collection, document, data):
        doc_ref = self.db.collection(collection).document(document)
        doc_ref.set(data)

    def delete_document(self, collection, document):
        self.db.collection(collection).document(document).delete()

    def update_data(self, collection, document, key, val):
        query = self.db.collection(collection).document(document)
        query.update({key: val})

    @staticmethod
    def iter_n_items(iterator, n):
        """
        :param iterator: iterator, for list use iterator = iter(lst); res = iter_n_items(iterator)
        :param n:
        :return:
        """
        res = []
        count = 0
        for i in iterator:
            count += 1
            if count > n:
                break
            res.append(i)
        return res


class Database(BaseDatabase):

    def __init__(self, key_path):
        super().__init__(key_path=key_path)


def get_vision_client(key_path):
    from google.cloud import vision
    set_env(key_path)
    client = vision.ImageAnnotatorClient()
    return client
