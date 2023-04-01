#!/usr/bin/env python
# coding: utf-8

import numpy as np  # NumPy for numerical operations on arrays/matrices
import pandas as pd
import os
import xml.etree.ElementTree as ET


folder_path = "./annotations"

# Get list of files in the folder
file_list = os.listdir(folder_path)

# Filter the files to only include XML files
xml_files = [file for file in file_list if file.endswith(".xml")]
bounding_box = []

# Loop through each XML file and do something with it (e.g. parse)
for xml_file in xml_files:
    xml_path = os.path.join(folder_path, xml_file)
    tree = ET.parse(xml_path)
    root = tree.getroot()
    child = root.findall('./object/bndbox')[0]
    boundary = [child[0].text, child[1].text,
                child[2].text, child[3].text, xml_file]
    bounding_box.append(boundary)

boundaries = pd.DataFrame(bounding_box, columns=[
                          'xmin', 'ymin', 'xmax', 'ymax', 'image'])
boundaries.head()

boundaries.to_csv('boundaries.csv')
