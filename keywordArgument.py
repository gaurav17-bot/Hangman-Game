def key(greeding,first,last):
    print(f"{greeding} {first} {last}")

key("hello","gaurav","adhikari")
key("Hello",first="Ram",last="karki") #keyword argument


#to generate phone number

def phNumber(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

number=phNumber(country=977,area=9868,first=698,last=820)
print(number)