from domain.message import Message
from domain.rules.rule_factory import get_rule_by_origem
from repositories.dual_repository import DualRepository
from concurrent.futures import ThreadPoolExecutor

class MessageProcessor:
    def __init__(self, table_name):
        self.repo = DualRepository(table_name)

    def process_batch(self, raw_messages):
        with ThreadPoolExecutor(max_workers=min(10, len(raw_messages))) as executor:
            executor.map(self.process, raw_messages)

    def process(self, raw_data):
        msg = Message(origem=raw_data["origem"], payload=raw_data["payload"])
        rule = get_rule_by_origem(msg.origem)
        rule.apply(msg, self.repo)
