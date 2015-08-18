#PySoy Modelling addon for Blender
bl_info = {
    "name": "PySoy Modeller",
    "description": "Model meshes and pickle data to PySoy and open file in Text Editor.",
    "author": "Suriya D Murthy(codesavory)",
    "version": (1, 0),
    "blender": (2, 69, 0),
    "location": "View3D Header",
    "warning": "X Error OpenGL: Display Buffer not refreshing sometimes, when running pysoy script mutiple times from inside Blender. Use subprocesses, until fix.",
    "wiki_url": "",
    "tracker_url": "",
    "support": 'COMMUNITY',
    "category": "Mesh"
}

import bpy
import pickle
import os

class pysoy_model(bpy.types.Operator):
	"""PySoy mesh modelling script"""              # blender will use this as a tooltip for menu items and buttons.
	bl_idname = "object.pysoy_model"               # unique identifier for buttons and menu items to reference.
	bl_label = "Model meshes in scene to Pysoy"    # display name in the interface.
	bl_options = {'REGISTER', 'UNDO'}              # enable undo for the operator.

	def execute(self, context):                    # execute() is called by blender when running the operator.

		#The original modeller script starts here
		print("___________________________________________")

		#Clearing meshes that are removed from objects
		for mesh in bpy.data.meshes:
			if mesh.name not in bpy.data.objects:  
				mesh.user_clear()
				bpy.data.meshes.remove(mesh)
	
		#List of all the meshes
		meshes=[]
		for mesh in bpy.data.meshes:
			meshes.append(mesh.name)
		
		#Printing meshes
		for i in range(len(meshes)):
			print(meshes[i])
		
		#List of all the vertices of all the meshes
		mesh_vertices=[]
		i=0
		for mesh in bpy.data.meshes:
			obj=mesh.name
			#print(mesh.name)
			mesh_vertices.append([])
			for ver in mesh.vertices:
				global_co = bpy.data.objects[obj].matrix_world * ver.co
				mesh_vertices[i].append([global_co.x,global_co.y,global_co.z])
			i+=1
		
		#Printing mesh vertices
		for i in range(len(mesh_vertices)):
			print(mesh_vertices[i])
			print("\n")
	
		#List of all the faces split into 3-vertices faces for all the meshes
		mesh_faces=[]
		i=0
		for mesh in bpy.data.meshes:
			mesh_faces.append([])
			for face in mesh.polygons:
				for j in range(len(face.vertices)-2):
					mesh_faces[i].append([face.vertices[0],face.vertices[j+1],face.vertices[j+2]])
			i+=1
		
		#Printing mesh faces
		for i in range(len(mesh_faces)):
			print(mesh_faces[i])
			print("\n")
		
		#pickling data: meshes[],mesh_vertices[] and mesh_faces[]
		with open('mesh_data.pik', 'wb') as f:
			pickle.dump([meshes, mesh_vertices, mesh_faces], f, -1)
		print("Completed Reading Blender mesh data and writting to Binary File")
		
		path_to_pysoy_file=bpy.utils.script_path_pref()+"/addons/pysoy_client.py"

		#open the psoy code in Blender
		text = bpy.data.texts.load(path_to_pysoy_file)
		for area in bpy.data.screens["Scripting"].areas:
			if area.type == 'TEXT_EDITOR':
				area.spaces[0].text = text
		self.report({'INFO'}, "See 'pysoy_client.py in Scripting > Text Editor'")		

		#Creating Command to execute PySoy File Created
		cmd="python3 "+path_to_pysoy_file
		os.system(cmd)
		#The script ends here
		
		return {'FINISHED'}	# this lets blender know the operator finished successfully.

def pysoy_mesh_button(self, context):
    self.layout.operator(
        pysoy_model.bl_idname,
        text="PySoy Modeller",
        icon='MOD_MESHDEFORM')

def register():
    bpy.utils.register_class(pysoy_model)
    bpy.types.VIEW3D_HT_header.append(pysoy_mesh_button)

def unregister():
    bpy.utils.unregister_class(pysoy_model)

# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()
