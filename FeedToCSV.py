from consumer.ia_consumer import IAConsumer
from writer.csv_dict_writer import CSVDictWriter
from transformer.ia_metadata_transformer import IAMetadataTransformer

writer = CSVDictWriter('output/ia-atguelph.csv')
transformer = IAMetadataTransformer()
consumer = IAConsumer(transformer=transformer, writer=writer, collection='atguelph')

