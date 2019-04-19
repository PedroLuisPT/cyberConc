# 2018-2019 Programação 2 (LTI)
# Grupo 055
# 53327 Jorge Roque
# 53469 Pedro Luís

class DateTime:

    def __init__(self,hoursMinutes):
        """
        Creates the time and splits it into hours and minutes
        Requires:
            .hoursMinutes, string of the time
        Ensures:
            . string with the hours and minutes
        """

        self._hoursMinutes = hoursMinutes
        

    def get_hoursMinutes(self):
        """
        Gets Date Time´s string representation of the hours and minutes
        """
        return self._hoursMinutes

    

    def set_hoursMinutes(self,newHoursMinutes):
        """
        Sets the newHoursMinutes into the current representation of the HoursMinutes
        Requires: newHoursMinutes, str representation of hoursMinutes
        """
        self._hoursMinutes=newHoursMinutes


    
    def get_hours(self,hoursMinutes):
        """
        Gets the hours from the hours and minutes str representation
        Requires:
                .hoursMinutes, str representation of the hours and minutes (hh:mm)
        """
        hoursMinutes = hoursMinutes.replace("h", ":")
        hoursMinutes = hoursMinutes.split(":")
        hours = int(hoursMinutes[0])                                                                                                        #this lines firstly replace the h with :, then it splits the hoursMinutes into two(hours[0],minutes[1]) HH:MM and return only the hours
        return hours


    def get_minutes(self,hoursMinutes):
        """
        Gets the minutes from the hours and minutes str representation
        Requires:
                .hoursMinutes, str representation of the hours and minutes (hh:mm)
        """
        hoursMinutes = hoursMinutes.replace("h", ":")
        hoursMinutes = hoursMinutes.split(":")
        minutes = int(hoursMinutes[1])                                                                                                      #this lines firstly replace the h with :, then it splits the hoursMinutes into two(hours[0],minutes[1]) HH:MM and return only the minutes
        
        return minutes

    
    def numberofMinutes(self,hoursMinutes):
        """
        Turns the str type hoursMinutes into a number of minutes
        Requires:
            .hoursMinutes, str type of the hours and minutes HH:MM
        Ensures:
            .a number of hours + minutes into only minutes
        """
        hours = self.get_hours(hoursMinutes) * 60
        minutes = self.get_minutes(hoursMinutes)                                                                                            #by now it has got the hours and minutes 
        totaltime = hours + minutes                                                                                                         #it now sums the hours and minutes into a number of minutes
        return totaltime

    

    def add_minutes(self,date,hm,added):
        """
        Adds the added value (minutes to add) to the time and gets a string with the updated time in a HHhMM form 
	Requires:
            .date, string with date in year-month-days form, 
            .hm, string with time in hours-minutes form,
            .added, int with the increment in minutes
	Ensures:
            .list with the date in year-month-day type and with the time in hour:minutes with the added value
        """
        hours=self.get_hours(hm)+(added //60)
        minutes=self.get_minutes(hm) + (added % 60)
        year, month, day = date.split('-')
        year=int(year)
        month=int(month)
        day=int(day)

        
        if minutes >= 60:                                                                       #if the number of minutes of past 60 it adds to the next hour the number of minutes left
            while minutes >=60:
                minutes = minutes - 60
                hours = hours + 1

        if hours >= 20:                                                                         #checks if it is necessary to change the hour, day, mont or year
            while hours >= 20:
                    hours = hours - 12
                    day =day+1
                    if day > 30:
                        day = day - 30
                        month =month+ 1
                        if month > 12:
                            year = year + 1
        
        if minutes >= 0 and minutes <= 9:                                                       #adds a 0 if the minutes are bellow or equal to 9 so it appears like 09 minutes
            minutes = '0' + str(minutes)                
            
        if hours >= 0 and hours <= 9:                                                           #adds a 0 if the hours are bellow or equal to 9 so it appears like 09 hours
            hours = '0' + str(hours)

        if month >= 1 and month <= 9:                                                           #adds a 0 if the month is bellow than 9 so it appears like 09 month (september)

            month = "0" + str(month)
            
        if day >= 1 and day <= 9:                                                               #adds a 0 if the day is bellow or equal to 9 so it appears like 09 day
            day = "0" + str(day)


        finalDate = str(year) + '-' + str(month) + '-' + str(day)
        finalTime = str(hours) + ":" + str(minutes)
        return finalDate, finalTime
        

    def __str__(self):
        """
        The string representation of the hoursMinutes (HH:MM)
        """

        return self._hoursMinutes
