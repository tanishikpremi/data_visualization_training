from three_Dfigures import cuboid_csa ,cuboid_tsa, cuboid_volume

print("--- Cuboid Calculator ---")
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

csa = cuboid_csa(length, width, height)
tsa = cuboid_tsa(length, width, height)
volume = cuboid_volume(length, width, height)

print(f"\nCurved/Lateral Surface Area: {csa:.2f}")
print(f"Total Surface Area: {tsa:.2f}")
print(f"Volume: {volume:.2f}")