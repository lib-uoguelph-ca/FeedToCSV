from consumer.ia_consumer import IAConsumer
from writer.csv_dict_writer import CSVDictWriter
from transformer.ia_metadata_transformer import IAMetadataTransformer
import logging

logger = logging.getLogger('FeedToCSV')
logger.addHandler(logging.FileHandler('output/FeedToCSV.log'))
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

writer = CSVDictWriter('output/ia-atguelph.csv')
transformer = IAMetadataTransformer()
consumer = IAConsumer(transformer=transformer, writer=writer, logger=logger, collection='atguelph')
consumer.process()