To run the python script for Blender which converts blender data to Pysoy

Steps to Setup Blender:
1. Download Blender tarball from: http://www.blender.org/download/ (Note that the work was tested in Blenderv2.74.0, unless blender has drastically changed you must be able to run it on any latest Blender)
2. Extract it using either any Archive Manager or run cmd:
$tar xvjf filename.tar.bz2
3. Open Terminal, go to this folder location you just extracted, run cmd: 
$./blender

Steps to setup PySoy scripts below:
1. Copy the pysoy module "soy.cpython-34m.so" from python packages location:
	'$/usr/lib/python3.*' or '$/usr/lib/python3.*/dist-packages'
to your blender folder you extracted initially:
	'$/your-blender-path/2.*/scripts/modules' or '$/your-blender-path/2.*/python/lib/python3.4'
*: Represents the version of python and blender you have downloaded or installed in your system.
2. Go to "User Preferences" inside Blender, tab "File", and specify '$/your-pysoy-path/plugins/blender2k15', in the "scripts" input.

Steps to run the script:
1. Change the Blender screen to 'Scripting' in the top Screen Layout.
2. In the Text Editor window, click 'open a new text block' button.
3. Go to the location of the script 'blender_server.py' in '$/your-pysoy-path/plugins/blender2k15/addons' and click open text block.
4. Model your mesh in Blender, design the game level.
5. Click 'Run Script' to convert it to PySoy meshes stored in 'pysoy_client.py' in the same folder.

Steps to use it as an addon(for easier workflow):
1. Go to "User Preferences" inside Blender, tab "Addon".
2. Type "pysoy" in search or look for the addon in the "Mesh" category.
3. Tick the enable addon to the right.
4. Save user settings, for this to be available everytime you open Blender.
5. You can find the addon in the "View3D" Header section appended towards the right of the 3D View Editor type.
6. To see the generated pysoy file, change the Screen Layout to "Scripting" and see the "Text Editor"
