import glob
import json
import os
from shutil import copyfile


# edit these variables
INPUT_DIRECTORY = ''
OUTPUT_DIRECTORY = ''
IMAGE_TYPE = '.jpg'


# edit label map here
label_map = {
    'Folder0': '0',
    'Folder1': '1',
    'Folder2': '2'
}


seen_images = set()
labels = []
i = 0
for label in os.listdir(INPUT_DIRECTORY):
    print('Processing', label)
    for im_filename in glob.glob(os.path.join(INPUT_DIRECTORY, label, '*'+IMAGE_TYPE)):
        # add the label for the image
        filename = os.path.basename(im_filename).split('.')[0]
        # only process each file once, there is overlap in the classes
        i += 1
        if filename not in seen_images:
            seen_images.add(filename)
            labels.append([filename+IMAGE_TYPE, label_map[label]])
            # copy the image to the folder
            copyfile(im_filename, os.path.join(OUTPUT_DIRECTORY, filename+IMAGE_TYPE))

with open(os.path.join(OUTPUT_DIRECTORY, 'dataset.json'), 'w') as f:
    json.dump({'labels': labels}, f)

print('Processed', str(i), 'images with', str(i - len(seen_images)), 'duplicates')
