marks = {
    "Anuja": 100,
    "Anjali": 68,
    "Anagha": 56,
    "Anusha": 78, 
    "Apurva": 88,
    0:"Anu"                       
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Anuja": 99, "Naina": 100})
# print(marks)

# print(marks.get("Anuja2"))# prints none
# print(marks["Anuja2"])# returns an error

# print(marks.pop("Anuja"))#Removes by key
# print(marks)

print(marks.popitem())#Removes last item, Removes by key
print(marks)
