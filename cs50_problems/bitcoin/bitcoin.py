import json
import requests
import sys

def main():
    try:
        n = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()

        rate = float(data["bpi"]["USD"]["rate_float"])

        result = n * rate

        print(f"${result:,.4f}")
        
    except ValueError:
        sys.exit("Command-line argument is not a number")

    except IndexError:
        sys.exit("Missing command-line argument")
    

main()