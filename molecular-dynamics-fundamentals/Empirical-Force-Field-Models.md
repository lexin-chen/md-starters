# 4. Empirical Force Field Models: Molecular Mechanics (Leach)
Outline adapted from Chapter 4 of Molecular Modelling by Andrew Leach

## 4.1. Introduction

- QM deals with electrons in a system
    - there are some semi-empirical schemes.
- Force field methods is known as **molecular mechanics**
    - ignore electronic motions
    - calculate the energy of a system as a function of the nuclear position only.
    - used to perform calculations on the systems containing significant numbers of atoms.
- Why molecular mechanics work?
    - Born-Oppenheimer approximation — energy as a function of the nuclear coordinates
- Molecular mechanics is based on the simple model of interactions within a system with angles and the rotations about single bonds.
- Transferability is a key attribute of force field, enables a set of parameters developed and tested on small number of cases to be applied to wider range of problems.

### 4.1.1. A Simple Molecular Mechanics Force Field

<aside>
💡 Force field contains terms to describe the 4 component picture of intra- and inter- molecular forces within the system.

</aside>

- Energetic penalties are associated with deviations of bonds and angles away from their ‘equilibrium’ values.
- There is a potential energy function that explains how the energy changes as bonds are rotated
- Force field contains terms that describe the interaction between non-bonded parts of the system.

$$
U(r^N) = \sum_{bonds}\frac{k_i}{2}(l_i-l_{i,0})^2+\sum_{angles}\frac{k_i}{2}(\theta_i-\theta_{i,0})^2+\sum_{torsions}\frac{V_n}{2}(1+\cos(n\omega-\gamma))+\sum_{i=1}^N\sum_{j=1}^N\left(4\varepsilon_{ij}\left[\left(\frac{\sigma_{ij}}{r_{ij}}^{12}\right)-\left(\frac{\sigma_{ij}}{r_{ij}}^{6}\right)\right]+\frac{q_iq_j}{4\pi\varepsilon_0r_{ij}}\right) \tag{4.1}
$$

- Potential Energy function — function of the positions )r_ of N particles
- First term — bonded interactions; modelled by harmonic potential; increase in energy as bond length deviates from reference value.
- second term — bonded interactions; modelled by harmonic potential; increase in energy as bond angle deviates from reference value.
- third term — bonded interactions; modelled by torsional potential; increase in energy as bond rotates from reference value.
- forth term — nonbonded interactions; modelled using Coulomb potential term for electrostatic interactions and Lennard-Jones potential for van der Waals.
- 4 key contribution to molecular mechanics force field
    - Bond stretching
    - Angle bending
    - Torsional terms
    - Non-bonded interactions

## 4.2. Some General Features of Molecular Mechanics Force Fields

- Need to define the constants
- Some parts of the force field can be considered standalone (bond and angle terms)
- But force field is considered one entity and not divide it into its individual component, interdependent.
- Transferability — same set of parameters can be used to model a series of related molecules. (for example, n-alkanes.)
    - Transferability of the functional form and parameters is an important feature of force field
- Only develop FF for small molecule system if particular accuracy is required.
- Force field is empirical — no ‘*correct*’ form for a force field
- Important to remember, there is always better force fields.
- Often a compromise between accuracy and computational efficiency.
    - most accurate function form may often be unsatisfactory for efficient computation.
    - As computational power increase, can incorporate more sophisticated model.
- Atom type — key concept in force fields.
    - In QM calculations, necessary to specify: atomic numbers of nuclei present; geometry of system; overall charge; spin multiplicity
    - In force field, necessary to specify: info about hybridization state; local environment.
        - for example, reference angle for tetrahedral C is 109.5$\degree$.
        - trigonal planar is 120$\degree$.

## 4.3. Bond Stretching

- The true bond stretching is not really harmonic but more like Morse potential
    - but it is not useful in molecular mechanics force fields because it is not amenable to efficient computations and it requires 3 parameters.
    - Not a problem because the effects seen in Morse potential to harmonic is very small.
- Force between bonded atoms are very strong
- Consider energy is required for bond to deviate significantly from its equilibrium value.
- High order is needed to model Morse curve. So harmonic is good enough.

## 4.4. Angle Bending

- harmonic potential
- less energy to bend angle than to stretch bonds

## 4.5. Torsional Terms

- bond-stretching and angle bending are the hard degrees of freedom and a substantial amount of energy is needed to deform them.

## 4.8. Introduction to Non-bonded Interactions

- Two groups: electrostatic interactions and van der waals.

## 4.9. Electrostatic Interactions

- *Partial charges* — charges restricted to nuclear centers
- electrostatic interaction between two groups are calculated as sum of interactions between pairs of point charges using Coulomb’s law.

$$
V=\sum_{i=1}^{N_A}\sum_{j=1}^{N_B}\frac{q_iq_j}{4\pi\varepsilon_0r_{ij}} \tag{4.19}
$$

- N(A) and N(B) are numbers of point charges in the two molecules
- Central multiple expansion — calculate electrostatic intermolecular interaction by treating a molecule as single entity
    - based upon electric moments or multipoles

### 4.9.5. Deriving Charge Models for Large Systems

- Impractical to perform QM calculations on a molecule with so many atoms, so it must be broken into fragments of a suitable size.
    - For example, to obtain partial atomic charges for amino acids, calculation on ’dipeptide’ fragments, which is more akin to the environment within a protein than in an isolated amino acid.
- Charge sets obtained from electrostatic potential fitting is dependent upon the basis set used to drive the wavefunction.
    - Charges don’t always improve if a larger basis set is used.
    - 5-31G* basis set is generally considered to give reasonable results for calculation relevant to the condensed phases.
    - Sometimes, can scale down to lower basis set or lower level of theory (semi-empirical)to get comparable results.
- A complicating factor is that the charges obtained from electrostatic potential fitting can depend on the conformation being inputted in the QM calculation.
    - To get around, get each charge weighted based on Boltzmann distribution.
    - Charges can vary continuously with the conformation.

### 4.9.6. Rapid Methods for Calculating Atomic Charges

- Gasteiger-Marsili approach uses the concept of partial equalisation of *orbital electronegativity.*
- Electronegativity is the power of an atom to attract electron
- Mulliken define electronegativity is the average of ionization potential $I_A$ and its electron affinity $E_A$.

$$
\chi_A = \frac{1}{2}(I_A+E_A)
$$

- Rappe and Goddard’s method of charge equilibration meth
    - employed in ‘Universal Force Field’ — calculating charge distributions over a wide range of molecules.
    - charge are dependent upon the molecular geometry
    - uses a series expansion of energy of an isolated atom in terms of the charge.

### 4.9.10. Polarization

- So far, mainly the focus is on ‘permanent’ features of charge distribution.
- Polarization- electrostatic interactions arises from changes in charge distribution of a molecule or atom caused by external field.
    - Effect of the external electric field is to induce dipole in the molecule.
    
$$
\mu_{ind}= \alpha E
$$   

   - mu is induced dipole moment proportional to the electric field, with the constant of proportionality being the polarizability alpha
- For isolated atoms, polarizability is isotropic
    - does not depend on orientation
- Interaction between dipole and induced dipole is independent of disorienting effect of thermal motions
- Important note is that dipole induced on a molecule (A) will affect the charge distribution of another molecule.

## 4.10 Van der waals interaction

- Electrostatics cannot account for all the non-bonded interactions in a system.
- Energy increases as the separation decreases further.

### 4.10.1 Dispersive Interactions

- An instantaneous dipole in a molecule can in turn induce a dipole in neighboring atoms, giving rise to an attractive effect.
- 

### 4.10.2. The Repulsive Contribution

### 4.10.3. Modelling Van der Waals Interactions

- Lennard-Jones 12-6 function

$$
\nu(r)=4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^{6}\right] \tag{4.63}
$$

Interactions between two atoms.

Has two adjustable parameters: collision diameter, sigma and well depth, epsilon. 

### 4.10.4. Van der Waals Interactions in Polyatomic Systems

- Interaction energy depend not only upon their separation but also their relative orientation and conformations.
- To calculate LJ interaction energy between two C-O molecules using two-site model would require van der waal parameters for carbon-carbon interactions and O-O interaction but also C-O interactions
- System containing N different types of atoms would require
- The charge-charge contribution to the potential energy is due to all pairs of charges in the central simulation box can be written:
