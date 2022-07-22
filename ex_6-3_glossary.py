glossary = {
    'dictionary': 'A collection of key value pairs inside {} and :.',
    'list': 'A collection of items in order uses [].',
    'range_function': 'range(1,5) will print 1 up to 5 so will print 1,2,3,4 but not 5 makes it easy to generate a '
                      'series of numbers ',
    'slice': 'select a group of items from a list ex print(numbers[0:3]) will print numbers at index up to but '
             'not including index 3 from the list named numbers ',
    'tuple': 'a list of items that is immutable uses () instead of []',
    'keys()': 'A method used to pull all the keys from a dictionary',
    'values()': 'A method used to pull all the values from a dictionary',
    'variables()': 'boxes that you can store values in or labels you can assign to values',
    'string': 'A series of characters anything inside quotes',
    'title()': 'A method that changes each word to title case'
}
for term, definition in glossary.items():
    print(f"\n{term}: {definition}")
