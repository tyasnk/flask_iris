import os
import pickle


class LoadModel:
    def __init__(self, model_dir, model_filename):
        filename = os.path.join(model_dir, model_filename)
        with open(filename, "rb") as f:
            self.model = pickle.load(f)
