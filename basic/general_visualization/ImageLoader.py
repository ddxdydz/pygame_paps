from basic.tools.create_error_surface import create_error_surface
from basic.tools.loading_files import load_image


class ImageLoader:
    def __init__(self, size_tick_scale):
        self.loaded_images = dict()
        self.size_tick_scale = size_tick_scale

    def load_images(self, images_library):
        for code in images_library.keys():
            width, height = images_library[code]["size"]
            self.loaded_images[code] = dict()
            self.loaded_images[code]["paths"] = dict()
            self.loaded_images[code]["imgs"] = dict()
            self.loaded_images[code]["size"] = width, height
            self.loaded_images[code]["one_tick_to_px"] = self.size_tick_scale
            for img_type in images_library[code]["paths"].keys():
                path = images_library[code]["paths"][img_type]
                scaled_size = width * self.size_tick_scale, height * self.size_tick_scale
                img = load_image(path, scaled_size)
                self.loaded_images[code]["paths"][img_type] = path
                self.loaded_images[code]["imgs"][img_type] = img

    def clear_loaded_images(self):
        self.loaded_images.clear()

    def reload_images(self):
        loaded_images_copy = self.loaded_images.copy()
        self.loaded_images.clear()
        self.load_images(loaded_images_copy)

    def set_size_tick_scale(self, size_tick_scale: int):
        if size_tick_scale < 0:
            size_tick_scale = 0
        self.size_tick_scale = size_tick_scale

    def check_image_code(self, code):
        if code in self.loaded_images.keys():
            return True
        print(f"Image code is not founded. Code: '{code}'")
        return False

    def check_img_type(self, code, img_type):
        if img_type in self.loaded_images[code]["imgs"].keys():
            return True
        print(f"Image img_type is not founded. Code: '{code}', img_type: '{img_type}'")
        return False

    def get_image_size(self, code):
        return self.loaded_images[code]["size"]

    def get_image_size_tick_scale(self, code):
        return self.loaded_images[code]["one_tick_to_px"]

    def get_image(self, code, img_type):

        if not self.check_image_code(code):
            return create_error_surface(20, 20)

        if not self.check_img_type(code, img_type):
            width, height = self.loaded_images[code]["size"]
            size_tick_scale = self.loaded_images[code]["one_tick_to_px"]
            return create_error_surface(width * size_tick_scale, height * size_tick_scale)

        return self.loaded_images[code]["imgs"][img_type]
