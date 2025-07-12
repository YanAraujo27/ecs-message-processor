import json
from services.processor import MessageProcessor

def handler(event, context=None):
    table_name = "tabela-final"
    processor = MessageProcessor(table_name)
    messages = [json.loads(record["body"]) for record in event["Records"]]
    processor.process_batch(messages)
