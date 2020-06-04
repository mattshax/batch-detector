#!/bin/bash

vid="walking"

# convert video to images
ffmpeg -i images/$vid.mp4 -r 1 images/$vid%05d.jpg


# ffmpeg -framerate 8 -pattern_type glob -i 'images_predict/*.jpg' -c:v libx264 -pix_fmt yuv420p out.mp4