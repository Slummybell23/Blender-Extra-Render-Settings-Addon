import bpy

class SelectPanal(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    #BL lable is the side bar lable.
    bl_label = "After Render Settings"
    bl_idname = "OBJECT_PT_ERsettings"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Extra Render Settings"

    def draw(self, context):
        #Draws all the icons
        row = self.layout.row()
        row.prop(context.window_manager.interface_vars, 'angles', expand=True)
        self.layout.operator("object.rotation", text="Save")
    







        # layout = self.layout


        # row = layout.row()
        # row.operator('render.nothing', text="Do nothing")


        
        # row = layout.row()
        # row.operator('render.shutdown', text="Shutdown")        
        
        # row = layout.row()
        # row.operator('render.sleep', text="Sleep")

        # row = self.layout.row()
        # row.prop(context.window_manager.interface_vars, 'angles', expand=True)
        # row.prop(context.window_manager.interface_vars, 'direction', expand=True)
        # 