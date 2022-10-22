#!/bin/bash
#export WEST_SIM_ROOT="$PWD"
if [ -n "$SEG_DEBUG" ] ; then
  set -x
  env | sort
fi

cd $WEST_SIM_ROOT

DIST=$(mktemp)

COMMAND="           parm common_files/step5_input.psf \n"
COMMAND="${COMMAND} trajin bstates/seg.pdb \n"
COMMAND="${COMMAND} reference common_files/step5_input.pdb \n"
COMMAND="${COMMAND} rmsd ca-rmsd :MOR&!@H= reference out $DIST mass\n"
COMMAND="${COMMAND} go"

echo -e "${COMMAND}" | $CPPTRAJ

cat $DIST | tail -n +2 | awk '{print $2}' > $WEST_PCOORD_RETURN

#rm $DIST

if [ -n "$SEG_DEBUG" ] ; then
  head -v $WEST_PCOORD_RETURN
fi
