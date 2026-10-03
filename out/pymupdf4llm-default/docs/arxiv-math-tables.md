**Rare-earth** **chalcogenide** **perovskites:** **A** **promising** **class** **of** **materials** **for** **optoelectronic**

**applications**


Surajit Adhikari <sup>1,</sup> <sup>_∗_</sup> and Priya Johari <sup>1,</sup> <sup>_†_</sup>

1 _Department_ _of_ _Physics,_ _School_ _of_ _Natural_ _Sciences,_
_Shiv_ _Nadar_ _Institution_ _of_ _Eminence,_ _Greater_ _Noida,_
_Gautam_ _Buddha_ _Nagar,_ _Uttar_ _Pradesh_ _201314,_ _India_


Chalcogenide perovskites have attracted significant attention for optoelectronic applications due
to their nontoxic composition, robust phase stability, and excellent optoelectronic properties. Among
them, rare-earth chalcogenide perovskites have recently emerged as promising candidates for nextgeneration devices. However, their excitonic and polaronic properties remain largely unexplored
due to the high computational cost of accurate theoretical treatments. In this work, we present
a comprehensive first-principles investigation of excitonic dynamics and polaronic effects in a series of III-III rare-earth chalcogenide perovskites ABX3 (A = Y, La; B = Sc, Y; X = S, Se), along
with their structural stability and optoelectronic properties, using state-of-the-art density functional
theory in conjunction with many-body perturbation theory within the G0W0 and Bethe-Salpeter
equation (BSE) frameworks. All investigated compounds satisfy the dynamical and mechanical stability criteria, although several are thermodynamically metastable at 0 K and may require kinetic
stabilization and/or finite-temperature effects for experimental realization. They exhibit quasiparticle band gaps in the range of 2.75 _−_ 4.47 eV, and the BSE calculations reveal strong optical
absorption spanning the visible to ultraviolet regions. The computed excitonic properties indicate intermediate-to-large exciton binding energies (0.148 _−_ 0.517 eV), moderately localized excitons, and strong electron-hole wavefunction overlap, indicative of favorable radiative recombination
characteristics and enhanced light-matter interaction. Furthermore, analysis based on the Fröhlich
model demonstrates intermediate-to-strong carrier-phonon coupling, with electron-phonon interactions generally stronger than hole-phonon interactions. Notably, charge-separated polaronic states
are energetically less favorable than bound excitonic states in most compounds, with the exception
of La(Sc, Y)Se3, while hole polarons exhibit significantly higher mobilities (up to _∼_ 40 cm <sup>2</sup> V <sup>_−_</sup> <sup>1</sup> s <sup>_−_</sup> <sup>1</sup> )
compared to electron polarons. Overall, rare-earth chalcogenide perovskites ABX3 exhibit a compelling combination of structural stability, tunable optoelectronic properties, pronounced excitonic
effects, and favorable polaronic transport, positioning them as promising lead-free materials for
next-generation optoelectronic devices, including light-emitting devices and photodetectors.



**I.** **INTRODUCTION:**


Over the last decade, inorganic-organic halide perovskites (IOHPs) have attracted extraordinary interest
owing to their outstanding electronic and optical characteristics [1–4]. This intense research focus has led to
remarkable progress in perovskite solar cells, with the
power conversion efficiency (PCE) rising rapidly from
an initial value of 3.8% to a record 27% [1, 5]. However, despite these impressive achievements, significant
challenges remain. Most high-performance IOHPs are
lead (Pb)-based, giving rise to serious toxicity concerns.
Moreover, their practical applicability is hindered by
poor long-term stability, including degradation and thermal and chemical instability associated with the organic
constituents [6, 7]. These limitations have motivated extensive efforts toward the development of environmentally benign, stable perovskite alternatives, opening new
pathways for next-generation optoelectronic materials.

Recently, chalcogenide perovskites have emerged as a
novel class of functional materials. Owing to their high


_∗_ [sa731@snu.edu.in](mailto:sa731@snu.edu.in)

_†_ [priya.johari@snu.edu.in](mailto:priya.johari@snu.edu.in)



structural stability, suitable band gaps, and excellent optoelectronic properties, several members of this family
have been identified as promising candidates for lightabsorbing and light-emitting applications [8–12]. Among
them, the II-IV chalcogenide perovskites with the general formula ABX3 (where A = Ca, Sr, Ba; B = Ti, Zr,
Sn, Hf; and X = S, Se) are the most extensively studied to date [10, 11, 13–17]. Further diversification of this
materials family can be achieved by exploring alternative elemental combinations at the cationic sites. In this
context, the III-III chalcogenide perovskites, although
already synthesized, remain largely unexplored as functional materials [18–21]. For optoelectronic applications,
access to a broader materials palette is highly advantageous, as it enables precise tuning of critical parameters
such as band gaps, band alignments, and structural properties, including lattice constants required for epitaxial
growth. Consequently, the exploration of III-III chalcogenide perovskites composed of environmentally benign,
non-toxic elements is highly desirable, as these materials
can effectively complement the existing family of II-IV
chalcogenide perovskites.


Recent studies on III-III chalcogenide perovskites have
unveiled promising opportunities for the design of stable and environmentally benign optoelectronic materials. For instance, Zhang _et_ _al._ theoretically predicted


the orthorhombic _Pnma_ (No. 62) crystal structure of
YScS3, reporting an indirect G0W0 band gap of 3.16
eV [22]. Subsequently, through density functional theory calculations, Zhang _et_ _al._ not only predicted but
also experimentally synthesized a light-emitting III-IIIS3 perovskite, LaScS3, exhibiting a direct band gap of
2.62 eV [18]. Furthermore, they also reported the prediction and experimental realization of the direct band
gap material LaScSe3, with a G0W0 band gap of 2.96
eV [19]. In addition, the _P_ 21 _/m_ crystal structure of the
LaYS3 perovskite has been both theoretically predicted
and experimentally synthesized, exhibiting an optimal
band gap of 2.0 eV, making it a promising wide band
gap photoabsorber for tandem solar energy conversion
devices [20, 21].


Most of the aforementioned studies have primarily focused on the electronic and optical properties of III-III
rare-earth chalcogenide perovskites. In contrast, their
excitonic and polaronic properties remain largely unexplored, despite their critical role in determining the performance of optoelectronic devices. Excitonic effects govern fundamental processes such as light absorption, emission, and charge separation. In contrast, polaron formation, arising from carrier-phonon interactions, strongly
influences charge transport and carrier mobility [15–17].
A quantitative description of these properties, however,
is computationally demanding and has therefore received
limited attention. This gap highlights the need for a comprehensive investigation of excitonic and polaronic effects
in these compounds, which has not yet been achieved and
is addressed in the present work.


In this work, we undertake a systematic and comprehensive investigation of the structural stability, as well as
the electronic, optical, excitonic, and polaronic properties of III-III rare-earth chalcogenide perovskites ABX3
(A = Y, La; B = Sc, Y; X = S, Se) in the orthorhombic _Pnma_ phase, a widely observed and energetically
competitive distorted perovskite structure that provides
a consistent framework for comparative analysis. Our
study is based on first-principles calculations within the
frameworks of density functional theory (DFT) [23, 24],
density functional perturbation theory (DFPT) [25], and
many-body perturbation theory (MBPT) [26, 27]. Initially, the crystal structures are optimized using the
semilocal PBE [28] as well as PBEsol [29] exchangecorrelation (xc) functionals, and all compounds are found
to be both dynamically and mechanically stable. However, several are thermodynamically metastable at 0 K,
suggesting that their experimental realization may require kinetic stabilization and/or finite-temperature effects. Subsequently, the electronic properties are investigated using both the HSE06 hybrid xc functional [30]
and the G0W0@PBE approach [31, 32], revealing quasiparticle band gaps in the range of 2.75 _−_ 4.47 eV. Following that, the optical response is computed by solving the Bethe-Salpeter equation (BSE) [33, 34] on top
of G0W0@PBE, enabling the evaluation of the dielectric function and exciton binding energies. The results



2


indicate that these perovskites exhibit intermediate-tohigh exciton binding energies, moderately localized excitons, and strong electron-hole wavefunction overlap, suggesting favorable radiative transitions and pronounced
light-matter interaction. Finally, we investigate the effects of carrier-phonon coupling and estimate the polaron mobility using the Fröhlich model [35] and the Hellwarth polaron model [36]. The analysis reveals intermediate to strong carrier-phonon coupling, with electronphonon interactions being more pronounced than those
of holes, resulting in lower electron mobility and comparatively higher hole mobility. Overall, this work provides a comprehensive understanding of rare-earth ABX3
(A = Y, La; B = Sc, Y; X = S, Se) chalcogenide perovskite compounds, highlighting their potential as leadfree perovskites with promising optoelectronic properties
for next-generation devices.


**II.** **COMPUTATIONAL** **DETAILS:**


In this work, first-principles calculations were carried out within the framework of density functional theory (DFT) [23, 24], density functional perturbation theory (DFPT) [25], and many-body perturbation theory
(MBPT) [26, 27], as implemented in the Vienna ab initio
Simulation Package (VASP) [37, 38]. The interaction between valence electrons and ionic cores was described using projector augmented-wave (PAW) pseudopotentials

[39]. Structural optimizations were carried out within
the generalized gradient approximation (GGA) using the
Perdew-Burke-Ernzerhof (PBE) [28] and the PBEsol [29]
exchange-correlation (xc) functionals. The inclusion of
PBEsol is motivated by its improved accuracy in describing equilibrium properties of solids, particularly lattice constants and structural distortions, which are crucial for reliably assessing dynamical stability and phonon
properties. A plane-wave cutoff energy of 400 eV was
employed, and the electronic self-consistent field convergence criterion was set to 10 <sup>_−_</sup> <sup>6</sup> eV. All structures were
fully optimized until the Hellmann-Feynman forces on
each atom were less than 0.01 eV/Å. Brillouin zone integrations were carried out using a Γ-centered 7 _×_ 7 _×_ 5
k-point mesh. The optimized crystal structures were visualized using the VESTA package [40]. Phonon dispersion curves were calculated using DFPT as implemented
in the PHONOPY package [41], employing 2 _×_ 2 _×_ 2
supercells. To assess the functional dependence of the
dynamical stability, the phonon spectra were computed
for crystal structures relaxed using both the PBE and
PBEsol exchange-correlation functionals.

Electronic band structures were initially obtained using the PBE xc functional including spin-orbit coupling
(SOC), which was found to have a negligible impact
on the overall band dispersion. To achieve improved
accuracy in bandgap estimation, hybrid xc functional
calculations using HSE06 [30] and quasiparticle corrections within the G0W0@PBE [31, 32] approach were per

formed. A Γ-centered 3 _×_ 3 _×_ 2 k-point mesh was employed for the G0W0 calculations. This choice is justified by the demonstrated convergence of the quasiparticle band gaps, while the use of denser k-point meshes
for the present 20-atom unit cells would incur a substantially higher computational cost and is therefore beyond the scope of the present work (for details, see Sec.
X of the SM [42]). The convergence of the quasiparticle bandgap with respect to the number of unoccupied bands (NBANDS), the plane-wave cutoff energy
(ENCUT), and the response-function cutoff energy (ENCUTGW) was carefully examined (for details, see Sec.
X of the SM [42]). Based on these convergence tests,
640 bands, a plane-wave cutoff energy of 400 eV, and a
response-function cutoff energy of 300 eV were adopted,
yielding quasiparticle bandgaps converged to within 0.05
eV. Carrier effective masses were calculated using the
SUMO code [43] via parabolic fitting near the band extrema. Optical properties were further refined by solving the Bethe-Salpeter equation (BSE) [33, 34] on top of
G0W0@PBE, explicitly including electron-hole interactions. The BSE kernel was constructed using 24 occupied
and 24 unoccupied bands, based on convergence tests (for
details, see Sec. XI of the SM [42]). Elastic and optical properties were post-processed using the VASPKIT
package [44], and the ionic contribution to the dielectric
constant was obtained from DFPT calculations.


**III.** **RESULTS** **AND** **DISCUSSIONS:**


In the present study, we conduct a comprehensive investigation of the optoelectronic properties of III-III rareearth chalcogenide perovskites ABX3 (A = Y, La; B =
Sc, Y; X = S, Se). The following sections provide an
in-depth analysis of their structural stability, electronic
structure, and transport characteristics, along with their
optical response, excitonic behavior, and polaronic effects. These results aim to establish a fundamental understanding of these materials and offer valuable insights
to guide future experimental studies.


FIG. 1. Crystal structures of rare-earth chalcogenide perovskites (a) YScX3, (b) LaScX3, and (c) LaYX3, respectively,
where X = S, Se.



3


**A.** **Structural** **Properties:**


Figure 1 illustrates the orthorhombic crystal structures
of rare-earth chalcogenide perovskites ABX3 (A = Y, La;
B = Sc, Y; and X = S, Se), crystallizing in the _Pnma_
space group (No. 62). Owing to the +3 valency of both
A- and B-site cations, these materials are categorized
as III-III chalcogenide perovskites. The unit cell contains four formula units (20 atoms), comprising 4 A-site
cations (Y or La), 4 B-site cations (Sc or Y), and 12
chalcogen anion atoms (S or Se). In this structure, the Asite cations exhibit 12-fold coordination, forming cuboctahedral environments with the surrounding chalcogen
atoms. In contrast, the B-site cations are 6-fold coordinated, giving rise to corner-sharing distorted [BX6] <sup>9</sup> <sup>_−_</sup>

octahedra. These octahedra are both tilted and distorted, leading to the characteristic orthorhombic symmetry of the _Pnma_ phase [12]. In this study, we report
for the first time the _Pnma_ phase of YScSe3, LaYS3,
and LaYSe3 compounds. The lattice parameters of the
optimized structures are calculated using both PBE and
PBEsol xc functionals and are summarized in Table I.
It is found that the lattice parameters of LaScSe3 are
in good agreement with the available experimental results (a = 6.77 Å, b = 7.53 Å, and c = 10.00 Å [19]).
Moreover, the PBE functional slightly overestimates the
lattice parameters, while PBEsol slightly underestimates
them, with both deviations being of comparable magnitude. This indicates that both functionals yield similar
accuracy, despite exhibiting opposite systematic deviations. In addition, the octahedral distortion parameters,
including the average bond length, polyhedral volume,
bond angle variance, and bond-length distortion index,
for the BX6 octahedra in these chalcogenide perovskites
are computed using both functionals and presented in
Table S1 (for details, see Sec. I of the SM [42]).

To assess the thermodynamic stability against decomposition, we calculated the decomposition enthalpy according to


ABX3 _→_ 1 _/_ 2 A2X3 + 1 _/_ 2 B2X3 (1)


for these III-III-X3 compounds that pass the phase stability criteria (for details, see Sec. II of the SM [42]).
The decomposition enthalpy (∆HD) of these compounds
is evaluated using both PBE and PBEsol xc functionals
and is tabulated in Table I. The LaScX3 (X = S, Se)
compounds exhibit positive ∆HD values with both functionals, indicating thermodynamic stability with respect
to the considered decomposition pathway. In contrast,
the remaining compounds exhibit negative ∆HD values,
indicating thermodynamic metastability at 0 K with respect to this decomposition pathway. The only exception is YScS3, which yields a positive ∆HD when using the PBEsol functional. Nevertheless, decomposition
enthalpy based on a single reaction does not constitute
a complete thermodynamic stability criterion, since alternative competing phases and decomposition pathways


4


TABLE I. Calculated lattice parameters and decomposition energies (∆HD) of ABX3 (A = Y, La; B = Sc, Y; and X = S, Se)
rare-earth chalcogenide perovskites using the PBE and PBEsol xc functional, respectively (PBEsol values in bold).


<u>Lattice</u> <u>parameters</u> <u>(Å)</u> ∆HD
Configurations
<u>a</u> <u>b</u> <u>c</u> <u>(meV/atom)</u>
YScS3 6.39 ( **6.27** ) 7.02 ( **6.97** ) 9.55 ( **9.37** ) -9.1 ( **5.0** )
YScSe3 6.67 ( **6.54** ) 7.35 ( **7.29** ) 10.00 ( **9.79** ) -28.9 ( **-6.8** )
LaScS3 6.59 ( **6.46** ) 7.21 ( **7.16** ) 9.65 ( **9.51** ) 26.0 ( **26.1** )
LaScSe3 6.83 ( **6.68** ) 7.58 ( **7.51** ) 10.08 ( **9.92** ) 13.5 ( **8.8** )
LaYS3 6.81 ( **6.70** ) 7.42 ( **7.37** ) 10.06 ( **9.88** ) -2.7 ( **-19.9** )
<u>LaYSe3</u> <u>7.04</u> <u>(</u> **<u>6.90</u>** <u>)</u> <u>7.78</u> <u>(</u> **<u>7.72</u>** <u>)</u> <u>10.48</u> <u>(</u> **<u>10.26</u>** <u>)</u> <u>-15.2</u> <u>(</u> **<u>-25</u>** <u>)</u>



may exist. A rigorous assessment therefore requires construction of the convex-hull phase diagram, which compares the energy of a compound against all known competing phases within the corresponding chemical space.
Compounds lying on the convex hull are thermodynamically stable, whereas those with positive energy above the
hull (Ehull) are metastable with respect to decomposition
into a combination of lower-energy phases.


To directly address this limitation, we constructed the
convex-hull phase diagrams for each A _−_ B _−_ X (A = Y,
La; B = Sc, Y; and X = S, Se) chemical space by incorporating all relevant competing binary and ternary
phases at the same DFT level. The calculated Ehull values are summarized in Table S3, while the corresponding
convex-hull diagrams are presented in Figure S1 (for details, see Sec. III of the SM [42]). The results show that
LaScX3 (X = S, Se) lie on the convex hull with Ehull =
0, confirming their thermodynamic stability at 0 K. The
remaining compounds possess finite positive Ehull values
(0.009 _−_ 0.029 eV), indicating metastability with respect
to competing equilibrium phases. It is important to note,
however, that a positive energy above the hull does not
necessarily preclude experimental realization. Numerous
experimentally synthesized materials are known to exist
as metastable phases because finite-temperature vibrational and configurational entropy, kinetic barriers, and
non-equilibrium synthesis routes can effectively stabilize
compounds that are slightly above the convex hull [45].
Consequently, the above-hull compounds identified here
should be regarded as metastable candidates that may
still be experimentally accessible under suitable synthesis conditions rather than as equilibrium-stable phases.
However, thermodynamic stability alone is insufficient to
ensure stability of these materials; therefore, dynamical
and mechanical stability are also examined.


The dynamical stability of the investigated perovskites
serves as a crucial indicator of their structural integrity
and suitability for functional applications. It is evaluated
through phonon dispersion relations, which describe the
vibrational behavior of atoms in the crystal lattice. For
a dynamically stable system at 0 K, all phonon frequencies are required to be real and positive across the entire
Brillouin zone; the occurrence of imaginary (negative)
frequencies signifies possible structural instabilities. To
assess this, self-consistent phonon calculations are performed within the DFPT framework using the structures



relaxed with both PBE and PBEsol xc functionals. The
computed phonon dispersion curves of ABX3 (A = Y,
La; B = Sc, Y; and X = S, Se), obtained using structures relaxed with the PBE and PBEsol xc functionals,
are presented in Figs. S2 and 2, respectively. Within
the PBE functional, YScS3, LaScS3, LaYS3, and LaYSe3
are dynamically stable at 0 K, as confirmed by the absence of imaginary phonon modes, whereas (Y, La)ScSe3
shows dynamical instabilities, as indicated by the presence of imaginary modes. Specifically, YScSe3 shows a
maximum imaginary frequency of -0.333 THz at the Γ
point, while LaScSe3 exhibits imaginary frequencies of
approximately -0.189 THz along the Γ _−_ X direction and
-0.349 THz at the U point. The relatively small magnitudes of these imaginary frequencies suggest the presence
of soft lattice instabilities rather than pronounced structural instabilities. This interpretation is further supported by the experimental realization of LaScSe3, indicating that these weak instabilities are unlikely to preclude its synthesis and may instead reflect the sensitivity
of the lattice dynamics to the equilibrium structural parameters [19]. In contrast, phonon calculations based on
the PBEsol-relaxed structures show no imaginary phonon
modes throughout the Brillouin zone for any of the investigated compounds, indicating dynamical stability within
the PBEsol framework. Together with the PBE results,
these findings suggest that the lattice dynamics of some
compounds are sensitive to small variations in the equilibrium lattice parameters and are therefore dependent
on the choice of exchange-correlation functional.


Beyond the thermodynamic and dynamical stability
discussed above, the mechanical stability and corresponding elastic properties of ABX3 (A = Y, La; B = Sc,
Y; X = S, Se) chalcogenide perovskites are further examined. It is well known that the suitability of a material
for practical device applications is strongly influenced by
its elastic behavior. The second-order elastic constants
( _Cij_ ) are calculated using the energy-strain method [46],
from which the relevant elastic properties are derived (for
details, see Sec. V of the SM [42]). Owing to the orthorhombic symmetry of all considered compounds, nine
independent elastic constants ( _C_ 11, _C_ 22, _C_ 33, _C_ 44, _C_ 55,
_C_ 66, _C_ 12, _C_ 13, and _C_ 23) are sufficient to describe their
mechanical stability and elastic behavior. The calculated
_Cij_ values, listed in Table S4, satisfy the Born stability
criteria [46], thereby confirming the excellent mechanical


stability of these orthorhombic chalcogenide perovskites.

Further, the bulk modulus ( _B_ ), shear modulus ( _G_ ),
Young’s modulus ( _Y_ ), and Poisson’s ratio ( _ν_ ) are evaluated within the Voigt-Reuss-Hill approximation [47, 48]
and are summarized in Table S4. The relatively larger
values of _B_ compared to _G_ indicate that the investigated
chalcogenide perovskites exhibit greater resistance to volume change than to shear deformation. The comparatively lower values of _G_ and _Y_ further suggest that these
materials possess a certain degree of mechanical flexibility. To assess the ductile or brittle nature of these
systems, we employ Pugh’s criterion based on the _B/G_
ratio [49], along with Poisson’s ratio ( _ν_ ). The obtained
values of _B/G >_ 1 _._ 75 and _ν_ _>_ 0 _._ 26 consistently indicate
that all the compounds exhibit ductile behavior. These
characteristics suggest that the investigated materials are
mechanically robust yet sufficiently flexible for potential
device applications.

Overall, the synthesizability of these III-III chalcogenide perovskites is established by the combined assessment of thermodynamic, dynamical, and mechanical
stability. Notably, LaScX3 (X = S, Se), which has already been experimentally synthesized [18, 19], is found
to be thermodynamically stable, consistent with its positive decomposition enthalpy. In contrast, the remaining compounds are metastable with respect to decomposition. Nevertheless, the absence of imaginary phonon
modes (within PBEsol) and the satisfaction of mechanical stability criteria confirm their dynamical and mechanical stability. These results suggest that, despite thermodynamic metastability, the compounds are likely experimentally accessible through kinetic stabilization or finitetemperature effects, with LaScX3 serving as a benchmark
system validating the reliability of the present approach.


FIG. 2. Phonon dispersion curves of the rare-earth chalcogenide perovskites (a) YScS3, (b) YScSe3, (c) LaScS3, (d)
LaScSe3, (e) LaYS3, and (f) LaYSe3, computed using the
DFPT method based on PBEsol-relaxed structures.


**B.** **Electronic** **properties:**


Following the assessment of structural stability, the
electronic properties, such as the band structure and par


5


tial density of states (PDOS) of rare-earth chalcogenide
perovskites ABX3 (A = Y, La; B = Sc, Y; and X =
S, Se) are evaluated to gain fundamental insight into
their suitability for optoelectronic applications. At first,
the electronic band structures of these chalcogenide perovskites are calculated using the semilocal GGA-PBE xc
functional, both with and without inclusion of spin-orbit
coupling (SOC). The GGA-PBE xc functional is found to
underestimate the band gaps due to the self-interaction
error of electrons (see Table II). Furthermore, SOC has a
negligible effect on the band gap (see Table S5 of the SM

[42]), as expected for chalcogenide perovskites [15–17].


Subsequently, the band gaps are computed more accurately using the hybrid HSE06 xc functional and the
many-body perturbation theory (MBPT)-based GW approach, specifically at the G0W0@PBE level. Figure 3
presents the band structures of these compounds, calculated using the hybrid HSE06 functional. Our calculated electronic band structures explicitly demonstrate
that YScX3 (X = S, Se) are indirect band gap materials.
In these compounds, the valence band maximum (VBM)
is located at the Γ-point, whereas the conduction band
minimum (CBM) occurs at the S-point in the Brillouin
zone [see Fig. 3(a)-(b)]. This spatial separation of the
band extrema confirms the indirect nature of the fundamental band gap, implying that optical transitions near
the band edge are phonon-assisted. In contrast, all other
compounds investigated in this study exhibit direct band
gaps. For these systems, both the VBM and CBM are
located at the same high-symmetry k-point, specifically
at the Γ-point [see Fig. 3(c)-(f)]. As a result, the fundamental electronic transition is momentum-conserving,
leading to a stronger optical absorption onset compared
to the indirect-gap counterparts.


The band gaps of these compounds, as calculated using the HSE06 functional and the G0W0@PBE approach,
are summarized in Table II. The HSE06 band gaps of
these chalcogenide perovskites are found to lie in the
range of 2.17 _−_ 3.45 eV, whereas the G0W0@PBE band
gaps are systematically larger, spanning 2.75 _−_ 4.47 eV.
This trend reflects the well-known tendency of manybody perturbation theory within the GW approximation
to yield improved quasiparticle energies by explicitly accounting for electron-electron interactions, thereby correcting the band gap underestimation inherent to standard and hybrid density functional approaches. Importantly, the G0W0@PBE results obtained in this work are
in good agreement with previously reported theoretical
studies [19, 22], confirming the reliability of the present
computational framework. The absence of exact quantitative agreement with previous reports can be attributed
to the sensitivity of G0W0 calculations to the choice of
starting functional, convergence parameters, and structural inputs. For the benchmark compound LaScS3, the
experimentally measured band gap (2.62 eV) is closer to
the HSE06 value (2.80 eV) than to the G0W0@PBE value
(3.72 eV) [18]. This discrepancy is likely attributable to
the inherent starting-point dependence of the single-shot


G0W0 approximation, the absence of self-consistency in
the GW calculations, residual convergence limitations,
and the neglect of finite-temperature and excitonic effects. Although G0W0 calculations based on an HSE06
starting point or self-consistent GW schemes could further reduce the starting-point dependence and improve
the quantitative accuracy of the quasiparticle energies,
such calculations are computationally prohibitive for the
large unit cells considered here. Nevertheless, the good
agreement with previous theoretical studies supports the
reliability of the present G0W0 results. Overall, the calculated band gaps place these chalcogenide perovskites
in the visible-to-ultraviolet wide-band-gap regime, highlighting their potential for optoelectronic applications.
Direct-gap compounds favor efficient light absorption and
emission (e.g., LEDs), whereas indirect-gap systems are
advantageous for longer carrier lifetime–based applications such as photodetectors and photocatalysis.


To gain deeper insight into the electronic structure, the
density of states (DOS) is calculated using the HSE06 xc
functional, as shown in Fig. S3 of the SM [42]. For
YScS3, the VBM is predominantly derived from S-3 _p_ orbitals, whereas the CBM is mainly contributed by Sc-3 _d_
orbitals. As expected, the CBM also exhibits hybridization between Y-4 _d_ and Sc-3 _d_ states. Similarly, in YScSe3,
the VBM is primarily composed of Se-4 _p_ orbitals, while
the CBM shows a noticeable downward shift due to enhanced hybridization between Se-4 _p_ and transition-metal
_d_ states, leading to the observed reduction in the band
gap. In contrast, for LaScX3 (X = S, Se), the CBM arises
from hybridized La-5 _d_ and Sc-3 _d_ states. The direct-toindirect band gap transition primarily arises from the interplay between _d_ - _d_ orbital hybridization and structural
distortions. In YScX3, stronger Y-4 _d−_ Sc-3 _d_ coupling
and larger octahedral tilting stabilize the CBM at the
S-point, resulting in an indirect gap. In contrast, weaker
La-5 _d−_ Sc-3 _d_ coupling and reduced tilting in LaScX3 shift
the conduction band upward at S-point and favor a minimum at Γ-point, leading to a direct band gap [18]. Furthermore, upon replacing Sc with Y (LaScX3 _→_ LaYX3),
the direct band gap nature is preserved, while the band
gap increases due to the higher energy and modified dispersion of Y-4 _d_ states relative to Sc-3 _d_ states, resulting
in an upward shift of the CBM in LaYX3.


To further substantiate the above interpretation, we
have included orbital-projected band structures near the
VBM and CBM in Fig. S4 of the SM [42]. These results explicitly identify the orbital character of the bandedge states and confirm that the evolution from a direct
to an indirect band gap is governed by changes in the
hybridization between Y-4 _d_ /La-5 _d_ and Sc-3 _d_ orbitals,
together with the accompanying structural distortions.
The orbital-projected bands provide direct microscopic
evidence for the orbital interactions responsible for the
shift of the CBM between the Γ and S points, thereby
supporting the mechanism proposed from the DOS analysis.



6


FIG. 3. Electronic band structures of the rare-earth chalcogenide perovskites (a) YScS3, (b) YScSe3, (c) LaScS3, (d)
LaScSe3, (e) LaYS3, and (f) LaYSe3, calculated using the
HSE06 xc functional. The Fermi level is set to be zero and
marked by the dashed line.



**C.** **Optical** **Properties:**


Beyond the electronic structure, the optical response
provides key insight into the suitability of these materials
for optoelectronic applications. In this work, the optical
response is accurately described by capturing many-body
effects through the Bethe-Salpeter equation (BSE) built
upon G0W0@PBE quasiparticle energies, ensuring a reliable treatment of excitonic contributions to the optical
spectra. In this framework, GW calculations determine
the fundamental bandgap, which is directly comparable
to photoelectron (PES) and inverse photoelectron spectroscopy (IPES) [31, 32], whereas BSE yields the optical
bandgap consistent with experimental absorption measurements [33, 34].

To evaluate the optical response of ABX3 (A = Y, La;
B = Sc, Y; and X = S, Se), we focus on the frequencydependent complex dielectric function, _ε_ ( _ω_ ) = [Re( _ε_ )]
+ i[Im( _ε_ )], which governs the interaction of electromagnetic radiation with the material. The imaginary part,



To gain insight into charge-carrier transport, we further calculate the effective masses of electrons ( _m_ <sup>_∗_</sup> _e_ <sup>)</sup> <sup>and</sup>

holes ( _m_ <sup>_∗_</sup> _h_ <sup>) for all compounds by fitting the</sup> <sup>_E −_</sup> <sup>_k_</sup> <sup>disper-</sup>

sion obtained from PBE band structures using the formula, _m_ <sup>_∗_</sup> = ℏ <sup>2 �</sup> _∂_ <sup>2</sup> _E_ ( _k_ ) _/∂k_ <sup>2�</sup> <sup>_−_</sup> <sup>1</sup>, and the results are sum


mula, _m_ <sup>_∗_</sup> = ℏ <sup>2 �</sup> _∂_ <sup>2</sup> _E_ ( _k_ ) _/∂k_ <sup>2�</sup> <sup>_−_</sup> <sup>1</sup>, and the results are sum
marized in Table II. For the direct band gap compounds,
the effective masses are evaluated as the harmonic mean
along the Γ _−_ X, Γ _−_ Y, and Γ _−_ Z directions, with results
listed in Table S6 of the SM [42]. In contrast, for YScX3
(X = S, Se), the electron effective masses are obtained
by averaging along the S _−_ X and S _−_ Y directions, consistent with the location of the CBM. From Table II, it is
evident that _m_ <sup>_∗_</sup> _e_ <sup>is</sup> <sup>significantly</sup> <sup>larger</sup> <sup>than</sup> <sup>_m∗_</sup> _h_ <sup>in</sup> <sup>these</sup>

compounds, indicating that holes are expected to possess
higher mobility than electrons. This suggests that these
materials are more favorable for p-type transport.




<sup>_∗_</sup> _e_ <sup>is</sup> <sup>significantly</sup> <sup>larger</sup> <sup>than</sup> <sup>_m∗_</sup> _h_


7


TABLE II. Bandgap (in eV) of ABX3 (A = Y, La; B = Sc, Y; and X = S, Se) rare-earth chalcogenide perovskites calculated
using different methods as well as computed average effective mass of electron ( _m_ <sup>_∗_</sup> _e_ <sup>)</sup> <sup>and</sup> <sup>hole</sup> <sup>(</sup> <sup>_m∗_</sup> _h_ <sup>).</sup> Here, _i_, _d_, _t_, and _e_

represent indirect, direct, theoretical, and experimental bandgaps, respectively. All values of the effective mass are in terms of
free-electron mass ( _m_ 0).




<sup>_<u>∗</u>_</sup> _<u>e</u>_ _<u>m</u>_ <sup>_<u>∗</u>_</sup> _<u>h</u>_



<u>Configurations</u> <u>PBE</u> <u>HSE06</u> <u>G0W0@PBE</u> <u>Previous</u> <u>Work</u> _<u>m</u>_ <sup>_<u>∗</u>_</sup> _<u>e</u>_



i <u>G0W0@PBE</u> _<u>e</u>_ _<u>h</u>_

YScS3 1.76 <sup>_<u>i</u>_</sup> (1.88 <sup>_<u>d</u>_</sup> ) 2.75 <sup>_<u>i</u>_</sup> (2.96 <sup>_<u>d</u>_</sup> ) 3.49 <sup>_<u>i</u>_</sup> (3.75 <sup>_<u>d</u>_</sup> ) 3.16 _t_ (G0W0) [22] 1.545 0.494
YScSe3 1.30 <sup>_i_</sup> (1.43 <sup>_d_</sup> ) 2.17 <sup>_i_</sup> (2.39 <sup>_d_</sup> ) 2.75 <sup>_i_</sup> (3.00 <sup>_d_</sup> ) 1.622 0.375
LaScS3 1.69 2.80 3.72 2.62 _e_ [18] 0.916 0.457
LaScSe3 1.27 2.27 2.94 2.96 _t_ (G0W0) [19] 0.851 0.350
LaYS3 2.25 3.45 4.47 1.255 0.542
<u>LaYSe3</u> <u>1.79</u> <u>2.87</u> <u>3.70</u> <u>1.180</u> <u>0.419</u>




[Im( _ε_ )], describes interband optical absorption arising
from electronic transitions between occupied and unoccupied states and is directly related to the absorption
spectrum and optical bandgap. In contrast, the real
part, [Re( _ε_ )], represents the dispersive response and determines key optical properties such as dielectric screening, refractive index, and polarization behavior. Notably,
the static limit _ε∞_ provides insight into the screening
strength, which influences excitonic effects and chargecarrier interactions. Together, these components offer
a comprehensive description of light-matter interaction
and are essential for assessing the suitability of these materials for optoelectronic applications.


FIG. 4. Spatially averaged real [Re( _ε_ )] and imaginary part

[Im( _ε_ )] of the electronic dielectric function for rare-earth
chalcogenide perovskites (a) YScS3, (b) YScSe3, (c) LaScS3,
(d) LaScSe3, (e) LaYS3, and (f) LaYSe3, respectively, calculated using the BSE@G0W0@PBE method. Peaks with cyan
color represent the oscillator strength.


The imaginary part of the dielectric function, [Im( _ε_ )],
for ABX3 (A = Y, La; B = Sc, Y; and X = S, Se)
perovskite compounds exhibits broad spectral coverage
from the visible to the ultraviolet region, as shown in
Figure 4. This response reflects the interplay of band
structure, momentum selection rules, and electron-hole
interactions, where direct gaps enable sharp absorption
edges, indirect gaps lead to phonon-assisted onset, and
excitonic effects renormalize the optical gap and enhance
near-edge spectral features. The oscillator strength spectra further identify the optically allowed excitonic transitions. Strong oscillator strength indicates a large tran


sition dipole moment and efficient light-matter coupling,
giving rise to intense absorption features, whereas weak
or nearly vanishing oscillator strength corresponds to optically inactive (dark) excitonic states that contribute
negligibly to the optical response. The energy eigenvalue of the first optically active (bright) exciton, which
defines the optical band gap ( _Eo_ ), spans 2.77 _−_ 3.96 eV
across the series, highlighting the substantial influence of
excitonic effects. Since the lowest excitonic state is optically active for all compounds investigated in this work,
its eigenvalue directly corresponds to the optical absorption onset. Notably, for LaScS3, the experimentally measured optical gap is 2.62 eV [18], whereas the present
BSE optical gap value is 3.40 eV. This discrepancy can
be attributed to the idealized nature of the calculations,
which neglect temperature effects, carrier-phonon renormalization, and defect-induced band tailing that typically reduce the measured absorption onset. Overall,
the strong and compositionally tunable optical absorption highlights the potential of these materials for optoelectronic applications, including photodetectors, lightemitting diodes, and laser devices.

In addition to the optical spectra, the electronic dielectric constant ( _ε∞_ ), defined as the zero-frequency limit
of the real part of the dielectric function, is evaluated
as a key descriptor of the optoelectronic response. This
quantity governs the screening of Coulomb interactions,
where larger _ε∞_ values reduce electron-hole attraction
and suppress carrier recombination, thereby, enhancing
device performance [50]. The calculated _ε∞_ values for
ABX3 (A = Y, La; B = Sc, Y; and X = S, Se), obtained
within the BSE framework, span the range of 2.26 _−_ 5.88,
as summarized in Table S13 of the SM [42]. These dielectric constants also serve as essential input parameters
for evaluating excitonic and polaronic properties, as discussed in the following sections.


**D.** **Excitonic** **Properties:**


In addition to the aforementioned electronic and optical properties, excitonic properties such as, exciton binding energy ( _EB_ ), excitonic temperature ( _Texc_ ), exciton
radius ( _rexc_ ), and the probability of the wavefunction for
the electron-hole ( _e−h_ ) pair at zero separation ( _|ϕn_ (0) _|_ <sup>2</sup> ),


play a crucial role in determining the performance of
optoelectronic devices. An exciton is a Coulomb-bound
_e −_ _h_ pair formed upon optical excitation, which renormalizes the optical gap and governs near-edge absorption
features. The exciton binding energy ( _EB_ ) quantifies the
energy required to dissociate the exciton into free charge
carriers, i.e., an electron in the conduction band and a
hole in the valence band. A lower _EB_ facilitates efficient
charge separation at or near room temperature, thereby
promoting enhanced photoelectric conversion efficiency,
particularly in photovoltaic applications. In contrast,
a higher _EB_ implies stronger Coulomb interaction between electrons and holes, leading to more stable and
tightly bound excitons. While this can hinder efficient
charge separation and reduce photocurrent generation in
photovoltaic devices, it is advantageous for applications
that rely on strong radiative recombination, such as lightemitting diodes and laser devices, where enhanced excitonic stability can improve emission efficiency.


The exciton binding energy ( _EB_ ) is obtained from firstprinciples Bethe-Salpeter equation (BSE) calculations as,
_EB_ = _Eg_ <sup>_dir_</sup> _−_ _Eo_, where _Eg_ <sup>_dir_</sup> is the direct quasiparti


8


XII of the SM [42]). From Table S13, it is observed that
the upper bounds ( _EBu_ = 0.102 _−_ 1.009 eV) for these compounds closely match the _EB_ values obtained using the
BSE@G0W0@PBE method, whereas the lower bounds
( _EBl_ ) are significantly smaller. This indicates that the
ionic contribution to the dielectric constant is negligible,
leading to _ε_ eff _→_ _ε∞_ . Therefore, at high frequencies,
dielectric screening is governed primarily by electronic
effects.


TABLE III. Calculated exciton parameters of ABX3 (A =
Y, La; B = Sc, Y; and X = S, Se) rare-earth chalcogenide
perovskites.



_g_

Configurations <sup>_Edir_</sup>



_g_ _Eo_ _EB_ _Texc_ _rexc_ _|ϕn_ (0) _|_ <sup><u>2</u></sup>

<sup>_<u>dir</u>_</sup>



_g_ <sup>_dir_</sup> _−_ _Eo_, where _Eg_ <sup>_dir_</sup>



_EB_ = _Eg_ <sup>_dir_</sup> _−_ _Eo_, where _Eg_ <sup>_dir_</sup> is the direct quasiparti
cle band gap from G0W0@PBE and _Eo_ denotes the energy eigenvalue of the first optically active (bright) excitonic state computed within BSE@G0W0@PBE [51, 52].
As summarized in Table III, the calculated _EB_ values for these chalcogenide perovskites decrease from Sto Se-containing counterparts and lie in the range of
0.148 _−_ 0.517 eV. Such moderately large binding energies indicate pronounced excitonic effects arising from
reduced dielectric screening and enhanced electron-hole
interactions, which are favorable for efficient radiative recombination in light-emitting and photodetection applications. Notably, LaYX3 exhibits a clear deviation from
the overall trend, showing comparatively enhanced excitonic binding. This behavior can be attributed to its reduced electronic dielectric screening (see Figure 4), which
strengthens the Coulomb interaction between electrons
and holes. While the absolute values of _EB_ may be somewhat overestimated due to the use of G0W0@PBE and
the neglect of temperature- and phonon-induced screening effects, the overall trends and qualitative description
of excitonic behavior remain robust. In particular, the
systematic variation across the series and the identification of intermediate excitonic character are expected to
be reliable, as they are primarily governed by dielectric
screening and carrier effective masses captured within the
present framework.


It is worth noting that when _EB_ significantly exceeds
the longitudinal optical (LO) phonon energy (ℏ _ωLO_ ), dielectric screening is dominated by the electronic contribution, while the ionic component becomes negligible. Consequently, _EB_ remains largely unaffected by lattice polarization effects [53]. As shown in Tables III and V, the
condition _EB_ _≫_ ℏ _ωLO_ is satisfied for the present compounds, justifying the neglect of ionic screening. This
behavior is further corroborated by estimates based on
the hydrogenic Wannier-Mott model (for details, see Sec.



where _ωLO_ denotes the characteristic longitudinal optical phonon frequency, and _ε∞_ and _εs_ represent the electronic and static dielectric constants, respectively. The
effective _ωLO_ is evaluated using the thermal “B” approach developed by Hellwarth _et_ _al._ [36], which accounts for the spectral contributions of multiple phonon
branches through an appropriate averaging scheme (for
details, see Sec. XIII of the SM [42]). Table IV shows
that phonon screening reduces _EB_ by 3.20 _−_ 9.26%, indicating that the overall reduction is not substantial in
these rare-earth chalcogenide perovskites. After incorporating the phonon-screening correction, the renormalized exciton binding energy ( _EB_ <sup>_′_</sup> <sup>)</sup> <sup>spans</sup> <sup>0.134</sup> <sup>_−_</sup> <sup>0.498</sup> <sup>eV.</sup>

This behavior suggests that the electronic contribution
to dielectric screening dominates over the ionic (phononmediated) component in these systems.



<u>(eV)</u> <u>(eV)</u> <u>(eV)</u> <u>(K)</u> <u>(nm)</u> <u>(10</u> <sup>27</sup> <u>m</u> <sup>_−_</sup> <sup>3</sup> <u>)</u>
YScS3 3.747 3.424 0.323 3745 0.69 0.97
YScSe3 3.005 2.772 0.233 2701 1.20 0.19
LaScS3 3.721 3.397 0.324 3757 0.58 1.61
LaScSe3 2.941 2.793 0.148 1716 0.86 0.50
LaYS3 4.472 3.955 0.517 5994 0.32 10.14
<u>LaYSe3</u> <u>3.701</u> <u>3.286</u> <u>0.415</u> <u>4812</u> <u>0.43</u> <u>3.87</u>



Further, the calculation of _EB_ within the standard
first-principles BSE framework includes only electronic
screening in the _e_ _−_ _h_ interaction kernel and neglects lattice (phonon) contributions. Such a static treatment can
be inadequate for polar materials, where carrier-phonon
coupling plays a crucial role in screening Coulomb interactions. To address this limitation, we adopt the approach of Filip _et al._ [54, 55], who introduced a correction
of phonon-screening under the assumption of isotropic
and parabolic band dispersion. The correction to the
exciton binding energy is given by




- �1 + _ωLO/EB_ + 3
<u>�1 +</u> <u>�1 +</u> _ωLO/EB_ <u>�3</u> <sup>_,_</sup>


(2)



∆ _EB_ <sup>_ph_</sup> <sup>=</sup> <sup>_−_</sup> <sup>2</sup> <sup>_ωLO_</sup>



�1 _−_ <sup>_<u>ε∞</u>_</sup>
_εs_


TABLE IV. Calculated exciton binding energy ( _EB_ ), phonon
screening corrections (∆ _EB_ <sup>_ph_</sup> <sup>), percentage of phonon screening</sup>

contribution to the reduction of exciton binding energy (%),
and corrected values of exciton binding energy ( _EB_ <sup>_′_</sup> <sup>) for ABX3</sup>

(A = Y, La; B = Sc, Y; and X = S, Se) rare-earth chalcogenide
perovskites.



Configurations _EB_ ∆ _EB_ <sup>_<u>ph</u>_</sup>



_B_ <sup>_<u>ph</u>_</sup> Reduction of _EB_ _E_ <sup>_′_</sup>



Configurations _EB_ _B_ Reduction of _EB_ _B_

<u>(eV)</u> <u>(meV)</u> <u>(%)</u> <u>(eV)</u>
YScS3 0.323 -19.20 5.94 0.304
YScSe3 0.233 -13.55 5.82 0.219
LaScS3 0.324 -19.41 5.99 0.305
LaScSe3 0.148 -13.70 9.26 0.134
LaYS3 0.517 -18.67 3.61 0.498
<u>LaYSe3</u> <u>0.415</u> <u>-13.29</u> <u>3.20</u> <u>0.402</u>



Next, several additional excitonic parameters, including the excitonic temperature ( _Texc_ ), exciton radius
( _rexc_ ), and the probability of the wavefunction for the
_e_ _−_ _h_ pair at zero separation ( _|ϕn_ (0) _|_ <sup>2</sup> ), are evaluated
and summarized in Table III. The excitonic temperature
( _Texc_ ) serves as a useful metric to quantify the thermal
stability of bound _e−h_ pairs in semiconductors and insulators. It is defined by relating the exciton binding energy
( _EB_ ) to thermal energy via the Boltzmann constant ( _kB_ )
as _Texc_ = _EB/kB_ . Physically, _Texc_ represents the characteristic temperature above which excitons are thermally
ionized into free carriers. When _Texc_ significantly exceeds
room temperature ( _∼_ 300 K), excitons are expected to
remain stable under ambient conditions, giving rise to
pronounced excitonic features in optical absorption and
emission spectra. Conversely, if _Texc_ is comparable to or
lower than room temperature, thermal dissociation becomes efficient, and the optoelectronic response is dominated by free carriers. In our study, the rare-earth chalcogenide perovskite compounds exhibit high excitonic temperatures (1716 _−_ 5994 K), reflecting strongly bound excitons that remain thermally stable far above room temperature and yield pronounced excitonic effects in their
optical response. Such robust excitonic stability is advantageous for optoelectronic applications, particularly in
light-emitting devices and photodetectors, where strong
light-matter interaction and efficient exciton generation
are desirable.

The exciton radius ( _rexc_ ) is evaluated within the hydrogenic Wannier-Mott model as [56, 57]:



_rexc_ = <sup>_<u>m</u>_</sup> <sup><u>0</u></sup>



9


states. In our study, the obtained _rexc_ values ( _∼_ 3.2 _−_ 12
Å) indicate moderately to strongly bound excitons with
spatial extents ranging from near unit-cell localization to
a few lattice constants, suggesting an intermediate character approaching the Wannier-Frenkel crossover regime.
Such excitons promote strong light-matter interaction,
highlighting the potential of these materials for optoelectronic applications. Within this framework, LaYX3
stands out by exhibiting a comparatively smaller exciton
radius, reflecting enhanced localization of the electronhole pair. This behavior originates from its relatively
weak electronic screening, which strengthens Coulomb
interactions and stabilizes more tightly bound excitonic
states.

To qualitatively assess the radiative recombination
propensity of excitons, we evaluate the probability density of the _e −_ _h_ pair at zero separation, _|ϕn_ (0) _|_ <sup>2</sup>, which
is given by [56, 57]:


<u>1</u>
_|ϕn_ (0) _|_ <sup>2</sup> = (4)
_π_ ( _rexc_ ) <sup>3</sup> _n_ <sup>3</sup> <sup>_._</sup>


Within the framework of radiative recombination, the
radiative decay rate is proportional to the _e_ _−_ _h_ overlap, i.e., _τrad_ <sup>_−_</sup> <sup>1</sup> <sup>_∝|ϕn_</sup> <sup>(0)</sup> <sup>_|_</sup> <sup>2.</sup> <sup>Consequently,</sup> <sup>larger</sup> <sup>values</sup> <sup>of</sup>

_|ϕn_ (0) _|_ <sup>2</sup> indicate stronger _e_ _−_ _h_ overlap and a greater
propensity for radiative transitions. In the present case,
LaYX3 exhibits an enhanced _|ϕn_ (0) _|_ <sup>2</sup>, consistent with its
reduced exciton radius, confirming stronger wavefunction
overlap and potentially larger oscillator strength. Since
neither radiative nor non-radiative exciton lifetimes are
explicitly calculated in this work, _|ϕn_ (0) _|_ <sup>2</sup> is employed
only as a qualitative descriptor of the radiative recombination tendency rather than as a direct measure of the
exciton lifetime ( _τexc_ ). These results indicate pronounced
light-matter interaction in the studied systems, which is
beneficial for optoelectronic and light-emitting applications.


**E.** **Polaronic** **Properties:**


Understanding the fundamental limits of carrier mobility in these chalcogenide perovskites requires a rigorous treatment of carrier-phonon interactions within a
first-principles framework [58, 59]. In polar semiconductors, transport at ambient conditions is primarily limited
by scattering with longitudinal optical phonons, arising
from the macroscopic electric fields associated with lattice polarization [15, 52]. This interaction leads to the
formation of polarons, wherein charge carriers become
dressed by lattice distortions, thereby altering their effective mass and transport dynamics. As a consequence,
mobility cannot be accurately described within a simple
band-like picture of free carriers.

The interaction between charge carriers and polar optical phonons can be effectively described within the framework of the Fröhlich Hamiltonian, which is valid in the



_µ_ <sup>_∗_</sup>



_ε_ eff _n_ <sup>2</sup> _rRy,_ (3)



_dir_



where _µ_ <sup>_∗_</sup> _dir_ <sup>is</sup> <sup>the</sup> <sup>reduced</sup> <sup>effective</sup> <sup>mass</sup> <sup>at</sup> <sup>the</sup> <sup>direct</sup>

band edge, _ε_ eff denotes the effective dielectric constant,
_n_ is the exciton energy level, and _rRy_ is the Bohr radius
(0.0529 nm). In this work, the high-frequency dielectric constant ( _ε∞_ ) is employed as the effective dielectric
screening ( _ε_ eff), and _n_ = 1 is considered, corresponding to the ground-state exciton and yielding the minimum exciton radius. The exciton radius serves as a key
descriptor of the spatial extent of the _e_ _−_ _h_ pair, distinguishing between localized and delocalized excitonic


low carrier-density regime [35]. The strength of this interaction is quantified by the dimensionless Fröhlich coupling constant, _α_, which incorporates the effects of dielectric screening, carrier effective mass, and the longitudinal
optical phonon frequency. It is defined as [15, 60]:



10


for most of the examined chalcogenide perovskites, the
energy of the charge-separated polaronic states is lower
than that of the bound exciton states, indicating that
the bound excitons are energetically more stable. However, in the case of La(Sc, Y)Se3, the charge-separated
polaronic states become more favorable than the bound
exciton states.

Feynman introduced a powerful variational approach
to address the Fröhlich Hamiltonian, which describes
the interaction between an electron (or hole) and a continuum of independent, harmonically oscillating phonon
modes within a quantum field theoretical framework [62].
As the electron (or hole) moves through the lattice, it
interacts with the polarization field it induces, which
evolves and decays over time. Within this formalism,
and in the weak-coupling limit (small _α_ ), the polaron
effective mass, _mp_, can be expressed as [17, 62]:



�1 _/_ 2
(5)




- <u>2</u> _<u>m∗ωLO</u>_

ℏ




_−_ <sup><u>1</u></sup>

_εs_



<u>1</u>
_α_ =
4 _πε_ 0



<u>1</u>

2




- <u>1</u>
_ε∞_




- _<u>e</u>_ <sup>2</sup>

ℏ _ωLO_



The calculated carrier-phonon coupling constants ( _α_ )
for the investigated compounds are summarized in Table
V. In general, _α >_ 10 signifies strong carrier-phonon coupling, whereas _α_ _≪_ 1 corresponds to the weak-coupling
regime [58]. Our results place these materials in the
intermediate-to-strong coupling regime, with _α_ values
ranging from 1.92 to 10.72. Furthermore, the carrierphonon interaction is found to be stronger for electrons
than for holes, with this trend being particularly pronounced in LaYX3 (X = S, Se), suggesting more significant polaronic renormalization of electron transport. It
should be emphasized that the present analysis is based
on the Fröhlich formalism, which provides a physically
meaningful description of the long-range interaction between charge carriers and longitudinal optical phonons
in polar materials using first-principles quantities, including the dielectric constants, effective carrier masses,
and longitudinal optical phonon frequencies. Consequently, the calculated Fröhlich coupling constants provide useful estimates of the strength of the long-range polar electron-phonon interaction and the associated largepolaron characteristics. However, this approach does not
explicitly evaluate the momentum- and mode-resolved
electron-phonon coupling matrix elements or identify the
individual phonon modes and electronic states contributing to the coupling. A comprehensive microscopic treatment based on first-principles electron-phonon coupling
calculations using density-functional perturbation theory
together with Wannier interpolation would provide such
information but is beyond the scope of the present work

[61]. Nevertheless, the Fröhlich model remains a widely
adopted framework for describing large-polaron behavior in polar semiconductors and is appropriate for the
objectives of the present study.

Polaron formation refers to the interaction of a charge
carrier, either an electron or a hole, with the surrounding
lattice, leading to a local structural distortion. This coupling lowers the quasiparticle (QP) energies, so that both
electron and hole states are stabilized during polaron formation. The polaron energy, _Ep_, can be estimated as
follows [15, 56]:


_Ep_ = ( _−α −_ 0 _._ 0123 _α_ <sup>2</sup> )ℏ _ωLO._ (6)


The QP gap associated with the polaronic states, obtained from the electron and hole polaron energies (Table V), is compared with the exciton binding energies,
_EB_, listed in Table III. This comparison reveals that,



_mp_ = _m_ <sup>_∗_</sup> <sup>�</sup>



1 + <sup>_<u>α</u>_</sup> - _._ (7)
6 <sup>+</sup> <sup>_<u>α</u>_</sup> 40 <sup>2</sup> <sup>+</sup> <sup>_..._</sup>



As shown in Table V, carrier-phonon coupling leads to
a substantial enhancement of the effective mass, with _mp_
increasing by approximately 41 _−_ 466%. This significant
renormalization indicates the presence of intermediate to
strong carrier-lattice interactions in the examined systems.

To further assess the impact of the enhanced polaron
effective mass, the polaron mobility is estimated using
the Hellwarth polaron model as [36, 57]:



<u>(3</u> <sup>_√_</sup> _<u>πe</u>_ <u>)</u> <u>sinh(</u> _<u>β/</u>_ <u>2)</u>
_µp_ =
2 _πcωLOm_ <sup>_∗_</sup> _α_ _β_ <sup>5</sup> <sup>_/_</sup> <sup>2</sup>



_<u>w</u>_ <sup>3</sup>

_v_ <sup>3</sup>



<u>1</u>
(8)
_K_ ( _a, b_ )



where _e_ is the electronic charge, _β_ = _hcωLO/kBT_, _w_
and _v_ are temperature-dependent variational parameters,
and _K_ ( _a, b_ ) is a function of _β_, _w_, and _v_ (for details, see
Sec. XIII of the SM [42]). The polaron mobility quantifies the ease with which a polaron propagates through
the lattice and is governed by both its effective mass and
the strength of carrier-lattice interactions. As the effective mass increases due to strong carrier-phonon coupling, the mobility correspondingly decreases, leading to
slower carrier transport. This behavior is evident in the
present systems (Table V), where hole polarons exhibit
significantly higher mobilities (2.12 _−_ 39.94 cm <sup>2</sup> V <sup>_−_</sup> <sup>1</sup> s <sup>_−_</sup> <sup>1</sup> )
compared to electron polarons (0.21 _−_ 3.87 cm <sup>2</sup> V <sup>_−_</sup> <sup>1</sup> s <sup>_−_</sup> <sup>1</sup> ).
This indicates stronger electron-phonon coupling and/or
larger effective masses for electrons, leading to more localized electron polarons and consequently reduced mobility. In contrast, the relatively lighter and less strongly
coupled hole polarons enable more efficient charge transport. Despite the relatively low electron mobility, the
favorable hole transport, combined with the structural
stability and non-toxicity of these materials, underscores
their potential for optoelectronic applications, particularly in devices where hole conduction plays a dominant
role.


11


TABLE V. Calculated polaron parameters of ABX3 (A = Y, La; B = Sc, Y; and X = S, Se) rare-earth chalcogenide perovskites.

_<u>α</u>_ _<u>Ep</u>_ <u>(meV)</u> _<u>mp/m</u>_ <sup>_<u>∗</u>_</sup> _<u>µp</u>_ <u>(cm</u> <sup><u>2</u></sup> <u>V</u> <sup>_<u>−</u>_</sup> <sup><u>1</u></sup> <u>s</u> <sup>_<u>−</u>_</sup> <sup><u>1</u></sup> <u>)</u>
Configurations _ωLO_ (THz)
_<u>e</u>_ _<u>h</u>_ _<u>e</u>_ _<u>h</u>_ _<u>e</u>_ _<u>h</u>_ _<u>e</u>_ _<u>h</u>_
YScS3 6.50 4.39 2.48 124.55 68.79 2.21 1.57 2.18 19.04
YScSe3 4.86 3.99 1.92 84.25 39.56 2.06 1.41 2.94 39.94
LaScS3 5.92 5.56 3.93 145.63 101.01 2.70 2.04 2.27 9.67
LaScSe3 4.47 4.94 3.17 97.00 60.97 2.43 1.78 3.87 21.31
LaYS3 5.32 10.72 7.04 267.32 168.53 5.66 3.41 0.21 2.12
<u>LaYSe3</u> <u>3.87</u> <u>10.58</u> <u>6.30</u> <u>191.63</u> <u>108.79</u> <u>5.56</u> <u>3.04</u> <u>0.34</u> <u>5.05</u>



A broader perspective can be obtained by comparing
the present III-III chalcogenide perovskites with the more
extensively studied II-IV systems ABX3 (A = Ca, Sr,
Ba; B = Ti, Zr, Sn, Hf; and X = S, Se). The latter typically exhibit smaller band gaps ( _∼_ 1.0 _−_ 2.5 eV),
larger dielectric screening, and correspondingly weaker
excitonic effects, resulting in more delocalized Wanniertype excitons and longer carrier diffusion lengths that
are advantageous for photovoltaic applications [13–17].
In addition, relatively weaker carrier-phonon coupling in
these systems leads to lighter polarons and higher carrier
mobility. In contrast, the III-III compounds investigated
here display wider band gaps (2.75 _−_ 4.47 eV), reduced dielectric screening, and moderately large exciton binding
energies, giving rise to more localized excitons with enhanced electron-hole overlap. This enhanced localization
is further accompanied by stronger carrier-phonon coupling, leading to heavier polaronic quasiparticles and reduced carrier mobility. While such polaronic effects may
limit efficient charge transport and charge separation,
they can simultaneously stabilize excitonic states and
suppress non-radiative recombination. Consequently, the
combination of strong excitonic binding and polaronic localization results in pronounced light-matter interaction
and enhanced radiative recombination, making these materials particularly promising for light-emitting and photodetection applications, albeit less favorable for photovoltaic performance.


**IV.** **CONCLUSION:**


In summary, we have systematically investigated the
ground- and excited-state properties of III-III rare-earth
chalcogenide perovskites ABX3 (A = Y, La; B = Sc,
Y; and X = S, Se) using state-of-the-art density functional theory, density functional perturbation theory, and
many-body perturbation theory. The calculated phonon
band structures and elastic constants confirm the dynamical and mechanical stability of these compounds. Our
electronic structure analysis reveals quasiparticle band
gaps (G0W0@PBE) in the range of 2.75 _−_ 4.47 eV, accompanied by lower hole effective masses compared to
electrons, indicating favorable p-type transport. The optical properties, computed within the BSE framework,
exhibit a strong absorption onset spanning the visible to



ultraviolet region, highlighting their potential for optoelectronic applications. Importantly, these compounds
exhibit pronounced excitonic effects, hosting stable excitons as evidenced by their intermediate-to-large binding energies (0.148 _−_ 0.517 eV), high excitonic temperatures, Wannier-Frenkel crossover character, and strong
electron-hole wavefunction overlap, indicative of pronounced light-matter interaction and favorable radiative recombination characteristics. Fröhlich’s mesoscopic
analysis indicates appreciable carrier-phonon coupling in
these systems, with electron-phonon interactions consistently outweighing their hole counterparts. Remarkably,
bound excitonic states dominate over charge-separated
polaronic configurations in nearly all compounds, with
La(Sc, Y)Se3 as an exception, while hole polarons demonstrate substantially higher mobilities (reaching up to _∼_
40 cm <sup>2</sup> V <sup>_−_</sup> <sup>1</sup> s <sup>_−_</sup> <sup>1</sup> ) than electrons. Overall, the interplay
between strong excitonic effects and favorable polaronic
transport, combined with excellent structural stability
and lead-free composition, establishes rare-earth chalcogenide perovskites ABX3 as promising candidates for
next-generation optoelectronic technologies. These materials are particularly attractive for applications in lightemitting devices and photodetectors, and they offer a viable platform for exploring excitonic optoelectronics in
environmentally benign systems.


**ACKNOWLEDGMENTS**


The authors would like to acknowledge the Council of Scientific and Industrial Research (CSIR), Government of India [Grant No. 3WS(007)/2023-24/EMRII/ASPIRE] for financial support. The authors acknowledge the High Performance Computing Cluster (HPCC)
‘Magus’ at Shiv Nadar Institution of Eminence for providing computational resources that have contributed to
the research results reported within this paper.


**DATA** **AVAILABILITY**


The data that support the findings of this article are
not publicly available. The data are available from the
authors upon reasonable request.


[1] A. Kojima, K. Teshima, Y. Shirai, and T. Miyasaka,

Organometal Halide Perovskites as Visible-Light Sensitizers for Photovoltaic Cells, J. Am. [Chem.](https://doi.org/10.1021/ja809598r) Soc. **131**,
[6050](https://doi.org/10.1021/ja809598r) (2009).

[2] N.-G. Park, Organometal Perovskite Light Absorbers To
ward a 20% Efficiency Low-Cost Solid-State Mesoscopic
Solar Cell, J. Phys. Chem. [Lett.](https://doi.org/10.1021/jz400892a) **4**, 2423 (2013).

[3] J. Berry, T. Buonassisi, D. A. Egger, G. Hodes, L. Kro
nik, Y.-L. Loo, I. Lubomirsky, S. R. Marder, Y. Mastai,
J. S. Miller, D. B. Mitzi, Y. Paz, A. M. Rappe, I. Riess,
B. Rybtchinski, O. Stafsudd, V. Stevanovic, M. F. Toney,
D. Zitoun, A. Kahn, D. Ginley, and D. Cahen, Hybrid
Organic-Inorganic Perovskites (HOIPs): Opportunities
and Challenges, Adv. Mater. **[27](https://doi.org/https://doi.org/10.1002/adma.201502294)**, 5102 (2015).

[4] D. A. Egger, A. M. Rappe, and L. Kronik, Hybrid

Organic-Inorganic Perovskites on the Move, Acc. [Chem.](https://doi.org/10.1021/acs.accounts.5b00540)
Res. **[49](https://doi.org/10.1021/acs.accounts.5b00540)**, 573 (2016).

[5] National Renewable Energy Laboratory (NREL), Best

Research Cell Efficiency Chart, `[https://www.nrel.gov/](https://www.nrel.gov/pv/cell-efficiency.html)`
`[pv/cell-efficiency.html](https://www.nrel.gov/pv/cell-efficiency.html)`, Accessed 2021-01-07 (2021).

[6] D. B. Straus, S. Guo, A. M. Abeykoon, and R. J.

Cava, Understanding the Instability of the Halide Perovskite CsPbI3 through Temperature-Dependent Structural Analysis, Adv.Mater. **32**, 2001069 (2020).

[7] A. Babayigit, A. Ethirajan, M. Muller, and B. Conings,

[Toxicity of organometal halide perovskite solar cells, Nat.](https://doi.org/10.1038/nmat4572)
Mater. **[15](https://doi.org/10.1038/nmat4572)**, 247 (2016).

[8] D. Tiwari, O. S. Hutter, and G. Longo, Chalcogenide per
ovskites for photovoltaics: current status and prospects,
J. Phys. Energy **3**, 034010 (2021).

[9] S. Niu, H. Huyan, Y. Liu, M. Yeung, K. Ye, L. Blanke
meier, T. Orvis, D. Sarkar, D. J. Singh, R. Kapadia, and
J. Ravichandran, Bandgap Control via Structural and
Chemical Tuning of Transition Metal Perovskite Chalcogenides, Adv. Mater. **29** [,](https://doi.org/https://doi.org/10.1002/adma.201604733) 1604733 (2017).

[10] X. Wu, W. Gao, J. Chai, C. Ming, M. Chen, H. Zeng,

P. Zhang, S. Zhang, and Y.-Y. Sun, Defect tolerance
in chalcogenide perovskite photovoltaic material BaZrS3,
Sci. China [Mater.](https://doi.org/10.1007/s40843-021-1683-0) **64**, 2976 (2021).

[11] Y.-Y. Sun, M. L. Agiorgousis, P. Zhang, and S. Zhang,

Chalcogenide Perovskites for Photovoltaics, Nano Lett.
**15**, [581](https://doi.org/10.1021/nl504046x) (2015).

[12] R. Lelieveld and D. J. W. IJdo, Sulphides with the

GdFeO3 structure, Acta Cryst. B **[36](https://doi.org/10.1107/S056774088000845X)**, 2223 (1980).

[13] M. Kumar, A. Singh, D. Gill, and S. Bhattacharya, Op
toelectronic Properties of Chalcogenide Perovskites by
Many-Body Perturbation Theory, J. Phys. [Chem.](https://doi.org/10.1021/acs.jpclett.1c01034) Lett.
**12**, [5301](https://doi.org/10.1021/acs.jpclett.1c01034) (2021).

[14] P. Basera and S. Bhattacharya, Chalcogenide Perovskites

(ABS3; A = Ba, Ca, Sr; B = Hf, Sn): An Emerging Class
of Semiconductors for Optoelectronics, J. [Phys.](https://doi.org/10.1021/acs.jpclett.2c01337) Chem.
Lett. **13** [,](https://doi.org/10.1021/acs.jpclett.2c01337) 6439 (2022).

[15] S. Adhikari and P. Johari, Photovoltaic properties of

_AB_ Se3 chalcogenide perovskites ( _A_ = Ca, Sr, Ba; _B_ =
Zr, Hf), Phys. Rev. B **[109](https://doi.org/10.1103/PhysRevB.109.174114)**, 174114 (2024).

[16] S. Adhikari, S. Das, and P. Johari, Post-transition metal

Sn-based chalcogenide perovskites: a promising leadfree and transition metal alternative for stable, highperformance photovoltaics, J. Mater. [Chem.](https://doi.org/10.1039/D4TC04701J) C **13**, 7792
[(2025).](https://doi.org/10.1039/D4TC04701J)



12


[17] S. Adhikari and P. Johari, Optimizing lead-free chalco
genide perovskites for high-efficiency photovoltaics via alloying, Phys. Rev. B **[112](https://doi.org/10.1103/wbdp-6n6g)**, 085206 (2025).

[18] H. Zhang, Y. Pan, Z. Liu, B. Zeng, X. Wu, C. Ming,

G. Xin, W. Zhou, H. Zeng, S. Zhang, and Y.-Y. Sun,
Indirect-to-direct band gap transition induced by _d−d_
coupling between cations in rare-earth chalcogenide perovskites, Phys. Rev. B **[110](https://doi.org/10.1103/PhysRevB.110.L041201)**, L041201 (2024).

[19] H. Zhang, X. Wu, K. Ding, L. Xie, K. Yang, C. Ming,

S. Bai, H. Zeng, S. Zhang, and Y.-Y. Sun, Prediction and
Synthesis of a Selenide Perovskite for Optoelectronics,
Chem. Mater. **[35](https://doi.org/10.1021/acs.chemmater.2c03676)**, 4128 (2023).

[20] K. Kuhar, A. Crovetto, M. Pandey, K. S. Thygesen,

B. Seger, P. C. K. Vesborg, O. Hansen, I. Chorkendorff,
and K. W. Jacobsen, Sulfide perovskites for solar energy conversion applications: computational screening
and synthesis of the selected compound LaYS3, [Energy](https://doi.org/10.1039/C7EE02702H)
Environ. [Sci.](https://doi.org/10.1039/C7EE02702H) **10**, 2579 (2017).

[21] A. Crovetto, R. Nielsen, M. Pandey, L. Watts, J. G.

Labram, M. Geisler, N. Stenger, K. W. Jacobsen,
O. Hansen, B. Seger, I. Chorkendorff, and P. C. K. Vesborg, Shining Light on Sulfide Perovskites: LaYS3 Material Properties and Solar Cells, Chem. [Mater.](https://doi.org/10.1021/acs.chemmater.9b00478) **31**, 3359
[(2019).](https://doi.org/10.1021/acs.chemmater.9b00478)

[22] H. Zhang, C. Ming, K. Yang, H. Zeng, S. Zhang, and

Y.-Y. Sun, Chalcogenide Perovskite YScS3 as a Potential
[p-Type Transparent Conducting Material, Chinese Phys.](https://doi.org/10.1088/0256-307X/37/9/097201)
Lett. **37**, 097201 (2020).

[23] P. Hohenberg and W. Kohn, Inhomogeneous Electron

Gas, Phys. Rev. **[136](https://doi.org/10.1103/PhysRev.136.B864)**, B864 (1964).

[24] W. Kohn and L. J. Sham, Self-Consistent Equations In
cluding Exchange and Correlation Effects, Phys. Rev.
**140**, [A1133](https://doi.org/10.1103/PhysRev.140.A1133) (1965).

[25] M. Gajdoš, K. Hummer, G. Kresse, J. Furthmüller, and

F. Bechstedt, Linear optical properties in the projectoraugmented wave methodology, Phys. Rev. [B](https://doi.org/10.1103/PhysRevB.73.045112) **73**, 045112
[(2006).](https://doi.org/10.1103/PhysRevB.73.045112)

[26] H. Jiang, P. Rinke, and M. Scheffler, Electronic proper
ties of lanthanide oxides from the _GW_ [perspective, Phys.](https://doi.org/10.1103/PhysRevB.86.125115)
Rev. B **86** [,](https://doi.org/10.1103/PhysRevB.86.125115) 125115 (2012).

[27] F. Fuchs, C. Rödl, A. Schleife, and F. Bechstedt, Efficient

_O_ ( _N_ <sup>2</sup> ) approach to solve the Bethe-Salpeter equation for
excitonic bound states, Phys. Rev. B **[78](https://doi.org/10.1103/PhysRevB.78.085103)**, 085103 (2008).

[28] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized

Gradient Approximation Made Simple, Phys. [Rev.](https://doi.org/10.1103/PhysRevLett.77.3865) Lett.
**77**, [3865](https://doi.org/10.1103/PhysRevLett.77.3865) (1996).

[29] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vy
drov, G. E. Scuseria, L. A. Constantin, X. Zhou, and
K. Burke, Restoring the Density-Gradient Expansion for
Exchange in Solids and Surfaces, Phys. Rev. Lett. **100**,
[136406](https://doi.org/10.1103/PhysRevLett.100.136406) (2008).

[30] J. Heyd, G. E. Scuseria, and M. Ernzerhof, Hybrid func
[tionals based on a screened Coulomb potential, J. Chem.](https://doi.org/10.1063/1.1564060)
Phys. **[118](https://doi.org/10.1063/1.1564060)**, 8207 (2003).

[31] L. Hedin, New Method for Calculating the One-Particle

Green’s Function with Application to the Electron-Gas
Problem, Phys. Rev. **[139](https://doi.org/10.1103/PhysRev.139.A796)**, A796 (1965).

[32] M. S. Hybertsen and S. G. Louie, First-Principles Theory

of Quasiparticles: Calculation of Band Gaps in Semicon[ductors and Insulators, Phys. Rev. Lett.](https://doi.org/10.1103/PhysRevLett.55.1418) **55**, 1418 (1985).


[33] S. Albrecht, L. Reining, R. Del Sole, and G. Onida,

Ab Initio Calculation of Excitonic Effects in the Opti[cal Spectra of Semiconductors, Phys. Rev. Lett.](https://doi.org/10.1103/PhysRevLett.80.4510) **80**, 4510
[(1998).](https://doi.org/10.1103/PhysRevLett.80.4510)

[34] M. Rohlfing and S. G. Louie, Electron-Hole Excitations

in Semiconductors and Insulators, Phys. [Rev.](https://doi.org/10.1103/PhysRevLett.81.2312) Lett. **81**,
[2312](https://doi.org/10.1103/PhysRevLett.81.2312) (1998).

[35] H. Fröhlich, Electrons in lattice fields, Adv. [Phys.](https://doi.org/10.1080/00018735400101213) **3**, 325

[(1954).](https://doi.org/10.1080/00018735400101213)

[36] R. W. Hellwarth and I. Biaggio, Mobility of an electron in

a multimode polar lattice, Phys. Rev. B **[60](https://doi.org/10.1103/PhysRevB.60.299)**, 299 (1999).

[37] G. Kresse and J. Furthmüller, Efficient iterative schemes

for ab initio total-energy calculations using a plane-wave
basis set, Phys. Rev. B **[54](https://doi.org/10.1103/PhysRevB.54.11169)**, 11169 (1996).

[38] G. Kresse and J. Furthm¨ _u_ ller, Efficiency of Ab-initio To
tal Energy Calculations for Metals and Semiconductors
Using a Plane-wave Basis Set, Comput. [Mater. Sci.](https://doi.org/https://doi.org/10.1016/0927-0256%0x2896%0x2900008-0) **6**, 15
[(1996).](https://doi.org/https://doi.org/10.1016/0927-0256%0x2896%0x2900008-0)

[39] P. E. Blöchl, Projector augmented-wave method, [Phys.](https://doi.org/10.1103/PhysRevB.50.17953)

Rev. B **[50](https://doi.org/10.1103/PhysRevB.50.17953)**, 17953 (1994).

[40] K. Momma and F. Izumi, _VESTA3_ for three-dimensional

visualization of crystal, volumetric and morphology data,
J. Appl. [Crystallogr.](https://doi.org/10.1107/S0021889811038970) **44**, 1272 (2011).

[41] A. Togo, L. Chaput, T. Tadano, and I. Tanaka, Imple
mentation strategies in phonopy and phono3py, J. [Phys.](https://doi.org/10.1088/1361-648X/acd831)
Condens. [Matter](https://doi.org/10.1088/1361-648X/acd831) **35**, 353001 (2023).

[42] See Supplemental Material (SM) at [URL will be inserted

by publisher] for details of distortion parameters, decomposition energy, convex hull, phonon dispersion curves,
mechanical properties, electronic DOS, effect of spinorbit coupling on bandgap, orbital projected band structures, effective masses of charge carriers, convergence of
G0W0 and BSE calculations, exciton binding energy obtained using the Wannier-Mott model, calculation of single phonon angular frequency and polaron mobility parameters for rare-earth chalcogenide perovskites ABX3
(A = Y, La; B = Sc, Y; and X = S, Se).

[43] A. M. Ganose, A. J. Jackson, and D. O. Scanlon, sumo:

Command-line tools for plotting and analysis of periodic ab initio calculations, J. Open [Source](https://doi.org/10.21105/joss.00717) Softw. **3**, 717
[(2018).](https://doi.org/10.21105/joss.00717)

[44] V. Wang, N. Xu, J.-C. Liu, G. Tang, and W.-T. Geng,

VASPKIT: A user-friendly interface facilitating highthroughput computing and analysis using VASP code,
Comput. Phys. [Commun.](https://doi.org/https://doi.org/10.1016/j.cpc.2021.108033) **267**, 108033 (2021).

[45] A. Chakravorty, S. Adhikari, and P. Johari, Unlocking

the optoelectronic potential of AGeX3 (A = Ca, Sr, Ba;
X = S, Se): A sustainable alternative in chalcogenide
perovskites, J. Chem. Phys. **[163](https://doi.org/10.1063/5.0298915)**, 234708 (2025).

[46] F. Mouhat and F.-X. Coudert, Necessary and sufficient

elastic stability conditions in various crystal systems,
Phys. Rev. B **[90](https://doi.org/10.1103/PhysRevB.90.224104)**, 224104 (2014).

[47] Z.-j. Wu, E.-j. Zhao, H.-p. Xiang, X.-f. Hao, X.-j. Liu,

and J. Meng, Crystal structures and elastic properties of
superhard IrN2 and IrN3 [from first principles, Phys. Rev.](https://doi.org/10.1103/PhysRevB.76.054115)



13


B **76**, [054115](https://doi.org/10.1103/PhysRevB.76.054115) (2007).

[48] R. Hill, The Elastic Behaviour of a Crystalline Aggregate,

Proc. Phys. Soc. A **65**, 349 (1952).

[49] S. Pugh, XCII. Relations between the elastic moduli

and the plastic properties of polycrystalline pure metals, London, Edinburgh [Dublin](https://doi.org/10.1080/14786440808520496) Philos. Mag. J. Sci. **45**,
[823](https://doi.org/10.1080/14786440808520496) (1954).

[50] X. Liu, B. Xie, C. Duan, Z. Wang, B. Fan, K. Zhang,

B. Lin, F. J. M. Colberts, W. Ma, R. A. J. Janssen,
F. Huang, and Y. Cao, A high dielectric constant nonfullerene acceptor for efficient bulk-heterojunction organic solar cells, J. Mater. [Chem.](https://doi.org/10.1039/C7TA10136H) A **6**, 395 (2018).

[51] S. Adhikari and P. Johari, Theoretical insights into

monovalent-metal-cation transmutation effects on leadfree halide double perovskites for optoelectronic applications, Phys. Rev. [Mater.](https://doi.org/10.1103/PhysRevMaterials.7.075401) **7**, 075401 (2023).

[52] S. Adhikari and P. Johari, Capturing optoelectronic

properties of Cs2AgSbBr6 _−x_ Cl _x_ ( _x_ = 0 _−_ 6) double
perovskites using many-body perturbation theory, [Phys.](https://doi.org/10.1103/PhysRevB.110.014101)
Rev. B **[110](https://doi.org/10.1103/PhysRevB.110.014101)**, 014101 (2024).

[53] M. Bokdam, T. Sander, A. Stroppa, S. Picozzi, D. D.

Sarma, C. Franchini, and G. Kresse, Role of Polar
Phonons in the Photo Excited State of Metal Halide Perovskites, Sci. Rep. **6**, [28618](https://doi.org/10.1038/srep28618) (2016).

[54] M. R. Filip, J. B. Haber, and J. B. Neaton, Phonon

Screening of Excitons in Semiconductors: Halide Perovskites and Beyond, Phys. Rev. [Lett.](https://doi.org/10.1103/PhysRevLett.127.067401) **127**, 067401
[(2021).](https://doi.org/10.1103/PhysRevLett.127.067401)

[55] S. Adhikari, S. S. Padelkar, J. J. Jasieniak, A. N. Si
monov, and A. Alam, Harnessing Linear and Nonlinear
Optical Responses in Ferroelectric LaMoN3 for Enhanced
Photovoltaic Efficiency, Chem. Mater. **[38](https://doi.org/10.1021/acs.chemmater.6c00120)**, 6271 (2026).

[56] S. Adhikari and P. Johari, Unveiling the impact of triva
lent metal cation transmutation on Cs2AgM(III)Cl6 double perovskites using many-body perturbation theory,
Phys. Rev. B **[112](https://doi.org/10.1103/vld9-2knx)**, 195208 (2025).

[57] S. Adhikari, A. Chakravorty, and P. Johari, Optical

and polaronic properties of vacancy-ordered double perovskites: A first-principles investigation, Phys. [Rev.](https://doi.org/10.1103/yy3w-vmj1) B
**113**, [045204](https://doi.org/10.1103/yy3w-vmj1) (2026).

[58] J. M. Frost, Calculating polaron mobility in halide per
ovskites, Phys. Rev. B **[96](https://doi.org/10.1103/PhysRevB.96.195202)**, 195202 (2017).

[59] L. M. Herz, Charge-Carrier Mobilities in Metal Halide

Perovskites: Fundamental Mechanisms and Limits, [ACS](https://doi.org/10.1021/acsenergylett.7b00276)
Energy [Lett.](https://doi.org/10.1021/acsenergylett.7b00276) **2**, 1539 (2017).

[60] S. Adhikari and P. Johari, Probing Optoelectronic Prop
erties of Stable Vacancy-Ordered Double Perovskites: Insights from Many-Body Perturbation Theory, Adv. Theory Simul. **[8](https://doi.org/https://doi.org/10.1002/adts.202400921)**, 2400921 (2025).

[61] F. Giustino, Electron-phonon interactions from first prin
ciples, Rev. Mod. Phys. **[89](https://doi.org/10.1103/RevModPhys.89.015003)**, 015003 (2017).

[62] R. P. Feynman, Slow Electrons in a Polar Crystal, [Phys.](https://doi.org/10.1103/PhysRev.97.660)

Rev. **[97](https://doi.org/10.1103/PhysRev.97.660)**, 660 (1955).


