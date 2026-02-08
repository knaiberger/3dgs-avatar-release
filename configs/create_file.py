import sys

method = sys.argv[1]
image = sys.argv[2]
distort = sys.argv[3]

name = "camerahmr_"+method+"_"+image+"_"+distort

if(method == "multiple"):
	with open("ps_camera/"+name+".yaml", "w") as f:
		f.write("# @package _global_\ncamera_name: "+name+"\ndataset:\n   camera_type: "+name+"_no_arah/"+name)
else:
	with open("ps_camera/"+name+".yaml", "w") as f:
		f.write("# @package _global_\ncamera_name: "+name+"\ndataset:\n   camera_type: "+name+"_no_arah/"+name+".pkl")

with open("ps_smpl/"+name+".yaml", "w") as f:
  f.write("# @package _global_\nsmpl_model_name: "+name+"\ndataset:\n   smpl_model_path: "+name)
