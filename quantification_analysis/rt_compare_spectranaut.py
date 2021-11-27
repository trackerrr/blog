import math
import matplotlib.pyplot as plt
import numpy as np

dir = "/Users/mac/Desktop/dia_data_reading/data/"
file1 = "R01"
file2 = "R02"

rt_file = dir + "rt_" + file1 + "_" + file2 + ".tsv"

results = np.genfromtxt(dir + file1 + "_peak_ms1_trails_" + file2 + ".tsv", delimiter='\t', skip_header=1)
rt_results = np.genfromtxt(rt_file)

rt1 = []
rt2 = []
rt_diff = []
rt_compare = []

for i in range(0, len(results)):
    rt1.append(results[i][1])
    rt2.append(results[i][5])
    # rt_diff.append(rt1 - rt2)
    rt_diff.append(results[i][8])

for i in range(1, len(rt_results)):
    rt_compare.append(rt_results[i][0] - rt_results[i-1][0])

rt1 = np.array(rt1)
rt2 = np.array(rt2)
rt_diff = np.array(rt_diff)
rt_compare = np.array(rt_compare)

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# ax.scatter(rt1, rt2, alpha=0.8, c="blue", edgecolors='none', s=30)
# plt.hist2d(rt1, rt2, bins=(100, 100), cmap=plt.cm.BuPu)
# plt.colorbar()
# plt.hist(rt_diff, bins='auto', label='all')
# plt.title(file1 + " vs " + file2 + " RT difference")
# plt.xlabel("rt(" + file1 + ") - rt(" + file2 + ")")
# plt.ylabel("counts")
# plt.savefig(file1 + "_vs_" + file2 +"_RT")
# plt.show()

plt.hist(rt_compare, bins='auto', label='all')
plt.title(file1 + " RT difference of adjacent scans")
plt.xlabel("")
plt.ylabel("counts")
plt.savefig(file1 +"_RT_adjacent_scans")
plt.show()

'''
plt.hist(rt1, bins='auto', label='all',color = "blue")
plt.hist(rt_diff, bins='auto', label='all', color = "red")
plt.xlabel(file1)
plt.ylabel("counts")
# plt.savefig(file1 + "_vs_" + file2 +"_RT")
plt.show()

plt.scatter(rt1, rt_diff, alpha=0.8, c="blue", edgecolors='none', s=30)
plt.xlabel(file1 + " RT")
plt.ylabel("rt(" + file1 + ") - rt(" + file2 + ")")
plt.savefig(file1 +"_vs_RTDiff_scatter")
plt.show()

plt.hist2d(rt1, rt_diff, bins=(100, 100))
plt.xlabel(file1 + " RT")
plt.ylabel("rt(" + file1 + ") - rt(" + file2 + ")")
plt.savefig(file1 +"_vs_RTDiff_hist2d")
plt.show()
'''



