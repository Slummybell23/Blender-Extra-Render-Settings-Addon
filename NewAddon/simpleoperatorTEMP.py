import bpy

class Global:
    v = "Nothing"

class No_OT_pe(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "render.nothing"
    bl_label = "Do Nothing"



    def execute(self, context):
        return {"CANCELLED", "FINISHED"}

class Shut_OT_down(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "render.shutdown"
    bl_label = "Shutdown "



    def execute(self, context):
        return {"CANCELLED", "FINISHED"}

class Sleep_OT_mode(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "render.sleep"
    bl_label = "Sleep"



    def execute(self, context):
        return {"CANCELLED", "FINISHED"}


class Rotation(bpy.types.Operator):
    bl_idname = "object.rotation"
    bl_label = "Rotate"
 
    def execute(self, context):
        print(context)
        rotationvalue = str(context.window_manager.interface_vars.angles)
        print(rotationvalue)

        Global.v = rotationvalue

        return {'FINISHED'}