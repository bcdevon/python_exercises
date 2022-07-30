sandwich_orders = ['reuben', 'club', 'cuban', 'monte cristo', 'cheese steak', 'grilled cheese']
finished_sandwiches = []

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print(f"I am making your {making_sandwich}.")

    finished_sandwiches.append(making_sandwich)
print(f"\nThese sandwiches are ready")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
