from .base_rule import BaseRule

class DefaultRule(BaseRule):
    def apply(self, message, repo):
        repo.put_item(message.payload)
