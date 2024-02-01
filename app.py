import tkinter as tk
from tkinter import filedialog
import spacy
from preprocessing import preprocess_data

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Function to perform data annotation
def annotate_data():
    # Open file dialog to select dataset
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "r") as file:
            data = file.read()

            # Preprocess the text data
            processed_data = preprocess_data(data)

            # Perform named entity recognition
            doc = nlp(processed_data)

            # Print the annotated entities
            for ent in doc.ents:
                print(f"Entity: {ent.text}, Type: {ent.label_}")

# Create the GUI
root = tk.Tk()
root.title("Data Annotation Tool")

# Create a button to trigger data annotation
annotate_button = tk.Button(root, text="Annotate Data", command=annotate_data)
annotate_button.pack()

# Run the GUI application
root.mainloop()
