import math

# --- CUBE ---
def cube_csa(side): return 4 * (side ** 2)
def cube_tsa(side): return 6 * (side ** 2)
def cube_volume(side): return side ** 3

# --- CUBOID ---
def cuboid_csa(l, w, h): return 2 * h * (l + w)
def cuboid_tsa(l, w, h): return 2 * (l*w + w*h + h*l)
def cuboid_volume(l, w, h): return l * w * h

# --- CYLINDER ---
def cylinder_csa(r, h): return 2 * math.pi * r * h
def cylinder_tsa(r, h): return 2 * math.pi * r * (r + h)
def cylinder_volume(r, h): return math.pi * (r ** 2) * h

# --- CONE ---
def cone_csa(r, h):
    slant_height = math.sqrt(r**2 + h**2)
    return math.pi * r * slant_height

def cone_tsa(r, h):
    slant_height = math.sqrt(r**2 + h**2)
    return math.pi * r * (r + slant_height)

def cone_volume(r, h): return (1/3) * math.pi * (r ** 2) * h

# --- SPHERE ---
def sphere_csa(r): return 4 * math.pi * (r ** 2)
def sphere_tsa(r): return 4 * math.pi * (r ** 2) 
def sphere_volume(r): return (4/3) * math.pi * (r ** 3)

# --- HEMISPHERE ---
def hemisphere_csa(r): return 2 * math.pi * (r ** 2)
def hemisphere_tsa(r): return 3 * math.pi * (r ** 2)
def hemisphere_volume(r): return (2/3) * math.pi * (r ** 3)