import math
import statistics

def generate_time_series(sample_rate, peaks):
    return [i/sample_rate*1000 for i in peaks] 


def calculate_BPM(peaks, sample_rate, total_datapoints):
    bpm = len(peaks)*60.0*sample_rate/(total_datapoints)
    return bpm
   
def calculate_RMSSD(peaks, sample_rate, total_datapoints):
    RR_intervals = []
    rmssd = 0
    peaks=generate_time_series(sample_rate, peaks)
    for i in range(len(peaks)-1):
        RR_interval = peaks[i+1] - peaks[i]
        RR_intervals.append(RR_interval)
   
    diff = []
    for i in range(len(peaks)-2):
        diff = RR_intervals[i] - RR_intervals[i+1]
        rmssd += diff*diff
   
    rmssd = rmssd / (len(peaks) - 2)
    rmssd = math.sqrt(rmssd)
    return rmssd

def calculate_SDNN(peaks, sample_rate, total_datapoints):
    RR_intervals = []
    sdnn = 0
    peaks=generate_time_series(sample_rate, peaks)
    for i in range(len(peaks)-1):
        RR_interval = peaks[i+1] - peaks[i]
        RR_intervals.append(RR_interval)
       
    sdnn = statistics.stdev(RR_intervals)
    return sdnn
