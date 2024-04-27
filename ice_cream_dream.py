from freezer import Freezer
from ice_cream import IceCream
from ice_cream import FlavoredIceCream

#So this file imports our Freezer, IceCream, and FlavoredIceCream classes from the freezer.py and ice_cream.py files.  

class IceCreamDream:
    """
    Attributes:
        walk_in_freezer (Freezer): The freezer where the ice cream is stored.

    Methods:
        move_in: Adds a vanilla ice cream to the freezer.
        move_out: Removes a vanilla ice cream from the freezer.
        freezer_status: Prints the flavor and status of each ice cream in the freezer.
        ice_cream_in_freezer_status: Returns the status of each ice cream in the freezer.
    """

    def __init__(self):
        self.walk_in_freezer = Freezer() #The walk_in_freezer attribute is initialized with a new instance of the Freezer class.  The Freezer class is imported from the freezer.py file.
        
    def move_in(self):
        """
        Adds a vanilla ice cream to the freezer.
        """
        self.walk_in_freezer.add(FlavoredIceCream("vanilla"))

    def move_out(self):
        """
        Removes a vanilla ice cream from the freezer.
        """
        self.walk_in_freezer.remove("vanilla")

    def clear_out(self):
        """
        Removes all vanilla ice cream from the freezer.
        """
        self.walk_in_freezer.remove_all("vanilla")

    def freezer_status(self):
        """
        Prints the flavor and status of each ice cream in the freezer.
        """
        for ic in self.walk_in_freezer.the_freezer:
            print((ic.flavor, ic.status))
        return "end of ice cream list"

    def ice_cream_in_freezer_status(self, freezlist):
        """
        Returns the status of each ice cream in the freezer.

        Args:
            freezlist (list): A list of ice cream objects.

        Returns:
            list: A list of ice cream statuses.
        """
        return [ic.status for ic in freezlist]