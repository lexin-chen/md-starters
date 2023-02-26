# Molecular dynamics simulations in biology

### Intro

- Why molecular dynamics?
    - biology is slower to embrace theoretical approaches because of the assumptions and methods that are applicable to large and complex system.
    - It led to the availability of supercomputers and their widespread available.
        - Not only molecular motions, but also refinement of NMR and X-ray data.
        - important for understanding motion, since it is very difficult in experimental work.

### What is molecular dynamics?

- science of simulating the the motions of a system of particles
    - can be applied to small atoms to diatomic molecules going through chemical reaction to galaxy large.
- knowledge of the interaction potential for the particles —> forces can be calculated
    - forces vary from simple gravitational to complex many body foces
    - many classical newtonian equations are adequate for many systems
- two attributes of MD that play a role in its wide applications and functions
    - provide individual particle motions as a function of time
        - so they can probe easier than experiments
    - computer alchemy changing the potential from representing one system to another —> power tool to calculate free energy differences

### Potential energy function

- begin with knowledge of the energy of the system as a function of atomic coordinates
- relative stability of the different possible stable or metastable structures.
- the forces acting on the atoms (first derivative of the potential) in respect to atom position can calculate dynamic behavior of the system by solving Newton equations of motions for the atoms as a function of time.
- only empirical energy functions provide potential surfaces for protein and large systems
- non bonded atoms make large contribution to potential energy of the folded or native structure.

- Simulation methods
    - many approaches to dynamics
        - Newton's equations of motion to solve for atoms of the system and any surrounding solvent.
    - To begin, dynamic simulation, initial set of atomic coordinates and velocities is required.
        -  `pdb` file

### Limitations and prospects

- The two limitations are
    - approx of the potential energy function
        - systematic errors
    - lengths of the simulation
        - statistical errors
- Current parameterization have shifted from  ab initio in isolated molecules to parametrization with emphasis on solution and crystal data.
