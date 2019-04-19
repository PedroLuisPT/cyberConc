# 2018-2019 Programação 2 (LTI)
# Grupo 055
# 53327 Jorge Roque
# 53469 Pedro Luís

class Clients:

        def __init__(self, name, location, date,timeAvailable, price, reputation, domain, timeNeeded):
            """
            Create Clients informations
            Requires: name, location, date,timeAvailable ,price, reputation, domain, timeNeeded are the
            strings representing of each parameters
            """
            
            self._name=name
            self._location=location
            self._date=date
            self._timeAvailable=timeAvailable
            self._price=price
            self._reputation=reputation
            self._domain=domain
            self._timeNeeded=timeNeeded


        def get_name(self):
            """
            Gets client´s name
            """

            return self._name

        def get_location(self):
            """
            Gets client´s location
            """

            return self._location

        def get_date(self):
            """
            Gets job date
            """

            return self._date

        def get_timeAvailable(self):
            """
            Gets time available for the job
            """

            return self._timeAvailable

        def get_price(self):
            """
            Gets client´s price
            """

            return self._price

        def get_reputation(self):
            """
            Gets client´s minimum wanted reputation
            """

            return self._reputation

        def get_domain(self):
            """
            Gets the wanted domain by the client
            """

            return self._domain

        def get_timeNeeded(self):
            """
            Gets the time needed for the client to wait for the job
            """
                
            return self._timeNeeded


#       -------------------- Begin of set´s -------------------------- #

        def set_name(self, newnNme):
            """
            Sets the new client´s name
            Requires:
                    .newName, client´s new Name
            """

            self._name = newName
            
        def set_location(self, newLocation):
            """
            Sets the new client´s wanted location
            Requires:
                    . newLocation, the new location wanted by the client
            """

            self._location = newLocation

        def set_date(self, newDate):
            """
            Sets the date wanted for the job
            Requires:
                    .newDate, the new date wanted for the realization of the job
            """

            self._date = newDate

        def set_timeAvailable(self, newTimeAvailable):
            """
            Sets the time available to the job
            Requires:
                    .an hour and minutes
            """

            self._timeAvailable = newTimeAvailable

        def set_price(self, newPrice):
            """
            Sets client´s new price to pay
            Requires:
                    .newPrice, the maximum price that the client wants to pay
            """

            self._price = newPrice

        def set_reputation(self, newReputation):
            """
            Sets the reputation required by the client
            Requires:
                    .newReputation, reputation in minimum stars required by the client
            """

            self._reputation = newReputation

        def set_domain(self, newDomain):
            """
            Sets Domain pretended for the job
            Requires:
                    .newDomain, domain of the client´s choice
            """

            self._domain = newDomain

        def set_timeNeeded(self, newTimeNeeded):
            """
            Sets the new time needed for the job
            Requires:
                    .newTimeNeeded, time of the duration of the job
            """

            self._timeNeeded = newTimeNeeded

#       -------------------- End of set´s -------------------------- #



        def __str__(self):
            """
            The string representation of the client´s  information
            """
            return str(self.get_name())+','+str(self.get_location())+','+str(self.get_date()) \
                   +','+str(self.get_timeAvailable())+','+str(self.get_price())+','+ str(self.get_domain())+','+str(self.get_timeNeeded())


        def __lt__(self,other):
            """
            If the current object is less than the other object
            """
            return (self.Client() < self.other())
                

        def __eq__(self, other):
            """
            If the current object is equal or not to the other object
            """
            return (self.Clients() == other.Clients())

        def items(self):
            """
            Permits to roll a for loop with objects
            """
            for elem in self._col:
                yield elem
                
            
                
                
                
