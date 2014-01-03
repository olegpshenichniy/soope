from PIL import Image

from soope import conf
import colors


class Transformer(object):
    """
    Convert .png level image to list.
    """

    def __init__(self, image_path, **kwargs):
        """
        image_path - path to map's image
        kwargs - colors constant names as keys and map render elements as values
        """

        self.image_path = image_path

        self._elements = {}

        for color in kwargs.keys():
            self._elements[getattr(colors, color)] = kwargs[color]

        # >>> self.elements
        # >>> {(121, 68, 59, 255): <class 'elements.brick.Brick'>}

    def convert(self):
        """
        Return list with special objects
        """

        converted_map_list = []
        im = Image.open(self.image_path)
        pix = im.load()

        x = y = 0

        for h in range(im.size[1]):
            for w in range(im.size[0]):

                if pix[w, h] in self._elements:

                    # similar to Brick(x, y)
                    pf = self._elements[pix[w, h]](x, y)
                    converted_map_list.append(pf)

                x += conf.MAP_STEP
            y += conf.MAP_STEP
            x = 0

        return converted_map_list