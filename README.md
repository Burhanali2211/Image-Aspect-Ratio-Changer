# Image Aspect Ratio Cropper

## Overview
This Python script processes all images in the current directory, cropping them to a specified target aspect ratio while preserving important content. It supports multiple aspect ratios commonly used for websites and social media platforms.

## Features
- Automatically detects and crops images to fit the specified aspect ratio.
- Supports popular aspect ratios like 16:9, 1:1, 4:3, and more.
- Saves cropped images with descriptive filenames.
- then that file requires any name of your desire and then save it
- Works with `.png`, `.jpg`, and `.jpeg` files.

## Supported Aspect Ratios
The script includes predefined aspect ratios for various use cases:

| Label               | Aspect Ratio |
|---------------------|-------------|
| Website Hero       | 16:9        |
| Website Logo       | 1:1         |
| Website Thumbnail  | 4:3         |
| Website Banner     | 21:9        |
| Social Media Post  | 1:1         |
| Instagram Story    | 9:16        |
| Facebook Cover     | 851:315     |
| Twitter Header     | 3:1         |
| Product Image      | 4:5         |
| Portfolio Image    | 3:2         |

## Installation
Make sure you have Python installed. Then install the required dependencies:

```bash
pip install pillow
```

## Usage
1. Place your images in the same directory as the script.
2. Run the script using the command:

```bash
python image_cropper.py
```

By default, the script crops images to a 16:9 aspect ratio (1920x1080). You can change the target width and height in the script:

```python
target_width = 1920
target_height = 1080
```


## License
This project is licensed under the MIT License.

## Author
Burhan Ali.

