'''
Author: daniele.bagni@xilinx.com
'''


import os
import numpy as np

###############################################################################
# project folders
###############################################################################

def get_script_directory():
    path = os.getcwd()
    return path

# get current directory
SCRIPT_DIR = get_script_directory()

# dataset top level folder
DATASET_DIR = os.path.join(SCRIPT_DIR, "dataset/cifar10")
# train, validation, test and calibration folders
TRAIN_DIR = os.path.join(DATASET_DIR, "train")
VALID_DIR = os.path.join(DATASET_DIR, "valid")
TEST_DIR  = os.path.join(DATASET_DIR, "test")
CALIB_DIR = os.path.join(DATASET_DIR, "calib")

# Augmented images folder
#AUG_IMG_DIR = os.path.join(SCRIPT_DIR,'aug_img/cifar10')

# Keras model folder
KERAS_MODEL_DIR = os.path.join(SCRIPT_DIR, "keras_model/cifar10")

# TF checkpoints folder
CHKPT_MODEL_DIR = os.path.join(SCRIPT_DIR, "tf_chkpts/cifar10")

# TensorBoard folder
TB_LOG_DIR = os.path.join(SCRIPT_DIR, "tb_logs/cifar10")

###############################################################################
# global variables
###############################################################################

# since we do not have validation data or access to the testing labels we need
# to take a number of images from the training data and use them instead
NUM_CLASSES      =    10
NUM_VAL_IMAGES   =  5000
NUM_TEST_IMAGES  =  5000
NUM_TRAIN_IMAGES = 50000

#Size of images
IMAGE_WIDTH  = 32
IMAGE_HEIGHT = 32

#normalization factor to scale image 0-255 values to 0-1 #DB
NORM_FACTOR = 255.0 # could be also 256.0

# label names for the FASHION MNIST dataset
labelNames_dict = { "airplane" : 0, "automobile" : 1, "bird" : 2, "cat" : 3, "deer" : 4, "dog" : 5,
                    "frog" : 6, "horse" : 7, "ship" : 8, "truck" : 9}
labelNames_list = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]



###############################################################################
# global functions
###############################################################################

def Normalize(x_test):
    x_test  = np.asarray(x_test)
    x_test = x_test.astype(np.float32)
    x_test = x_test/NORM_FACTOR
    x_test = x_test -0.5
    out_x_test = x_test *2
    return out_x_test


def ScaleTo1(x_test):
    x_test  = np.asarray(x_test)
    x_test = x_test.astype(np.float32)
    our_x_test = x_test/NORM_FACTOR
    return out_x_test
