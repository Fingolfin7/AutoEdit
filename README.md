# Python Application for Basic Batch Image Edits

A simple Python program using Pillow that allows users to make basic edits to multiple image files simultaneously.

## Setup
- Download or clone the repo
- Create a virtual environment and install the requirements with pip.
  ```
  pip install -r requirements.txt
  ```

- run the `GUI.py` file.

## Usage Example

### Select Images:
Press the `Select Images` button to select the list of images you would like to edit.

![image](https://github.com/user-attachments/assets/dc949a25-e42b-437d-b15b-6c7b3345a269)

The selected images will be displayed with their count.

### Adjust Settings:

You can adjust the brightness, contrast, sharpness, and rotate angle using the respective input fields.
Choose a filter from the dropdown menu if needed.

### Apply Edits:

Click the `Apply Edits` button to apply the selected adjustments to all the chosen images. A progress bar will indicate the completion status of the edits.

*_Note:_* Edits will only be applied if the user changes the default values:
Brightness will be adjusted only if its value is different from 1.0.
Contrast will be adjusted only if its value is different from 1.0.
Sharpness will be adjusted only if its value is different from 1.0.
Rotation will be applied only if the angle is different from 0.
A filter will be applied only if it is selected from the dropdown menu.

### Save Images:

Enter the output folder path in the `Output Folder` field.
Click the Save Images button to save the edited images to the specified folder.

### Reset:
Click the Reset button to clear all selections and reset the input fields to their default values.

### Available Filters
The following filters can be applied to the images:

- BLUR
- CONTOUR
- DETAIL
- EDGE_ENHANCE
- EDGE_ENHANCE_MORE
- EMBOSS
- FIND_EDGES
- SHARPEN
- SMOOTH
- SMOOTH_MORE


## Additional Notes
The program uses the Pillow library for image processing and tkinter for the GUI.
The progress bar shows the progress of the image editing process, giving feedback to the user.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
