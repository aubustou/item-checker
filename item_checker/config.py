from dataclasses import dataclass
import json
ACCURACY_THRESHOLD = 50

CONFIG: Config = None  # type: ignore

@dataclass
class Config:
    accuracy_threshold: int = ACCURACY_THRESHOLD

def load_settings() -> None:
    global CONFIG

    with open('settings.json', 'r') as f:
        CONFIG = Config(**json.load(f))
