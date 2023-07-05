# Automated pH Adjustment of Viscous Formulations by Physics-informed ML

We have developed the first-of-its-kind pH robot capable of small-scale batch titrations for viscous liquid formulations. The fully autonomous, closed-loop pH adjustment is driven by a "physics-informed" ML-driven titration algorithm. The work is detailed in an article undergoing publication and this GitHub repository is part of the electronic supplementary information (ESI) released with the project. 

It should be noted that the pH robot can titrate a wide variety of systems, including aqueous solutions, but the focus has been presented on viscous formulations as the robot's design, along with mixing and cleaning protocols, were optimised to overcome the engineering challenge of titrating viscous systems. Furthermore, the titration algorithm can generally work with the use of any strong-strong or weak-strong acid/base pairs. A standalone [web application](https://aniketchitre-accelerate-titrations-titrationalgo-webapp-z383g2.streamlit.app) is also linked if you wish to use the hybrid ML algorithm to accelerate bench top pH adjustments, without additionally adopting the robotic technology. 

## Assembly of the pH Robot

Please find a bill of materials and assembly guide enclosed with the paper's ESI. Several components need to be 3d-printed and their designs can be found under the `CAD_DesignFiles` directory. Please download these files and follow the detailed instructions from the assembly guide.

## Operation of the pH Robot 

1. Clone the repo

```console
git clone https://github.com/sustainable-processes/ACJC.git
```

2. Create a virtual environment and install the dependencies

Firstly, follow the steps to create a virtualenv for your respective OS system ([Mac](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html)/[Windows](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html)). Then install the required package dependencies for this project.

```console
pip install -r requirements.txt
```
It is recommended to use Python version 3.9 or 3.10 to avoid package installation conflicts.


3. Open and run `pHRobot_Operation.ipynb`

### Description of the Code Files

The Jupyter Notebook is a completely commented-out self-contained file to guide the reader to operate the pH robot. The notebook is divided into sections: 

0. Importing Packages and Hardware Objects

The pH robot operates using an object-oriented framework and calls upon the various class object definitions under the `hardware` directory:

* `PlatformMovement.py` controls the robot's movement in a cartesian geometry.
* `C3000_SyringePumpsv2.py` controls high-precision TriContinent C-series syringe pumps to dose acid/base.
* `Sentron_pHmeter.py` logs data from the Sentron MicroFET pH probe.
* `Stirrer_WashPump.py` controls two pumps (inlet/outlet) to the robot's washing station, as well as the impeller for mixing the analyte.

1. Initialising Hardware and Protocol Functions

i) Initaites communication with the hardware objects;
ii) Defines fixed co-ordinates for the sample jars;
iii) Defines functions to be called within the titration algorithm for autonomous execution of the robot's unit operations.

2. Titration Algorithm

The "physics-informed" ML titration algorithm is defined. Please see the manuscript (to be published) with this work for details.

4. Platform Operation and Results

Finally, the pH robot can be called to titrate a single sample at a time, or a batch of samples (up to 12). `pHRobot_Operation.ipynb` has been provided with some sample output to show you what successful execution of a batch of pH adjustments on the robot should look like. 

## Titration Algorithm Web App 

A separate web application (https://aniketchitre-accelerate-titrations-titrationalgo-webapp-z383g2.streamlit.app) has been developed and hosted on Streamlit to accelerate traditional pH adjustment workflows. This is the same algorithm as run on the pH robot and found in the Jupyter Notebook, except it's for those interested parties that may wish to adopt the algorithm, without necessarily reproducing the pH platform we have presented. Please note if the web application has gone to sleep, you may simply "wake up" the app from your end. 


## Issues 

Submit an issue or email [Aniket Chitre](ac2349@cam.ac.uk) for any software-related issues (e.g., titration algorithm/web app, control of the pH robot) and [Jayce Cheng](jayce_cheng@imre.a-star.edu.sg) for any hardware related questions (e.g., assembly of the pH robot). 


## Citing

If you find this project useful, we encourage you to: 
* Star this repository &#11088;
* Cite our paper (_in preparation_)

