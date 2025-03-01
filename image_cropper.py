import os
from PIL import Image

def aspect_ratio_recommendations():
    recommendations = {
        "website_hero": (16, 9),
        "website_logo": (1, 1),
        "website_thumbnail": (4, 3),
        "website_banner": (21, 9),
        "social_media_post": (1, 1),
        "instagram_story": (9, 16),
        "facebook_cover": (851, 315),
        "twitter_header": (3, 1),
        "product_image": (4, 5),
        "portfolio_image": (3, 2),
    }
    return recommendations

def get_aspect_ratio_label(width, height):
    recommendations = aspect_ratio_recommendations()
    for label, (rec_width, rec_height) in recommendations.items():
        if width / height == rec_width / rec_height:
            return label
    return "custom"

def crop_image(image, target_width, target_height):
    img_width, img_height = image.size
    target_aspect = target_width / target_height
    img_aspect = img_width / img_height

    if img_aspect > target_aspect:
        new_width = int(target_aspect * img_height)
        new_height = img_height
    else:
        new_width = img_width
        new_height = int(img_width / target_aspect)

    left = (img_width - new_width) / 2
    top = (img_height - new_height) / 2
    right = (img_width + new_width) / 2
    bottom = (img_height + new_height) / 2

    return image.crop((left, top, right, bottom))

def process_images_in_directory(target_width, target_height):
    directory = os.getcwd()
    recommendations = aspect_ratio_recommendations()
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as img:
                aspect_label = get_aspect_ratio_label(target_width, target_height)
                print(f"Processing {filename} for {aspect_label}")
                cropped_img = crop_image(img, target_width, target_height)
                save_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}_cropped_{aspect_label}.jpg")
                cropped_img.save(save_path)
                print(f"Saved cropped image as {save_path}")

if __name__ == "__main__":
    # Example target aspect ratio (e.g., 16:9 for a website banner)
    target_width = 1920
    target_height = 1080

    process_images_in_directory(target_width, target_height)
