# rowing-classifier
Deep Learning Model to classify rowing images. 

 The model can classify 6 different types of boats: Eights, Fours, Quads, Doubles, Pairs and Singles. It's still a work in progress but it's ~90% accurate so far. 

 ## Heatmap images
 I've added some utility functions that generate a heatmap based off the activations of the last convolutional layer, using the Grad-CAM method. It's explained very well in [Deep Learning with Python](https://www.amazon.co.uk/Deep-Learning-Python-Francois-Chollet/dp/1617294438) by Francois Chollet.

 Using this I've made a short gif based off a video of my crew rowing from last year, the heatmap helps to show where in the image the models deems relevant for it's prediction:

 ![alt-text](https://github.com/michael-diggin/rowing-classifier/blob/master/cul_eight.gif?raw=true) 

 ## Images

 The images are being provided by Ben Rodford, you can view his website [here](https://www.benrodfordphotography.co.uk). He takes great quality photos of nearly every rowing event in the UK. 

 ## What's Next?
 Following on from making the model more accurate (image augmentation, fine tuning etc), the goal is to have a deployable web application, I'll be using Flask to handle that. 