from . import Consumer
class IAConsumer(Consumer):
    def __init__(self, transformer, writer, collection):
        super().__init__(transformer, writer)
        self.collection = collection

    def process(self):
        pass