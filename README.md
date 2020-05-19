# ndvi_py

Algorithm to calculate the NDVI index of input image and return the index calculate as pseudocolor image.

Arguments:
  inputImg    Path of the input image for calculation of NDVI index.
  cmap        Color map to apply to the output file. Compatible with
              matplotlib colormaps.
  output      Path for the image with the NDVI index.

Example: 

python run.py pino.jpg RdYlGn ndvi_pseudocolor.png

