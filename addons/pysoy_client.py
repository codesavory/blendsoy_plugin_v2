import soy
import pickle
from time import sleep

import pickle
with open('mesh_data.pik', 'rb') as f:
    meshes, mesh_vertices, mesh_faces = pickle.load(f)

#Printing meshes
for i in range(len(meshes)):
	print(meshes[i])

#Printing mesh vertices
for i in range(len(mesh_vertices)):
	print(mesh_vertices[i])
	print("\n")

#Printing mesh faces
for i in range(len(mesh_faces)):
	print(mesh_faces[i])
	print("\n")

#Pysoy environment creation
client = soy.Client()
room = soy.scenes.Room(soy.atoms.Size((30.0,30.0,30.0)))
room['cam'] = soy.bodies.Camera((0,0,25))
client.window.append(soy.widgets.Projector(room['cam']))
room['light'] = soy.bodies.Light((0, 0, 5))
m1 = soy.materials.Colored("red")
m2 = soy.materials.Colored("green")
m3 = soy.materials.Colored("blue")
m4 = soy.materials.Colored("yellow")

i=0
for mesh in meshes:
	room[mesh] = soy.bodies.Mesh()
	#room[mesh].addTorque(10,7,9)
	for j in range(len(mesh_faces[i])):
		v1=soy.atoms.Vertex(soy.atoms.Position(mesh_vertices[i][mesh_faces[i][j][0]]),soy.atoms.Vector((0,0,0)) ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
		v2=soy.atoms.Vertex(soy.atoms.Position(mesh_vertices[i][mesh_faces[i][j][1]]),soy.atoms.Vector((0,0,0)) ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
		v3=soy.atoms.Vertex(soy.atoms.Position(mesh_vertices[i][mesh_faces[i][j][2]]),soy.atoms.Vector((0,0,0)) ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
		f1=soy.atoms.Face(v1,v2,v3,m1)
		room[mesh].append(f1)
	i+=1
print("Completed Rendering PySoy Scene of blender.")

if __name__ == '__main__' :
	while client.window :
		sleep(.1)
