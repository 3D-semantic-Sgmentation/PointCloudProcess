
import numpy as np
import pandas as pd
from plyfile import PlyData, PlyElement




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
        print(name)
        data_np[:, i] = data_pd[name]
    return data_np


if __name__ == "__main__":
    #path = "../Toronto_3D/*.ply"
    path = "../Toronto_3D/L001.ply"
    read_ply_with_parameters(path)
    #show_point_clouds_in_points(path)
