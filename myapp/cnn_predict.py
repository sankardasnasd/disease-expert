from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

# Load the trained model
loaded_model = load_model("D:\\aiii\\Disease_Expert\\Disease_Expert\\new__model_new.h5",compile=False)  # Use the path where you saved your trained model
print("patnilla")
# Function to preprocess the image for prediction
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image
    predictions = loaded_model.predict(img_array)
    class_labels = ['Akne','Benign','Ekzama','Enfeksiyonel','Malign','Pigment']
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]
    print(predicted_class_label,';;;;;;;;;;;;;;;;;;;;;;;;;')
    return predicted_class_label


# Example usage:


# Make predictions

# Map predicted class index to label
# class_labels = ['Akne','Benign','Ekzama','Enfeksiyonel','Malign','Pigment']
# predicted_class_index = np.argmax(predictions)
# predicted_class_label = class_labels[predicted_class_index]

# print("Predicted Class:", predicted_class_label)

# preprocess_image(r"D:\aiii\Disease_Expert\Disease_Expert\media\disease_prediction\20240129-233342.jpg")