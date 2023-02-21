# Guide_PC210_ImageExtractor

This repo holds sample code to extract "hidden" content from Guide PC210 thermal camera.

The camera creates the `IR_` jpeg file with lots of data after the JPEG end mark.

There is 4 byte per pixel data for each of the 192\*256 pixels where only one of the bytes seem to hold IR image data.
The byte order does not seem constant, as for the different sample images you need to look at different bytes to get the thermal information.

Currently, the expected IR data is pushed to the red channel, the other channels display the other unkown data scaled by 8 so it doesn't affect the image but is visible in e.g. gimp.

Maybe somebody is up for analyzing this a bit further? :-)

After the pixel data there is a json blob with meta data.


## examples
![](IRI_20221009_080550.jpg)
![](tmphbcqj97c.PNG)

![](IRI_20221009_081110.jpg)
![](tmp772ymjte.PNG)
