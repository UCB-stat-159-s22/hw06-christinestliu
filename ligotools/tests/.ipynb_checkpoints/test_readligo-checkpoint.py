from ligotools import readligo as rl

def test_loaddata_H1(): 
    load_H1_test = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain, time, channel_dict = rl.loaddata(load_H1_test, 'H1')
    assert (strain is not None) & (time is not None) & (channel_dict is not None) 

def test_loaddata_L1():
    load_L1_test = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    strain, time, channel_dict = rl.loaddata(load_L1_test, 'L1')
    assert (strain is not None) & (time is not None) & (channel_dict is not None)

def test_read_hdf5_H1():
    read_H1_test = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnameLidst = rl.read_hdf5(read_H1_test, 'H1')
    assert (strain is not None) & (gpsStart is not None) & (ts is not None) & (qmask is not None) & (shortnameList is not None) & (injmask is not None)

def test_read_hdf5_L1():
    read_L1_test = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnameLidst = rl.read_hdf5(read_L1_test, 'L1')
    assert (strain is not None) & (gpsStart is not None) & (ts is not None) & (qmask is not None) & (shortnameList is not None) & (injmask is not None)
