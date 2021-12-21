import torch
import torch.nn as nn
class neuralModel(nn.Module):
    def __init__(self,device):
        super(neuralModel,self).__init__()
        self.device=device
    def dump(self,filename):
        torch.save(model,filename)
    def load(self,filename):
        state_dict=torch.load(open(filename,"rb"),map_location=self.device)
        self.load_state_dict(state_dict,strict=True)
