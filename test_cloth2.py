
from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models
assert ImageUrlCreateEntry and models

# Replace with a valid key
training_key = "b43835f3fb8e4552ba7e3a435c711a96"
prediction_key = "f5d2cb8353664dc0aa7a8be0d729a832"
projectID = "bdb3e2bd-4350-4601-8cc8-ce02abc69b64"

trainer = training_api.TrainingApi(training_key)
predictor = prediction_endpoint.PredictionEndpoint(prediction_key)


with open("./data/test/o-fb8f2a951aed49358dfd70859cc74890", mode="rb") as test_data:
    results = predictor.predict_image(projectID, test_data.read())

# Display the results.
for prediction in results.predictions:
    print ("\t" + prediction.tag + ": {0:.2f}%".format(prediction.probability * 100))

