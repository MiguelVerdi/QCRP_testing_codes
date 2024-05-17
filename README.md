# QCRP Test Code Repository

The general procedure to simulate the QCRP experiment is contained in this repository. The procedure has been tested on a virtual machine running Ubuntu `20.04.6` with `ns-3.33` software. The detailed procedure is described as follows:

- 4 types of scenarios are included: `*` = Dense, Sparse, Usparse, Vsparse.
- 4 types of algorithms are included: `**` = AODV, NPCA, PQGR, DGGR.

Each scenario is described by a `.mat` file generated by an external program. These files are located in the `ExperimentDataFiles\Routing_compare_0922` directory and are named as `highway*_**.mat`. These files will be the ones to start working with.

## Proposed Algorithm

Each of the `ExperimentDataFiles\Routing_compare_0922\highway*_**.mat` files is processed in MATLAB Online using the script `ExperimentPrograms\DataProcessingFiles\ExperimentmToCSVComparison.m`. The code should be copied and pasted into MATLAB, and the file should be loaded when prompted by the program. This process generates the `.csv` files found in `ExperimentDataFiles`, specifically in the `ExperimentFiles\**\highway*_**.csv` directory. The data from the `.mat` files is unpacked into these `.csv` files for easy reading by C++.

- A special kind of experiment called DGGR is included. The files are found in `ExperimentFiles\DGGR\highway*_DGGR.mat` and are processed using `ExperimentPrograms\DataProcessingFiles\ExperimentmToCSVDGGR.m`. The code should be copied and pasted into MATLAB, and the `.mat` file from `ExperimentDataFiles\Routing_compare_0922` should be loaded when prompted. This generates the files found in `ExperimentDataFiles`.

- The `ExperimentDataFiles\highway*_**.csv` files are the input for the main C++ simulation. To run this simulation, the `ns3.33` simulation software must be installed. The `.csv` file should be placed in the `ns-allinone-3.33\ns3-3.33` folder. The `ExperimentPrograms\MainSimulation\ExperimentMain.cc` and `ExperimentPrograms\MainSimulation\HighwayExperiment.h` programs should be saved in `ns-allinone-3.33\ns3-3.33\scratch`. The input file must be specified in the main function of `ExperimentPrograms\MainSimulation\ExperimentMain.cc`.

- This experiment takes approximately 4 hours to run and generates the files `ExperimentDataFiles\**\highway*_**_Result.csv`.

- Finally, this file is run in the Python3 program `ExperimentPrograms\VisualizationPrograms\PlotFileExperiment.py`, where the file_path variable must be specified with the file to display.

- There are 4 types of plots: `***` = PDR, Latency, Hops, Distance, DataRate.

- This generates the `ExperimentResultPlots(output)\**\highway*_**_Result_***_plot.png` files.

- Additionally, a final plot is generated with all these graphs together: `ExperimentResultPlots(output)\**\highway*_**_Result_AllFigures.png`.


# General specifications of the simulation

- All the parameters can be changed in the `ExperimentPrograms\MainSimulation\HighwayExperiment.h` for configuration `HighwayExperiment::Configure()`. 

## Simulation Time
The simulation time is set to 1s.

## Communication Specifications
- **Application Protocol:** onoff
- **Sending Rate:** 90 Mbps
- **Max Packages:** 10,000 packages
- **Packet Size:** 500 bytes
- There is a special parameter called `disconDistance` that provides a lower bound for cases where the cars are too far apart. This distance is set to 90 meters.
- A multi-hop ad-hoc network is generated in each experiment with static routing.

### Channel
- **Tx Power:** 23 dBm
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
- The special vehicle with ID = 1 is the source vehicle.

## IP Classification
- **Mask:** 255.255.255.0
- Networks between hops should be in the form 10.x.x.x.
- The second position represents the sender's type (1, 2, 3).
- The third position represents the ID of the car without the class.
- The fourth position represents the sender or receiver (2 for receiver, 1 for sender).
- Example: Car `3031` sending to car `2021`.
  In that case, the network ID would be 10.3.31.0 and the sender would be IP(10.3.31.1) sending to receiver IP(10.3.32.2).
- If the source vehicle is sending, IP(10.0.1.x).

## Cars Simulation
- **Start Position and Start Velocity:** As per the routing evaluation files.
- **Highway Specification:** 5 km.
- **Track of Highway:** 3.5 meters.

## Files `highway*_**.mat` Unpack
- **Filename Format:** `highway*_**.mat`


**Variables:**

1. **`Cluster_time.mat`:** Entire cluster information
   - Timestamp is in the first column.
   - Cluster information of each time slot (ID, x location, y location, speed) is in the second column.
   - Complete cluster information is in the first row.
   - Cluster head information is in the second row.

2. **`Routing_eval.mat`:** Entire routing information
   - Timestamp is in the first column.
   - Cluster information of each time slot (ID, x location, y location, speed) is in the second column.
   - Routing path of each cluster is in the first row.
   - Measured per-hop delay is in the second row.
   - Measured per-hop reliability is in the third column.
   - Measured per-hop channel capacity is in the fourth column.
   - Measured per-hop cost is in the fifth column.

3. **`T_pred_con.mat`:** Prediction time interval
   - Each value corresponds to the number of seconds for mobility prediction.

4. **`T_update_con.mat`:** Time period to spot connection loss
   - Each value corresponds to the number of seconds to update the global topology.

## Data Stacking
- `highway*_PQGR.mat` -> `var3 T_pred_con.mat`
- The time slot is in column 1, and cluster information (GPCA and LPCA) is in the second column.
- `*` = Dense, Sparse, Usparse, Vsparse

**GPCA:** Presented every T_update_con time slots iterations.
1. The number of clusters in the simulation is contained in the column `Relays` (iterate over the three clusters).
2. Inside each cluster, the forward path is in the first row, and the backward path is in the second one (iterate over these two).
3. Each row represents the (cluster ID, x position (m), y position (m), velocity (m/s)).

## Data Formatting for Simulation
- `highway*_**.mat` -> `ExperimentData.m` -> `highway*_**.csv`
- For comparison, it remains the same
- `*` = Dense, Sparse, Usparse, Vsparse

| Iteration (I) | Time (Seconds) | GPCA | Cluster (C) | Node Position | Direction (D) | ID  | X    | Y    | V     |
| --------------| --------------- | ---- | ----------- | ------------- | ------------- | --- | ---- | ---- | ----- |
| 5             | 303             | False| 1           | 1             | 0             | 3020| 384  | -4.8 | 39.35 |
| 19            | 401             | True | 2           | 3             | 1             | 2033| 666.74| -8   | 34.25 |

- In the direction column, `0` means forward, and `1` means backward.

## Data Writing
When the simulation runs, the program generates a file `highway*_**_simResults.csv` with the following headers:

| Time | Total Clusters | GPCA | Max Th | Avg Th | Min Th | Max Lat | Avg Lat | Min Lat | Max PDR | Avg PDR | Min PDR | Max Dist | Avg Dist | Min Dist | Max Hop | Avg Hop | Min Hop |
|------|----------------|------|--------|--------|--------|---------|---------|---------|---------|---------|---------|----------|----------|----------|---------|---------|---------|
| 271  | 3              | 1    | 89.0279| 88.941 | 88.809 | 0.0097876| 0.0078271| 0.0033623| 0.9879  | 0.9817  | 0.9771  | 95.5058  | 77.051   | 61.9015  | 4       | 3.4     | 2       |
| 279  | 3              | 0    | 89.3051| 89.0168| 88.9182| 0.0227674| 0.0130128| 0.0065037| 0.9881  | 0.9780  | 0.9549  | 60.8249  | 46.8088  | 39.3827  | 8       | 5       | 3       |
