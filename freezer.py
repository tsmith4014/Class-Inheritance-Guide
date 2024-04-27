
class Freezer:
    """
    A class representing a freezer for storing ice cream.

    Attributes:
    - the_freezer (list): A list to store the ice cream objects.
    - capacity (int): The maximum capacity of the freezer.

    Methods:
    - add(ice_cream): Adds an ice cream object to the freezer.
    - remove(flavor): Removes all ice cream objects with the specified flavor from the freezer.
    - add_time(time): Increases the age of all ice cream objects in the freezer by the specified time.
    - __str__(): Returns a string representation of the freezer's capacity.
    """

    def __init__(self, capacity=10): #this is where the Freezer init is defined.  The init is a method that initializes the object called a constructor also know as a dunder method.  Not sure which sounds cooler but it seems like most folks say dunder method.  Basicly this is where classes are initizalized. Dont get confused by self, this is just a way to refer to the object that is being created.  The self is the first parameter of any method in a class.  The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.  This allows us to substanciate a fresh new object of the class.
    
        self.the_freezer = [] # the freezer is an empty list that will store the ice cream objects.
        self.capacity = capacity # max capacity of the freezer is set to 10 in the parameter on line 17 where the init is defined. 

    def add(self, ice_cream):
        self.the_freezer.append(ice_cream) #this is the method that adds ice cream to the freezer.  The ice cream object is passed as a parameter.  The append method is used to add the ice cream object to the list of ice cream objects in the freezer.
    
    def remove(self, flavor):
        for i, ic in enumerate(self.the_freezer):
            if ic.flavor == flavor:
                del self.the_freezer[i]
                break

    def remove_all(self, flavor):
        self.the_freezer = [ic for ic in self.the_freezer if ic.flavor != flavor] #this is the method that removes all of a type of ice cream from the freezer.  The flavor of the ice cream is passed as a parameter.  The list comprehension is used to create a new list of ice cream objects that do not have the specified flavor.  The new list is then assigned to the freezer.  Think if ic for ic in self.the_freezer if ic.flavor != flavor as a way to filter out the ice cream objects with the specified flavor.

    def add_time(self, time):
        for ic in self.the_freezer:
            ic.age += time
            ic.status = ic.check_status() #this is the method that adds time to the ice cream objects in the freezer.  The time is passed as a parameter.  A for loop is used to iterate over each ice cream object in the freezer.  The age of each ice cream object is increased by the specified time.  The check_status method is called to update the status of each ice cream object.  The check_status method is defined in the IceCream class and this is what classes are cool we can call methods from other classes when we are using them in our class.  This is the concept of Class Inheritance.  When the ice_cream_and_freezers_spec.py (this is a confusing name for our unittest file) is run the check_status method is called to update the status of each ice cream object in the freezer.  Even though freezer and ice_cream.py are different .py files they are still in the same directory so they can be imported and used in the same file.  When one class is used in another class this way it allows us to use the methods and attributes of the imported class in the class that is importing it.  This is kinda of the point of all this, its tough to get at first but once you get it you will be like oh.
    def __str__(self): #A string representation of the freezer's capacity is returned.  The __str__ method is defined to return a string representation of the freezer's capacity.  The string representation is formatted to show the number of ice cream objects in the freezer and the maximum capacity of the freezer.  The len function is used to get the number of ice cream objects in the freezer.  The capacity of the freezer is accessed using the self keyword.  The f-string is used to format the string representation.  The f-string is a string that is prefixed with the letter f.  The f-string allows us to insert variables and expressions into the string by using curly braces.  The curly braces are used to insert the number of ice cream objects in the freezer and the maximum capacity of the freezer into the string.  The __str__ method is called when the string representation of the freezer is needed.  The strip method is used to remove any leading or trailing whitespace from the string representation.  The string representation is returned.  The string representation is used in the test case to check if the freezer is empty.  The test case is checking if the string representation of the freezer is "Capacity: 0 of 10".  Hope this helps.  I know it is a lot but it is important to understand how classes work
        return f""" 
            Capacity: {len(self.the_freezer)} of {self.capacity} 
            """ 








