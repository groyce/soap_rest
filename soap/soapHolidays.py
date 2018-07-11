from __future__ import print_function
import zeep

# display a title
print("Print Holiday Dates for a Year")
print()

# get input from the user
country = (input("Enter country Code\t\t"))
year =  (input("Enter year\t\t"))

# obtain results
client = zeep.Client(
    wsdl='http://www.holidaywebservice.com/HolidayService_v2/HolidayService2.asmx?WSDL')

dollars = (client.service.GetHolidaysForYear(country,year))

#print result
print (dollars)