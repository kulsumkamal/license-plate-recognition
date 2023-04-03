# License Plate Recognition using Image Segmentation

This project aims to build a License Plate Recognition (LPR) system using image segmentation techniques. We used a dataset of 433 images collected from Kaggle.

## Dataset

The dataset consists of 433 images of vehicles with their license plates in different locations, orientations, and lighting conditions. The dataset is divided into a training set of 346 images and a test set of 87 images. The dataset can be downloaded from https://www.kaggle.com/datasets/andrewmvd/car-plate-detection .

## Installation

To clone the repo, run the following command in your terminal:

```bash
git clone https://github.com/kulsumkamal/license-plate-recognition.git
```

## Usage

To extract masks on the train images, run the following command:

```bash
mask_extraction.py
```

To train the segment model, open the Image segmentation.ipynb file by opening the jupyter terminal:

```bash
jupyter notebook
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

We would like to thank Kaggle for providing the dataset used in this project.
