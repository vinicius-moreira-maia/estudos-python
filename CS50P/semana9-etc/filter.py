students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

"""
def is_gryffindor(s):
    return s["house"] == "Gryffindor" # retorna True ou False
"""

# o parâmetro 's' é cada elemento do iterável 'students'
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
print(list(gryffindors))

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
