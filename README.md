# stylegan2-ada-pytorch-tools
Some tools to make using NVLabs stylegan2 easier.


# Some useful commands to prepare data

## Resize the images and convert to 3-channel color images (! forces resolution)
```mogrify -resize 512x512! -quality 100 -define png:format=png24 -type TrueColor -path <OUTPUT_IMAGE_FOLDER> <INPUT_IMAGE_FOLDER>/*```

## Create dataset zip file for training to use
```python stylegan2-ada-pytorch/dataset_tool.py --source <INPUT_IMAGE_FOLDER> --dest <DATASET_ZIP_FILE>```

## Train the model
```python stylegan2-ada-pytorch/train.py --outdir=<MODEL_DIRECTORY> --data=<DATASET_ZIP_FILE> --mirror=1 --cond=1 --gpus=2 --snap=10```
