from torchvision import datasets
from torchvision import transforms
from torchvision import utils
from torch.utils.data import Dataset 
from torch.utils.data import DataLoader
import torch 
import os
# Ignore warnings
import warnings
import matplotlib.pyplot as plt
import pathlib
warnings.filterwarnings("ignore")
from skimage import io


class CustomDataset(Dataset):
    """Create a custom dataset object."""
    def __init__(self, root_dir, transform=None):
        self.root_dir = pathlib.Path(root_dir)
        self.transform = transform
        self.files = os.listdir(self.root_dir)

    def __len__(self):
        return len(os.listdir(self.root_dir))

    def __getitem__(self, idx):
        img_name = self.root_dir/self.files[idx]
        image = io.imread(img_name)
        if self.transform:
            image = self.transform(image)
        return image


def show_batch(sample_batched):
    images_batch = sample_batched
    batch_size = len(images_batch)
    grid = utils.make_grid(images_batch)
    plt.imshow(grid.numpy().transpose((1, 2, 0)))
    


if __name__ == '__main__':
    compose = transforms.Compose(
        [
            transforms.ToPILImage(),
            transforms.Resize((256, 256)),
            transforms.ToTensor(),
            #transforms.Normalize((.5, .5, .5), (.5, .5, .5))
        ])
    gta = CustomDataset(root_dir='/home/abanihirwe/datasets/gta/images/', transform=compose)
    print(len(gta))
    
    gta_loader = DataLoader(gta, num_workers=2, shuffle=True, batch_size=4)
    for i_batch, sample_batched in enumerate(gta_loader):
        print(i_batch, sample_batched.size())

        if i_batch == 3:
            show_batch(sample_batched)
            plt.show()
            break