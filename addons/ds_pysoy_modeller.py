#from mesh_vertices_generate import *
import bpy
import soy
from time import sleep
print("___________________________________________")

#Clearing meshes that are removed from objects
for mesh in bpy.data.meshes:
	if mesh.name not in bpy.data.objects:  
		mesh.user_clear()
		bpy.data.meshes.remove(mesh)

meshes=[]
for mesh in bpy.data.meshes:
	meshes.append(mesh.name)

mesh_vertices=[]
i=0
for mesh in bpy.data.meshes:
	obj=mesh.name
	#print(mesh.name)
	mesh_vertices.append([])
	for ver in mesh.vertices:
		global_co = bpy.data.objects[obj].matrix_world * ver.co
		mesh_vertices[i].append(global_co)
	i+=1

#Printing mesh vertices
for i in range(len(mesh_vertices)):
	print(mesh_vertices[i])
	print("\n")

mesh_faces=[]
i=0
for mesh in bpy.data.meshes:
	mesh_faces.append([])
	for face in mesh.polygons:
		for j in range(len(face.vertices)-2):
			mesh_faces[i].append([face.vertices[0],face.vertices[j+1],face.vertices[j+2]])
	i+=1

#Printing 3 face
for i in range(len(mesh_faces)):
	print(mesh_faces[i])
	print("\n")

client = soy.Client()
room = soy.scenes.Room(soy.atoms.Size((12.0,12.0,12.0)))
room['cam'] = soy.bodies.Camera((0,0,15))
client.window.append(soy.widgets.Projector(room['cam']))
room['light'] = soy.bodies.Light((0, 0, 5))
m1 = soy.materials.Colored("red")
m2 = soy.materials.Colored("green")
m3 = soy.materials.Colored("blue")
m4 = soy.materials.Colored("yellow")

i=0
for mesh in bpy.data.meshes:
	room[mesh.name] = soy.bodies.Mesh()
	room[mesh.name].addTorque(10,7,9)
	for j in range(len(mesh_faces[i])):
		#pos=mesh_vertices[i][mesh_faces[i][j][0]]
		v1=soy.atoms.Vertex(soy.atoms.Position(mesh_vertices[i][mesh_faces[i][j][0]]),soy.atoms.Vector((0,0,0)) ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
		v2=soy.atoms.Vertex(soy.atoms.Position(mesh_vertices[i][mesh_faces[i][j][1]]),soy.atoms.Vector((0,0,0)) ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
		v3=soy.atoms.Vertex(soy.atoms.Position(mesh_vertices[i][mesh_faces[i][j][2]]),soy.atoms.Vector((0,0,0)) ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
		f1=soy.atoms.Face(v1,v2,v3,m1)
		room[mesh.name].append(f1)
	i+=1
print("Completed Rendering PySoy Scene of blender.")

if __name__ == '__main__' :
	while client.window :
		sleep(.1)
