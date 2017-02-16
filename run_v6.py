import os
import training_v6
# os.system('python training_v3.py -p0')
# os.system('python training_v3.py -p1')
# os.system('python training_v3.py -p2')
# os.system('python training_v3.py -p3')
# os.system('python training_v3.py -p4')
# os.system('python training_v3.py -p4')
# os.system('python training_v3.py -p5')

acc_list = []
count = 4
pcov = 93
pfc = 93
pcov2 = 93
pfc2 = 93
retrain = 4
model_tag = 'pcov'+str(pcov)+'pcov'+str(pcov2)+'pfc'+str(pfc)+'pfc'+str(pfc2)
while (count < 10):
    param = [
    ('-pcov',pcov),
    ('-pcov2',pcov2),
    ('-pfc',pfc),
    ('-pfc2',pfc2),
    ('-m',model_tag)
    ]
    pfc = pfc+1
    acc = training_v5.main(param)
    model_tag = 'pcov'+str(pcov)+'pfc'+str(pfc)
    acc_list.append(acc)
    count = count + 1
    if (acc < 0.985):
        break

print (acc)

print('accuracy summary: {}'.format(acc_list))
