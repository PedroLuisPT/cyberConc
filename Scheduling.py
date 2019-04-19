# 2018-2019 Programação 2 (LTI)
# Grupo 055
# 53327 Jorge Roque
# 53469 Pedro Luís

from FilesReading import FilesReading
from DateTime import DateTime
from operator import itemgetter
from copy import deepcopy
from Experts import Experts
from Clients import Clients


class Scheduling:

    def __init__(self):
        """
        Creates a object of the type scheduling.
        """
        pass


    def schedule(self, experts, clients, header):
        """
        Assign a client to a expert
        Requires :
            . a list of experts that comes from the output of filesReading().read_experts()
            . a list of clients that comes from the output of filesReading().read_clients()
        Ensures :
            . a list of the scheduling of the clients to the experts, according to every single condition
        """
        

        schedule=[]
                
        for client in clients:
            teste=False
            i=0
            expertsList = sorted(experts, key=lambda x:(x.get_lastorder(),x.get_hourAvailable(),x.get_price(),x.get_money(),x.get_name()))                         #orders the expertsList before entering the for that runs threw the experts

            while i < len(expertsList) and teste == False:

                    expert = expertsList[i]
                    
                    if client.get_domain() in expert.get_domain() and client.get_reputation() <= expert.get_reputation() \
                        and int(client.get_price()) >= int(expert.get_price()) \
                        and client.get_location() == expert.get_location():                                                                                             #makes the initial verifications specified in the project
                        
                        date = [(expert.get_lastorder(),expert.get_hourAvailable()),(client.get_date(),client.get_timeAvailable())]                                 
                        dateSorted = sorted(date, key=lambda x:x[0])

                        if date != dateSorted:
                                corresp = [DateTime(dateSorted[1][1]).add_minutes(dateSorted[1][0],dateSorted[1][1],60)[0]\
                                        ,DateTime(dateSorted[1][1]).add_minutes(dateSorted[1][0],dateSorted[1][1],60)[1],client.get_name(),expert.get_name()]
                        
                        else:
                                corresp = [dateSorted[1][0],dateSorted[1][1],client.get_name(),expert.get_name()]
                            

                        schedule.append(corresp)
                        expertsList[i].set_lastorder(DateTime(corresp[1]).add_minutes(corresp[0],corresp[1] \
                                    ,DateTime(corresp[1]).numberofMinutes(client.get_timeNeeded()))[0])                                                                 #updates the date that the experts will be available for the next job

                        expertsList[i].set_hourAvailable(DateTime(corresp[1]).add_minutes(corresp[0],corresp[1]\
                                    ,DateTime(corresp[1]).numberofMinutes(client.get_timeNeeded()))[1])                                                                 #updates the hour that the expert will be available for the next job

                        expertsList[i].set_money(float(expertsList[i].get_money())+(float(expert.get_price())) \
                                                 
                                        * float(DateTime(client.get_timeNeeded()).get_hours(client.get_timeNeeded())) \
                                        +  ((float(expert.get_price())) * float(DateTime(client.get_timeNeeded()).get_minutes(client.get_timeNeeded())))/60)            #updates the experts money ammount after getting corresponded to a client
            
                        teste=True
                        
                    i=i+1
                    
            if teste == False:
                schedule.append([header[0], DateTime(header[1]).add_minutes(header[0], header[1], 30)[1],client.get_name(),"declined"])                                 #declines the client that didn´t have a expert to be matched to

        expertsList = sorted(experts, key=lambda x:(x.get_lastorder(),x.get_hourAvailable(),x.get_price(),x.get_money(),x.get_name()))                                      #sorts the final list of experts to be orderd by the lastorder, price, money and finnaly by name
        schedule = sorted(schedule, key=lambda x:(x[0],x[1]))


        return schedule,expertsList
