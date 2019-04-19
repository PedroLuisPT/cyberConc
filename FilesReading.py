# 2018-2019 Programação 2 (LTI)
# Grupo 055
# 53327 Jorge Roque
# 53469 Pedro Luís

from Clients import Clients
from Experts import Experts

class FilesReading:
    
    def __init__(self):
        """
        """ 
        pass
        
    def read_experts(self,expertsFile):
        """
        Reads a file with operators into a collection
        Requires:
            .expertsFile, str that is a text file with a list of experts
        Ensures:
            .a collection of the experts
        """

        openFile=open(expertsFile,'r')

        for i in range(7):                                                                                                                                  #skips the header
            openFile.readline()

        expertsList=[]

        for line in openFile:                                                                                                                               #writes the experts line by line while spliting them by a comma, and the speciality get separated by ; if more than one
            linebyLine = line.strip().split(', ')
            linebyLine[2]=linebyLine[2][1:-1].split('; ')

            expertsList.append(Experts(linebyLine[0],linebyLine[1],linebyLine[2],linebyLine[3],linebyLine[4],linebyLine[5],linebyLine[6],linebyLine[7]))    #writes the experts field by field              

        return expertsList



    def read_clients(self,clientsFile):
        """
        Read a file with clients into a collection.
        Requires:
            .clientsFile, str with the name of a text file with a list of clients.
        Ensures:
            .clientsList, a collection of clients
        """

        openFile=open(clientsFile,'r')

        for i in range(7):                                                                                                                                  # skips the header
            openFile.readline()

        clientsList=[]

        for line in openFile:
            lineList = line.strip().split(', ')                                                                                                             # splits the line (1 client) and inserts a comma between every field 
            clientsList.append(Clients(lineList[0],lineList[1],lineList[2],lineList[3],float(lineList[4]),lineList[5],lineList[6],lineList[7]))             #writes the experts field by field
    
        return clientsList
            
            
    def read_header(self,fileName):
        """
        Reads a file into a collection of the header
        Requires:
            .filename, str with the name of the file
        Ensures:
            .the header into a collection
        """

        file=open(fileName,'r')
        header=[]

        lines=file.readline()
        
        day = file.readline()                                 
        header.append(day.strip())                                                                                                      #appends into the header list the day
    
        file.readline()                                                                                                                 
    
        time = file.readline()                                
        header.append(time.strip())                                                                                                     #appends into the header list the time    
    
        file.readline()
    
        company = file.readline()                             
        header.append(company.strip())                                                                                                  #appends into the header list the company name      
    
        file.close()

        return header

        
    def __str__(self):
        """
        The string representation of the Clients and Experts 
        """

        return Clients.__str__(),Experts.__str__()
