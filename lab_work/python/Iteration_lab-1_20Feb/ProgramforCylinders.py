from three_Dfigures import cylinder_csa,cylinder_tsa,cylinder_volume

print("--- Cylinder Calculator ---")
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

csa = cylinder_csa(radius, height)
tsa = cylinder_tsa(radius, height)
volume = cylinder_volume(radius, height)

print(f"\nCurved Surface Area: {csa:.2f}")
print(f"Total Surface Area: {tsa:.2f}")
print(f"Volume: {volume:.2f}")