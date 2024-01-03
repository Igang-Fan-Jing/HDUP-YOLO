import torch 
from model.gdip_model import GatedDIP
from model.yolov3 import Yolov3

class Yolov3GatedDIP(torch.nn.Module):
    def __init__(self):
        super(Yolov3GatedDIP,self).__init__()
        self.gated_dip = GatedDIP(256)
        self.yolov3 = Yolov3()
        #self.yolov3.load_darknet_weights(weights_path)
    
    def forward(self,x):
        out_x,gates = self.gated_dip(x)
        p,p_d = self.yolov3(out_x)
        return out_x,gates,p,p_d
