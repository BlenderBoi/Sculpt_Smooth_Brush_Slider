
import bpy

bl_info = {
    "name": "Sculpt Smooth Strength Slider",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (3, 00, 0),
    "location": "Sculpt Toolbar",
    "description": "Expose Sculpt Smooth Brush's Strength Slider in Toolbar, so that it can be access no matter which brush you are using ",
    "warning": "",
    "doc_url": "",
    "category": "Tools",
}

def add_smooth_slider(self, context):
    layout = self.layout

    Smooth_Brush = bpy.data.brushes.get("Smooth")

    if context.mode == "SCULPT":
    

        if Smooth_Brush:
            layout.prop(Smooth_Brush, "strength",  text="Smooth Strength", icon="BRUSH_SMOOTH"  )



def register():



    bpy.types.VIEW3D_HT_tool_header.prepend(add_smooth_slider)





def unregister():


    bpy.types.VIEW3D_HT_tool_header.remove(add_smooth_slider)




if __name__ == "__main__":
    register()
