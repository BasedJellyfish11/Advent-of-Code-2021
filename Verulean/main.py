from datetime import datetime as dt


def main(n=dt.today().day):
    print(__import__(f"aoc{n}").solve())


if __name__ == '__main__':
    main()
