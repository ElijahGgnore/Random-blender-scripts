import bpy
import bmesh

ob = bpy.context.object
me = ob.data
bm = bmesh.from_edit_mesh(me)
verts = list(bm.verts)

lowestv = verts.pop()
lowestv.select_set(False)
lowest = lowestv.co[2]

for i in verts:
    i.select_set(False)
    if i.co[2] < lowest:
        lowest = i.co[2]
        lowestv = i
lowestv.select_set(True)
bm.select_flush_mode()
bmesh.update_edit_mesh(me)