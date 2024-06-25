import torch
import numpy as np
from NNyyy_nn import Net # 请确保从同一文件导入Net类
from sklearn.metrics import accuracy_score
import pandas as pd
model = Net()
#model.load_state_dict(torch.load('/ifs1/User/yanyueyang/yyy/ROS/ref/step09/nn/xgboos_2class.pkl'))
#nn__2class.pkl
model.load_state_dict(torch.load('nn_nclass_model_ac01.pth'))
data={}
#data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2]
with open('DPC.out', 'r') as f:

    lines = f.readlines()
    lines = lines[1:]
    id=lines[0]
    print(id)
    for line in lines:
        items = line.strip().split("\t")
        name = items[0]
        features = [float(item) for item in items[1:]]
        data[name] = features
#tensor_data = torch.tensor([data], dtype=torch.float32)
tensor_data = torch.tensor(list(data.values()), dtype=torch.float32)
output = model(tensor_data)
f1=output.detach().numpy()
f2=pd.DataFrame(f1)

f2.replace({"0":"thioredoxin reductase", "1":"cytochrome c peroxidase", "2":"peroxidase", "3":"glutathione peroxidase", "4":"nickel superoxide dismutase", "5":"alkyl hydroperoxide reductase", "6":"thioredoxin 1", "7":"thioredoxin 2", "8":"glutaredoxin 1", "9":"glutaredoxin 2", "10":"catalase", "11":"catalase-peroxidase", "12":"superoxide dismutase 2", "13":"superoxide dismutase 1", "14":"NADH peroxidase", "15":"superoxide reductase", "16":"Mn-containing catalase", "17":"monothiol glutaredoxin", "18":"thiol peroxidase", "19":"peroxiredoxin 5", "20":"peroxiredoxin 6", "21":"peroxiredoxin 1", "22":"alkyl hydroperoxide reductase 1", "23":"rubrerythrin", "24":"peroxiredoxin 3", "25":"glutaredoxin 3"},inplace=True)
f2.to_csv("final_Nclass.out",sep="\t",index=False)
print(f2.idxmax(1))
f2.to_csv("N_nn.out",sep=" ",index=False)
f3=pd.DataFrame(f2.idxmax(1))
f3.to_csv("N_nn.res",sep=" ",index=False)
#predictions = torch.argmax(output, dim=1).tolist()
#print(output)
#for i, name in enumerate(data.keys()):
#    print("样本 %s 的预测结果为: %d" % (name, predictions[i]))
#    print(predictions[i])
