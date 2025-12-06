import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")


try:
    a = float(sys.argv[1])

except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=c68d46eba3f8af4ced9c77cb1706b9470444645d11ead1012e4e02b2ca5aa91b")

    o = response.json()
    x = o["data"]["priceUsd"]
    x = float(x)
    print(f"${x*a:,.4f}")

except requests.RequestException:
    sys.exit()

except KeyError:
    sys.exit()



