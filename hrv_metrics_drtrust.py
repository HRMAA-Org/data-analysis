import heartpy as hp
import numpy as np
import csv
from ecg_metrics import *

with open("detected_line.csv") as file:
    data = csv.reader(file)
    for row in data:
        voltage_string = row


def get_bpm_metric(voltage_string):
    voltage_data = np.array(list(map(int, voltage_string)))
    sample_rate = len(voltage_data) / 30
    # Processes data. Window size is sensitivity towards peaks. Low window size implies more peaks detected.
    working_data, measures = hp.process(voltage_data, sample_rate, windowsize=0.6)

    hp.plotter(working_data, measures, show=False).savefig("analysis_drtrust.jpg")
    # Returns a list with first element as bpm and second as rmssd. Change rmssd to sdnn if you want to use that metric.
    return {
        "bpm": measures["bpm"],
        "sdnn": measures["sdnn"],
        "rmssd": measures["rmssd"],
        "ashman_bpm": calculate_BPM(
            working_data["peaklist"], sample_rate, len(voltage_data)
        ),
        "ashman_sdnn": calculate_SDNN(
            working_data["peaklist"], sample_rate, len(voltage_data)
        ),
        "ashman_rmssd": calculate_RMSSD(
            working_data["peaklist"], sample_rate, len(voltage_data)
        ),
    }


print(get_bpm_metric(voltage_string))
