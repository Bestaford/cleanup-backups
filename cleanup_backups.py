import calendar
import os
import sys
import datetime


def main():
    args = sys.argv
    args.pop(0)
    for path in args:
        cleanup(path)
    print("Done!")


def cleanup(path):
    for filename in os.listdir(path):
        file = os.path.join(path, filename)
        if os.path.isfile(file):
            try:
                backup_date = get_date(filename)
                last_month_day = calendar.monthrange(backup_date.year, backup_date.month)[1]
                now = datetime.datetime.now().date()
                if backup_date <= (now - datetime.timedelta(days=10)) and backup_date.day != last_month_day:
                    os.remove(file)
                    print("Removed: " + file)
            except Exception as error:
                print(error)
                continue


def get_date(filename):
    part1 = filename[filename.index("_") + 1:]
    part2 = part1[:part1.index(".")]
    return datetime.datetime.strptime(part2, "%d_%m_%Y").date()


if __name__ == "__main__":
    main()
