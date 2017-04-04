from .metadata_transformer import MetadataTransformer
import os, re

class InmagicMetadataTransformer(MetadataTransformer):
    def __init__(self):
        super().__init__()
        self.mapping = {
            'dc.title en': 'Title-of-Document',
            'dc.contributor': self._get_dc_contributor,
            'dc.contributor.affiliation': self._get_uofg,
            'dc.contributor.editor': self._get_empty,
            'dc.date.issued': 'Date-of-Document',
            'dc.date.copyright': 'Date-of-Document',
            'dc.description.abstract': self._get_empty,
            'dc.description.tableofcontents': self._get_empty,
            'dc.description': self._get_empty,
            'dc.language.iso': self._get_dc_language,
            'dc.publisher': self._get_uofg,
            'dc.relation.ispartofseries': self._get_empty,
            'dc.rights': self._get_empty,
            'dc.rights.holder': self._get_uofg,
            'dc.rights.uri': self._get_empty,
            'dc.source': self._get_empty,
            'dc.subject': self._get_dc_subject,
            'dc.type': self._get_dc_type,
            'files': self._get_files,
        }

    def _get_dc_contributor(self, row):
        return "Communications & Public Affairs"

    def _get_uofg(self, row):
        return "University of Guelph"

    def _get_dc_subject(self, row):
        return ";".join(['At Guelph', 'Campus news'])

    def _get_dc_type(self, row):
        return "Newspaper"

    def _get_dc_language(self, row):
        return "en"

    def _get_files(self, row):
        value = row['PDF-of-Document']
        value = re.sub(r'\\', os.sep, value)
        return value