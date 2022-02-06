
import numpy as np
import pandas as pd
from plyfile import PlyData, PlyElement
from pypcd import pypcd
# python -m pip install --user git+https://github.com/DanielPollithy/pypcd.git

# ply file
def read_ply_with_parameters(path):
    '''
    :param path: path to .ply(onlu) file
    :return: return point cloud data in array
    '''
    plydata = PlyData.read(path)
    data = plydata.elements[0].data
    print(plydata.elements)
    data_pd = pd.DataFrame(data)
    data_np = np.zeros(data_pd.shape, dtype=float)
    property_names = data[0].dtype.names
    for i, name in enumerate(property_names):
        print(name) # print parameters
        data_np[:, i] = data_pd[name]
    return data_np

# pcd file
def read_pcd_with_parameters(path):
    '''
    :param path: path to .pcd(onlu) file
    :return: return point cloud data in array
    '''
    pc = pypcd.PointCloud.from_path(path)
    pc_data = pc.pc_data
    #print(pc_data)
    pc_array = np.array([pc_data["x"], pc_data["y"], pc_data["z"]], dtype=np.float32)
    return pc_array

if __name__ == "__main__":
    #path = "../Toronto_3D/*.ply"
    #path = "../Toronto_3D/L001.ply"
    #path = "../TUM-MLS/labeled/class.pcd"
    #read_ply_with_parameters(path)
    #show_point_clouds_in_points(path)


