import heartpy as hp
import numpy as np
import csv
import sys
from metrics_formulae_improved import *

csvdata = [[],[]]

with open(sys.argv[1]) as file: #voltagestring
    data = csv.reader(file)
    for row in data:
        csvdata[0].append(row[0])
        csvdata[1].append(row[1])



def get_bpm_metric(voltage_string, time_string):

    # Modify the "," to whatever string separator you are using
    voltage_data = np.array(voltage_string, dtype=int)
    time_data = np.array(time_string, dtype=int)

    # my_sample_rate=len(time_data)*1000/(time_data[-1]-time_data[0])
    # Estimates sample rate using time data
    sample_rate = hp.get_samplerate_mstimer(time_data)

    # Processes data. Window size is sensitivity towards peaks. Low window size implies more peaks detected.
    clean_data= hp.remove_baseline_wander(voltage_data, sample_rate)
    working_data, measures = hp.process(clean_data, sample_rate, windowsize=0.6)

    hp.plotter(working_data, measures, show=False).savefig("analysis_arduino.jpg")

    # Returns a list with first element as bpm and second as rmssd. Change rmssd to sdnn if you want to use that metric.
    return [
        measures["bpm"],
        measures["sdnn"],
        measures["rmssd"],
    #    calculate_BPM(working_data["peaklist"], time_data, len(voltage_data)),
    #   calculate_SDNN(working_data["peaklist"], time_data),
    #    calculate_RMSSD(working_data["peaklist"], time_data),
    ]

#switch time and voltage by exchanging the 1 and 0

print(get_bpm_metric(csvdata[1], csvdata[0]))
