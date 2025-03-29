capitals={"Nepal":"Kathmandu","India":"Delhi"}
# print(capitals)


# print(capitals.get("Nepal"))


# capitals.update({"China":"Bejing"})
# print(capitals)


# capitals.pop("India")
# print(capitals)


# capitals.popitem()
# print(capitals)


# keys=capitals.keys()
# print(keys)

# #for print iterative

# for key in capitals.keys():
#     print(key)

# values=capitals.values()
# print(values)



capitals.update({"France":"Paris","Pakistan":"Islamabad","Srilanka":"Colombo"})
print(capitals)

items=capitals.items()
for key,value in capitals.items():
    print(f"{key}:{value}")