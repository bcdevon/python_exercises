favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
should_poll = ['jen', 'brady']
for name in should_poll:
    if name in favorite_languages:
        print(f"{name} thank you for responding")
    else:
        print(f"{name} please respond")
