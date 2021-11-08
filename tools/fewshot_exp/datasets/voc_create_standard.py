import os
from maskrcnn_benchmark.data.datasets.voc import PascalVOCDataset
cls = PascalVOCDataset.CLASSES[1:]
yolodir = '../Fewshot_Detection'
for shot in [10, 5, 3, 2, 1]:
    ids = []
    for c in cls:
        with open(yolodir + '/data/vocsplit/box_%dshot_%s_train.txt'%(shot, c)) as f:
            content = f.readlines()
        content = [i.strip().split('/')[-1][:-4] for i in content]
        ids += content
    ids = list(set(ids))
    with open('datasets/voc/VOC2007/ImageSets/Main/trainval_%dshot_novel_standard.txt'%shot, 'w+') as f:
        for i in ids:
            if '_' not in i:
                f.write(i + '\n')
    with open('datasets/voc/VOC2012/ImageSets/Main/trainval_%dshot_novel_standard.txt'%shot, 'w+') as f:
        for i in ids:
            if '_' in i:
                f.write(i + '\n')

