my_dict = {
    "name": "Sajeeb",
    "fav_language": "JAVA",
    "one": 1,
    'two': 2.5,
}

print(my_dict)

my_dict2 = dict(
    {
        "name": "Amirul Islam",
        "ROll": 212048,
        "section": "A",
        "Group": "Commerce",

    }
)

print(my_dict2["name"])  # Amirul Islam
print(my_dict2["Group"])  # Commerce


print(my_dict2["ROll"]) #212048

print(my_dict2.get("section")) #A

my_dict2["fav_group"] = "Scince"
print(my_dict2)
my_dict2["fav_group"] = "Arts"
print(my_dict2)

print(my_dict2.pop("Group"))
print(my_dict2)

my_dict2.clear()
print(my_dict2)

my_dict2["I Love What"] = "nothing"
print(my_dict2)