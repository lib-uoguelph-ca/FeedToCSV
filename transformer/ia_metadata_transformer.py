from .metadata_transformer import MetadataTransformer

class IAMetadataTransformer(MetadataTransformer):
    def __init__(self):
        super().__init__()
        self.mapping = {}
