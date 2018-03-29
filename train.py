
from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models
import os
import time
assert ImageUrlCreateEntry and os and models and prediction_endpoint

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''       setting option                           '''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
training_key = "b43835f3fb8e4552ba7e3a435c711a96"
prediction_key = "f5d2cb8353664dc0aa7a8be0d729a832"
train_dir = "./data/train/"
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''       creating project                         '''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

trainer = training_api.TrainingApi(training_key)
print ("Creating project...")
project = trainer.create_project("Clothes Recognition")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''       make tags                                '''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

print ("Making tags...")
tags={}
for label in os.listdir(train_dir):
    tags[label]=trainer.create_tag(project.id, label)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''       load image                               '''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

print ("Loading images...")
# if the images were on disk in a folder called Images alongside the sample.py, then
# they can be added by using the following:
for label in tags:
    image_dir= train_dir+label
    for image in os.listdir(image_dir):
        with open(image_dir +'/'+  image, mode="rb") as img_data: 
            trainer.create_images_from_data(project.id, img_data.read(), [ tags[label].id ])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''       load image                               '''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status == "Training"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    time.sleep(1)

# The iteration is now trained. Make it the default project endpoint
trainer.update_iteration(project.id, iteration.id, is_default=True)
print ("Done!")


print("Project ID is {}".format(project.id))
