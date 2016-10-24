#!/bin/bash
# This is a bash script to generate the slurm
echo "Please input the number of copies you want to submit"
read N_copies

for ((i=0;i<N_copies;i++)); do
    echo "#!/bin/bash" >> job$i.slurm
    echo "#SBATCH -A cs5014" >> job$i.slurm
    echo "#SBATCH -p development" >> job$i.slurm
    echo "module load anaconda3" >> job$i.slurm
    echo "python caculate_dis.py >> totaldistance.txt" >>job$i.slurm
    sbatch job$i.slurm
    sleep 1

done 
