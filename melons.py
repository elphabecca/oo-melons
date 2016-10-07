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



    def get_total(self):
        """Calculate price."""

        base_price = 5
        
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

