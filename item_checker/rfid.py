import time
from typing import Optional

from .config import READER


def get_tag_id() -> Optional[str]:
    tags = READER.read()
    if tags:
        return tags[0].epc
    else:
        return None


def loop():
    while True:
        data = get_tag_id()
        if data:
            print(data)
        time.sleep(1)
