
from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models
import os
import time
assert ImageUrlCreateEntry and os and models

# Replace with a valid key
training_key = "b43835f3fb8e4552ba7e3a435c711a96"
prediction_key = "f5d2cb8353664dc0aa7a8be0d729a832"

trainer = training_api.TrainingApi(training_key)

# Create a new project
print ("Creating project...")
project = trainer.create_project("Clothes Recognition")

# Make two tags in the new project
long_pant_tag= trainer.create_tag(project.id, "long_pant")
pants_tag = trainer.create_tag(project.id, "pants")


# if the images were on disk in a folder called Images alongside the sample.py, then
# they can be added by using the following:
train_dir = "./data/train/"
long_pant_dir = train_dir+'long_pant/'
for image in os.listdir(long_pant_dir):
    with open(long_pant_dir+  image, mode="rb") as img_data: 
        trainer.create_images_from_data(project.id, img_data.read(), [ long_pant_tag.id ])

pants_dir = train_dir+'pants/'
for image in os.listdir(pants_dir):
    with open(pants_dir+ image, mode="rb") as img_data: 
        trainer.create_images_from_data(project.id, img_data.read(), [ pants_tag.id ])

print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status == "Training"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    time.sleep(1)

# The iteration is now trained. Make it the default project endpoint
trainer.update_iteration(project.id, iteration.id, is_default=True)
print ("Done!")



# Now there is a trained endpoint that can be used to make a prediction

predictor = prediction_endpoint.PredictionEndpoint(prediction_key)


# if the images were on disk in a folder called Images alongside the sample.py, then
# they can be added by using the following.

# Open the sample image and get back the prediction results.
with open("./data/test/image1", mode="rb") as test_data:
    results = predictor.predict_image(project.id, test_data.read(), iteration.id)

# Display the results.
for prediction in results.predictions:
        print ("\t" + prediction.tag + ": {0:.2f}%".format(prediction.probability * 100))
