from ligotools.utils import *
from ligotools import readligo as rl
from scipy.signal import butter, filtfilt
from os.path import exists
import matplotlib.mlab as mlab
from scipy.interpolate import interp1d
from os import path
from os.path import exists
from os import remove

fs = 4096
fn_H1 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
Pxx_H1, freqs = mlab.psd(strain_H1, fs, 4*fs)
psd_H1 = interp1d(freqs, Pxx_H1)
dt_H1 = time_H1[1] - time_H1[0]

fn_L1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
Pxx_L1, freqs = mlab.psd(strain_L1, fs, 4*fs)
psd_L1 = interp1d(freqs, Pxx_L1)
dt_L1 = time_H1[1] - time_H1[0]

def test_whiten():
    assert len(whiten(strain_H1, psd_H1, dt_H1)) == 131072
    
def test_write_wavfile(): 
    wavfile_test = whiten(strain_H1, psd_H1, dt_H1)
    write_wavfile("audio/temp.wav", fs, wavfile_test)
    assert exists("audio/temp.wav")
    remove("audio/temp.wav")
    
def test_reqshift(): 
    L1_shift = reqshift(whiten(strain_L1, psd_L1, dt_L1), 400.0, fs)
    assert len(L1_shift) == 131072
    
def test_plot_func():
    fband = [43.0, 300.0]
    bb, ab = butter(4, [fband[0]*2./fs, fband[1]*2./fs], btype='band')
    normalization = np.sqrt((fband[1]-fband[0])/(fs/2))
    
    test_white_L1 = whiten(strain_L1, psd_L1, dt_L1)
    L1_whiten = filtfilt(bb, ab, test_white_L1) / normalization
    #plot_func('L1', 0, 0, 1126259462.4324, 13.2, 'GW150914', 'png', 1126259462.44, 0, 0, 999.74, 0, 0, 4096, 'g', 0)
    assert exists('figurs/'+'GW150914'+"_"+"L1"+"_matchfreq."+"png")
    remove('figurs/'+'GW150914'+"_"+"L1"+"_matchfreq."+"png")