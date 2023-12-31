import bpy

def capitalize_first(string):
    for i,s in enumerate(string):
        if s.isalpha():
            return string[:i] + string[i].upper() + string[i+1:]


for obj in bpy.data.objects:
    obj.name = capitalize_first(obj.name).strip()
for sc in bpy.data.collections:
    sc.name = capitalize_first(sc.name).strip()
for mesh in bpy.data.meshes:
    mesh.name = capitalize_first(mesh.name).strip()
for mat in bpy.data.materials:
    mat.name = capitalize_first(mat.name).strip()
capitalize_first