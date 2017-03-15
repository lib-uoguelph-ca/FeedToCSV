class Consumer:
    def __init__(self, transformer, writer):
        self.transformer = transformer
        self.writer = writer

    def process(self):
        raise NotImplementedError