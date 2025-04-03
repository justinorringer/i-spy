from PIL import Image
import os

# Set the folder path where images are stored
folder_path = "~/Documents/NN/JPEG"  # Update this path
output_folder = "~/Documents/NN/merged_images"  # Folder to save merged images

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get list of images and sort them
image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))])

# Merge images in pairs (batch size = 2)
batch_size = 2  # Change to merge more images side by side
count = 1  # Naming starts from 1

for i in range(0, len(image_files), batch_size):
    images_to_merge = image_files[i:i + batch_size]  # Get images in the batch
    
    if len(images_to_merge) < 2:
        break  # Skip if not enough images for a batch

    # Open images
    img_list = [Image.open(os.path.join(folder_path, img)) for img in images_to_merge]

    # Ensure all images have the same height
    max_height = max(img.height for img in img_list)
    images_resized = [img.resize((int(img.width * max_height / img.height), max_height)) for img in img_list]

    # Merge horizontally
    total_width = sum(img.width for img in images_resized)
    merged_img = Image.new("RGB", (total_width, max_height), (255, 255, 255))

    # Paste images
    x_offset = 0
    for img in images_resized:
        merged_img.paste(img, (x_offset, 0))
        x_offset += img.width

    # Save merged image with sequential numbering
    output_path = os.path.join(output_folder, f"{count}.jpg")
    merged_img.save(output_path)
    print(f"Saved: {output_path}")
    
    count += 1  # Increment filename number

print("Merging complete!")
