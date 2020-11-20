import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import json

def get_produce(json_file):
    # Each row in dataset contains json-like data structure, converts
    sizes = json.loads(json_file)
    # Assumptions for parameters
    flat_fraction = np.random.normal(.42,.1)
    pct_roof_farmed = np.random.normal(.3,.05)
    produce_rate_per_sf = np.random.uniform(.5,3)
    # Initialize lists                                 
    flat_roof_size = []
    dist = []
    # Loop through each bin and the distribution of the capacity                                 
    for size in sizes:
        # Predicted rooftop solar capacity in KWs DC
        kw_install = size[0]
        # Number of roofs in this bin
        roofs = size[1]
        # Convert to watts, divide by 250 W panel, multiply by size of panel in sq ft, get fraction flat 
        sqft = kw_install * 1000 / 250 * flat_fraction * 17.6183686
        # Append to lists
        flat_roof_size.append(sqft)
        dist.append(roofs)
    # Convert to numpy for element-wise multiplication property
    flat_roof_size = np.array(flat_roof_size) 
    dist = np.array(dist) 
    # Only considers roofs above 10,000 Square Feet
    size_above_10000 = flat_roof_size[flat_roof_size > 10000]
    dist_above_10000 = dist[flat_roof_size > 10000]
    return (np.sum(size_above_10000 * dist_above_10000 * produce_rate_per_sf * pct_roof_farmed),np.sum(dist_above_10000))
