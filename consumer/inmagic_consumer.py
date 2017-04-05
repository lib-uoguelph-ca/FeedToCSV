from .consumer import Consumer

from shutil import copyfile
import xml.etree.ElementTree as ET
import re, os

class InmagicConsumer(Consumer):

    def __init__(self, transformer, writer, logger, input_file_path, num_threads=4, output_dir="output", file_base_path="/Volumes/CPAarchive/PDF"):
        self.transformer = transformer
        self.writer = writer
        self.logger = logger
        self.input_file_path = input_file_path
        self.num_threads = num_threads
        self.output_dir = output_dir
        self.root = self._load_xml_file()
        self.namespaces = {'inm': 'http://www.inmagic.com/webpublisher/query'}
        self.file_base_path = file_base_path

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
            self._download_file(transformed)

    """
    Given a inm:Record node, build a dict with the metadata. 
    """
    def _get_item_metadata(self, node):
        item = {}
        for child in node:
            tag = re.sub(r"{.*}", "", child.tag)
            item[tag] = child.text

        return item

    """
    Download the file and store it in the output directory.
    """
    def _download_file(self, item):
        self._create_output_dirs(item)
        self._copy_file(item)

    """
    Create the directory structure required for the file in the output directory
    """
    def _create_output_dirs(self, item):
        file_path = item['files']
        dir_path = os.path.dirname(file_path)
        print(dir_path)

        output_dir_path = self.output_dir + os.sep + dir_path
        if dir_path and not os.path.isdir(output_dir_path):
            os.makedirs(output_dir_path)

    """
    If the file doesn't exist already, copy the file to the output folder.
    """
    def _copy_file(self, item):
        out_file_path = self.output_dir + os.sep + item['files']
        in_file_path = self.file_base_path + os.sep + item['files']

        if os.path.exists(out_file_path):
            return

        try:
            copyfile(in_file_path, out_file_path)
        except FileNotFoundError as e:
            message = "Error: Couldn't copy {file}: File not found".format(file=item['files'])
            self.logger.error(message)
