#This scipt runs on the Blender side, where all the mesh data are read
import bpy
import pickle
import os

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
print("Completed Reading Blender mesh data and written to Binary File")

#Creating Command to execute PySoy File Created
path=bpy.utils.script_path_pref()
cmd="python3 "+path+"/addons/pysoy_client.py"
os.system(cmd)
