# config.py

# gets home dir cross platform

import math

# note: if you used our download scripts, this should be right
VOCroot = '/data/PASCAL_VOC/VOCdevkit'  # path to VOCdevkit root dir
COCOroot = '/data/MSCOCO/'
COCO_train_year = '2014'
COCO_test_year = '2015'

# min/max sizes given by following equation:
def get_min_sizes(n_feature_maps, min_dim, min_ratio = 20, max_ratio = 90):
    step = int(math.floor((max_ratio - min_ratio) / (n_feature_maps - 2)))
    min_sizes = []
    for ratio in range(min_ratio, max_ratio + 1, step):
        min_sizes.append(min_dim * ratio / 100.)
    min_sizes = [min_dim*0.1]+min_sizes
    return min_sizes

def get_max_sizes(n_feature_maps, min_dim, min_ratio = 20, max_ratio = 90):
    step = int(math.floor((max_ratio - min_ratio) / (n_feature_maps - 2)))
    max_sizes = []
    for ratio in range(min_ratio, max_ratio + 1, step):
        max_sizes.append(min_dim * (ratio + step) / 100.)
    max_sizes = [min_dim*0.2]+max_sizes
    return max_sizes

# RFB CONFIGS
VOC_300 = {
    'feature_maps': [38, 19, 10, 5, 3, 1],

    'min_dim': 300,

    'steps': [8, 16, 32, 64, 100, 300],

    'min_sizes': get_min_sizes(6, 300),

    'max_sizes': get_max_sizes(6, 300),

    'aspect_ratios': [[2, 3], [2, 3], [2, 3], [2, 3], [2], [2]],

    'variance': [0.1, 0.2],

    'clip': True,
}

VOC_300_mod = {
    'feature_maps': [75, 38, 19, 10, 5, 3, 1],

    'min_dim': 300,

    'steps': [4, 8, 16, 32, 64, 100, 300],

    'min_sizes': get_min_sizes(7, 300),

    'max_sizes': get_max_sizes(7, 300),

    'aspect_ratios': [[2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [2], [2]],

    'variance': [0.1, 0.2],

    'clip': True,
}

VOC_512 = {
    'feature_maps': [64, 32, 16, 8, 4, 2, 1],

    'min_dim': 512,

    'steps': [8, 16, 32, 64, 128, 256, 512],

    'min_sizes': [35.84, 76.8, 153.6, 230.4, 307.2, 384.0, 460.8],

    'max_sizes': [76.8, 153.6, 230.4, 307.2, 384.0, 460.8, 537.6],

    'aspect_ratios': [[2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [2], [2]],

    'variance': [0.1, 0.2],

    'clip': True,
}

COCO_300 = {
    'feature_maps': [38, 19, 10, 5, 3, 1],

    'min_dim': 300,

    'steps': [8, 16, 32, 64, 100, 300],

    'min_sizes': get_min_sizes(7, 300),

    'max_sizes': get_max_sizes(7, 300),

    'aspect_ratios': [[2, 3], [2, 3], [2, 3], [2, 3], [2], [2]],

    'variance': [0.1, 0.2],

    'clip': True,
}

COCO_300_mod = {
    'feature_maps': [75, 38, 19, 10, 5, 3, 1],

    'min_dim': 300,

    'steps': [4, 8, 16, 32, 64, 100, 300],

    'min_sizes': get_min_sizes(7, 300),

    'max_sizes': get_max_sizes(7, 300),

    'aspect_ratios': [[2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [2], [2]],

    'variance': [0.1, 0.2],

    'clip': True,
}

COCO_512 = {
    'feature_maps': [64, 32, 16, 8, 4, 2, 1],

    'min_dim': 512,

    'steps': [8, 16, 32, 64, 128, 256, 512],

    'min_sizes': [20.48, 51.2, 133.12, 215.04, 296.96, 378.88, 460.8],

    'max_sizes': [51.2, 133.12, 215.04, 296.96, 378.88, 460.8, 542.72],

    'aspect_ratios': [[2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [2], [2]],

    'variance': [0.1, 0.2],

    'clip': True,
}

COCO_mobile_300 = {
    'feature_maps': [19, 10, 5, 3, 2, 1],

    'min_dim': 300,

    'steps': [16, 32, 64, 100, 150, 300],

    'min_sizes': [45, 90, 135, 180, 225, 270],

    'max_sizes': [90, 135, 180, 225, 270, 315],

    'aspect_ratios': [[2, 3], [2, 3], [2, 3], [2, 3], [2], [2]],

    'variance': [0.1, 0.2],

    'clip': True,
}

VOC_320 = {
    'feature_maps': [40, 20, 10, 5],

    'min_dim': 320,

    'steps': [8, 16, 32, 64],

    'min_sizes': [32, 64, 128, 256],

    'max_sizes': [],

    'aspect_ratios': [[2], [2], [2], [2]],

    'variance': [0.1, 0.2],

    'clip': True,
}
