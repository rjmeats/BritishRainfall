# Produce jpg files with different levels of compression quality to see how this affects size and readability.

import os.path
import shutil           # To copy the original jpg file
from PIL import Image   # Use PIL to do the jpg handling

def compress_jpg(source_jpg, q, jpg_output_directory) :

    # Put the generated jpg file into the output directory, inserting a quality indicator into the file name.
    compressed_jpg = jpg_output_directory + os.path.sep + os.path.basename(source_jpg).replace('.jpg', f'.q{q:02d}.jpg')

    # Get PIL to create the compressed version of the jpg file.
    im = Image.open(source_jpg)
    im.save(compressed_jpg, optimize=True, quality=q)

    source_size = os.path.getsize (source_jpg)
    compressed_size = os.path.getsize (compressed_jpg)
    print(f'{source_jpg} : q = {q:2d} : {source_size:7d} bytes => {compressed_size:7d} bytes : {compressed_size*100/source_size:.0f} %')

    return compressed_jpg

def main(source_jpgs, qs, jpg_output_directory):

    if not os.path.isdir(jpg_output_directory) :
        print(f'** Output directory "{jpg_output_directory}" does not exist')
        return

    for source_jpg in source_jpgs :
        print()
        print(f'Running jpg compression tests using source jpg file {source_jpg}')
        print()

        shutil.copy(source_jpg, jpg_output_directory)

        for q in qs:
            compress_jpg(source_jpg, q, jpg_output_directory)

if __name__ == "__main__" :

    # Isle of May files from a range of dates
    file1 = 'TYRain_1677-1886_B_pt2-page-147.jpg'
    file2 = 'TYRain_1900-1909_29_pt1-page-038.jpg'
    file3 = 'TYRain_1951-1960_28_pt1-page-041.jpg'
    source_jpgs = [file1, file2, file3]
    qs = [1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    jpg_output_directory = 'jpg_output'

    main(source_jpgs, qs, jpg_output_directory)

