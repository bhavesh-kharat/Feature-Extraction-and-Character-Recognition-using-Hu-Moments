from skimage.filters import threshold_otsu, threshold_li, threshold_yen
from skimage.measure import label, regionprops, moments, moments_central, moments_normalized, moments_hu
import cv2
import numpy as np
from skimage import io
from collections import Counter

num_features = 12
knn_neighbors = 5



def get_threshold(image_path):
    img = cv2.imread(image_path,0)
    blur = cv2.GaussianBlur(img,(3,3),0)

    tmp,img_binary = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)

    kernel = np.ones((3,3),np.uint8)

    # Applying Errosion and Dilation on the image
    closing = cv2.morphologyEx(~img_binary, cv2.MORPH_CLOSE, kernel)

    return closing


def classify(D_index, train_labels):
#    nearest neighbor

#    k-NN
    pred_labels_test = []
    for idx,row in enumerate(D_index):
        k_labels = [train_labels[row[i]] for i in range(0,knn_neighbors)]
        most_common,num_most_common = Counter(k_labels).most_common(1)[0]
        pred_labels_test.append(most_common)
    return pred_labels_test


def extract_features(roi, props):

    features = []

    m = moments(roi)
    # print(m)

    cr = m[0, 1] / m[0, 0]
    cc = m[1, 0] / m[0, 0]

    mu = moments_central(roi, (cr, cc))
    nu = moments_normalized(mu)

    #finding Seven Features
    hu = moments_hu(nu)

    # seven features to be put into feature list
    features.extend(hu)

    # print(features)

    features.append(roi.shape[1]/roi.shape[0])
    features.append(props.eccentricity)
    features.append(props.convex_area/props.area)
    features.append(props.orientation)
    features.append(props.euler_number)
    
    return np.array([features])