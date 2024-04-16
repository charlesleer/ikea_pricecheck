import requests

def get_product_id(url):
    parts = url.split('-')
    return parts[-1]

def format_price(price):
    if price is None:
        return "Price not found"
    else:
        formatted_price = "{:,.0f}".format(price).replace(",", "")
        if formatted_price.endswith(" 00"):
            formatted_price = formatted_price[:-3]
        return formatted_price
def get_price(product_id, country_code):
    last_three_digits = product_id[-3:]
    if country_code == "se":
        json_url = f"https://www.ikea.com/{country_code}/sv/products/{last_three_digits}/{product_id}.json"
    else:
        json_url = f"https://www.ikea.com/{country_code}/{country_code}/products/{last_three_digits}/{product_id}.json"

    response = requests.get(json_url)
    if response.status_code == 200:
        data = response.json()
        currency_code = data['currencyCode']
        price = format_price(data['priceNumeral'])

        return price, currency_code
    else:
        print("Failed to retrieve data:", response.status_code)
        return None, None


def main():
    product_url = input("Enter the product url: ")
    product_id = get_product_id(product_url)[:-1]
    countries = [("Finland", "fi"), ("Netherlands", "nl"), ("Sweden", "se")]  # Add more countries if needed

    for country, country_code in countries:
        price, currency_code = get_price(product_id, country_code)

        if price and currency_code:
            formatted_price = f"{price} {currency_code}"
            print(f"Price in {country}: {formatted_price}")
        else:
            print(f"Price not found for {country}")


if __name__ == "__main__":
    main()
