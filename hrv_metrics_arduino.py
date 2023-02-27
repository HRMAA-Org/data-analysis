import heartpy as hp
import numpy as np
import csv
from ecg_metrics_new import *

csvdata = []

with open("arduino1.csv") as file:
    data = csv.reader(file)
    for row in data:
        csvdata.append(row)


def get_bpm_metric(voltage_string, time_string):

    # Modify the "," to whatever string separator you are using
    voltage_data = np.array(voltage_string, dtype=int)
    time_data = np.array(time_string, dtype=int)

    # my_sample_rate=len(time_data)*1000/(time_data[-1]-time_data[0])
    # print(my_sample_rate)
    # Estimates sample rate using time data
    sample_rate = hp.get_samplerate_mstimer(time_data)

    # Processes data. Window size is sensitivity towards peaks. Low window size implies more peaks detected.
    # clean_data= hp.remove_baseline_wander(voltage_data, sample_rate)
    working_data, measures = hp.process(voltage_data, sample_rate, windowsize=0.6)
    print(working_data)

    hp.plotter(working_data, measures, show=False).savefig("analysis_arduino.jpg")

    # Returns a list with first element as bpm and second as rmssd. Change rmssd to sdnn if you want to use that metric.
    return [
        measures["bpm"],
        measures["sdnn"],
        measures["rmssd"],
        calculate_BPM(working_data["peaklist"], time_data, len(voltage_data)),
        calculate_SDNN(working_data["peaklist"], time_data),
        calculate_RMSSD(working_data["peaklist"], time_data),
    ]


print(get_bpm_metric(csvdata[1], csvdata[0]))
