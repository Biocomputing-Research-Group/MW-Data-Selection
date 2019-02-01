
import mne
import numpy as np

fname = 'D:\Mind wandering\sourcedata-20181112T195058Z-001\sourcedata\sub-02\eeg\sub-02_ses-11_task-BreathCounting_eeg.bdf'
raw = mne.io.read_raw_edf(fname,preload=True)

events = mne.find_events(raw, initial_event=True)

info = raw.info

data = raw._data[0:64]

mw = []

for i in range(0, events.shape[0]):
    if events[i,2] == 30:
        mw.append(events[i,0])

shape_myarray=(64,data.shape[1])

mw_duration = np.zeros(shape_myarray)

for j in range(0,len(mw)):
    mw_duration = data[:,mw[j]-32:mw[j]+32].copy()
    np.savetxt("MW_" + str(j+450) + ".txt", mw_duration, delimiter = ',', header = 'MW')


f = []

for i in range(0, events.shape[0]):
    if events[i,2] == 50:
        f.append(events[i,0])

shape_myarray=(64,data.shape[1])

f_duration = np.zeros(shape_myarray)

for j in range(0,len(f)):
    f_duration = data[:,f[j]:f[j]+64].copy()
    np.savetxt("F_" + str(j+487) + ".txt", f_duration, delimiter = ',', header = 'F')







