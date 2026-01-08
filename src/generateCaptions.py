import os
from pathlib import Path
from PIL import Image
import pandas as pd
from tqdm import tqdm
import shutil

class CarDatasetCollector:
    "Collects car images from a specified directory structure."
