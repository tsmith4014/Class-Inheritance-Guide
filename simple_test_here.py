from ice_cream import FlavoredIceCream
from ice_cream_dream import IceCreamDream

# Initialize the IceCreamDream instance
dream = IceCreamDream()

# Add a variety of flavors to the freezer
flavors = ["chocolate", "strawberry", "mint", "cookie dough", "rocky road"]

for flavor in flavors:
    dream.walk_in_freezer.add(FlavoredIceCream(flavor))
    print(f"Added {flavor} ice cream to the freezer.")

# Display the current status of ice creams in the freezer
print("\nCurrent status of ice creams in the freezer:")
print(dream.freezer_status())

# Add vanilla ice cream from the freezer
dream.walk_in_freezer.add(FlavoredIceCream("vanilla"))
print("\nAdded vanilla ice cream to the freezer using dream.walk__in_freezer.add(FlavoredIceCream('vanilla')).")
print(dream.freezer_status())
dream.move_in() 
print(f"\nAdding vanilla ice cream from the freezer using dream.move.")
print(dream.freezer_status())
dream.move_in()
print(f"\nAdding vanilla ice cream from the freezer using dream.move.")
print(dream.freezer_status())
dream.move_out()
print(f"\nRemoving a vanilla ice cream from the freezer using dream.move_out.")   
dream.clear_out()
print(f"\nRemoving all vanilla ice cream from the freezer using dream.clear_out.")

# Display the final status of ice creams in the freezer
print("\nFinal status of ice creams in the freezer:")
print(dream.freezer_status())