from .consumer import Consumer
import internetarchive as ia

class IAConsumer(Consumer):

    def __init__(self, transformer, writer, collection):
        #super().__init__(transformer, writer)
        self.collection = collection
        self.items = [
            "p1atguelphvol31uofg",
            "p2atguelphvol31uofg",
        ]

    def process(self):
        pass

    def _load(self):
        pass

    def _get_items(self):
        pass

    def _search(self):
        query = "collection:{}".format(self.collection)
        result = ia.search_items(query)


