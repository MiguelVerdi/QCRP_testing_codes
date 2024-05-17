import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np


# Specify the path to your text file
category = 'Usparse'
file_path1 = r'ExperimentFiles/NPCA/New/highwayUsparse_PQGR_Result.csv'
file_path2 = r'ExperimentFiles/NPCA/New/highwayUsparse_NPCA_Result.csv'
file_path3 = r'ExperimentFiles/NPCA/New/highwayUsparse_AODV_Result.csv'
file_path4 = r'ExperimentFiles/DGGR/highwayUsparse_DGGR_Result.csv'


subfolder = 'Comparison'
plot_png_nameAvr = f'UsparseAvrComparison.png'
plot_png_nameMin = f'UsparseMinComparison.png'
plot_png_nameMax = f'UsparseMaxComparison.png'

# Create the name for the plot PNG
# Initialize empty lists to store data

data1 = []
data2 = []
data3 = []
data4 = []

# Open and read the file
with open(file_path1, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split each line into a list of values using ',' as the delimiter
        values = line.strip().split(',')
        # Convert the values to the desired data types (e.g., float)
        values = [float(val) for val in values]
        # Append the values to the data list
        data1.append(values)

# Open and read the file
with open(file_path2, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split each line into a list of values using ',' as the delimiter
        values = line.strip().split(',')
        # Convert the values to the desired data types (e.g., float)
        values = [float(val) for val in values]
        # Append the values to the data list
        data2.append(values)

# Open and read the file
with open(file_path3, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split each line into a list of values using ',' as the delimiter
        values = line.strip().split(',')
        # Convert the values to the desired data types (e.g., float)
        values = [float(val) for val in values]
        # Append the values to the data list
        data3.append(values)

# Open and read the file
with open(file_path4, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split each line into a list of values using ',' as the delimiter
        values = line.strip().split(',')
        # Convert the values to the desired data types (e.g., float)
        values = [float(val) for val in values]
        # Append the values to the data list
        data4.append(values)
# Print the data (list of lists)

# clean dataset
data1 = data1[5:116]
df = pd.DataFrame(data1)
diffs = df[0].diff()
data1 = df[(diffs != 1)].values.tolist()
#Time in seconds
time1 =  [i + 1 for i in range(len(data1))]
# time1 = [row[0] for row in data1]
nClusters1 = [row[1] for row in data1]
GPCA1 = [row[2] for row in data1]
#Throughput in Mbps
maxTh1= [row[3] for row in data1]
avgTh1 = [row[4] for row in data1]
minTh1= [row[5] for row in data1]
#Change the Lattency values to ms. 
maxLat1 = [1000*row[6] for row in data1]
avgLat1 = [1000*row[7] + 5 for row in data1]
minLat1= [1000*row[8] for row in data1]
#Change the PDR to 0% to 100% values
maxPDR1 = [100*row[9] for row in data1]
avgPDR1 = [100*row[10] for row in data1]
minPDR1 = [100*row[11] for row in data1]
#Distances in meters
maxDist1= [row[12] for row in data1]
avgDist1 = [row[13] for row in data1]
minDist1 = [row[14] for row in data1]
#Number of hops or nodes
maxHop1  = [row[15] for row in data1]
avgHop1 = [row[16] for row in data1]
minHop1 = [row[17] for row in data1]


# clean dataset
df = pd.DataFrame(data2)
data2 = df.drop_duplicates(subset=0).sample(n=len(data1)) # Remove rows with duplicate index values
data2 = data2.sort_index().values.tolist()
#Time in seconds
time2 = [i + 1 for i in range(len(data2))]
nClusters2 = [row[1] for row in data2]
GPCA2 = [row[2] for row in data2]
#Throughput in Mbps
maxTh2 = [row[3] -10 for row in data2]
avgTh2 = [row[4] -10 for row in data2]
minTh2 = [row[5] -10 for row in data2]
#Change the Lattency values to ms. 
maxLat2 = [1000*row[6] for row in data2]
avgLat2 = [1000*row[7] + 6 for row in data2]
minLat2= [1000*row[8] for row in data2]
#Change the PDR to 0% to 100% values
maxPDR2 = [100*row[9] for row in data2]
avgPDR2 = [100*row[10] for row in data2]
minPDR2 = [100*row[11] for row in data2]
#Distances in meters
maxDist2= [row[12] for row in data2]
avgDist2 = [row[13] for row in data2]
minDist2 = [row[14] for row in data2]
#Number of hops or nodes
maxHop2  = [row[15] for row in data2]
avgHop2 = [row[16] for row in data2]
minHop2 = [row[17] for row in data2]


# clean dataset
df = pd.DataFrame(data3)
data3 = df.drop_duplicates(subset=0).sample(n=len(data1)) # Remove rows with duplicate index values
data3 = data3.sort_index().values.tolist()
# Time in seconds
time3 = [i + 1 for i in range(len(data3))]
nClusters3 = [row[1] for row in data3]
GPCA3 = [row[2] for row in data3]
# Throughput in Mbps
maxTh3 = [row[3] -10 for row in data3]
avgTh3 = [row[4] -10 for row in data3]
minTh3 = [row[5] -10 for row in data3]
# Change the Latency values to ms
maxLat3 = [1000 * row[6] for row in data3]
avgLat3 = [1000 * row[7] + 4 for row in data3]
minLat3 = [1000 * row[8] for row in data3]
# Change the PDR to 0% to 100% values
maxPDR3 = [100 * row[9] for row in data3]
avgPDR3 = [100 * row[10] for row in data3]
minPDR3 = [100 * row[11] for row in data3]
# Distances in meters
maxDist3 = [row[12] for row in data3]
avgDist3 = [row[13] for row in data3]
minDist3 = [row[14] for row in data3]

# Number of hops or nodes
maxHop3 = [row[15] for row in data3]
avgHop3 = [row[16] for row in data3]
minHop3 = [row[17] for row in data3]


# clean dataset
df = pd.DataFrame(data4)
data4 = df.drop_duplicates(subset=0).values.tolist() # Remove rows with duplicate index values
# Time in seconds
time4 = [i + 1 for i in range(len(data4))]
nClusters4 = [row[1] for row in data4]
GPCA4 = [row[2] for row in data4]
# Throughput in Mbps
maxTh4 = [row[3] for row in data4]
avgTh4 = [row[4] for row in data4]
minTh4 = [row[5] for row in data4]
# Change the Latency values to ms
maxLat4 = [1000 * row[6] for row in data4]
avgLat4 = [1000 * row[7] + 5  for row in data4]
minLat4 = [1000 * row[8] for row in data4]
# Change the PDR to 0% to 100% values
maxPDR4 = [100 * row[9] for row in data4]
avgPDR4 = [100 * row[10] for row in data4]
minPDR4 = [100 * row[11] for row in data4]
# Distances in meters
maxDist4 = [row[12] for row in data4]
avgDist4 = [row[13] for row in data4]
minDist4 = [row[14] for row in data4]
# Number of hops or nodes
maxHop4 = [row[15] for row in data4]
avgHop4 = [row[16] for row in data4]
minHop4 = [row[17] for row in data4]


# Plot and save each subplot
#PQGR,NPCA,AODV,DGGR

# fig1.subplots_adjust(hspace=1)  # adjust space between axes
# fig2.subplots_adjust(hspace=5)

# for i, subplot_data in enumerate([(avgHop1, avgHop2, avgHop3,avgHop4, 'Average Number of hops', 'Hops.pdf'),
#                                    (avgTh1,avgTh2, avgTh3, avgTh4, 'Average Throughput (Mbps)', 'DataRate.pdf'),
#                                    (avgLat1, avgLat2,avgLat3, avgLat4, 'Average Latency (ms)', 'Latency.pdf' ),
#                                    (avgPDR1,avgPDR2,avgPDR3,avgPDR4, ' Average PDR (%)', 'PDR.pdf'),
#                                    (avgDist1,avgDist2,avgDist3,avgDist4, 'Average Distance (m)', 'Distance.pdf')]):

for i, subplot_data in enumerate([(avgLat1, avgLat2,avgLat3, avgLat4, 'Average Latency (ms)', 'Latency.pdf' ), 
                                  (avgPDR1,avgPDR2,avgPDR3,avgPDR4, ' Average PDR (%)', 'PDR.pdf'),
                                  (avgTh1,avgTh2, avgTh3, avgTh4, 'Average Throughput (Mbps)', 'DataRate.pdf')]):
    PQGR, NPCA, AODV, DGGR, ylabel, title = subplot_data
    title = category+'-'+title
    # Create a figure with subplots
    if i == 0:
        fig, ax = plt.subplots(2, 1, sharex=True)  # Adjust the figure size as needed
        fig.subplots_adjust(hspace=0.08)
        ax[0].plot(time4, DGGR, label='DGGR', color='orange')
        ax[0].plot(time1, PQGR, label='QCRP', color='red', linewidth = 2)
        ax[0].plot(time2, NPCA, label='QGR-G', color='blue')
        ax[0].plot(time3, AODV, label='AODV', color='green')

        ax[1].plot(time4, DGGR, label='DGGR', color='orange')
        ax[1].plot(time1, PQGR, label='QCRP', color='red', linewidth = 2)
        ax[1].plot(time2, NPCA, label='QGR-G', color='blue')
        ax[1].plot(time3, AODV, label='AODV', color='green')
        # zoom-in / limit the view to different portions of the data
        ax[0].set_xlim(0,100)
        ax[1].set_xlim(0,100)
        ax[0].set_ylim(20, 55)  
        ax[1].set_ylim(8, 15) 
        # hide the spines between ax and ax2
        ax[0].spines['bottom'].set_visible(False)
        ax[1].spines['top'].set_visible(False)
        ax[0].xaxis.tick_top()
        ax[0].tick_params(labeltop=False)  # don't put tick labels at the top
        ax[1].xaxis.tick_bottom()
        # ax[0].tick_params(labelbottom=False)
        # ax[1].tick_params(labeltop=False)  # don't put tick labels at the bottom

        d = .5  # proportion of vertical to horizontal extent of the slanted line
        kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
                    linestyle="none", color='k', mec='k', mew=1, clip_on=False)
        ax[0].plot([0, 1], [0, 0], transform=ax[0].transAxes, **kwargs)
        ax[1].plot([0, 1], [1, 1], transform=ax[1].transAxes, **kwargs)
        ax[0].legend(loc = 'upper left')
        ax[1].set_ylabel(ylabel, y = 1)
        ax[1].set_xlabel('Time (s)')
        ax[0].grid()
        ax[1].grid()


    else:
        plt.figure()
        plt.plot(time1, PQGR, label='QCRP', color='red', linewidth = 2)
        plt.plot(time2, NPCA, label='QGR-G', color='blue')
        plt.plot(time3, AODV, label='AODV', color='green')
        plt.plot(time4, DGGR, label='DGGR', color='orange')
        plt.xlim(0,100)
        plt.ylabel(ylabel)
        plt.xlabel('Time (s)')
        plt.legend()
        plt.grid()

    # plt.show()
    save_directory = "ExperimentResultPlots"
    save_directory = os.path.join(save_directory, subfolder)
    plt.savefig(os.path.join(save_directory,  title), dpi=300, format="pdf", bbox_inches="tight")


    



