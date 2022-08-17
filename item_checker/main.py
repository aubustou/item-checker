from .config import load_settings
from .rfid import loop


def main():
    load_settings()

    loop()


if __name__ == "__main__":
    main()
