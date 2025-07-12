def adapt_message(raw):
    return {
        "origem": raw.get("origem"),
        "payload": raw.get("payload")
    }
