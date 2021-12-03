from datetime import datetime as dt


def main(n=dt.today().day):
    exec(f"from aoc{n} import solve", globals())
    print(solve())


if __name__ == '__main__':
    main()