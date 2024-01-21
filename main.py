from PIL import Image
from PIL import ImageFilter
class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()
    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Файл не знайден!')
        self.original.show()
    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0]+str(len(self.changed)) + '.png'
        rotated.save(new_filename)
    def do_cropped(self):
        box = (250, 100, 600, 400)
        cropped = self.original.crop(box)
        self.changed.append(cropped)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.png'
        cropped.save(new_filename)
MyImage = ImageEditor('1645493267_1-kartinkin-net-p-kartinki-spanch-boba-1.png')
MyImage.open()
MyImage.do_left()
MyImage.do_cropped()
for im in MyImage.changed:
    im.show()