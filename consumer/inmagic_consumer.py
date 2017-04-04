from .consumer import Consumer

import xml.etree.ElementTree as ET
import re

class InmagicConsumer(Consumer):

    def __init__(self, transformer, writer, logger, input_file_path, num_threads=4, output_dir="inmagic-output"):
        self.transformer = transformer
        self.writer = writer
        self.logger = logger
        self.input_file_path = input_file_path
        self.num_threads = num_threads
        self.output_dir = output_dir
        self.root = self._load_xml_file()
        self.namespaces = {'inm': 'http://www.inmagic.com/webpublisher/query'}

    def _load_xml_file(self):
        return ET.parse(self.input_file_path).getroot()

    """ 
    Iterate through the items,
      * Build the metadata
      * Write metadata to an output file
      * Dowload the files associated with each item.
    """
    def process(self):
        items = self.root.findall('.//inm:Record', self.namespaces)
        for node in items:
            item = self._get_item_metadata(node)

            transformed = self.transformer.transform(item)
            self.writer.write(transformed)
            #self.download_files(item)

    def _get_item_metadata(self, node):
        item = {}
        for child in node:
            tag = re.sub(r"{.*}", "", child.tag)
            item[tag] = child.text

        return item
