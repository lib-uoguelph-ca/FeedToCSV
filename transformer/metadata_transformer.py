from typing import Iterable, Any, Mapping

class MetadataTransformer:
    def __init__(self):
        self.mapping = {}

    def transform(self, data: Iterable[ Mapping[str, Any] ]):
        for row in data:
            self._transform_row(row)

    def _transform_row(self, row):
        result = {}

        for key in self.mapping():
            if callable(self.mapping[key]):
                result[key] = self.mapping[key](row)
            elif isinstance(self.mapping[key], str):
                result[key] = row[self.mapping[key]]
            else:
                raise KeyError("Metadata Transformer: Invalid mapping")

        return result