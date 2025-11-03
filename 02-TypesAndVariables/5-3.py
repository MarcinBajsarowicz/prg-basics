###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input("b="))
c = int(input("c="))
volume_of_cuboid = a*b * c
surface_are_cuboid = 2 * (a*b + a*c + b*c)

print(f"The volume of cuboid equals {volume_of_cuboid}")
print(f"The surface area of cuboid equals {surface_are_cuboid}")