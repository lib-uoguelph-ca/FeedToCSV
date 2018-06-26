from .metadata_transformer import MetadataTransformer

class IAOACReviewTransformer(MetadataTransformer):
    def __init__(self):
        super().__init__()
        self.mapping = {
            'dc.title en': 'title',
            'dc.contributor': 'contributor',
            'dc.contributor.affiliation': self._get_uofg,
            'dc.contributor.editor': self._get_empty,
            'dc.date.issued': 'date',
            'dc.date.copyright': 'date',
            'dc.description.abstract': 'description',
            'dc.description.tableofcontents': 'description_tableofcontents',
            'dc.language.iso': 'language',
            'dc.publisher': 'publisher',
            'dc.relation.ispartofseries': 'series',
            'dc.rights.holder': self._get_uofg,
            'dc.rights.uri': 'licensurl',
            'dc.source': 'identifier-access',
            'dc.subject': self._get_subjects,
            'dc.type': 'type',
            'files': self._get_files,
        }

    def _get_uofg(self, row):
        return "University of Guelph"

    def _get_files(self, row):
        return ";".join(row['files'])

    def _get_subjects(self, row):
        return ";".join(row['subject'])