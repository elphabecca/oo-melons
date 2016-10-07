import random
import datetime

"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """general information for any melon order """

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_base_price(self):
        """Choose a random integer between 5 and 9 as the base_price."""
        #8-11am, Monday-Friday
        splurge_base = random.randint(5,9)
        rush_hour = datetime.weekday(0, 4) and 8 < datetime.hour < 10

        if datetime.now() in rush_hour:
            return splurge_base + 4

        return splurge_base 



    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        
        if self.species == 'Christmas':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        return total




class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    tax = 0.08
    order_type = "domestic"
    country_code = "USA"

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, "USA")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, country_code)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):

        if self.qty < 10:
            return super(InternationalMelonOrder, self).get_total() + 3
        
        return super(InternationalMelonOrder, self).get_total()

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    order_type = "domestic"
    country_code = "USA"

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(GovernmentMelonOrder, self).__init__(species, qty, "USA")
        self.passed_inspection = False

    def mark_inspection_passed(self, passed):
        """Set mark_inspection_passed to whatever the boolean is."""

        self.mark_inspection_passed = passed

