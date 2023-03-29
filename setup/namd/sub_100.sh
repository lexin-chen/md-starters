#!/bin/bash
#SBATCH --account=colina
#SBATCH --qos=colina
#SBATCH --job-name=w_mor
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

ml cuda/10.0.130 namd/3.0
cd $SLURM_SUBMIT_DIR

/apps/cuda/11.0.207/base/namd/3.0/NAMD_3.0alpha7_Linux-x86_64-multicore-CUDA/namd3 step7_production4.inp>step7_production4.log
/apps/cuda/11.0.207/base/namd/3.0/NAMD_3.0alpha7_Linux-x86_64-multicore-CUDA/namd3 step7_production5.inp>step7_production5.log

#for f in *.inp;do
#        b="$(basename $f .inp)"
#        echo Processing conf file $b
#	/apps/cuda/11.0.207/base/namd/3.0/NAMD_3.0alpha7_Linux-x86_64-multicore-CUDA/namd3 $f>${b}.log
#done

