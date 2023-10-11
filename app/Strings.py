course = 'Python for "Beginners"'
another = course[:]
print(another)

# Formatted Strings

first = "Zackary"
last = "Hughes"
message = first + " [" + last + "] is a coder."
msg = f"{first} [{last}] is a coder."
print(message)
print(msg)

# String Methods

course = 'Python for "Beginners"'
print(len(course))

print(course.upper())
print(course.title())
print(course)

print(course.replace("Beginners", "Absolute Beginners"))

print("Python" in course)
print("python" in course)

