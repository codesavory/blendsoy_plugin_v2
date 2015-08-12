#This file generates mesh_vertices.txt which contains the vertices of all the meshes in Blender Scene
import bpy
def create_vertices():#This Function generates the vertices w.r.t to the initial position of creation of the mesh
	print("-------------------------------------")
	f=open('mesh_vertices.txt','w')
	for mesh in bpy.data.meshes:
	    	#print(mesh.name)
	    	f.write(mesh.name)
	    	f.write('\n')
	    	for ver in mesh.vertices:
	        	#print("Local Vertices:",ver.co)
	        	f.write(str(ver.co.x)+' '+str(ver.co.y)+' '+str(ver.co.z)+' ')
	        	f.write('\n')
	    	f.write('\n')
	f.close()

def create_global_vertices():#This Function generates the vertices w.r.t to the global position of the mesh
	#print("-------------------------------------")
	f=open('mesh_vertices.txt','w')
	for mesh in bpy.data.meshes:
		obj=mesh.name
		#print(mesh.name)
		f.write(mesh.name)
		f.write('\n')
		for ver in mesh.vertices:
			local_co = ver.co
			global_co = bpy.data.objects[obj].matrix_world * local_co
			#print("Global Vertices:",global_co)
			f.write(str(global_co[0])+' '+str(global_co[1])+' '+str(global_co[2])+' ')
			f.write('\n')
		f.write('\n')
	f.close()

if __name__=="__main__":
    create_global_vertices()
