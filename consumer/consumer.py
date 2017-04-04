class Consumer:
    def __init__(self, transformer, writer, logger, output_dir="output"):
        self.transformer = transformer
        self.writer = writer
        self.logger = logger

    def process(self):
        raise NotImplementedError