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
The edited files will be saved in the output folder path specified in the `Output Folder` field.

**_Note:_** Edits will only be applied if the user changes the default values:
- Brightness, Contrast, and Sharpness will be adjusted only if the value is different from 1.0.
- Rotation will be applied only if the angle is different from 0.
- A filter will be applied only if it is selected from the dropdown menu.


![image](https://github.com/user-attachments/assets/6accec42-407e-408f-8f95-8c759ab4b5d0)


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


### Output Examples
Gandalf (original):

![LOTR Gandalf](https://github.com/user-attachments/assets/97209112-7c5d-4818-92ac-804c6b831c3b)

Brightness 2

![LOTR Gandalf](https://github.com/user-attachments/assets/c2ee55b5-0192-44e7-8521-63c700937a6a)

Contrast 2

![LOTR Gandalf](https://github.com/user-attachments/assets/b8b8ba02-05c7-4785-9f03-c9f89b5dde0e)

Sharpness 2

![LOTR Gandalf](https://github.com/user-attachments/assets/cdd70ad1-b2a1-435f-8d85-9cfa6f1c105a)

Rotate 30 degrees

![LOTR Gandalf](https://github.com/user-attachments/assets/d926cf94-8794-49d2-a245-0e61cb63686a)

#### Filters

Blur

![LOTR Gandalf](https://github.com/user-attachments/assets/34e11526-bbd3-4e36-831f-672a2d706713)

Detail

![LOTR Gandalf](https://github.com/user-attachments/assets/519f2c07-27fd-4ec9-ab6c-2aeb10f8ed8a)

Find Edges

![LOTR Gandalf](https://github.com/user-attachments/assets/dbe02f78-0b72-4943-a5d9-58975486ed3b)

Emboss

![LOTR Gandalf](https://github.com/user-attachments/assets/bc66ba1d-5fdb-43b9-9412-d1c55765b6af)

Contour

![LOTR Gandalf](https://github.com/user-attachments/assets/64581992-a582-447e-af80-e38a2af939a6)


## Additional Notes
The program uses the Pillow library for image processing and tkinter for the GUI.
The progress bar shows the progress of the image editing process, giving feedback to the user.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
