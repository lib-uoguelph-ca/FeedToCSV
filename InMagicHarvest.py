from consumer.inmagic_consumer import InmagicConsumer
from writer.csv_dict_writer import CSVDictWriter
from transformer.inmagic_metadata_transformer import InmagicMetadataTransformer
import logging

logger = logging.getLogger('FeedToCSV')
#logger.addHandler(logging.FileHandler('output/FeedToCSV.log'))
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

writer = CSVDictWriter('output/inmagic-atguelph.csv')
transformer = InmagicMetadataTransformer()
consumer = InmagicConsumer(transformer=transformer, writer=writer, logger=logger, input_file_path="input/AtGuelph-Inmagic.xml")
consumer.process()