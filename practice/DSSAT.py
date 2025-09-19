from DSSATTools import (
    Crop, SoilProfile, Weather, Management, DSSAT, SoilLayer,
    available_cultivars,TabularSubsection
)
#import DSSATTools
import pandas as pd
from datetime import datetime , timedelta
import numpy as np
#import pyeto 

import logging # creating logs

import os

import glob
#import rasterio
# Specify the absolute path for the log file
log_path = r"C:Python\DSSAT_Bushland\task_log.log"

# Ensure the directory exists; if not, create it
log_dir = os.path.dirname(log_path)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure logging to write to the file
logging.basicConfig(filename=log_path, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')