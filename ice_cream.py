# The IceCream class represents an ice cream object.
class IceCream:
    """
    A class representing an ice cream.

    Attributes:
        time_to_freeze (int): The time it takes for the ice cream to freeze in hours.
        time_to_burn (int): The time it takes for the ice cream to burn in hours.
        age (int): The age of the ice cream in hours.
        status (str): The status of the ice cream based on its age.

    Methods:
        __init__(self, age=0): Initializes the age and status of the ice cream.
        check_status(self): Determines the status of the ice cream based on its age.
    """

    time_to_freeze = 5  # hours to freeze ice cream
    time_to_burn = 100  # hours, it takes 3 days for ice cream to burn 

    def __init__(self, age=0):#this is the init method that initializes the age and status of the ice cream.  The age of the ice cream is passed as a parameter.  The age of the ice cream is set to the specified age (we use 0 here).
        """
        Initializes a new instance of the IceCream class.

        Args:
            age (int, optional): The age of the ice cream in hours. Defaults to 0.
        """
        self.age = age
        self.status = self.check_status()

    def check_status(self):
        """
        Determines the status of the ice cream based on its age.

        Returns:
            str: The status of the ice cream.
        """
        if self.age <= 2:
            return "runny"
        elif self.age >= self.time_to_burn:
            return "freezer_burned"
        elif self.age < self.time_to_freeze:
            return "almost_ready"
        elif self.age >= self.time_to_freeze:
            return "ready"


class FlavoredIceCream(IceCream): #Here is another cool thing about Classes The FlavoredIceCream class is a subclass of the IceCream class.  The FlavoredIceCream class inherits the attributes and methods of the IceCream class. This allows us to make new classes and not have to recreate the wheel and do a lot of rework aka this is DRY DON'T REPEAT YOURSELF. ;)

    def __init__(self, flavor, age=0):
        super().__init__(age) #Here is our super that is used to call the __init__ method of the parent class.  The super function is used to call the __init__ method of the parent class.

        self.flavor = flavor #The flavor of the ice cream is passed as a parameter.  The flavor of the ice cream is set to the specified flavor.

    def __str__(self): #A string representation of the flavored ice cream is returned.  The __str__ method is defined to return a string representation of the flavored ice cream. Easy peasy lemon squeezy.
        return f""" 
        flavor: {self.flavor}
        status: {self.status}
        """