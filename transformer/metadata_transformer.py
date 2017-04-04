from typing import Iterable, Any, Mapping

class MetadataTransformer:
    def __init__(self):
        self.mapping = {}

    def transform(self, data):

        try:
            result = []

            for row in data:
                result.append(self._transform_row(row))

        except TypeError:
            result = self._transform_row(data)

        return result

    def _transform_row(self, row):
        result = {}

        for key in self.mapping:
            if callable(self.mapping[key]):
                result[key] = self.mapping[key](row)
            elif isinstance(self.mapping[key], str):
                result[key] = row[self.mapping[key]]
            else:
                raise KeyError("Metadata Transformer: Invalid mapping")

        return result

    def _get_empty(self, row):
        return ""

    def _get_files(self, row):
        return ";".join(row['files'])