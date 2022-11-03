#1. Find wednesday using an index

days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
siku = list(days)
print(days[2])

#2. Using a function a find the length of the tuple.
print(len(days))

#3. Replace Thursday with Thur
siku = list(days)
siku[3] = "Thur"
days = tuple(siku)
print(days)