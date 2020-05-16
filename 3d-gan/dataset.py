import gzip
import os
import torch
import numpy as np
from torch.utils.data import Dataset

class ModelNet10GAN(Dataset):
    """
    Custom dataset for training a 3D-GAN, without using a variational autoencoder.
    I have not implemented download of dataset. I don't know how to download using python script (too lazy to find out).
    """
    def __init__(self, dir="./", download=False):
        """
        Args:
            dir (string): Path in which you want the dataset 
                to be saved (keep a minimum space of 9 GBs).
            download (boolean): Set to True if you want to download. 
                Default=False.
        """
        self.dir=dir
        self.download=download
        self.transform=transform
        if not _check_exists():
            raise RuntimeError('modelnet10.npy.gz not present in '+self.dir)
        with gzip.open(self.dir+'modelnet10.npy.gz','rb') as f:
            self.arr=np.load(f)
        

    def __len__(self):
        return (self.arr.shape[0]-1)

    def _check_exists(self):
        return (os.path.exists(self.dir+"modelnet10.npy.gz"))

    def __getitem__(self, ind):
        """
        Args:
            ind (int): Index of the sample you want. 

        Returns:
            Tensor: (torch.Tensor, Size: (1,64,64,64))
        """
        return torch.tensor(self.arr[ind+1])