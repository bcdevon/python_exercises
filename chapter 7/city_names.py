def city_country(city, country):
    get_city_country_formatted = f"{city.title()}, {country.title()}"
    return get_city_country_formatted


while True:
    print("enter q at any time to quit")
    city_name = input("\nenter name of city: ")
    if city_name == "q":
        break
    country_name = input("what country is the city in: ")
    if country_name == "q":
        break

    formatted_city_country = city_country(city_name, country_name)
    print(f"{formatted_city_country}")
