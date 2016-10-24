#!/bin/bash
#SBATCH -A cs5014
#SBATCH -p development
module load anaconda3
python caculate_dis.py >> arraytotaldistance.txt
