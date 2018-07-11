from __future__ import print_function
import zeep

# display a title
print("Convert number to text/dollars")
print()

# get input from the user
dollar_number= float(input("Enter number of dollars\t\t"))

# obtain results
client = zeep.Client(
    wsdl='http://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL')

dollars = (client.service.NumberToDollars(dollar_number))

#print result
print (dollars)