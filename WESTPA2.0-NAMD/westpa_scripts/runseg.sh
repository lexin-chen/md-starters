#!/bin/bash

if [ -n "$SEG_DEBUG" ] ; then
  set -x
  env | sort
fi

cd $WEST_SIM_ROOT
mkdir -pv $WEST_CURRENT_SEG_DATA_REF
cd $WEST_CURRENT_SEG_DATA_REF

ln -sv $WEST_SIM_ROOT/common_files/step5_input.psf .
ln -sv $WEST_SIM_ROOT/common_files/step5_input.pdb .
ln -sv $WEST_SIM_ROOT/common_files/toppar .

sed "s/RAND/$WEST_RAND16/g" $WEST_SIM_ROOT/common_files/md.in > md.in
ln -sv $WEST_PARENT_DATA_REF/seg.coor ./parent.coor
ln -sv $WEST_PARENT_DATA_REF/seg.dcd  ./parent.dcd
ln -sv $WEST_PARENT_DATA_REF/seg.vel  ./parent.vel
ln -sv $WEST_PARENT_DATA_REF/seg.xsc  ./parent.xsc

#run namd simulation
ml cuda/10.0.130  gcc/7.3.0 amber/20 namd/3.0
export CUDA_DEVICES=(`echo $CUDA_VISIBLE_DEVICES_ALLOCATED | tr , ' '`)    #takes all the SLURM allocated CUDA devices and puts them into an temporary array CUDA_DEVICES
export CUDA_VISIBLE_DEVICES=${CUDA_DEVICES[$WM_PROCESS_INDEX]}             #expose the GPU device for the NAMD execution line the follows. The exposed GPU device is tagged to the $WM_PROCESS_INDEX. The  $WM_PROCESS_INDEX is correlated to the --n-workers that was requested

echo "RUNSEG.SH: CUDA_VISIBLE_DEVICES_ALLOCATED = " $CUDA_VISIBLE_DEVICES_ALLOCATED
echo "RUNSEG.SH: WM_PROCESS_INDEX = " $WM_PROCESS_INDEX
echo "RUNSEG.SH: CUDA_VISIBLE_DEVICES = " $CUDA_VISIBLE_DEVICES
/apps/cuda/11.0.207/base/namd/3.0/NAMD_3.0alpha7_Linux-x86_64-multicore-CUDA/namd3 md.in > seg.log

#analysis from cpptraj
cpptraj -i /orange/colina/le.chen/opioid_receptor/westpa_tutorials-main/test2/try3/westpa_scripts/cpptraj.in
cat pcoord.dat | tail -n +2 | awk '{print $2}' >> $WEST_PCOORD_RETURN

#cpptraj -p *.psf -y *.dcd -ya 'lastframe' -x seg.pdb

# Clean up
rm -f $TEMP md.in \
  seg.restart.coor seg.restart.coor.old seg.restart.vel seg.restart.vel.old\
  seg.restart.xsc seg.restart.xsc.old step5_input.psf step5_input.pdb FFTW_NAMD_3.0alpha7_Linux-x86_64-multicore-CUDA.txt\
  parent.dcd
rm -r toppar
