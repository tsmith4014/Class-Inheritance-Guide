import unittest
from freezer import Freezer
from ice_cream import IceCream
from ice_cream import FlavoredIceCream
from ice_cream_dream import IceCreamDream

class TestFreezer(unittest.TestCase):
    def test_add_cone(self):
        """
        Test case for adding a cone to the freezer.
        """
        test_freezer = Freezer() #we instantiate a new object of the Freezer class.  The new object is assigned to the variable test_freezer. 
        test_freezer.add(FlavoredIceCream("vanilla")) #we add a new ice cream object to the freezer.  The ice cream object is created using the FlavoredIceCream class.  The flavor of the ice cream is set to "vanilla".  The add method is called to add the ice cream object to the freezer.
        self.assertEqual(len(test_freezer.the_freezer), 1) #we check if the ice cream object was added to the freezer.  The length of the list of ice cream objects in the freezer is checked.  The length of the list of ice cream objects in the freezer should be 1.

        #ok that is one example above explained.  use gpt or try and figure this out yourself below.  But These are all just ways to test, this file acts like a runner or parent file and pulls in 2 children to test and has access to all there class goodies.

    def test_str(self):
        """
        Test case for checking the string representation of the freezer.
        """
        test_freezer = Freezer()
        self.assertEqual(test_freezer.__str__().strip(), "Capacity: 0 of 10")

    def test_remove_cone_if_ready(self):
        """
        Test case for removing a cone from the freezer if it is ready.
        """
        test_freezer = Freezer()
        test_freezer.add(FlavoredIceCream("vanilla"))
        test_freezer.remove("vanilla")
        self.assertEqual(len(test_freezer.the_freezer), 0)

    def test_add_time(self):
        """
        Test case for adding time to the freezer.
        """
        test_freezer = Freezer()
        test_freezer.add(FlavoredIceCream("vanilla"))
        test_freezer.add_time(1)
        self.assertEqual(test_freezer.the_freezer[0].age, 1)

    def test_status_change_with_time(self):
        """
        Test case for checking the status change of ice cream with time.
        """
        test_freezer = Freezer()
        test_ice_cream = FlavoredIceCream("vanilla")
        test_freezer.add(test_ice_cream)
        self.assertEqual(test_ice_cream.status, "runny")
        test_freezer.add_time(3)
        self.assertEqual(test_ice_cream.status, "almost_ready")
        test_freezer.add_time(3)
        self.assertEqual(test_ice_cream.status, "ready")
        test_freezer.add_time(100)
        self.assertEqual(test_ice_cream.status, "freezer_burned")

class TestIceCream(unittest.TestCase):
    def test_check_status(self):
        """
        Test case for checking the status of ice cream.
        """
        test_ice_cream = IceCream()
        self.assertEqual(test_ice_cream.check_status(), "runny")
        test_ice_cream.age = 3
        self.assertEqual(test_ice_cream.check_status(), "almost_ready")
        test_ice_cream.age = 5
        self.assertEqual(test_ice_cream.check_status(), "ready")
        test_ice_cream.age = 100
        self.assertEqual(test_ice_cream.check_status(), "freezer_burned")

class TestFlavoredIceCream(unittest.TestCase):
    def test_str(self):
        """
        Test case for checking the string representation of flavored ice cream.
        """
        test_ice_cream = FlavoredIceCream("vanilla")
        self.assertEqual(test_ice_cream.__str__().strip(), "flavor: vanilla\n        status: runny")


class TestIceCreamDream(unittest.TestCase):
    def test_move_in(self):
        """
        Test case for moving ice cream into the ice cream dream.
        """
        test_ice_cream_dream = IceCreamDream()
        test_ice_cream_dream.move_in()
        self.assertEqual(len(test_ice_cream_dream.walk_in_freezer.the_freezer), 1)

    def test_move_out(self):
        """
        Test case for moving ice cream out of the ice cream dream.
        """
        test_ice_cream_dream = IceCreamDream()
        test_ice_cream_dream.move_in()
        test_ice_cream_dream.move_out()
        self.assertEqual(len(test_ice_cream_dream.walk_in_freezer.the_freezer), 0)

    def test_freezer_status(self):
        """
        Test case for checking the status of the ice cream dream's freezer.
        """
        test_ice_cream_dream = IceCreamDream()
        test_ice_cream_dream.move_in()
        self.assertEqual(test_ice_cream_dream.freezer_status(), "end of ice cream list")

    def test_ice_cream_in_freezer_status(self):
        """
        Test case for checking the status of ice cream in the freezer.
        """
        test_ice_cream_dream = IceCreamDream()
        test_ice_cream_dream.move_in()
        # Assuming ice_cream_in_freezer_status() returns a list of statuses
        self.assertEqual(test_ice_cream_dream.ice_cream_in_freezer_status(test_ice_cream_dream.walk_in_freezer.the_freezer), ["runny"])