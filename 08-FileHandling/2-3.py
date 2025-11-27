# Makes a copy of a text file and prints the content

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# Read the content of the original file
with open(original_file, 'r') as file:
    content = file.read()  # Read the entire content of the original file

# Write the content to the target file (copy)
with open(target_file, 'w') as file:
    file.write(content)  # Write the content to the target file

# Print the content to verify the copy
print("Content of the copied file:")
print(content)  # Print the content of the copied file