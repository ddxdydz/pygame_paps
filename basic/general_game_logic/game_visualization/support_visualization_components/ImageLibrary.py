from basic.tools.create_error_surface import create_error_surface
from basic.tools.loading.loading_files import load_image


class ImageLibrary:
    def __init__(self):
        self.loaded_images = dict()

    def load_images(self, images_library: dict, tick_size: int):
        for code in images_library.keys():
            width, height = images_library[code]["size"]
            self.loaded_images[code] = dict()
            self.loaded_images[code]["paths"] = dict()
            self.loaded_images[code]["imgs"] = dict()
            self.loaded_images[code]["size"] = width, height

            convert_alpha = False
            if "convert_alpha" in images_library[code].keys():
                if images_library[code]["convert_alpha"]:
                    convert_alpha = True
            self.loaded_images[code]["convert_alpha"] = convert_alpha

            for img_type in images_library[code]["paths"].keys():
                    path = images_library[code]["paths"][img_type]
                    img = load_image(path, (width * tick_size, height * tick_size), convert_alpha)
                    self.loaded_images[code]["paths"][img_type] = path
                    self.loaded_images[code]["imgs"][img_type] = img
                    self.loaded_images[code]["tick_size"] = tick_size

    def clear_loaded_images(self):
        self.loaded_images.clear()

    def reload_images(self, tick_size: int):
        if tick_size < 0:
            raise Exception(f"ImageLoader Error: tick_size = {tick_size} < 0")
        loaded_images_copied = self.loaded_images.copy()
        self.clear_loaded_images()
        self.load_images(loaded_images_copied, tick_size)
        print(f"ImageLoader Warning: Game images was reloaded! tick_size: {tick_size}")

    def check_image_code(self, code):
        if code in self.loaded_images.keys():
            return True
        print(f"ImageLoader Warning: Image code is not founded. Code: '{code}'")
        return False

    def check_img_type(self, code, img_type):
        if img_type in self.loaded_images[code]["imgs"].keys():
            return True
        print(f"ImageLoader Warning: Image img_type is not founded. " +
              f"Code: '{code}', img_type: '{img_type}'")
        return False

    def get_image_size(self, code):
        return self.loaded_images[code]["size"]

    def get_image(self, code, img_type):

        if not self.check_image_code(code):
            return create_error_surface(20, 20)

        if not self.check_img_type(code, img_type):
            width, height = self.loaded_images[code]["size"]
            tick_size = self.loaded_images[code]["one_tick_to_px"]
            return create_error_surface(width * tick_size, height * tick_size)

        return self.loaded_images[code]["imgs"][img_type]
