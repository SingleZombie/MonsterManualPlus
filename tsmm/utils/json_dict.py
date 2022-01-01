import json
import os


class JsonDict(dict):

    def __init__(self, cfg_path):
        super().__init__()
        self.path = cfg_path
        self.dir, self.fn = os.path.split(cfg_path)
        if os.path.exists(cfg_path):
            with open(cfg_path, 'r') as fp:
                new_dict = json.load(fp)
                # TODO: Can we avoid copying dict?
                for key in new_dict:
                    self[key] = new_dict[key]

    def save(self):
        # We only help users create one dir.
        os.makedirs(self.dir, exist_ok=True)
        with open(self.path, 'w') as fp:
            json.dump(self, fp)
