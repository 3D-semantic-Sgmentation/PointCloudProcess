import numpy as np
import open3d as o3d
import glob



def show_point_clouds_in_voxel():
    voxel_size = 0.02
    pcds = []
    for f in glob.glob("../Toronto_3D/*.ply"):
        print(f)
        pcd = o3d.io.read_point_cloud(f)
        pcd_down = pcd.voxel_down_sample(voxel_size=voxel_size)
        pcds.append(pcd_down)

    # Visualize the point cloud within open3d
    o3d.visualization.draw_geometries(pcds,
                                      zoom=0.3412,
                                      front=[0.4257, -0.2125, -0.8795],
                                      lookat=[2.6172, 2.0475, 1.532],
                                      up=[-0.0694, -0.9768, 0.2024])


def show_point_clouds_in_points(path):
    # Read .ply file
    pcds = []
    for f in glob.glob(path):
        pcd = o3d.io.read_point_cloud(f)  # Read the point cloud
        print(type(pcd))
        print(f)
        pcds.append(pcd)
    # Visualize the point cloud within open3d
    o3d.visualization.draw_geometries(pcds)

    # Convert open3d format to numpy array
    # Here, you have the point cloud in numpy format.
    # point_cloud_in_numpy = np.asarray(pcds.points)

def demo_crop_geometry(path):
    print("Demo for manual geometry cropping")
    print(
        "1) Press 'Y' twice to align geometry with negative direction of y-axis"
    )
    print("2) Press 'K' to lock screen and to switch to selection mode")
    print("3) Drag for rectangle selection,")
    print("   or use ctrl + left click for polygon selection")
    print("4) Press 'C' to get a selected geometry and to save it")
    print("5) Press 'F' to switch to freeview mode")
    pcd = o3d.io.read_point_cloud(path)
    print(pcd)
    #pcd.paint_uniform_color([0.5, 0.5, 0.5])
    o3d.visualization.draw_geometries([pcd])
    #o3d.visualization.draw_geometries_with_editing([pcd])



if __name__ == "__main__":
    #path = "../Toronto_3D/*.ply"
    path = "../TUM-MLS/labeled/class.pcd"
    #show_point_clouds_in_points(path)
    demo_crop_geometry(path)
    # Crop point cloud

    # write a new file
    # o3d.io.write_point_cloud("copy_of_fragment.pcd", pcd)

    #show_point_clouds_in_points(path)
