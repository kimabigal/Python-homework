country_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "UK": "London"
}


country = input("Enter a country name: ")
capital = country_capitals.get(country)

if capital:
    print(f"{country}: {capital}")
else:
    print("Country is not found")