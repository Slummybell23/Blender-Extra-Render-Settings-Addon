import bpy

class InterfaceVars(bpy.types.PropertyGroup):
    angles = bpy.props.EnumProperty(
        items=[
            ('Nothing', 'Do Nothing', 'Does nothing after rendering.', '', 0),
            ('Sleep', 'SLeep', '30', '', 1),
            ('Shutdown', 'ShutdownPC', '60', '', 2),
            ('BlendShutdown', 'Shutdown Blender', '90', '', 3),
            
        ],
        default='Nothing'
    )

