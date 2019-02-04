import mne
import numpy as np

#select the address of original dataset
fname = '...\sourcedata\sub-01\eeg\sub-01_ses-01_task-BreathCounting_eeg.bdf'

#read the dataset
raw = mne.io.read_raw_edf(fname,preload=True)

#save the events of the dataset in a variable
events = mne.find_events(raw, initial_event=True)

#get the data information
info = raw.info

#select the first 64 channels(the first 64 channels are EEG data)
data = raw._data[0:64]

mw = []

#extract mind wandering events in dataset
for i in range(0, events.shape[0]):
    if events[i,2] == 30:
        mw.append(events[i,0])

shape_myarray=(64,data.shape[1])

#define an array of zeros for mind wandering data
mw_duration = np.zeros(shape_myarray)

#save 8-second mind wandering samples
for j in range(0,len(mw)):
    mw_duration = data[:,mw[j]-10240:mw[j]-2048].copy()
    np.savetxt("MW_" + str(j) + ".txt", mw_duration, delimiter = ',', header = 'MW')


f = []

#extract focusing state events in dataset
for i in range(0, events.shape[0]):
    if events[i,2] == 50:
        f.append(events[i,0])

shape_myarray=(64,data.shape[1])

#define an array of zeros for focusing state data
f_duration = np.zeros(shape_myarray)

#save 8-second mind wandering samples
for j in range(0,len(f)):
    f_duration = data[:,f[j]:f[j]+8192].copy()
    np.savetxt("F_" + str(j) + ".txt", f_duration, delimiter = ',', header = 'F')







