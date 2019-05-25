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
  
  
