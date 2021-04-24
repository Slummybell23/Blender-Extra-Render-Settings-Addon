bl_info = {
    "name": "TestPlug",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}


import bpy


from . simpleoperatorTEMP import (Global, No_OT_pe, Shut_OT_down, Sleep_OT_mode, Rotation)
from . SimplePanelTEMP    import SelectPanal
from . Interfacevars import InterfaceVars
from bpy.app.handlers import persistent

#Classes to register
classes = (
    No_OT_pe,
    SelectPanal,
    Shut_OT_down,
    Sleep_OT_mode,
    InterfaceVars,
    Rotation

)

#Function to run after a render is complete. INCLUDES IMAGE RENDERS
@persistent
def action(dummy):
    #Option selected by user
    v = Global.v
    
    print(v)
    if v == "BlendShutdown":
        bpy.ops.wm.quit_blender()
    elif v == "Shutdown":
        import os
        os.system('shutdown /p /f')
    elif v == "Sleep":
        import os
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")






def register():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)
    bpy.types.WindowManager.interface_vars = bpy.props.PointerProperty(type=InterfaceVars)
    bpy.app.handlers.render_complete.append(action)

def unregister():
    from bpy.utils import unregister_class
    bpy.app.handlers.render_complete.remove(action)
    del bpy.types.WindowManager.interface_vars
    for cls in reversed(classes):
        unregister_class(cls)



if __name__ == "__main__":
    register()
