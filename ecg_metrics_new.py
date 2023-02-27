import math
import statistics


def calculate_BPM(peaks, sample_rate, total_datapoints):
    bpm = len(peaks) * 60.0 * sample_rate / (total_datapoints)
    return bpm


def calculate_RMSSD(peaks, time_series):
    RR_intervals = []
    rmssd = 0
    for i in range(len(peaks) - 1):
        RR_interval = time_series[peaks[i + 1]] - time_series[peaks[i]]
        RR_intervals.append(RR_interval)

    diff = []
    for i in range(len(peaks) - 2):
        diff = RR_intervals[i] - RR_intervals[i + 1]
        rmssd += diff * diff

    rmssd = rmssd / (len(peaks) - 2)
    rmssd = math.sqrt(rmssd)
    return rmssd


def calculate_SDNN(peaks, time_series):
    RR_intervals = []
    sdnn = 0
    for i in range(len(peaks) - 1):
        RR_interval = time_series[peaks[i + 1]] - time_series[peaks[i]]
        RR_intervals.append(RR_interval)

    sdnn = statistics.stdev(RR_intervals)
    return sdnn
