from three_Dfigures import cone_csa , cone_tsa , cone_volume

print("--- Cone Calculator ---")
radius = float(input("Enter the radius of the base of the cone: "))
height = float(input("Enter the vertical height of the cone: "))

csa = cone_csa(radius, height)
tsa = cone_tsa(radius, height)
volume = cone_volume(radius, height)

print(f"\nCurved Surface Area: {csa:.2f}")
print(f"Total Surface Area: {tsa:.2f}")
print(f"Volume: {volume:.2f}")