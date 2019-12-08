#!/usr/bin/env bash

# Modify the pythonpath
PYTHONPATH=./src:$PYTHONPATH

# Launch you envs
#source activate pytorch-0.4.0

# Location for storing the checkpoint
dir=$1

# Location of your dataset
ntu=$2

# Training the CNN-backbone
#python src/main.py --dir $dir --root $ntu -b 10 -j 4 --epochs 10 --time 8 --pose-predictions
CUDA_VISIBLE_DEVICES=0,1 python src/main.py --dir $dir --root $ntu -b 64 -j 8 --epochs 10 --time 8 --pose-predictions

# Training the Glimpse Clouds
#python src/main.py --dir $dir --root $ntu -b 32 -j 4 --epochs 10 --time 8 --glimpse-clouds --pose-predictions
CUDA_VISIBLE_DEVICES=0,1 python src/main.py --dir $dir --root $ntu -b 64 -j 8 --epochs 10 --time 8 --glimpse-clouds --pose-predictions
# Evaluating on the test set
#python src/main.py --dir $dir --root $ntu -b 32 -j 4 --time 8 --glimpse-clouds --pose-predictions -e
#CUDA_VISIBLE_DEVICES=0,1 python src/main.py --dir $dir --root $ntu -b 64 -j 8 --time 8 --glimpse-clouds --pose-predictions -e # slow
CUDA_VISIBLE_DEVICES=0,1 python src/main.py --dir $dir --root $ntu -b 32 -j 4 --time 8 --glimpse-clouds --pose-predictions -e
