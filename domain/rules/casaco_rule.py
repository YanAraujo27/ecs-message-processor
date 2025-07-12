from .base_rule import BaseRule

class CasacoRule(BaseRule):
    def apply(self, message, repo):
        id_val = message.payload.get("fechava", {}).get("id")
        existing = repo.get_by_fechava_id(id_val)

        if existing:
            updated = existing.copy()
            for k, v in message.payload.items():
                if v is not None:
                    updated[k] = v
            repo.put_item(updated)
        else:
            base = repo.get_base_item()
            base["itens"].append(message.payload)
            repo.put_item(base)
