# Guide_PC210_ImageExtractor

This repo holds sample code to extract "hidden" content from Guide PC210 thermal camera.

The camera creates the `IR_` jpeg file with lots of data after the JPEG end mark.

There is 4 byte per pixel data for each of the 192*256 pixels where only one of the bytes seem to hold IR image data.
It seems that the other bytes are also of use because I think there is also the edge detection from the picture blending as well as some over/under"exposure" information in there.

After the pixel data there is a json blob with meta data.
