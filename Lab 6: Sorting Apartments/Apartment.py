# Joseph Chang, CS9, Lab 6

class Apartment():
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}" \
		.format(self.rent, self.metersFromUCSB, self.condition)

    def __lt__(self, rhs):
        if self.rent < rhs.rent:
            return True
        elif self.rent > rhs.rent:
            return False
        else:
            if self.metersFromUCSB < rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB > rhs.metersFromUCSB:
                return False
            else:
                if len(self.condition) > len(rhs.condition):
                    return True
                elif len(self.condition) <= len(rhs.condition):
                    return False

    def __gt__(self, rhs):
        if self.rent > rhs.rent:
            return True
        elif self.rent < rhs.rent:
            return False
        else:
            if self.metersFromUCSB > rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB < rhs.metersFromUCSB:
                return False
            else:
                if len(self.condition) < len(rhs.condition):
                    return True
                elif len(self.condition) >= len(rhs.condition):
                    return False

    def __eq__(self, rhs):
        if self.rent == rhs.rent:
            return True
        elif self.rent != rhs.rent:
            return False
        else:
            if self.metersFromUCSB == rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB != rhs.metersFromUCSB:
                return False
            else:
                if len(self.condition) == len(rhs.condition):
                    return True
                elif len(self.condition) != len(rhs.condition):
                    return False

