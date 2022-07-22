cities = {
    'palmer': {
        'country': 'USA',
        'population': 20000,
        'fact': 'a town in Alaska'
    },
    'salem': {
        'country': 'USA',
        'population': 32000,
        'fact': 'the capital of Oregon',
    },
    'istanbul': {
        'country': 'Turkey',
        'population': 60000,
        'fact': 'a city that spans two continents'
    }
}
for city, info in cities.items():
    print(f"\n{city.title()}")
    about = f"Is in {info['country']} and {info['fact']} "
    num_people = f"with a populations of {info['population']}"
    print(about)
    print(num_people)
