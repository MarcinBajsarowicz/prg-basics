# Seven Wonders of the World
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
seven_wonders = sorted(seven_wonders)

# Write data to the file
with open(file_name, 'w') as file:
    for item in seven_wonders:
        file.write(item + '\n')  # Write each wonder on a new line

# Now open the file and print its contents
with open(file_name, 'r') as file:
    # Read all lines and print them
    content = file.read()
    print(content)