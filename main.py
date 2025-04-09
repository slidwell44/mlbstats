# main.py

import statsapi as mlb


def main():
    response = mlb.schedule(team=116, start_date="03/01/2025", end_date="04/08/2025")
    print(response)


if __name__ == "__main__":
    main()
