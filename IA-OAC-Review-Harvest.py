from consumer.ia_consumer import IAConsumer
from writer.csv_dict_writer import CSVDictWriter
from transformer.ia_oacreview_transformer import IAOACReviewTransformer
import logging

# Set up logging
logger = logging.getLogger('FeedToCSV')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
fh = logging.FileHandler('output/errors.log')
fh.setLevel(logging.ERROR)
logger.addHandler(fh)

writer = CSVDictWriter('output/harvest.csv')
transformer = IAOACReviewTransformer()
consumer = IAConsumer(transformer=transformer, writer=writer, logger=logger, collection='oac_review', num_threads=6)
consumer.process()