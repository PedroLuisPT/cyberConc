# 2018-2019 Programação 2 (LTI)
# Grupo 055
# 53327 Jorge Roque
# 53469 Pedro Luís

from FilesReading import FilesReading
from DateTime import DateTime

class FilesWriting:

    def __init__(self):
        """
        """
        pass

    def write_experts(self, header, experts):
        """
        Writes the experts in a file with header
        Requires:
            .header, correspondent to the experts
            .experts, output from the scheduling
        """
        
        hm=DateTime(header[1]).add_minutes(header[0], header[1],30)
        date=header[0].split('-')
        filename = str(date[0])+'y'+ str(date[1])+'m'+ str(date[2])+ "experts" + str(hm[1]).replace(':','h') + ".txt"                           #gets the final file name with the date with the type YYYYyMMmDD then the "experts" string then the hour updated
        
        
        file=open(filename,'w')
        file.write('Day:\n')
        file.write(hm[0] + '\n')
        file.write('Time:\n')
        file.write(hm[1] + '\n')
        file.write('Company:\n')
        file.write(header[2] + '\n')
        file.write('Experts:')
        file.write('\n')                                                                                                                        #the header at the end of the lines above is now written in the file with the updated hour

        for line in experts:
            file.write(str(line))                                                                                                               #in this line i am writting into the file the line by line of the experts and switching line with \n
            file.write("\n")

       
        file.close()  


        
    def write_scheduling(self, header, schedule):
        """
        Writes the schedule in a file with header
        Requires:
            .header, correspondent to the schedule
            .schedule, output from the scheduling()
        """
        
        hm=DateTime(header[1]).add_minutes(header[0],header[1],30)
        date=header[0].split('-')
        filename = str(date[0])+'y'+ str(date[1])+'m'+ str(date[2])+ "schedule" + str(hm[1]).replace(':','h') + ".txt"                      #gets the final file name with the date with the type YYYYyMMmDD then the "schedule" string then the hour updated
        
        file=open(filename,'w')
        file.write('Day:\n')
        file.write(hm[0] + '\n')
        file.write('Time:\n')
        file.write(hm[1] + '\n')
        file.write('Company:\n')
        file.write(header[2] + '\n')
        file.write('Schedule:')
        file.write('\n')                                                                                                                    #the header at the end of the lines above is now written in the file with the updated hour
        
        for line in schedule:
            file.write(str(line).replace('[','').replace(']','').replace("'",''))                                                           #in this line i am writting the line by line of the scheduling and replacing the [,] and ' with blank 
            file.write("\n")
        file.close()
