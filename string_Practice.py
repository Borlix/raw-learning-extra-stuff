string = "Peace is a godly gift"
print(type(string))
print(len(string))
print(string)

# Concatenation
print("godly"+"gift")
# Indexing
print(string[3])
# Slicing/Substring
print(string[11:16])
# Search
ind = string.index("gift")
print(ind)
search = string.find("godly")
print(search)
if "Peace" in string:
    print("Found!")
    
