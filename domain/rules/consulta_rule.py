from .base_rule import BaseRule

class ConsultaRule(BaseRule):
    def apply(self, message, repo):
        existing = repo.get_by_id(message.payload["id"])
        if existing and existing["id"] == message.payload["id"]:
            repo.put_item(message.payload)
