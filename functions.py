import glob
import cv2
import os
import numpy as np

def read_image():
    
    # ------------------------------------
    # read_image() read the image from image file
    # resize each image to same size 224*224
    # then store the whole images in 4D array
    # return the image.array.shape.
    # ------------------------------------
    
    path  = glob.glob(os.path.join('images/*')) # get the path of images
    image_array = np.zeros((len(path), 224, 224, 3)) # initailize an 4D array in numpy
    for i in range(0,len(path)):
        image = cv2.imread(path[i]) # read image based on the path
        image = cv2.resize(image, (224, 224)) # resize the image
        cv2.imshow('orginal',image)
        image_array[i,:,:,:] = image # Store the image into 4D array
    return image_array.shape # return a 4D array

def show_image(num):
    
    # ------------------------------------
    # show the images that choose.
    # ------------------------------------
    
    path = glob.glob(os.path.join('images/*')) # get the path of images
    image1 = cv2.imread(path[num]) # read images
    image1 = cv2.resize(image1, (224, 224)) # resize the image to same size
    cv2.imshow('orginal',image1) # show the image chosed
    cv2.waitKey(1)
    return True


def show_path(num):
    
    # ------------------------------------
    # show the path that choose.
    # ------------------------------------
    
    path  = glob.glob(os.path.join('images/*')) # get the path of images
    return print(path[num]) # print path



def print_functoion():
    print('Which image you want to check?')
    num = int(input())
    show_image(num)
    
    print('Do you want to see the path of the image?')
    num1 = int(input())
    if num1 == 1:
        show_path(num)
    elif num1 == 0:
        print('Continue.')
    
    print('Do you want to store all data into a array?')
    num2 = int(input())
    if num2 == 1:
        read_image()
        
        print(read_image())
    else:
        print('Thank you!')

