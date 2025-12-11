names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']
sorted_names = sorted(names, key=lambda name: name[1])

print("Sorted list:")
for name in sorted_names:
    print(name)