import numpy as np
import matplotlib.pyplot as plt

latitudeLength = 111086.2
longitudeLength = 81978.2

averages_log_file = np.genfromtxt("averages_log_file_long.txt", delimiter=", ")
averages_log_file_0odom = np.genfromtxt("averages_log_file_0odom.txt", delimiter=", ")
averages_log_file_01odom = np.genfromtxt("averages_log_file_01odom.txt", delimiter=", ")
gps_log_file = np.genfromtxt("ENTRY_GPS_comp.csv", delimiter=", ")

print(averages_log_file)
print(averages_log_file[:, 0])

pf_result_xs = averages_log_file[:, 0]
pf_result_ys = averages_log_file[:, 1]

pf_results2_xs = averages_log_file_0odom[:, 0]
pf_results2_ys = averages_log_file_0odom[:, 1]

pf_results_01_xs = averages_log_file_01odom[:, 0]
pf_results_01_ys = averages_log_file_01odom[:, 1]

print(gps_log_file)

print(gps_log_file[:, 2])
gps_xs = gps_log_file[:, 2]
gps_ys = gps_log_file[:, 3]

pf_result_xs = gps_xs[0] + pf_result_xs / latitudeLength
pf_result_ys = gps_ys[0] - pf_result_ys / longitudeLength

pf_results2_xs = gps_xs[0] + pf_results2_xs / latitudeLength
pf_results2_ys = gps_ys[0] - pf_results2_ys / longitudeLength

pf_results_01_xs = gps_xs[0] + pf_results_01_xs / latitudeLength
pf_results_01_ys = gps_ys[0] - pf_results_01_ys / longitudeLength

fig, axes = plt.subplots()

axes.plot(pf_result_xs, pf_result_ys, label='C++ Particle Filter')
#axes.plot(pf_results2_xs, pf_results2_ys)
#axes.plot(pf_results_01_xs, pf_results_01_ys)
axes.plot(gps_xs, gps_ys, label='GPS data')

plt.legend()

print(len(gps_xs))
print(len(pf_result_xs))

plt.show()