# Joseph Chang, Lab 08, CS 9

class Car:

    def __init__(self, make = "", model = "", year = None, price = None):

        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        elif self.make < rhs.make:
            return False
        else:
            if self.model > rhs.model:
                return True
            elif self.model < rhs.model:
                return False
            else:
                if self.year > rhs.year:
                    return True
                elif self.year < rhs.year:
                    return False
                else:
                    if self.price > rhs.price:
                        return True
                    elif self.price <= rhs.price:
                        return False

    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        elif self.make > rhs.make:
            return False
        else:
            if self.model < rhs.model:
                return True
            elif self.model > rhs.model:
                return False
            else:
                if self.year < rhs.year:
                    return True
                elif self.year > rhs.year:
                    return False
                else:
                    if self.price < rhs.price:
                        return True
                    elif self.price >= rhs.price:
                        return False

    def __eq__(self, rhs):
        if self.make == rhs.make and self.model == rhs.model and\
           self.year == rhs.year and self.price == rhs.price:
            return True
        else:
            return False


    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}" \
		.format(self.make, self.model, self.year, self.price)


