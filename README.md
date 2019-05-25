# VoronoiTessellations
Python3 script to create [Voronoi](https://en.wikipedia.org/wiki/Voronoi_diagram) Tessellations (Mosaic pattern) on images. The script basically does 2D k-means-like clustering of the pixels based on fixed pre-defined cluster centres (which can be set to be random), and averages the RGB values for each cluster group and assigns all the pixels in the group the average value. Further options allow selectively applying average to only one of the RGB channels or exchanging values of the channels randomly (see [docs](https://github.com/Stochastic13/VoronoiTessellations/blob/master/VorTes%20docs.pdf)).


This is my first ever open-source repository. :)

### Requirements
1. Python3
2. numpy
3. [Pillow (PIL fork)](http://pillow.readthedocs.io/en/5.2.x/)
4. tkinter (for GUI. Usually the part of standard Python download)
5. multiprocessing (for the fast method. Part of the standard Python download)

### How to Run
The script can be called from the terminal. The simplest run with default options is thus:

    python VoronoiMain.py input.jpg output.jpg no_of_clusters

You can run the following command to see help:
    
    python VoronoiMain.py -h
    VoronoiMain.py [-h] [--rescale RESCALE] [--border BORDER]
                      [--method METHOD] [--threshold THRESHOLD]
                      [--clusmap CLUSMAP] [--probmap PROBMAP]
                      [--channel {r,g,b,rand,rb,rg,bg,randdual}]
                      [--verbose VERBOSE] [--seed SEED]
                      [--gaussianvars [GAUSSIANVARS [GAUSSIANVARS ...]]]
                      input output cn

    positional arguments:
      input                 Input Image file
      output                Output Image file
      cn                    Number of clusters
    optional arguments:
      -h, --help            show this help message and exit
      --rescale RESCALE     Rescaling factor for large images
      --border BORDER       Make border [1/0]?
      --method METHOD       fast vs low_mem methods. Default is low_mem.
      --threshold THRESHOLD
                            Only for borders. Threshold distance.
      --clusmap CLUSMAP     Load a specific cluster map as tab-separated text file
      --probmap PROBMAP     Load a 2D probability map for cluster generation
      --channel {r,g,b,rand,rb,rg,bg,randdual}
                            Whether to tessellate along only R,G,B or
                            combinations?
      --verbose VERBOSE     Print progress?[1/0]
      --seed SEED           Seed for PRNG
      --gaussianvars [GAUSSIANVARS [GAUSSIANVARS ...]]
                            Only for gaussian probmap
                            (mx,my,sigmax,sigmay,corr(opt),spacing(opt))
                            
For further details, see the [docs](https://github.com/Stochastic13/VoronoiTessellations/blob/master/VorTes%20docs.pdf).

### GUI
This allows an easy way of generating custom cluster maps. Run `gui_clusmap.py` with the input file and the output file as the arguments. For further details, refer [docs](https://github.com/Stochastic13/VoronoiTessellations/blob/master/VorTes%20docs.pdf).

### Performance
For each of the following test, an image of size **1728 x 2304 pixels**, and ran on a **i7-8th Gen Acer Predator Helios 300 with 16GB RAM**. t_clus represents the time in seconds for the cluster computation step, t_avg the time for the averaging step in seconds and the max memory represents the maximum RAM memory used in MB (not very reliable, but approximately true). The seed is 123 wherever applicable. lm stands for low_mem and f stands for fast methods.


|Options | t_clus | t_avg | max memory|
|--------|--------|-------|-----------|
|cn 1000 rescale 2 lm | 9 | 8 | 30|
|cn 1000 rescale 2 f | 4 | 4 | 394|
|cn 500 border lm | 143 | 20 | 47|
|clusmap A lm | 48 | 63 | 50|
|clusmap A f | 16 | 8 | 751|
|cn 1000 channel r lm | 37 | 13 | 51|
|cn 1000 channel r f | 13 | 5 | 754|
|cn 500 gaussian lm | 28 | 17 | 98|
|cn 500 gaussian f | 11 | 4 | 930|
|cn 2000 probmap B lm | 50 | 51 | 50|
|cn 2000 probmap B f | 14 | 5 | 760|


### Examples
Source:
<div align=çenter>
  <img src='demo\original.jpg' height=250px>
  </div>
 cn 1500, fast, seed 123
<div align=çenter>
  <img src='demo\auto1500_f_s123.jpg' height=250px>
  </div>
  
 Using a custom `clusmap` 
 
<div align=çenter>
  <img src='demo\clusmap_f_s123.jpg' height=250px>
  </div>
  
 `--channel r` and `--channel randdual`
 
<div align=çenter>
  <img src='demo\r_f_seed123.jpg' height=250px>
  <img src='demo\randdual_lm_seed123.jpg' height=250px>
  </div>
  
  
