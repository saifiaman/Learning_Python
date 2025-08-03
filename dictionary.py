# Dictionary in Python = a Collection of key-value pairs
# Dictionary is mutable, unordered, and indexed

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "Japan": "Tokyo",
    "France": "Paris"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))
# Returns "Not Found" if key doesn't exist
print(capitals.get("Germany", "Not Found"))
# Returns None if key doesn't exist
print(capitals.get("Germany"))

capitals.update({"Germany": "Berlin"})
capitals.popitem()
# capitals.clear()
print(capitals)

for key, value in capitals.items():
    print(f"{key} - {value}")
