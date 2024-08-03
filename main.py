import os
from random import choice

from AutoEdit import AutoEdit


def test_brightness(testImages: list):
    print("Testing brightness")
    auto_edit = AutoEdit(images=testImages)
    auto_edit.adjust_brightness(1.5)
    auto_edit.save_images('output/brighter')
    auto_edit.clear_images()


def test_contrast(testImages: list):
    print("Testing contrast")
    auto_edit = AutoEdit(images=testImages)
    auto_edit.adjust_contrast(1.5)
    auto_edit.save_images('output/contrast')
    auto_edit.clear_images()


def test_sharpness(testImages: list):
    print("Testing sharpness")
    auto_edit = AutoEdit(images=testImages)
    auto_edit.adjust_sharpness(1.5)
    auto_edit.save_images('output/sharpness')
    auto_edit.clear_images()


def test_rotate(testImages: list):
    print("Testing rotate")
    auto_edit = AutoEdit(images=testImages)
    auto_edit.rotate_images(90)
    auto_edit.save_images('output/rotate')
    auto_edit.clear_images()


def test_filter(testImages: list):
    print("Testing filters")
    auto_edit = AutoEdit(images=testImages)
    filter_effect = choice(list(auto_edit.filter_effects.keys()))
    auto_edit.apply_filter(filter_effect)
    auto_edit.save_images(f'output/filters/{filter_effect}')
    auto_edit.clear_images()


def main():
    testImages = [os.path.join('test_images', img) for img in os.listdir('test_images')]

    print(testImages)
    test_brightness(testImages)
    test_contrast(testImages)
    test_sharpness(testImages)
    test_rotate(testImages)
    test_filter(testImages)



if __name__ == '__main__':
    main()
