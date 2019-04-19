# 2018-2019 Programação 2 (LTI)
# Grupo 055
# 53327 Jorge Roque
# 53469 Pedro Luís

class Experts:

        def __init__(self, name, location, domain, reputation, price, lastorder, hourAvailable, money ):
                """
                Create Experts informations
                Requires: strings representing each parameters
                Ensures
                """
            
                self._name=name
                self._location=location
                self._domain=domain
                self._reputation=reputation
                self._price=price
                self._lastorder=lastorder
                self._hourAvailable=hourAvailable
                self._money=money


        def get_name(self):
            """
            Gets expert´s name
            """

            return self._name

        def get_location(self):
            """
            Gets expert´s location
            """

            return self._location

        def get_domain(self):
            """
            Gets expert´s domain
            """

            return self._domain

        def get_reputation(self):
            """
            Gets expert´s reputation
            """

            return self._reputation
        
        def get_price(self):
            """
            Gets expert´s price
            """

            return self._price

        def get_lastorder(self):
            """
            Gets expert´s price
            """

            return self._lastorder

        def get_hourAvailable(self):
            """
            Gets expert´s price
            """

            return self._hourAvailable

        def get_money(self):
            """
            Gets expert´s price
            """

            return self._money


#          -------------------- Begin of set´s -------------------------- #
    
        def set_money(self,newAmmount):
            """
            Sets the new ammount of money owned
            Requires:
                    .newAmmount as float representating the ammount of money owned          
            """
            self._money = newAmmount

        def set_hourAvailable(self,newTime):
            """
            Sets the new time
            Requires:
                    .newTime as a str
            """
            self._hourAvailable = newTime
            

        def set_lastorder(self,updatedOrder):
            """
            Updates the last order that the expert got
            Requires:
                    .updatedOrder, as str
            """
            self._lastorder = updatedOrder

        def set_name(self, name):
            """
            Sets expert´s name
            Requires: The name of the expert
            """

            self._name = name

        def set_location(self, newLocation):
            """
            Sets expert´s location
            Requires:
                    .newLocation, the location of the job
            """

            self._location = newLocation

        def set_domain(self, newDomain):
            """
            Sets the new expert´s domain
            Requires:
                    .newDomain, the domain of the job required
            """

            self._domain = newDomain

        def set_reputation(self, newReputation):
            """
            Sets new expert´s reputation
            Requires:
                    .newReputation, the reputation of the Expert
            """

            self._reputation = newReputation

        def set_price(self, newPrice):
            """
            Gets new expert´s price
            Requires:
                    .newPrice, the price that the Expert takes for the job
            """

            self._price = price

            

#       -------------------- End of set´s -------------------------- #


        def __str__(self):
            """
            The string representation of the expert´s information
            """

            result = str(self.get_name()) + ', ' + str(self.get_location())+', ('
            
            for item in self.get_domain():                                                                              # verifies if the expert has more than one speciality and writes them
                    result = result + item
                    if  item != self.get_domain()[-1]:
                        result = result + '; '
        
            result = result + '), ' + str(self.get_reputation()) + ', ' + str(self.get_price())  + ', ' + str(self.get_lastorder()) \
                     + ', ' + str(self.get_hourAvailable()) + ', ' + str(self.get_money())

            return result
            
            
        def __lt__(self, other):
            """
            Verifies if the current object is less than the other object
            """
            return (self.Experts > self.other)
            

        def __eq__(self, other):
            """
            Verifies if the current object is equal or not to the other object
            """
            return (self.Experts == self.other)
             


        def items(self):
            """
            Permits to roll a for loop with objects
            """
            for elem in self._col:
                yield elem   
