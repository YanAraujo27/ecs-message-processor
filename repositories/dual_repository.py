import os
import time
import boto3
from botocore.exceptions import ClientError

class DualRepository:
    def __init__(self, table_name):
        self.use_dax = os.getenv("USE_DAX", "false").lower() == "true"
        self.table_name = table_name

        if self.use_dax:
            try:
                import amazondax
                self.client_dax = amazondax.AmazonDaxClient(endpoint_url=os.getenv("DAX_ENDPOINT"))
            except ImportError:
                self.client_dax = None

        self.client_dynamo = boto3.resource("dynamodb").Table(table_name)

    def put_item(self, item):
        if self.use_dax and self.client_dax:
            for attempt in range(2):
                try:
                    self.client_dax.put_item(TableName=self.table_name, Item=item)
                    return
                except Exception as e:
                    print(f"[DAX ERROR - Attempt {attempt+1}] {e}")
                    time.sleep(0.1)
        self.client_dynamo.put_item(Item=item)

    def get_by_id(self, id_val):
        return self.client_dynamo.get_item(Key={"id": id_val}).get("Item")

    def get_by_fechava_id(self, fechava_id):
        return self.client_dynamo.query(
            IndexName="fechava_id-index",
            KeyConditionExpression=Key("fechava.id").eq(fechava_id)
        ).get("Items", [None])[0]

    def get_base_item(self):
        return {"id": "base", "itens": []}
