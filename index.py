import requests
from CONFIG import HELIUS_API_KEY
import matplotlib.pyplot as plot

url = "https://api.helius.xyz/v1/nft-events?api-key=" + HELIUS_API_KEY


def get_sales(url):
    priceList = []
    data = requests.post(url, json={
        "query": {
            "sources": ["MAGIC_EDEN"],
            "types": ["NFT_SALE"],
            "nftCollectionFilters": {
                # y00ts collection address: 4mKSoDDqApmF1DqXvVTSL6tu2zixrSSNjqMxUnwvVzy2
                "verifiedCollectionAddress": ["4mKSoDDqApmF1DqXvVTSL6tu2zixrSSNjqMxUnwvVzy2"]
            }
        }
    }).json()

    for item in data["result"]:
        # The below line extracts and appends the sale prices from the API response and puts them into a list called priceList
        # It does some formatting too, converting the # to a float, formatting it to the proper decimal place, and cutting the price to a max of 2 decimal places
        # It also adds commas for values that are in the quadruple-digits and above.
        priceList.append(float("{:,.2f}".format(item["amount"]/1000000000)))
    xAxis = []
    count = 0
    for item in priceList:
        count += 1
        c = xAxis.append(count)

    # print(xAxis)

    #print("Sales: ", priceList)

    plot.scatter(xAxis, priceList)
    plot.show()


get_sales(url)
