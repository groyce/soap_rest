from __future__ import print_function
import zeep

# display a title
print("Print Holiday Dates for a Year")
print()

# get input from the user
country = (input("Enter country Code\t\t"))


# obtain results
client = zeep.Client(
    wsdl='http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')

countryInfo = (client.service.FullCountryInfo(country))

#print result
print (countryInfo)