import numpy as np
import cv2 as cv
import sys
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


## function to make predictions

#inputs a keras model and the filepath for a photo of a hand relative to the local directory
#photo must be RGB
#returns an array that sums to 1 with prediction weights for each class the model can detect.
def load_and_predict_photo(model, path):
    #loading photo
    photo = image.load_img(path,
                           grayscale=False,
                           color_mode="rgb",
                           target_size=model.input_shape[1:3],
                           interpolation="nearest")
    input_arr = image.img_to_array(photo)
    input_arr = np.array([input_arr])  #this model predicts based on batches. Making solo batch.
    predictions = model.predict(input_arr)
    return predictions



## importing trained model
print('importing model')
model = load_model("model_5") #  loads a model from this folder
print('model imported')



## video feed
# press s to snap an image
# press q to quit

vid_feed = cv.VideoCapture(0) #  goes with the first camera it can find in this device

#  creates a new window titled by the input string
cv.namedWindow('test')
print('video feed launching')
while True:
    success_bool, frame = vid_feed.read()
    
    if (not success_bool):
        print('error reading video feed')
        break        
    
    #cropping frame
    frame = frame[150:310, 90:250] #  [ V , > ]
    
    cv.imshow('test', frame)
    # cv.waitKey(1) waits 1ms for a key press,
    # returning that pressed key as a string
    k = cv.waitKey(1) 

    ## press 's' to save the image and make a prediction on it
    if k == ord("s"):
        cv.imwrite('data/opencv_images/test_capture.png', frame)
        print('image saved')
        prediction_array = load_and_predict_photo(model = model, path = 'data/opencv_images/test_capture.png')
        print(prediction_array)
    elif k == ord("q"):
        print('quit')
        break
    else:
        pass

#closes all windows opened by cv
cv.destroyAllWindows()    
    