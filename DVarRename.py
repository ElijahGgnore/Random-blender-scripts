bl_info = {
    "name": "Driver variable rename",
    "author": "",
    "version": (1, 0),
    "blender": (3, 5),
    "location": "View3D > Sidebar > Edit",
    "description": "rename driver variables",
    "category": "3D View"}

import bpy
from bpy.types import bpy_prop_collection



class DVARRENAME_PT_rename_driver_var(bpy.types.Panel):
    bl_label = "Rename a driver variable"
    bl_category = "Edit"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="My Select Panel")

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label(text="Selection Tools")
        box.operator("object.select_all").action = 'TOGGLE'
        row = box.row()
        row.operator("object.select_all").action = 'INVERT'
        row.operator("object.select_random")


def register():
    bpy.utils.register_class(DVARRENAME_PT_rename_driver_var)


def unregister():
     bpy.utils.unregister_class(DVARRENAME_PT_rename_driver_var)

    
def rename(oldname, newname):
    
    def rename(col):
        for o in col:
            ad = getattr(o, "animation_data", None)
            if not ad:
                continue
            for d in ad.drivers:
                for v in d.driver.variables:
                    print(v.targets[0].data_path)
                    if (
                        v.type == 'SINGLE_PROP'
                        and v.targets[0].data_path == f'{oldname}' ):
                            
                        v.targets[0].data_path = f'{newname}'
    while next(filter(None, (
        rename(getattr(bpy.data, p)) 
        for p in  dir(bpy.data) 
        if isinstance(
                getattr(bpy.data, p, None), 
                bpy_prop_collection
                )                
        )
        ), None):
            continue
      
if __name__ == "__main__":
#   register()
    rename('pose.bones["Blades2_unfold1"].location[2]', 'pose.bones["Blades2_unfold"].location[2]')