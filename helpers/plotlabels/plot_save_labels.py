# load libraries
import os
import cv2
import numpy as np
import pandas as pd
from glob import glob
import xml.etree.ElementTree as ET

import matplotlib.image as mpimg
import matplotlib.patches as patches
import matplotlib.pyplot as plt

def xml_to_csv(xml_folder, output_file=None):
    """Converts a folder of XML label files into a pandas DataFrame and/or
    CSV file.
    :param xml_folder: The path to the folder containing the XML files.
    :type xml_folder: str
    :param output_file: (Optional) If given, saves a CSV file containing
        the XML data in the file output_file. If None, does not save to
        any file. Defaults to None.
    :type output_file: str or None
    :return: A pandas DataFrame containing the XML data.
    :rtype: pandas.DataFrame
    """

    xml_list = []
    # Loop through every XML file
    for xml_file in glob(xml_folder + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        filename = root.find('filename').text
        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)

        # Each object represents each actual image label
        for member in root.findall('object'):
            box = member.find('bndbox')
            label = member.find('name').text

            # Add image file name, image size, label, and box coordinates to CSV file
            row = (filename, width, height, label, int(box[0].text),
                   int(box[1].text), int(box[2].text), int(box[3].text))
            xml_list.append(row)

    # Save as a CSV file
    column_names = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_names)

    if output_file is not None:
        xml_df.to_csv(output_file, index=None)

    return xml_df


def show_labeled_image(path, image, output, boxes, labels=None):
    """Show the image along with the specified boxes around detected objects.
    Also displays each box's label if a list of labels is provided.
    If you want to save just use 'plt.savefig(...)' instead of 'plt.show()'
    :param path: path of the image/xml files
    :param image: The image to plot. If the image is a normalized
        torch.Tensor object, it will automatically be reverse-normalized
        and converted to a PIL image for plotting.
    :type image: numpy.ndarray or torch.Tensor
    :param boxes: A torch tensor of size (N, 4) where N is the number
        of boxes to plot, or simply size 4 if N is 1.
    :type boxes: torch.Tensor
    :param labels: (Optional) A list of size N giving the labels of
            each box (labels[i] corresponds to boxes[i]). Defaults to None.
    :type labels: torch.Tensor or None
    """

    fig, ax = plt.subplots(1)
    # expects an image file
    img = mpimg.imread(path + image)
    ax.imshow(img)

    # Plot each box
    for i in range(boxes.shape[0]):
        box = boxes[i]
        width, height = (box[2] - box[0]).item(), (box[3] - box[1]).item()
        initial_pos = (box[0].item(), box[1].item())
        rect = patches.Rectangle(initial_pos,  width, height, linewidth=1,
                                 edgecolor='r', facecolor='none')
        if labels:
            ax.text(box[0] + 5, box[1] - 5, '{}'.format(labels[i]), color='red')

        ax.add_patch(rect)

    # uncomment below line to show the plots
    #plt.show()
    # comment below line if you don't want to save
    plt.savefig(path + output)

# set folder paths, output files etc.
folder = 'C:/Continuum/Anaconda3/envs/innventure/workspace/certificates/test/'
output_file = folder + 'bounding_boxes.csv'

# dataframe with filename, class, bounding box coordinates etc.
df = xml_to_csv(folder, output_file)

# iterate through every image in folder
for img in os.listdir(folder):
    # filter images
    if '.jpg' in img:
        # identify file name
        f = img.split('/')[-1]
        o = f.split('.')[0]
        # set output file with bounding boxes
        o += '_bb.jpg'

        # set labels & boxes
        labels = list(df['class'].loc[df.filename == f].values)
        boxes = df[['xmin', 'ymin', 'xmax', 'ymax']].loc[df.filename == f].values

        #print(folder+img)
        show_labeled_image(folder, img, o, boxes, labels)

