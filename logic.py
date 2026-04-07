import re
import random

messagelist = [
    "[message] is crazy bro",
    "some guy said [message]",
    "[message] got me rolling on the floor",
    "[message] im dead",
    "[message] 99999 percent aura",
    "he cooked with [message]",
    "[message] 0/10 ragebait unfunny",
    "[message] haha so funny wow"
]

def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def clean_message(text: str) -> str:
    text = normalize_text(text)

    # mention temizle
    text = re.sub(r"<@!?(\d+)>", "", text)

    return text.strip()


def shorten_message(text: str, max_length: int = 60) -> str:
    if len(text) <= max_length:
        return text

    return text[:max_length].rstrip() + "..."


def is_valid_message(text: str) -> bool:
    text = clean_message(text)

    if not text:
        return False

    if len(text) < 3:
        return False

    return True


def should_reply(chance=0.4) -> bool:
    return random.random() < chance


def analyze_message(text: str) -> dict:
    cleaned = clean_message(text)

    return {
        "valid": is_valid_message(cleaned),
        "should_reply": should_reply(),
        "message_for_reply": shorten_message(cleaned)
    }

def createreply(text):
    analyzed = analyze_message(text)
    reply_text = analyzed["message_for_reply"]
    phrase = messagelist[random.randint(0,7)]
    result = phrase.replace("[message]", '"' + reply_text + '"')
    return result