import bpy

class InterfaceVars(bpy.types.PropertyGroup):
    angles = bpy.props.EnumProperty(
        items=[
            ('Nothing', 'Do Nothing', 'Does nothing after rendering.', '', 0),
            ('Sleep', 'Sleep', 'Puts pc to sleep after render.', '', 1),
            ('Shutdown', 'ShutdownPC', 'Shut Downs pc after rendering.', '', 2),
            ('BlendShutdown', 'Shutdown Blender', 'Shuts down blender after rendering.', '', 3),
            
        ],
        default='Nothing'
    )

