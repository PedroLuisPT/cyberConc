# 2018-2019 Programação 2 (LTI)
# Grupo 055
# 53327 Jorge Roque
# 53469 Pedro Luís

from Clients import Clients
from Experts import Experts
from FilesReading import FilesReading
from FilesWriting import FilesWriting
from Scheduling import Scheduling
import sys


def assign(expertsFile,clientsFile):
    """
    Assign experts to given clients.
    Requires:
        .expertsFile, clientsFile are str, with the names of the files representing the list of experts and clients, respectively,
        following the format indicated in the project.
    Ensures:
        .Two output files, respectively, with the listing of schedules and the updated listing of experts, following the format
    and naming convention indicated in the project
    """
    
    
    experts= FilesReading().read_experts(expertsFile)                                                                           #reads the file of the experts
    clients= FilesReading().read_clients(clientsFile)                                                                           #reads the file of the clients
    
    header=FilesReading().read_header(expertsFile)                                                                              #reads the header

    sched=Scheduling().schedule(experts,clients,header)                                                                         #does the correspondence from a client into a expert
    schedule,expertsList=sched

    FilesWriting().write_scheduling(header,schedule)                                                                            #writes the schedule
    FilesWriting().write_experts(header,expertsList)                                                                            #writes the updated experts


expertsFile, clientsFile = sys.argv[1:]
assign(expertsFile, clientsFile)
