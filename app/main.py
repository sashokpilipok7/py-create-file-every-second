from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep
import os

script_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    while True:
        date = datetime.now()
        hours = date.strftime("%H")
        minutes = date.strftime("%M")
        seconds = date.strftime("%S")
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        file_path = os.path.join(script_dir, file_name)
        with open(file_path, "w") as f:
            f.write(str(date))
            print(str(date), file_name)
            sleep(1)


if __name__ == "__main__":
    main()
