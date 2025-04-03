import pytesseract
from PIL import Image
import os
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_images(folder_path):
    """
    Extracts text from all images in a given folder using pytesseract.

    :param folder_path: Path to the folder containing images
    :return: Dictionary with image filenames as keys and extracted text as values
    """
    extracted_texts = {}

    # Get list of images and sort them
    image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))])

    for img_name in image_files:
        img_path = os.path.join(folder_path, img_name)
        try:
            img = Image.open(img_path)
            text = pytesseract.image_to_string(img).strip()  # Extract text and remove extra spaces
            extracted_texts[img_name] = text

            # Process text with spaCy for named entity recognition
            doc = nlp(text)
            for ent in doc.ents:
                print(ent.text, ent.label_)

        except Exception as e:
            print(f"Error processing {img_name}: {e}")

    return extracted_texts

# Example Usage:
if __name__ == "__main__":
    folder = "./merged_images"  # Update with your path
    extracted_data = extract_text_from_images(folder)

    # Print extracted text
    for filename, text in extracted_data.items():
        print(f"\n==== Extracted from {filename} ====\n{text}")