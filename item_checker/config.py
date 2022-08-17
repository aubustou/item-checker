import json
import time
from dataclasses import dataclass
from pathlib import Path

from mercury import Reader

ACCURACY_THRESHOLD = 50

CONFIG: Config = None  # type: ignore
READER: Reader = None  # type: ignore


@dataclass
class Config:
    accuracy_threshold: int = ACCURACY_THRESHOLD
    reader_device: str = "/dev/ttyS0"
    reader_region: str = "EU3"
    reader_read_plan: str = "GEN2"


def load_settings() -> None:
    global CONFIG, READER

    if (settings_path := Path("settings.json")).exists():
        CONFIG = Config(**json.load(settings_path.open()))
    else:
        CONFIG = Config()

    time.sleep(2)
    READER = Reader("tmr://" + CONFIG.device)
    READER.set_region(CONFIG.region)
    READER.set_read_plan([1], CONFIG.read_plan)
