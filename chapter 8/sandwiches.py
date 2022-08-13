def make_sandwich(*ingredients):
    print(f"\nThe sandwich I am making includes the following:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


make_sandwich('ham', 'lettuce', 'cheese', 'bread')
