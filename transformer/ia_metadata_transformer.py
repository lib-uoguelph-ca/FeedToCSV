from .metadata_transformer import MetadataTransformer

class IAMetadataTransformer(MetadataTransformer):
    def __init__(self):
        super().__init__()
        self.mapping = {
            'dc.title en': 'title',
            'dc.contributor': self._get_dc_contributor,
            'dc.contributor.affiliation': self._get_uofg,
            'dc.contributor.editor': self._get_empty,
            'dc.date.issued': 'date',
            'dc.date.copyright': 'date',
            'dc.description.abstract': self._get_empty,
            'dc.description.tableofcontents': self._get_empty,
            'dc.description': 'notes',
            'dc.language.iso': 'language',
            'dc.publisher': 'publisher',
            'dc.relation.ispartofseries': self._get_dc_relation_ispartofseries,
            'dc.rights': self._get_empty,
            'dc.rights.holder': self._get_uofg,
            'dc.rights.uri': self._get_empty,
            'dc.source': 'identifier-access',
            'dc.subject': self._get_dc_subject,
            'dc.type': self._get_dc_type,
            'files': self._get_files,
        }
    def _get_dc_contributor(self, row):
        return "Communications & Public Affairs"

    def _get_uofg(self, row):
        return "University of Guelph"

    def _get_dc_relation_ispartofseries(self, row):
        return "At Guelph; Volume {volume} Number {number}".format(volume=row['volume'], number=row['issue'])

    def _get_dc_subject(self, row):
        return ";".join(['At Guelph', 'Campus news'])

    def _get_dc_type(self, row):
        return "Newspaper"

    def _get_files(self, row):
        return ";".join(row['files'])