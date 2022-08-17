from .config import load_settings


def main():
    load_settings()

    from .rfid import loop
    loop()


if __name__ == "__main__":
    main()
