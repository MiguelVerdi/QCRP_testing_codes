# QCRP Test Code Repository

This repository contains the general procedure to simulate the QCRP experiment. The procedure has been tested on a virtual machine running Ubuntu `20.04.6` with `ns-3.33` software. The detailed procedure is described as follows:

- There are 4 types of scenarios: `*` = Dense, Sparse, Usparse, Vsparse.
- There are 4 types of algorithms: `**` = AODV, NPCA, PQGR, DGGR.

Each scenario is described by a `.mat` file generated by an external program. These files are located in the `ExperimentDataFiles/Routing_compare_0922` directory and are named as `highway*_**.mat`. These will be the files you start working with.

## Proposed Algorithm

Each of the `ExperimentDataFiles/Routing_compare_0922/highway*_**.mat` files is processed in MATLAB Online using the script `ExperimentPrograms/DataProcessingFiles/ExperimentmToCSVComparison.m`. To do this, copy and paste the code into MATLAB and load the file when prompted by the program. This process generates the `.csv` files found in `ExperimentDataFiles`, specifically in the `ExperimentFiles/**/highway*_**.csv` directory. These `.csv` files contain the data from the `.mat` files, unpacked so that C++ can read them more easily.


- There is an special kind of experiment called DGGR, the files are found in `ExperimentFiles/DGGR/highway*_DGGR.mat` this file is processed in `ExperimentPrograms\DataProcessingFiles\ExperimentmToCSVDGGR.m` you only have to copy paste the code in matlab and charge the file after running the program, it would ask for the file this should be the .mat file found in `ExperimentDataFiles\Routing_compare_0922`, this generates the files found in `ExerimentDataFiles`.
- 

- The `ExperimentDataFiles/highway*_**.csv` files are the input for the main C++ simulation, to run this file you must have installed the simulation software `ns3.33` and in the `ns-allinone-3.33/ns3-. 33` folder paste the `.csv` file, save the `ExperimentPrograms\MainSimulation\ExperimentMain.cc` and `ExperimentPrograms\MainSimulation\HighwayExperiment.h` program in `ns-allinone-3.33/ns3-.33/scratch` and to modify the input file you must specify it in the main function of `ExperimentPrograms\MainSimulation\ExperimentMain.cc`.
  
- This experiment takes approximately 4 hours to run and generates the files `ExperimentDataFiles\**\highway*_**_Result.csv`. 

- Finally this file is run in the python3 program `ExperimentPrograms\VisualizationPrograms\PlotFileExperiment.py` where you must specify in the file_path variable the file you want to display.

- There are 4 types of plots `***` = PDR,Lattency,Hops,Distance,DataRate. 
  
- This generates the `ExperimentResultPlots(output)\**\highway*_**_Result_***_plot.png` files.

- In addition a final plot is generated with all these graphs together `ExperimentResultPlots(output)\**\highway*_**_Result_AllFigures.png`.

# General specifications of the simulation
- All the parameters can be changes in the `ExperimentPrograms\MainSimulation\HighwayExperiment.h` for configurtion `HighwayExperiment::Configure()` 
## Simulation Time
Simulation time = 1s.
## Communication Specifications
- **Application Protocol:** onoff
- **Sending Rate:** 90 Mbps
- **Max Packages:** 10,000 packages
- **Packet Size:** 500 bytes
- There is a special parameter called `disconDistance` that provides a lower bound for cases where the cars are too far apart. This distance is 90 meters.
- It generates a multi-hop ad-hoc network in each experiment with static routing.

### Channel
- **Tx Power:** 35 dBm
- **Frequency:** 5.9 GHz
- **Bandwidth:** 40 MHz
- **Phy Mode:** VhtMcs6

## Vehicle Classification
- **ID Format:** 4 numbers (type XXX)
- **Types:**
  - 1 - Slow Vehicle
  - 2 - Normal Vehicle
  - 3 - Fast Vehicle
- Example: ID = 2012 represents vehicle 12 of normal velocity vehicles.
- Special Vehicle with ID = 1 is the source vehicle.

## IP Classification
- **Mask:** 255.255.255.0
- Networks between hops should be in the form 10.x.x.x.
- Second position represents the sender's type (1, 2, 3).
- Third position represents the ID of the car without the class.
- Fourth position represents the sender or receiver (2 for receiver, 1 for sender).
- Example: Car `3031` sending to car `2021`.
  In that case, the network ID would be 10.3.31.0 and the sender would be IP(10.3.31.1) sending to receiver IP(10.3.32.2).
- If the source vehicle is sending, IP(10.0.1.x).

## Cars Simulation
- **Start Position and Start Velocity:** As the routing eval files.
- **Highway Specification:** 5 km.
- **Track of Highway:** 3.5 meters.

## Files `highway*_**.mat` Unpack
- **Filename Format:** `highway*_**.mat`


**Variables:**
1. **`Cluster_time.mat`:** Entire cluster information
   - First column: Timestamp
   - Second column: Cluster information of each time slot (ID, x location, y location, speed)
   - First row: Complete cluster information
   - Second row: Cluster head information

2. **`Routing_eval.mat`:** Entire routing information
   - First column: Timestamp
   - Second column: Cluster information of each time slot (ID, x location, y location, speed)
   - First row: Routing path of each cluster
   - Second row: Measured per-hop delay
   - Third column: Measured per-hop reliability
   - Fourth column: Measured per-hop channel capacity
   - Fifth column: Measured per-hop cost

3. **`T_pred_con.mat`:** Prediction time interval
   - Each value corresponds to the number of seconds for mobility prediction

4. **`T_update_con.mat`:** Time period to spot connection loss
   - Each value corresponds to the number of seconds to update the global topology

## Data Stacking
- `highway*_PQGR.mat` -> `var3 T_pred_con.mat`
- Column 1 is the time slot, the second column has cluster information (GPCA and LPCA)
- `*` = Dense, Sparse, Usparse, Vsparse

**GPCA:** Presented every T_update_con time slots iterations.
1. The column `Relays` contains the number of clusters in the simulation (iterate over the three clusters).
2. Inside each cluster, the first row is the forward path, and the second one is the backward path (iterate over these two).
3. Each row represents the (cluster ID, x position (m), y position (m), velocity (m/s)).

## Data Formatting for Simulation
- `highway*_**.mat` -> `ExperimentData.m` -> `highway*_**.csv`
- For the comparison, it is the same
- `*` = Dense, Sparse, Usparse, Vsparse

| Iteration (I) | Time (Seconds) | GPCA | Cluster (C) | Node Position | Direction (D) | ID  | X    | Y    | V     |
| --------------| --------------- | ---- | ----------- | ------------- | ------------- | --- | ---- | ---- | ----- |
| 5             | 303             | False| 1           | 1             | 0             | 3020| 384  | -4.8 | 39.35 |
| 19            | 401             | True | 2           | 3             | 1             | 2033| 666.74| -8   | 34.25 |

- In the direction column, `0` means forward, and `1` means backward.

## Data Writing
When running the simulation, the program generates a file `highway*_**_simResults.csv` with the following headers:

| Time | Total Clusters | GPCA | Max Th | Avg Th | Min Th | Max Lat | Avg Lat | Min Lat | Max PDR | Avg PDR | Min PDR | Max Dist | Avg Dist | Min Dist | Max Hop | Avg Hop | Min Hop |
|------|----------------|------|--------|--------|--------|---------|---------|---------|---------|---------|---------|----------|----------|----------|---------|---------|---------|
| 271  | 3              | 1    | 89.0279| 88.941 | 88.809 | 0.0097876| 0.0078271| 0.0033623| 0.9879  | 0.9817  | 0.9771  | 95.5058  | 77.051   | 61.9015  | 4       | 3.4     | 2       |
| 279  | 3              | 0    | 89.3051| 89.0168| 88.9182| 0.0227674| 0.0130128| 0.0065037| 0.9881  | 0.9780  | 0.9549  | 60.8249  | 46.8088  | 39.3827  | 8       | 5       | 3       |

