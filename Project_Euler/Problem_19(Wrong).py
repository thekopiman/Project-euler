#!/usr/bin/env python3
'''
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''



class SundayCalculation():
    def __init__(self, starting_year = 1901, ending_year = 2000):
        self.starting_year = starting_year
        self.ending_year = ending_year + 1
        self.years = {}

        for year in list(range(self.starting_year, self.ending_year)):
            if self.leap_year(year):
                self.years[year] = 366
            else:
                self.years[year] = 365

        # number_of_days = sum([x for x in self.years.values()]) # 36524


    def leap_year(self, year):
        '''
        Returns True or False
        '''
        if year%4 == 0:
            if year%100 == 0:
                if year%400 == 0:
                    return False
                else: return True
            else: return True
        else: return False
    
    def check_sunday(self, days, using_1900_as_reference = True):
        '''
        Returns True or False
        '''
        if using_1900_as_reference:
            if (days + 366)%7 == 0:
                return True
            else: return False
        else:
            if days%7 == 0:
                return True
            else: return False
    def first_day_of_month(self):
        '''
        Creates a list of days which is the first day of the month
        '''
        days = [1]
        for year in self.years:
            for month in range(1,13):
                try:
                    days.append(self.days_in_a_month(self.years[year], month) + days[-1])
                except TypeError:
                    continue
        return days
    
    def days_in_a_month(self, year, month : int):
        '''
        month is in int (Eg. Jan = 1, Feb = 2 ...)
        '''
        if month == 2:
            if self.leap_year(year):
                return 29
            else: return 28
        elif month == 9 or  month == 4 or month == 6 or month == 11:
            return 30
        else: return 31




if __name__ == "__main__":
    trial1 = SundayCalculation()
    counter = 0
    for day in trial1.first_day_of_month():
        if trial1.check_sunday(day):
            print(day)
            counter += 1
    
    print(counter) #172
