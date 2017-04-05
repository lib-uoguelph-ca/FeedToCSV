from consumer.ia_consumer import IAConsumer
from writer.csv_dict_writer import CSVDictWriter
from transformer.ia_metadata_transformer import IAMetadataTransformer
import logging

# Set up logging
logger = logging.getLogger('FeedToCSV')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
fh = logging.FileHandler('output/errors.log')
fh.setLevel(logging.ERROR)
logger.addHandler(fh)

writer = CSVDictWriter('output/ia-atguelph.csv')
transformer = IAMetadataTransformer()
consumer = IAConsumer(transformer=transformer, writer=writer, logger=logger, collection='atguelph')
consumer.process()