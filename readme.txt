To run the python script for Blender which converts blender data to Pysoy

Steps to Setup Blender:
1. Download Blender tarball from: http://www.blender.org/download/ (Note that the work was tested in Blenderv2.74.0, unless blender has drastically changed you must be able to run it on any latest Blender)
2. Extract it using either any Archive Manager or run cmd:
$tar xvjf filename.tar.bz2
3. Open Terminal, go to this folder location you just extracted, run cmd: 
$./blender
4. You will now be running Blender, you can have fun with it here.

Steps to setup PySoy scripts below:
1. Copy the pysoy module "soy.cpython-34m.so" from python packages location:
	'$/usr/lib/python3.*' or '$/usr/lib/python3.*/dist-packages'
to your blender folder you extracted initially:
	'$/your-blender-path/2.*/scripts/modules' or '$/your-blender-path/2.*/python/lib/python3.4'
*: Represents the version of python and blender you have downloaded or installed in your system.
2. Go to "User Preferences" inside Blender, tab "File", and specify '$/your-pysoy-path/plugins/blender2k15', in the "scripts" input.

Steps to run the script:
1. Change the Blender screen to 'Scripting' on the top tool bar.
2. In the Text Editor window, click 'open a new text block' button to the right.
3. Go to the location of the script 'ds_pysoy_modeller.py' in '$/yourblenderpath/2.*/scripts/addons' and click open text block.
4. Click 'Run Script' to convert it to PySoy code.

Warning: Blender might crash running the above scripts. Nothing to worry.
