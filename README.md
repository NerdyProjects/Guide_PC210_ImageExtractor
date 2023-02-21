# Guide_PC210_ImageExtractor

This repo holds sample code to extract "hidden" content from Guide PC210 thermal camera.

The camera creates the `IR_` jpeg file with lots of data after the JPEG end mark.

There is 4 byte per pixel data for each of the 192*256 pixels where only one of the bytes seem to hold IR image data.
The byte order does not seem constant, as for the different sample images you need to look at different bytes to get the thermal information.

Maybe somebody is up for analyzing this a bit further? :-)

After the pixel data there is a json blob with meta data.
