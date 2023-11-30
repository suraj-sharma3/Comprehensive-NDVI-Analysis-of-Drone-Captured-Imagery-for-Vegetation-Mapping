import numpy as np
import rasterio
import matplotlib.pyplot as plt
import os

# Function to categorize average NDVI values into specific ranges
def categorize_ndvi(avg_ndvi):
    if avg_ndvi < 0:
        return "NDVI Range: -1 to 0\nWater Bodies or Barren Surfaces"
    elif avg_ndvi < 0.2:
        return "NDVI Range: 0 to 0.2\nNon-Vegetated or Sparse Vegetation (e.g., bare soil, urban areas)"
    elif avg_ndvi < 0.5:
        return "NDVI Range: 0.2 to 0.5\nShrublands, Grasslands, and Croplands (moderate vegetation cover)"
    elif avg_ndvi < 0.8:
        return "NDVI Range: 0.5 to 0.8\nDense and Healthy Vegetation (e.g., forests, rainforests)"
    else:
        return "NDVI Range: 0.8 to 1\nSaturated and Dense Vegetation (Rare)"

# Function to calculate NDVI statistics
def calculate_ndvi(red_path, nir_path):
    try:
        # Open the red band TIFF file
        with rasterio.open(red_path) as band4:
            # Read the red band data and convert it to float64 data type
            red = band4.read(1).astype('float64')
    except Exception as e:
        print(f"Error opening {red_path}: {e}")
        return None

    try:
        # Open the near-infrared (NIR) band TIFF file
        with rasterio.open(nir_path) as band5:
            # Read the NIR band data and convert it to float64 data type
            nir = band5.read(1).astype('float64')
    except Exception as e:
        print(f"Error opening {nir_path}: {e}")
        return None

    # Calculate NDVI using the formula: (NIR - Red) / (NIR + Red)
    ndvi = np.where(
        (nir + red) == 0.0,  # Handle cases where denominator is zero
        0.0,
        (nir - red) / (nir + red)
    )

    # Calculate average, minimum, and maximum NDVI values
    average_ndvi = np.mean(ndvi)
    min_ndvi = np.min(ndvi)
    max_ndvi = np.max(ndvi)

    # Categorize the average NDVI value
    ndvi_category = categorize_ndvi(average_ndvi)

    # Return values including category
    return str(average_ndvi), str(min_ndvi), str(max_ndvi), ndvi_category


