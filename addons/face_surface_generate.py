#This file generates face_surface.txt, which reads a mesh in Blender scene and generates the surface i.e., it reads all the faces of the mesh and finds out which all vertices are used to create each face.
import bpy
def create_face_vertices():
	f=open("face_surface.txt",'w')        
	for mesh in bpy.data.meshes:
		#print(mesh.name)
		#print(len(mesh.polygons))
		f.write(mesh.name)
		f.write('\n')
		for face in mesh.polygons:
			if(len(face.vertices)==3):
				for vert in face.vertices:
					f.write(str(mesh.vertices[vert].index)+' ')

			elif(len(face.vertices)==4):
				f.write(str(mesh.vertices[face.vertices[0]].index)+' ')
				f.write(str(mesh.vertices[face.vertices[1]].index)+' ')
				f.write(str(mesh.vertices[face.vertices[2]].index)+' ')
				f.write('\n')
				f.write(str(mesh.vertices[face.vertices[0]].index)+' ')
				f.write(str(mesh.vertices[face.vertices[2]].index)+' ')
				f.write(str(mesh.vertices[face.vertices[3]].index)+' ')
			
			'''for vert in face.vertices:
				print(str(mesh.vertices[vert].index)+' ')
			n=input("continue?")
			if(n=='\n'):
				continue'''
			f.write('\n')
		f.write('\n')
	f.close()

if __name__=="__main__":
    create_face_vertices()
