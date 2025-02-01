import torch
path = 'E:/WX/ShiYan/yoloV8/ultralytics/runs/detect/train 0.933/weights/best.pt'
pretrained_dict = torch.load(path)
for k, v in pretrained_dict.items():  # k 参数名 v 对应参数值
        print(k,v)
