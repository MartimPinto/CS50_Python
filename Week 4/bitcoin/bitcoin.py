import requests
import sys
import json


def main():
    n = check_args()
    try:
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json"
        ).json()
        response = float(response["bpi"]["USD"]["rate_float"])
        print(f"${n * response:,.4f}")
    except requests.RequestException:
        pass


def check_args():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
        return n
    except:
        sys.exit("Command-line argument is not a number")


if __name__ == "__main__":
    main()
