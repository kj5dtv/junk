import numpy as np
import matplotlib.pyplot as plt

HEIGHT, WIDTH = 256, 320
NOTE_HEIGHT = 5
NOTE_SPACING = 0

MARY_HAD_ALL = [3, 2, 1, 2, 3, 3, 3, 2, 2, 2, 3, 5, 5, 3, 2, 1, 2, 3, 3, 3, 3, 2, 2, 3, 2, 1]
DIXIE = [5, 3, 1, 1, 1, 2, 3, 4, 5, 5, 5, 3]

class ScaleBrightness:
    def __init__(self, scale_type='major'):
        self.scale_brightness = np.array([0, 25, 51, 76, 102, 127, 153, 178, 204, 229, 242, 255], dtype=np.uint8)
        self.scale_type = scale_type
        self.scales = {
            'chromatic': list(range(1, 13)),
            'major': [1, 3, 5, 6, 8, 10, 12],
            'minor': [1, 3, 4, 6, 8, 9, 11]
        }

    def get_brightness_values(self, notes):
        scale = self.scales.get(self.scale_type, self.scales['major'])
        return [self.scale_brightness[scale[note - 1] - 1] for note in notes]

class SSTVImage:
    def __init__(self, height=HEIGHT, width=WIDTH, note_height=NOTE_HEIGHT, spacing=NOTE_SPACING):
        self.height = height
        self.width = width
        self.note_height = note_height
        self.spacing = spacing
        self.image = np.zeros((height, width), dtype=np.uint8)

    def add_notes(self, brightness_values):
        y = 0
        for value in brightness_values:
            if y + self.note_height <= self.height:
                self.image[y:y+self.note_height, :] = value
            y += self.note_height + self.spacing

    def save_image(self, filename):
        plt.imsave(filename, self.image, cmap='gray')

    def display_image(self):
        plt.imshow(self.image, cmap='gray')
        plt.axis('off')
        plt.show()

def main():
    melody = MARY_HAD_ALL  
    scale_type = 'major'  # 'chromatic', 'minor'
    
    scale_brightness = ScaleBrightness(scale_type=scale_type)
    brightness_values = scale_brightness.get_brightness_values(melody)
    
    sstv = SSTVImage()
    sstv.add_notes(brightness_values)
    sstv.display_image()

if __name__ == "__main__":
    main()