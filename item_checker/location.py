import logging
import time

from gi.repository import Geoclue

from .config import CONFIG


def get_location() -> tuple[str, str]:
    latitude = None
    longitude = None

    step = 0
    timeout = time.time() + 60
    while time.time() < timeout:
        clue = Geoclue.Simple.new_sync("something", Geoclue.AccuracyLevel.EXACT, None)
        location = clue.get_location()
        latitude = location.get_property("latitude")
        longitude = location.get_property("longitude")
        accuracy = location.get_property("accuracy")
        logging.info(
            "%s: coordinates: %s %s with accuracy: %f",
            step,
            latitude,
            longitude,
            accuracy,
        )
        if accuracy < CONFIG.accuracy_threshold:
            break
        else:
            step += 1
            time.sleep(1)

    if latitude is None or longitude is None:
        raise RuntimeError("No location found")

    return latitude, longitude
