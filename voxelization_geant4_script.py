import glob
import numpy             as np
import pandas            as pd
import matplotlib.pyplot as plt

from math import sqrt
from invisible_cities.evm.event_model import BHit
from invisible_cities.reco import paolina_functions as plf

df = pd.read_csv("data_1000keV_local.csv")

trk_lengths = []
for i in range(df.event_number.max()+1):
    hit_list = [BHit(row.x, row.y, row.z, 1.) for indx, row in df.iterrows()]
    voxels = plf.voxelize_hits(hit_list, np.array((1., 1., 1.)))
    tracks = plf.make_track_graphs(voxels)
    all_lengths = []
    for i in np.arange(len(tracks)):
        all_lengths.append(plf.length(tracks[i]))
    
    trk_lengths.append(max(all_lengths))

plt.figure(0)
plt.hist(trk_lengths, range=(0,100), bins=50)
plt.xlabel("Track length (mm)")
plt.savefig("/data5/users/miryam/temp/voxel/img/voxel_track_length_1000keV_local.pdf")
plt.close(0)
