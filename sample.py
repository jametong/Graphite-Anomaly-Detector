#!/usr/bin/env python

from detector.detector import SlidingWindowDetector, SpikeDetector
from pylab import show, plot

import sys
import json
import time

def main(filename):
    fp = open(filename, 'r')

    data = json.load(fp)

    fp.close()

    detector_data = data[0]['datapoints']

    timeseries = [t[0] for t in detector_data]
    timestamps = [t[1] for t in detector_data]

    res = SlidingWindowDetector.detect_anomalies(timeseries, timestamps)

    plot_data(timeseries, timestamps, res)

def plot_data(timeseries, timestamps, res):
    """Plots results for timeseries"""
    r_t = []
    r_d = []
    for r in res:
        r_t.append(r)
        r_d.append(0)

    plot(timestamps, timeseries, r_t, r_d, "rs")
    show()

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

