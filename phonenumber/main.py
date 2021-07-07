import phonenumbers
number="+9175XXXXXX"
from phonenumbers import geocoder
from phonenumbers import carrier
cr= phonenumbers.parse(number, "RO")
print(carrier.name_for_number(cr, "en"))
ch = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch,"en"))
