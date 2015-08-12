#This is the main file, which combines all the generator file to model the Blender mesh in PySoy.
import bpy
import os
import soy
from time import sleep
from mesh_vertices_generate import *
from face_surface_generate import *

#generate the face mesh file
create_face_vertices()
        
#generate the mesh vertices file
create_global_vertices()

def coord(vertex_no,mesh):
	global c_mesh
	c_mesh=verts[0]
	no=0
	skip_flag=0
	for i in range(1,len(verts)-1): #range(1,len) since the 1st line of the file is mesh name and last line is '\n'
		if verts[i] == '\n':
			c_mesh=verts[i+1]
			no=0
			skip_flag=1

		elif verts[i] != '\n' and c_mesh==mesh:
			if skip_flag==0:
				if int(vertex_no)==no:
					verts_co=verts[i].split()
					verts_co[0]=float(verts_co[0])
					verts_co[1]=float(verts_co[1])
					verts_co[2]=float(verts_co[2])
					return(verts_co)
				no+=1 #because the first vertex index= 0
			else:
				skip_flag=0

#Finding Blender Path
path=bpy.app.binary_path
path=path.rstrip(path[-7:])

#open the face mesh file
f=open(path+'face_surface.txt','r')
faces = f.readlines()
mesh=faces[0]#Read the 1st Mesh name

#open the mesh vertices file
v=open(path+'mesh_vertices.txt','r')
verts=v.readlines()
c_mesh=verts[0]#Read the 1st Mesh name

meshes=[]
meshes.append(verts[0])
for i in range(1,len(verts)-1):
	if verts[i] == '\n':
		meshes.append(verts[i+1])

f=open("meshes.txt",'w')
for i in range(len(meshes)):
	f.write(meshes[i])
	print(meshes[i])
f.close()
#generate the PySoy Modeller for any general mesh
#PySoy Setup
client = soy.Client()
room = soy.scenes.Room(soy.atoms.Size((8.0,8.0,8.0)))
room['cam'] = soy.bodies.Camera((0,0,25))
client.window.append(soy.widgets.Projector(room['cam']))
room['light'] = soy.bodies.Light((0, 0, 5))
m1 = soy.materials.Colored("red")
m2 = soy.materials.Colored("green")
m3 = soy.materials.Colored("blue")
m4 = soy.materials.Colored("yellow")
room[mesh] = soy.bodies.Mesh()
#room[mesh].addTorque(10,7,9)
#room[mesh].addForce(5, 0, 0)

vert_list=[]
face_list=[]
skip_flag=0
for i in range(1,len(faces)-1): #range(1,len-1) since the 1st line of the file is mesh name and last line is '\n'  
	if faces[i] == '\n':
		#room[mesh].addTorque(10,7,9)
		mesh=faces[i+1]
		room[mesh] = soy.bodies.Mesh()
		#room[mesh].addTorque(10,7,9)
		skip_flag=1
	elif faces[i] != '\n':
		if skip_flag==0:
			face_vert=faces[i].split()

			v_coord=coord(face_vert[0],mesh)
			v1=soy.atoms.Vertex(soy.atoms.Position((v_coord[0],v_coord[1],v_coord[2])),soy.atoms.Vector((0,0,0)) ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
			vert_list.append(v1)

			v_coord=coord(face_vert[1],mesh)
			v2=soy.atoms.Vertex(soy.atoms.Position((v_coord[0],v_coord[1],v_coord[2])),soy.atoms.Vector((0,0,0)) ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
			vert_list.append(v2)

			v_coord=coord(face_vert[2],mesh)
			v3=soy.atoms.Vertex(soy.atoms.Position((v_coord[0],v_coord[1],v_coord[2])),soy.atoms.Vector((0,0,0)) ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
			vert_list.append(v3)

			f1=soy.atoms.Face(v1,v2,v3,m1)
			face_list.append(f1)
			room[mesh].append(f1)
			
		else:
			skip_flag=0
print("Completed Rendering PySoy Scene of blender.")

if __name__ == '__main__' :
	while client.window :
		sleep(.1)
