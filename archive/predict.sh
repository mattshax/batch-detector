
# yolo9000
./darknet detector test cfg/combine9k.data cfg/yolo9000.cfg ../models/yolo9000/yolo9000-weights/yolo9000.weights -thresh .08 -dont_show /scratch/images/city00001.jpg

# openimages
./darknet detector test cfg/openimages.data cfg/yolov3-openimages.cfg ../yolov3-openimages.weights -thresh 0.01 -dont_show /scratch/images/walking00001.jpg 

# yolov3
./darknet detector test cfg/coco.data cfg/yolov3.cfg ../models/yolov3.weights -thresh 0.3 -dont_show /scratch/images/walking00001.jpg 

# yolov4
./darknet detector test cfg/coco.data cfg/yolov4.cfg ../models/yolov4.weights -thresh 0.3 -dont_show /scratch/images/walking00001.jpg 

# csresnext50-panet-spp-original-optimal_final
./darknet detector test cfg/coco.data cfg/csresnext50-panet-spp-original-optimal.cfg ../models/csresnext50-panet-spp-original-optimal_final.weights -thresh 0.25 -dont_show /scratch/images/walking00001.jpg 

# video test
./darknet detector demo cfg/coco.data cfg/csresnext50-panet-spp-original-optimal.cfg ../models/csresnext50-panet-spp-original-optimal_final.weights ../videos/walking.mp4 -i 0 -dont_show -thresh 0.25

./darknet detector demo cfg/coco.data cfg/yolov4.cfg ../models/yolov4.weights ../videos/walking.mp4 -i 0 -dont_show -thresh 0.25