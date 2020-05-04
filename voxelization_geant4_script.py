import glob
import numpy             as np
import pandas            as pd
import matplotlib.pyplot as plt

from math import sqrt
from invisible_cities.evm.event_model import BHit
from invisible_cities.reco import paolina_functions as plf

df = pd.read_csv("data_1000keV_local.csv", usecols=["event_number", "x", "y", "z"])

mask = df.event_number < 20
df   = df[mask]

trk_lengths = []
for i in range(df.event_number.max()+1):
    #df_i = df[df.event_number == i]
    hit_list = [BHit(row.x, row.y, row.z, 1.) for indx, row in df[df.event_number == i].iterrows()]
    voxels = plf.voxelize_hits(hit_list, np.array((1., 1., 1.)))
    tracks = plf.make_track_graphs(voxels)
    
    all_lengths = []
    for j in np.arange(len(tracks)):
        all_lengths.append(plf.length(tracks[j]))
    
    trk_lengths.append(max(all_lengths))

plt.figure(0)
plt.hist(trk_lengths, range=(0,200), bins=70)
plt.xlabel("Track length (mm)")
plt.savefig("/data5/users/miryam/temp/voxel/img/voxel_track_length_1000keV_local_20events.pdf")
plt.close(0)
