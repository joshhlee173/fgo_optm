import pandas as pd
import numpy as np
import glob
import os

def load_all_csv(data_path):
    data_dict = {}
    
    # Automatically search for all CSV files
    for file in glob.glob(os.path.join(data_path, "*.csv")):
        file_name = os.path.basename(file).replace('.csv', '')
        df = pd.read_csv(file)
        
        # Handle timestamps if they exist
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
            df.set_index('timestamp', inplace=True)
            df = df.sort_index()

        data_dict[file_name] = df

    return data_dict

# Example usage
data_path = "data/csv_files/test_run_2/"
data_dict = load_all_csv(data_path)

# Access example data
imu = data_dict['22_37_40_vehicle_imu_0'].head()
gyro = data_dict['22_37_40_sensor_gyro_0'].head()

# Factor Graph
import symforce
try:
    symforce.set_epsilon_to_symbol()
except symforce.AlreadyUsedEpsilon:
    print("Already set symforce epsilon")
    pass

import symforce.symbolic as sf

# gnss_data = np.load(data_dict['22_37_40_vehicle_global_position_groundtruth_0.csv'])
gt = data_dict['22_37_40_vehicle_global_position_groundtruth_0'].head()
gt = pd.read_csv(data_path + '22_37_40_vehicle_global_position_groundtruth_0.csv')
print(gt.to_numpy()[0,:])