import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if matches := re.search(r"^(\d+)(?::(\d\d))? (AM|PM) to (\d+)(?::(\d\d))? (AM|PM)$", s):
        hour1 = int(matches.group(1))
        min1 = 0 if matches.group(2) == None else int(matches.group(2))
        hour2 = int(matches.group(4))
        min2 = 0 if matches.group(5) == None else int(matches.group(5))

        if (hour1 in range(1, 13) and min1 in range(0, 60) and hour2 in range(1, 13) and min2 in range(0, 60)):
            if matches.group(3) == "PM":
                hour1 = 12 if hour1 == 12 else hour1 + 12
            if matches.group(3) == "AM" and hour1 == 12:
                hour1 = 0
            if matches.group(6) == "PM":
                hour2 = 12 if hour2 == 12 else hour2 + 12
            if matches.group(6) == "AM" and hour2 == 12:
                hour2 = 0
            return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"
        else:
            raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()
