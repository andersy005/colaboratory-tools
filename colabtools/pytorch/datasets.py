from torchvision import datasets
from torchvision import transforms 
from torch.utils.data import Dataset 
from torch.utils.data import DataLoader
import torch 


class CustomDataset(Dataset):
    """Create a custom dataset object."""
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.files = os.listdir(root_dir)

    def __len__(self):
        return len(os.listdir(self.root_dir))

    def __getitem__(self, idx):
        img_name = self.root_dir/self.files[idx]
        image = io.imread(img_name)
        if self.transform:
            image = self.transform(image)
        return image
