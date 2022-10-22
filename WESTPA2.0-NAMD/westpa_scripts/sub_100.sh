#!/bin/bash
#SBATCH --account=colina
#SBATCH --qos=colina
#SBATCH --job-name=w_analysis
#SBATCH --output=job.out
#SBATCH --error=job.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --distribution=block:block
#SBATCH --time=7-00:00:00
#SBATCH --mem-per-cpu=25gb
#SBATCH --partition=gpu
#SBATCH --gres=gpu:a100:1

##SBATCH --mail-type=none
#SBATCH --mail-user=some_user@some_domain.com
ml conda
conda activate westpa-2022.02
cd $SLURM_SUBMIT_DIR/..
#python westpa_scripts/analysis.py
#plothist evolution pdist.h5 0 -o hist.pdf
python westpa_scripts/python.py

