import re
import argparse
import json
import struct
from collections import defaultdict
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

parser = argparse.ArgumentParser(
                    prog = 'Guide PC210 jpeg IR image extractor',
                    description = 'Extracts uncompressed "raw" IR data from Jpegs after the JPEG end marker'
                    )
parser.add_argument('filename')           # positional argument
parser.add_argument('-v', '--verbose',
                    action='store_true', help='calculates and outputs some histogram data about the bytes')  # on/off flag
parser.add_argument('-s', '--show',
                    action='store_true', help='display the image')  # on/off flag
parser.add_argument('-d', '--dest_file', action='store', help='store result to file. Filetype is decided by filename extension (refer to PIL lib)')

args = parser.parse_args()
WIDTH=192
HEIGHT=256
JPEG_END = b"\xFF\xD9"
META_START = b"\x00\x7B\x0A\x20"

with open(args.filename, mode="rb") as file:
    content = file.read()
    match = re.search(JPEG_END, content)
    start = match.end()+20
    img = Image.new('RGB', (WIDTH, HEIGHT))
    pixels = img.load()
    # pixels[100,100] = (255,0,0)
    b1v = defaultdict(int)
    b2v = defaultdict(int)
    b3v = []
    b = defaultdict(int)
    meta_part = content[start+WIDTH*4*HEIGHT:]
    (pad, length) = struct.unpack('<134pI', meta_part[0:138])
    print(json.dumps(json.loads(meta_part[138:(138+length)]), indent=2))


    for y in range(HEIGHT):
        for x in range(WIDTH):
            b1 = content[start+(WIDTH*y*4)+(x*4)+0]
            b2 = content[start+(WIDTH*y*4)+(x*4)+1]
            b3 = content[start+(WIDTH*y*4)+(x*4)+2]
            pixels[x, y] = (b3, int(b2/8), int(b3/8))
            b1v[b1] += 1
            b2v[b2] += 1
            b3v.append(b3)
            combined = b3
            b[combined] += 1

    if args.verbose:
        print(sorted(b1v))
        print(sorted(b2v))
        print(len(b))
        print(sorted(b))
        #b = np.array(b2v)
        #plt.hist(b, bins=range(257))
        #plt.title("histogram")
        #plt.show()

    if args.show:
        img.show()

    if args.dest_file:
        img.save(args['dest_file'])
