
import cv2                  # OpenCV library for image processing
import numpy as np  # NumPy for numerical operations on arrays/matrices
import pandas as pd
import matplotlib.pyplot as plt  # Matplotlib for visualizations
import os


folder_path = "C:\\Users\\kulsum kamal\\Downloads\\license plate detection\\images"

# Get list of files in the folder
file_list = os.listdir(folder_path)

# Filter the files to only include image files
image_files = [file for file in file_list if file.endswith(
    ".jpg") or file.endswith(".jpeg") or file.endswith(".png")]
images = []

# Loop through each image file and read it using cv2.imread
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)
    images.append([image, image_file])


boundaries = pd.read_csv('boundaries.csv')
boundaries.columns = ['id', 'xmin', 'ymin', 'xmax', 'ymax', 'image']

folder_path = "C:\\Users\\kulsum kamal\\Downloads\\license plate detection\\masks"

for index, row in boundaries.iterrows():
    image = images[index][0]

    # Create a NumPy array of zeros with the same shape as the input image
    mask = np.zeros_like(image)

    # Extract the boundary coordinates from the row
    pts = row.values[1:5]

    # Convert the boundary coordinates to a NumPy array of shape (N,1,2), where N is the number of vertices
    boundary_pts = np.array([[pts[0], pts[1]], [pts[2], pts[1]], [
                            pts[2], pts[3]], [pts[0], pts[3]]], dtype=np.int32)

    # Fill the mask with white color (255) inside the boundary region
    cv2.fillPoly(mask, [boundary_pts], (255, 255, 255))

    # Apply the mask to the input image using bitwise_and
    masked_image = cv2.bitwise_and(image, mask)

    # Construct the file name for the output image using os.path.join
    file_name = os.path.join(folder_path, images[index][1])

    # Save the masked image to the output folder
    cv2.imwrite(file_name, masked_image)
