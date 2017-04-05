from consumer.inmagic_consumer import InmagicConsumer
from writer.csv_dict_writer import CSVDictWriter
from transformer.inmagic_metadata_transformer import InmagicMetadataTransformer
import logging

# Set up logging
logger = logging.getLogger('FeedToCSV')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
fh = logging.FileHandler('output/errors.log')
fh.setLevel(logging.ERROR)
logger.addHandler(fh)

# Set up components
writer = CSVDictWriter('output/inmagic-atguelph.csv')
transformer = InmagicMetadataTransformer()
consumer = InmagicConsumer(transformer=transformer, writer=writer, logger=logger, input_file_path="input/AtGuelph-Inmagic.xml")
consumer.process()