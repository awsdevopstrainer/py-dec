state_lang = {
    "kerala": "malayalam",
    "tamilnadu": "tamil",
    "andra": "telugu",
    "karnataka": "kannada",
}

# print(state_lang)
# print(type(state_lang))

# print(state_lang["kerala"])

# to add 
state_lang["maharashtra"] = "marathi"

# update
# state_lang["karnataka"] = "tulu"

# print(state_lang)

# del state_lang["andra"]

# print(state_lang)

# for langs in state_lang:
#     print(state_lang[langs])

# print(dir(state_lang))

# print(state_lang.keys())

# print(state_lang.values())

# print(state_lang.pop("kerala"))
# print(state_lang)


newstate = {
    "west_bengal": "bengali",
    "odissha": "oriya"
}

print(newstate)

state_lang.update(newstate)

print(state_lang)
