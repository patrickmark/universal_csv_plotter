#do whatever you want in this file

import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    os.chdir(os.path.dirname(__file__))
    print(os.getcwd())

    import csv_importer as ci
    import data_plotter as dplt

    data = ci.read_network_analyzer_csv("IIDEAL.csv")

    dplt.plot_complex(data.f,data.re,data.im)


if __name__ == "__main__":
    main()