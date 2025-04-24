faculty = ["het", "Professor", "Ankit", "Smith", "Manan", "prince"]

long_names = list(filter(lambda name: len(name) > 8, faculty))
print("Names longer than 8 characters:", long_names)
