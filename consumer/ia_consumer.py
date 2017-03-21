from .consumer import Consumer
import internetarchive as ia

class IAConsumer(Consumer):

    def __init__(self, transformer, writer, collection):
        #super().__init__(transformer, writer)
        self.collection = collection
        self.session = ia.get_session(config_file='ia.ini')
        self.item_ids = self._search()

    def process(self):
        pass

    def _load(self):
        pass

    def _get_items(self):
        pass

    def _search(self):
        query = "collection:{}".format(self.collection)
        result = ia.search_items(query, archive_session=self.session)

        items = []
        for item in result:
            items.append(item['identifier'])

        return items


