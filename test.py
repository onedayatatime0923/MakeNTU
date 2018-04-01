
import sys
from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models
import os
assert ImageUrlCreateEntry and models and os

# Replace with a valid key
training_key = "b43835f3fb8e4552ba7e3a435c711a96"
prediction_key = "f5d2cb8353664dc0aa7a8be0d729a832"
projectID = "0fedcb43-1707-406d-9072-899c06d85a3c"
test_dir = "./data/test/"

trainer = training_api.TrainingApi(training_key)
predictor = prediction_endpoint.PredictionEndpoint(prediction_key)


with open(sys.argv[1], mode="rb") as test_data:
    results = predictor.predict_image(projectID, test_data.read())
# Display the results.
#print('image {}'.format(sys.argv[1]))
print(results.predictions[0].tag)
#for prediction in results.predictions:
    #print ("\t" + prediction.tag + ": {0:.2f}%".format(prediction.probability * 100))

