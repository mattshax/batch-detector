import cv2
import time
import subprocess
import sys,os,json
import shutil

SPLIT_VIDEO=True
PROCESS_IMAGES=True
COMPILE_VIDEO=True
PLOT_RESULTS=True

if SPLIT_VIDEO == True:
    
    video = 'videos/walking.mp4'
    outdir = 'images'
    
    if os.path.exists(outdir) == False:
        os.mkdir(outdir)
    else:
        shutil.rmtree(outdir)
        os.mkdir(outdir)
    
    fps = 3
    
    cmd = 'ffmpeg -i '+video+' -r ' + str(fps) + ' ' + outdir+'/'+os.path.basename(video).replace('.mp4','')+'%05d.jpg'
    
    output = subprocess.check_output(cmd, shell=True)
    

if PROCESS_IMAGES == True:

    indir='images'
    outdir='images_predict'
    
    if os.path.exists(outdir) == False:
        os.mkdir(outdir)
    else:
        shutil.rmtree(outdir)
        os.mkdir(outdir)
    
    countItems = ['person','backpack','handbag']
    
    import darknet

    results={}
    
    """
    # BATCH ANALYSIS
    img_samples = []
    for filename in sorted(os.listdir(indir)):
        #print(indir+'/'+filename)
        img_samples.append(indir+'/'+filename)
    threshold=0.25
    data="darknet/cfg/coco.data"
    config="darknet/cfg/yolov4.cfg"
    model="models/yolov4.weights"
    out = darknet.performBatchDetect(img_samples=img_samples, batch_size=3,thresh= threshold, configPath = config, weightPath = model, metaPath=data)
    print(out)
    """
    
    for filename in sorted(os.listdir(indir)):
        
        print(indir+'/'+filename)
        
        # yolo4
        data="darknet/cfg/coco.data"
        config="darknet/cfg/yolov4.cfg"
        model="models/yolov4.weights"
        
        # yolo9000
        # data="darknet/cfg/combine9k.data"
        # config="darknet/cfg/yolo9000.cfg"
        # model="models/yolo9000.weights"
        
        # yolo-openimages
        # data="models/yolo_open_images/yolo.data"
        # config="models/yolo_open_images/yolov3-spp.cfg"
        # model="models/yolo_open_images/yolov3-spp_final.weights"
        
        threshold=0.25
        
        outimg = indir.replace('images','images_predict')+"/"+filename.replace('.png','.jpg')
        out = darknet.performDetect(imagePath=indir+'/'+filename, thresh= threshold, configPath = config, weightPath = model, metaPath=data, showImage= True, makeImageOnly = True, initOnly= False,outImage=outimg,includeClasses=countItems)
        
        counts={}
        for i in countItems:
            counts[i] = 0
        
        for i in out:
            if i[0] in countItems:
                counts[i[0]] += 1
        
        results[filename] = counts
        
    with open("results.json", "w") as myfile:
        myfile.write("{}\n".format(json.dumps(results, indent=4, sort_keys=True)))


if COMPILE_VIDEO == True:
    
    fr = 6
    indir='images_predict'
    outfile = 'results.mp4'
    
    cmd = 'ffmpeg -framerate '+str(fr)+' -pattern_type glob -y -i "'+indir+'/*.jpg" -c:v libx264 -pix_fmt yuv420p '+outfile
    
    output = subprocess.check_output(cmd, shell=True)


if PLOT_RESULTS == True:
    
    # with open('results.json') as file:
    #     content = json.load(file)
    
    import pandas as pd
    import matplotlib as mpl
    mpl.use('Agg')
    import matplotlib.pyplot as plt
    
    data = pd.read_json('results.json')
    data = data.transpose()
    
    print(data.describe())
    
    data = data.reset_index()

    data.plot(kind='line')
    plt.savefig('results.png')