import numpy as np
from scipy.spatial.distance import cdist
from skimage.measure import label, regionprops, moments, moments_central, moments_normalized, moments_hu
from skimage import io
import matplotlib.pyplot as plt
import pickle
import utilities
from matplotlib.patches import Rectangle



label_map = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4,'F':5, 'G':6, 'H':7, 'I':8,
            'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16,'R':14,
            'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25
             }

inv_label_map = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E',5:'F', 6:'G', 7:'H', 8:'I',
                 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q',17:'R',
                 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}

label_list = []
component_list = []
def test(image, train_features, train_labels, train_mean, train_std):
    features, bbox_list = extract_features(image)
    features = (features - train_mean)/train_std
    D = cdist(features, train_features)
    D_index = np.argsort(D, axis=1)
    pred_labels_test = utilities.classify(D_index, train_labels)
    ax = plt.gca()
    s = ''

    for idx,box in enumerate(bbox_list):

        center_x = (box[0] + box[2])/2
        center_y = box[3] + 10
        ax.text(center_y, center_x, str(inv_label_map[pred_labels_test[idx]]), fontsize=8, color='yellow')
        s = s + str(inv_label_map[pred_labels_test[idx]])
    print(s)
    label_list.append(s)

    io.show()

    return bbox_list, pred_labels_test
    


def extract_features(image_path):
    features = np.array([[0]*utilities.num_features])
    bbox_list = np.array([[0,0,0,0]])
    
    img_binary = utilities.get_threshold(image_path)
    
    io.imshow(img_binary)
    img_label = label(img_binary, background=0)
    
#    print ('connected components : ', np.amax(img_label))
    p = image_path.find('/')
    q = image_path.find('.')
    print("\n\n"+image_path[p+1:q])
    
    regions = regionprops(img_label)
    ax = plt.gca()
    
    for props in regions:
        minr, minc, maxr, maxc = props.bbox

        # if (maxc - minc) < 10 or (maxr - minr) < 10:
        #     continue
        
        ax.add_patch(Rectangle((minc, minr), maxc - minc, maxr - minr, fill=False, edgecolor='red', linewidth=2))
        
        roi = img_binary[minr:maxr, minc:maxc]
        curr_features = utilities.extract_features(roi, props)
        features = np.append(features,curr_features,axis=0)
        bbox_list = np.append(bbox_list, np.array([[minr, minc, maxr, maxc]]),axis=0)
    
    print ('components : ', len(features)-1)

    component_list.append(len(features)-1)
    
    features = np.delete(features, 0, 0)
    print(features)
    bbox_list = np.delete(bbox_list, 0, 0)
    
    return features,bbox_list;

