from .metadata_transformer import MetadataTransformer

class IAOACReviewTransformer(MetadataTransformer):
    def __init__(self):
        super().__init__()
        self.mapping = {
            'dc.title': 'title',
            'dc.creator': 'creator',
            'dc.format': self._get_pdf_format,
            'dc.contributor': self._get_contributor,
            'dc.contributor.affiliation': self._get_contributor_affiliation,
            'dc.contributor.editor': 'editor',
            'dc.date.issued': 'date',
            'dc.date.copyright': 'year',
            'dc.description.abstract': 'description',
            'dc.description.tableofcontents': 'description_tableofcontents',
            'dc.language.iso': 'language',
            'dc.publisher': 'publisher',
            'dc.relation.ispartofseries': 'series',
            'dc.rights': self._get_empty,
            'dc.rights.holder': 'rights',
            'dc.rights.uri': 'licensurl',
            'dc.subject': self._get_subjects,
            'dc.type': 'type',
            'files': self._get_files,
        }

    def get_pdf_format(self, row):
        return "pdf"

    def _get_contributor(self, row):
        values = row['contributor'].split(',')
        return values[0]

    def _get_contributor_affiliation(self, row):
        values = row['contributor'].split(',')
        return values[1]

    def _get_uofg(self, row):
        return "University of Guelph"

    def _get_files(self, row):
        return ";".join(row['files'])

    def _get_subjects(self, row):
        return ";".join(row['subject'])