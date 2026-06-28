import simplemathlib as sml

v1 = sml.Vector2(3.0,4.0)
v2 = sml.Vector2(5,0)
print(v1)
print(v2)
print(v2.normalized())
print(v1.innerProduct(v2))
print(v1.crossProduct(v2))