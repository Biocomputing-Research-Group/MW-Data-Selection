# MW-Data-Selection

The code generates mind wandering and focusing samples from the original dataset .It uses mne pythone software to process EEG files. It outputs a dataset including mind wandering and focusing state samples. Each file is a 8-second 64-channel EEG signals. 

# Current Version
V 1.0

# Setup and Installation
Basic Dependencies:
  1. Download the original dataset (Dataset is available on: https://sccn.ucsd.edu/~arno/fam2data/publicly_available_EEG_data.html)
  2. Copy all bdf files to your project directory.

Installation Steps:
  1. Download MW-Data-Selection file.
  2. Creat a new project and add the downloaded file to your project. Import the following packages to your project interpreter: mne and numpy.
  3. Excute the project.
  
# Output
The code generates multiple comma seperated text files whose names staring with mw and f, defining each data samples. Each file has 64 rows as channels and 8192 columns (8 seconds EEG recording with 1024 Hz sample rate). The generated files can be opened by Microsoft Excel.

# Questions
  sh0773@unt.edu
