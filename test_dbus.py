import time
from gi.repository import Geoclue

ACCURACY_THRESHOLD = 50

timeout = time.time() + 60
while time.time() < timeout:
    clue = Geoclue.Simple.new_sync("something", Geoclue.AccuracyLevel.EXACT, None)
    location = clue.get_location()
    print("latitude: %f" % location.get_property("latitude"))
    print("longitude: %f" % location.get_property("longitude"))
    accuracy = location.get_property("accuracy")
    print("accuracy: %f" % accuracy)
    if accuracy < ACCURACY_THRESHOLD:
        break
    else:
        time.sleep(1)
