def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"my {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name="indy")
describe_pet(animal_type="hamster", pet_name="harry")
