import os
from PIL import Image, ImageEnhance, ImageFilter


class AutoEdit:
    def __init__(self, images=None):
        self.temp_path = os.path.join(os.path.dirname(__file__), 'temp')
        self.__images = []
        if images:
            self.set_images(images)

        self.filter_effects = {
            "BLUR": ImageFilter.BLUR,
            "CONTOUR": ImageFilter.CONTOUR,
            "DETAIL": ImageFilter.DETAIL,
            "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
            "EDGE_ENHANCE_MORE": ImageFilter.EDGE_ENHANCE_MORE,
            "EMBOSS": ImageFilter.EMBOSS,
            "FIND_EDGES": ImageFilter.FIND_EDGES,
            "SHARPEN": ImageFilter.SHARPEN,
            "SMOOTH": ImageFilter.SMOOTH,
            "SMOOTH_MORE": ImageFilter.SMOOTH_MORE
        }

    def set_images(self, img_list: list):
        if not os.path.isdir(self.temp_path):
            os.makedirs(self.temp_path)

        for image in img_list:
            try:
                # create a copy of the image in the temp folder to avoid overwriting the original
                with Image.open(image) as img:
                    new_path = os.path.join(self.temp_path, os.path.basename(image))
                    img.save(new_path)
                    self.__images.append(new_path)
            except Exception as e:
                print("Failed to open image: ", e)



    def get_filters(self):
        return list(self.filter_effects.keys())


    def clear_images(self):
        self.__images = []
        self.__del__()

    def adjust_brightness(self, exposure: float):
        """
        Adjust the brightness of the images. The exposure parameter is a float value that can be used to adjust the
        brightness of the images. A value of 1.0 will not change the brightness, a value less than 1.0 will make the
        image darker, and a value greater than 1.0 will make the image brighter.
        :param exposure: float value to adjust the brightness of the images
        """
        for image in self.__images:
            img = Image.open(image)
            img = ImageEnhance.Brightness(img).enhance(exposure)
            img.save(image)

    def adjust_contrast(self, contrast: float):
        """
        Adjust the contrast of the images. The contrast parameter is a float value that can be used to adjust the
        contrast of the images. A value of 1.0 will not change the contrast, a value less than 1.0 will decrease the
        contrast, and a value greater than 1.0 will increase the contrast.
        :param contrast: float value to adjust the contrast of the images
        """
        for image in self.__images:
            img = Image.open(image)
            img = ImageEnhance.Contrast(img).enhance(contrast)
            img.save(image)

    def adjust_sharpness(self, sharpness: float):
        """
        Adjust the sharpness of the images. The sharpness parameter is a float value that can be used to adjust the
        sharpness of the images. A value of 1.0 will not change the sharpness, a value less than 1.0 will decrease the
        sharpness, and a value greater than 1.0 will increase the sharpness.
        :param sharpness: float value to adjust the sharpness of the images
        """
        for image in self.__images:
            img = Image.open(image)
            img = ImageEnhance.Sharpness(img).enhance(sharpness)
            img.save(image)

    def rotate_images(self, angle: float):
        for image in self.__images:
            img = Image.open(image)
            img = img.rotate(angle)
            img.save(image)


    def apply_filter(self, filter_name: str):
        if filter_name not in self.filter_effects:
            raise ValueError(f"Invalid filter name: {filter_name}, must be one of {self.filter_effects.keys()}")

        filter_name = self.filter_effects[filter_name]

        for image in self.__images:
            img = Image.open(image)
            img = img.filter(filter_name)
            img.save(image)

    def save_images(self, path: str = 'output'):
        if not os.path.isdir(path):
            os.makedirs(path)

        for image in self.__images:
            img = Image.open(image)
            save_path = os.path.join(path, os.path.basename(image))
            if os.path.exists(save_path):
                os.remove(save_path)
            img.save(save_path)

        print(f"Images saved to {os.path.normpath(path)} successfully!")

    def __del__(self):
        # clean up the temp folder
        if os.path.isdir(self.temp_path):
            for file in os.listdir(self.temp_path):
                os.remove(os.path.join(self.temp_path, file))
            os.rmdir(self.temp_path)