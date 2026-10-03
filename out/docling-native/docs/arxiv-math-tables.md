Rare-earth chalcogenide perovskites: A promising class of materials for optoelectronic

applications

Surajit Adhikari 1, ∗ and Priya Johari 1, †

1 Department of Physics, School of Natural Sciences,

Shiv Nadar Institution of Eminence, Greater Noida,

Gautam Buddha Nagar, Uttar Pradesh 201314, India

Chalcogenide perovskites have attracted significant attention for optoelectronic applications due

to their nontoxic composition, robust phase stability, and excellent optoelectronic properties. Among

them, rare-earth chalcogenide perovskites have recently emerged as promising candidates for next-

generation devices. However, their excitonic and polaronic properties remain largely unexplored

due to the high computational cost of accurate theoretical treatments. In this work, we present

a comprehensive first-principles investigation of excitonic dynamics and polaronic effects in a se-

ries of III-III rare-earth chalcogenide perovskites ABX3 (A = Y, La; B = Sc, Y; X = S, Se), along

with their structural stability and optoelectronic properties, using state-of-the-art density functional

theory in conjunction with many-body perturbation theory within the G0W0 and Bethe-Salpeter

equation (BSE) frameworks. All investigated compounds satisfy the dynamical and mechanical sta-

bility criteria, although several are thermodynamically metastable at 0 K and may require kinetic

stabilization and/or finite-temperature effects for experimental realization. They exhibit quasi-

particle band gaps in the range of 2.75-4.47 eV, and the BSE calculations reveal strong optical

absorption spanning the visible to ultraviolet regions. The computed excitonic properties indi-

cate intermediate-to-large exciton binding energies (0.148-0.517 eV), moderately localized exci-

tons, and strong electron-hole wavefunction overlap, indicative of favorable radiative recombination

characteristics and enhanced light-matter interaction. Furthermore, analysis based on the Fröhlich

model demonstrates intermediate-to-strong carrier-phonon coupling, with electron-phonon interac-

tions generally stronger than hole-phonon interactions. Notably, charge-separated polaronic states

are energetically less favorable than bound excitonic states in most compounds, with the exception

of La(Sc, Y)Se3, while hole polarons exhibit significantly higher mobilities (up to ∼ 40 cm 2 V-1 s-1 )

compared to electron polarons. Overall, rare-earth chalcogenide perovskites ABX3 exhibit a com-

pelling combination of structural stability, tunable optoelectronic properties, pronounced excitonic

effects, and favorable polaronic transport, positioning them as promising lead-free materials for

next-generation optoelectronic devices, including light-emitting devices and photodetectors.

I. INTRODUCTION:

Over the last decade, inorganic-organic halide per-

ovskites (IOHPs) have attracted extraordinary interest

owing to their outstanding electronic and optical char-

acteristics [1-4]. This intense research focus has led to

remarkable progress in perovskite solar cells, with the

power conversion efficiency (PCE) rising rapidly from

an initial value of 3.8% to a record 27% [1, 5]. How-

ever, despite these impressive achievements, significant

challenges remain. Most high-performance IOHPs are

lead (Pb)-based, giving rise to serious toxicity concerns.

Moreover, their practical applicability is hindered by

poor long-term stability, including degradation and ther-

mal and chemical instability associated with the organic

constituents [6, 7]. These limitations have motivated ex-

tensive efforts toward the development of environmen-

tally benign, stable perovskite alternatives, opening new

pathways for next-generation optoelectronic materials.

Recently, chalcogenide perovskites have emerged as a

novel class of functional materials. Owing to their high

∗ sa731@snu.edu.in

† priya.johari@snu.edu.in

structural stability, suitable band gaps, and excellent op-

toelectronic properties, several members of this family

have been identified as promising candidates for light-

absorbing and light-emitting applications [8-12]. Among

them, the II-IV chalcogenide perovskites with the gen-

eral formula ABX3 (where A = Ca, Sr, Ba; B = Ti, Zr,

Sn, Hf; and X = S, Se) are the most extensively stud-

ied to date [10, 11, 13-17]. Further diversification of this

materials family can be achieved by exploring alterna-

tive elemental combinations at the cationic sites. In this

context, the III-III chalcogenide perovskites, although

already synthesized, remain largely unexplored as func-

tional materials [18-21]. For optoelectronic applications,

access to a broader materials palette is highly advanta-

geous, as it enables precise tuning of critical parameters

such as band gaps, band alignments, and structural prop-

erties, including lattice constants required for epitaxial

growth. Consequently, the exploration of III-III chalco-

genide perovskites composed of environmentally benign,

non-toxic elements is highly desirable, as these materials

can effectively complement the existing family of II-IV

chalcogenide perovskites.

Recent studies on III-III chalcogenide perovskites have

unveiled promising opportunities for the design of sta-

ble and environmentally benign optoelectronic materi-

als. For instance, Zhang et al. theoretically predicted

arXiv:2608.15882v1 [cond-mat.mtrl-sci] 16 Aug 2026

2

the orthorhombic Pnma (No. 62) crystal structure of

YScS3, reporting an indirect G0W0 band gap of 3.16

eV [22]. Subsequently, through density functional the-

ory calculations, Zhang et al. not only predicted but

also experimentally synthesized a light-emitting III-III-

S3 perovskite, LaScS3, exhibiting a direct band gap of

2.62 eV [18]. Furthermore, they also reported the pre-

diction and experimental realization of the direct band

gap material LaScSe3, with a G0W0 band gap of 2.96

eV [19]. In addition, the P21/m crystal structure of the

LaYS3 perovskite has been both theoretically predicted

and experimentally synthesized, exhibiting an optimal

band gap of 2.0 eV, making it a promising wide band

gap photoabsorber for tandem solar energy conversion

devices [20, 21].

Most of the aforementioned studies have primarily fo-

cused on the electronic and optical properties of III-III

rare-earth chalcogenide perovskites. In contrast, their

excitonic and polaronic properties remain largely unex-

plored, despite their critical role in determining the per-

formance of optoelectronic devices. Excitonic effects gov-

ern fundamental processes such as light absorption, emis-

sion, and charge separation. In contrast, polaron forma-

tion, arising from carrier-phonon interactions, strongly

influences charge transport and carrier mobility [15-17].

A quantitative description of these properties, however,

is computationally demanding and has therefore received

limited attention. This gap highlights the need for a com-

prehensive investigation of excitonic and polaronic effects

in these compounds, which has not yet been achieved and

is addressed in the present work.

In this work, we undertake a systematic and compre-

hensive investigation of the structural stability, as well as

the electronic, optical, excitonic, and polaronic proper-

ties of III-III rare-earth chalcogenide perovskites ABX3

(A = Y, La; B = Sc, Y; X = S, Se) in the orthorhom-

bic Pnma phase, a widely observed and energetically

competitive distorted perovskite structure that provides

a consistent framework for comparative analysis. Our

study is based on first-principles calculations within the

frameworks of density functional theory (DFT) [23, 24],

density functional perturbation theory (DFPT) [25], and

many-body perturbation theory (MBPT) [26, 27]. Ini-

tially, the crystal structures are optimized using the

semilocal PBE [28] as well as PBEsol [29] exchange-

correlation (xc) functionals, and all compounds are found

to be both dynamically and mechanically stable. How-

ever, several are thermodynamically metastable at 0 K,

suggesting that their experimental realization may re-

quire kinetic stabilization and/or finite-temperature ef-

fects. Subsequently, the electronic properties are inves-

tigated using both the HSE06 hybrid xc functional [30]

and the G0W0@PBE approach [31, 32], revealing quasi-

particle band gaps in the range of 2.75-4.47 eV. Fol-

lowing that, the optical response is computed by solv-

ing the Bethe-Salpeter equation (BSE) [33, 34] on top

of G0W0@PBE, enabling the evaluation of the dielec-

tric function and exciton binding energies. The results

indicate that these perovskites exhibit intermediate-to-

high exciton binding energies, moderately localized exci-

tons, and strong electron-hole wavefunction overlap, sug-

gesting favorable radiative transitions and pronounced

light-matter interaction. Finally, we investigate the ef-

fects of carrier-phonon coupling and estimate the po-

laron mobility using the Fröhlich model [35] and the Hell-

warth polaron model [36]. The analysis reveals interme-

diate to strong carrier-phonon coupling, with electron-

phonon interactions being more pronounced than those

of holes, resulting in lower electron mobility and com-

paratively higher hole mobility. Overall, this work pro-

vides a comprehensive understanding of rare-earth ABX3

(A = Y, La; B = Sc, Y; X = S, Se) chalcogenide per-

ovskite compounds, highlighting their potential as lead-

free perovskites with promising optoelectronic properties

for next-generation devices.

II. COMPUTATIONAL DETAILS:

In this work, first-principles calculations were car-

ried out within the framework of density functional the-

ory (DFT) [23, 24], density functional perturbation the-

ory (DFPT) [25], and many-body perturbation theory

(MBPT) [26, 27], as implemented in the Vienna ab initio

Simulation Package (VASP) [37, 38]. The interaction be-

tween valence electrons and ionic cores was described us-

ing projector augmented-wave (PAW) pseudopotentials

[39]. Structural optimizations were carried out within

the generalized gradient approximation (GGA) using the

Perdew-Burke-Ernzerhof (PBE) [28] and the PBEsol [29]

exchange-correlation (xc) functionals. The inclusion of

PBEsol is motivated by its improved accuracy in de-

scribing equilibrium properties of solids, particularly lat-

tice constants and structural distortions, which are cru-

cial for reliably assessing dynamical stability and phonon

properties. A plane-wave cutoff energy of 400 eV was

employed, and the electronic self-consistent field conver-

gence criterion was set to 10-6 eV. All structures were

fully optimized until the Hellmann-Feynman forces on

each atom were less than 0.01 eV/Å. Brillouin zone in-

tegrations were carried out using a Γ-centered 7 × 7 × 5

k-point mesh. The optimized crystal structures were vi-

sualized using the VESTA package [40]. Phonon disper-

sion curves were calculated using DFPT as implemented

in the PHONOPY package [41], employing 2 × 2 × 2

supercells. To assess the functional dependence of the

dynamical stability, the phonon spectra were computed

for crystal structures relaxed using both the PBE and

PBEsol exchange-correlation functionals.

Electronic band structures were initially obtained us-

ing the PBE xc functional including spin-orbit coupling

(SOC), which was found to have a negligible impact

on the overall band dispersion. To achieve improved

accuracy in bandgap estimation, hybrid xc functional

calculations using HSE06 [30] and quasiparticle correc-

tions within the G0W0@PBE [31, 32] approach were per-

3

formed. A Γ-centered 3 × 3 × 2 k-point mesh was em-

ployed for the G0W0 calculations. This choice is justi-

fied by the demonstrated convergence of the quasiparti-

cle band gaps, while the use of denser k-point meshes

for the present 20-atom unit cells would incur a sub-

stantially higher computational cost and is therefore be-

yond the scope of the present work (for details, see Sec.

X of the SM [42]). The convergence of the quasipar-

ticle bandgap with respect to the number of unoccu-

pied bands (NBANDS), the plane-wave cutoff energy

(ENCUT), and the response-function cutoff energy (EN-

CUTGW) was carefully examined (for details, see Sec.

X of the SM [42]). Based on these convergence tests,

640 bands, a plane-wave cutoff energy of 400 eV, and a

response-function cutoff energy of 300 eV were adopted,

yielding quasiparticle bandgaps converged to within 0.05

eV. Carrier effective masses were calculated using the

SUMO code [43] via parabolic fitting near the band ex-

trema. Optical properties were further refined by solv-

ing the Bethe-Salpeter equation (BSE) [33, 34] on top of

G0W0@PBE, explicitly including electron-hole interac-

tions. The BSE kernel was constructed using 24 occupied

and 24 unoccupied bands, based on convergence tests (for

details, see Sec. XI of the SM [42]). Elastic and opti-

cal properties were post-processed using the VASPKIT

package [44], and the ionic contribution to the dielectric

constant was obtained from DFPT calculations.

III. RESULTS AND DISCUSSIONS:

In the present study, we conduct a comprehensive in-

vestigation of the optoelectronic properties of III-III rare-

earth chalcogenide perovskites ABX3 (A = Y, La; B =

Sc, Y; X = S, Se). The following sections provide an

in-depth analysis of their structural stability, electronic

structure, and transport characteristics, along with their

optical response, excitonic behavior, and polaronic ef-

fects. These results aim to establish a fundamental un-

derstanding of these materials and offer valuable insights

to guide future experimental studies.

FIG. 1. Crystal structures of rare-earth chalcogenide per-

ovskites (a) YScX3, (b) LaScX3, and (c) LaYX3, respectively,

where X = S, Se.

A. Structural Properties:

Figure 1 illustrates the orthorhombic crystal structures

of rare-earth chalcogenide perovskites ABX3 (A = Y, La;

B = Sc, Y; and X = S, Se), crystallizing in the Pnma

space group (No. 62). Owing to the +3 valency of both

A- and B-site cations, these materials are categorized

as III-III chalcogenide perovskites. The unit cell con-

tains four formula units (20 atoms), comprising 4 A-site

cations (Y or La), 4 B-site cations (Sc or Y), and 12

chalcogen anion atoms (S or Se). In this structure, the A-

site cations exhibit 12-fold coordination, forming cuboc-

tahedral environments with the surrounding chalcogen

atoms. In contrast, the B-site cations are 6-fold coor-

dinated, giving rise to corner-sharing distorted [BX6] 9-

octahedra. These octahedra are both tilted and dis-

torted, leading to the characteristic orthorhombic sym-

metry of the Pnma phase [12]. In this study, we report

for the first time the Pnma phase of YScSe3, LaYS3,

and LaYSe3 compounds. The lattice parameters of the

optimized structures are calculated using both PBE and

PBEsol xc functionals and are summarized in Table I.

It is found that the lattice parameters of LaScSe3 are

in good agreement with the available experimental re-

sults (a = 6.77 Å, b = 7.53 Å, and c = 10.00 Å [19]).

Moreover, the PBE functional slightly overestimates the

lattice parameters, while PBEsol slightly underestimates

them, with both deviations being of comparable magni-

tude. This indicates that both functionals yield similar

accuracy, despite exhibiting opposite systematic devia-

tions. In addition, the octahedral distortion parameters,

including the average bond length, polyhedral volume,

bond angle variance, and bond-length distortion index,

for the BX6 octahedra in these chalcogenide perovskites

are computed using both functionals and presented in

Table S1 (for details, see Sec. I of the SM [42]).

To assess the thermodynamic stability against decom-

position, we calculated the decomposition enthalpy ac-

cording to

ABX3 → 1/2 A2X3 + 1/2 B2X3

(1)

for these III-III-X3 compounds that pass the phase sta-

bility criteria (for details, see Sec. II of the SM [42]).

The decomposition enthalpy (∆HD) of these compounds

is evaluated using both PBE and PBEsol xc functionals

and is tabulated in Table I. The LaScX3 (X = S, Se)

compounds exhibit positive ∆HD values with both func-

tionals, indicating thermodynamic stability with respect

to the considered decomposition pathway. In contrast,

the remaining compounds exhibit negative ∆HD values,

indicating thermodynamic metastability at 0 K with re-

spect to this decomposition pathway. The only excep-

tion is YScS3, which yields a positive ∆HD when us-

ing the PBEsol functional. Nevertheless, decomposition

enthalpy based on a single reaction does not constitute

a complete thermodynamic stability criterion, since al-

ternative competing phases and decomposition pathways

<!-- image -->

4

TABLE I. Calculated lattice parameters and decomposition energies (∆HD) of ABX3 (A = Y, La; B = Sc, Y; and X = S, Se)

rare-earth chalcogenide perovskites using the PBE and PBEsol xc functional, respectively (PBEsol values in bold).

Configurations

Lattice parameters (Å)

∆HD

a

b

c

(meV/atom)

YScS3

6.39 (6.27) 7.02 (6.97) 9.55 (9.37)

-9.1 (5.0)

YScSe3

6.67 (6.54) 7.35 (7.29) 10.00 (9.79)

-28.9 (-6.8)

LaScS3

6.59 (6.46) 7.21 (7.16) 9.65 (9.51)

26.0 (26.1)

LaScSe3

6.83 (6.68) 7.58 (7.51) 10.08 (9.92)

13.5 (8.8)

LaYS3

6.81 (6.70) 7.42 (7.37) 10.06 (9.88)

-2.7 (-19.9)

LaYSe3

7.04 (6.90) 7.78 (7.72) 10.48 (10.26)

-15.2 (-25)

may exist. A rigorous assessment therefore requires con-

struction of the convex-hull phase diagram, which com-

pares the energy of a compound against all known com-

peting phases within the corresponding chemical space.

Compounds lying on the convex hull are thermodynami-

cally stable, whereas those with positive energy above the

hull (Ehull) are metastable with respect to decomposition

into a combination of lower-energy phases.

To directly address this limitation, we constructed the

convex-hull phase diagrams for each A-B-X (A = Y,

La; B = Sc, Y; and X = S, Se) chemical space by in-

corporating all relevant competing binary and ternary

phases at the same DFT level. The calculated Ehull val-

ues are summarized in Table S3, while the corresponding

convex-hull diagrams are presented in Figure S1 (for de-

tails, see Sec. III of the SM [42]). The results show that

LaScX3 (X = S, Se) lie on the convex hull with Ehull =

0, confirming their thermodynamic stability at 0 K. The

remaining compounds possess finite positive Ehull values

(0.009-0.029 eV), indicating metastability with respect

to competing equilibrium phases. It is important to note,

however, that a positive energy above the hull does not

necessarily preclude experimental realization. Numerous

experimentally synthesized materials are known to exist

as metastable phases because finite-temperature vibra-

tional and configurational entropy, kinetic barriers, and

non-equilibrium synthesis routes can effectively stabilize

compounds that are slightly above the convex hull [45].

Consequently, the above-hull compounds identified here

should be regarded as metastable candidates that may

still be experimentally accessible under suitable synthe-

sis conditions rather than as equilibrium-stable phases.

However, thermodynamic stability alone is insufficient to

ensure stability of these materials; therefore, dynamical

and mechanical stability are also examined.

The dynamical stability of the investigated perovskites

serves as a crucial indicator of their structural integrity

and suitability for functional applications. It is evaluated

through phonon dispersion relations, which describe the

vibrational behavior of atoms in the crystal lattice. For

a dynamically stable system at 0 K, all phonon frequen-

cies are required to be real and positive across the entire

Brillouin zone; the occurrence of imaginary (negative)

frequencies signifies possible structural instabilities. To

assess this, self-consistent phonon calculations are per-

formed within the DFPT framework using the structures

relaxed with both PBE and PBEsol xc functionals. The

computed phonon dispersion curves of ABX3 (A = Y,

La; B = Sc, Y; and X = S, Se), obtained using struc-

tures relaxed with the PBE and PBEsol xc functionals,

are presented in Figs. S2 and 2, respectively. Within

the PBE functional, YScS3, LaScS3, LaYS3, and LaYSe3

are dynamically stable at 0 K, as confirmed by the ab-

sence of imaginary phonon modes, whereas (Y, La)ScSe3

shows dynamical instabilities, as indicated by the pres-

ence of imaginary modes. Specifically, YScSe3 shows a

maximum imaginary frequency of -0.333 THz at the Γ

point, while LaScSe3 exhibits imaginary frequencies of

approximately -0.189 THz along the Γ-X direction and

-0.349 THz at the U point. The relatively small magni-

tudes of these imaginary frequencies suggest the presence

of soft lattice instabilities rather than pronounced struc-

tural instabilities. This interpretation is further sup-

ported by the experimental realization of LaScSe3, in-

dicating that these weak instabilities are unlikely to pre-

clude its synthesis and may instead reflect the sensitivity

of the lattice dynamics to the equilibrium structural pa-

rameters [19]. In contrast, phonon calculations based on

the PBEsol-relaxed structures show no imaginary phonon

modes throughout the Brillouin zone for any of the inves-

tigated compounds, indicating dynamical stability within

the PBEsol framework. Together with the PBE results,

these findings suggest that the lattice dynamics of some

compounds are sensitive to small variations in the equi-

librium lattice parameters and are therefore dependent

on the choice of exchange-correlation functional.

Beyond the thermodynamic and dynamical stability

discussed above, the mechanical stability and corre-

sponding elastic properties of ABX3 (A = Y, La; B = Sc,

Y; X = S, Se) chalcogenide perovskites are further exam-

ined. It is well known that the suitability of a material

for practical device applications is strongly influenced by

its elastic behavior. The second-order elastic constants

(Cij) are calculated using the energy-strain method [46],

from which the relevant elastic properties are derived (for

details, see Sec. V of the SM [42]). Owing to the or-

thorhombic symmetry of all considered compounds, nine

independent elastic constants (C11, C22, C33, C44, C55,

C66, C12, C13, and C23) are sufficient to describe their

mechanical stability and elastic behavior. The calculated

Cij values, listed in Table S4, satisfy the Born stability

criteria [46], thereby confirming the excellent mechanical

5

stability of these orthorhombic chalcogenide perovskites.

Further, the bulk modulus (B), shear modulus (G),

Young's modulus (Y ), and Poisson's ratio (ν) are evalu-

ated within the Voigt-Reuss-Hill approximation [47, 48]

and are summarized in Table S4. The relatively larger

values of B compared to G indicate that the investigated

chalcogenide perovskites exhibit greater resistance to vol-

ume change than to shear deformation. The compara-

tively lower values of G and Y further suggest that these

materials possess a certain degree of mechanical flexi-

bility. To assess the ductile or brittle nature of these

systems, we employ Pugh's criterion based on the B/G

ratio [49], along with Poisson's ratio (ν). The obtained

values of B/G &gt; 1.75 and ν &gt; 0.26 consistently indicate

that all the compounds exhibit ductile behavior. These

characteristics suggest that the investigated materials are

mechanically robust yet sufficiently flexible for potential

device applications.

Overall, the synthesizability of these III-III chalco-

genide perovskites is established by the combined as-

sessment of thermodynamic, dynamical, and mechanical

stability. Notably, LaScX3 (X = S, Se), which has al-

ready been experimentally synthesized [18, 19], is found

to be thermodynamically stable, consistent with its pos-

itive decomposition enthalpy. In contrast, the remain-

ing compounds are metastable with respect to decompo-

sition. Nevertheless, the absence of imaginary phonon

modes (within PBEsol) and the satisfaction of mechani-

cal stability criteria confirm their dynamical and mechan-

ical stability. These results suggest that, despite thermo-

dynamic metastability, the compounds are likely experi-

mentally accessible through kinetic stabilization or finite-

temperature effects, with LaScX3 serving as a benchmark

system validating the reliability of the present approach.

FIG. 2. Phonon dispersion curves of the rare-earth chalco-

genide perovskites (a) YScS3, (b) YScSe3, (c) LaScS3, (d)

LaScSe3, (e) LaYS3, and (f) LaYSe3, computed using the

DFPT method based on PBEsol-relaxed structures.

B. Electronic properties:

Following the assessment of structural stability, the

electronic properties, such as the band structure and par-

tial density of states (PDOS) of rare-earth chalcogenide

perovskites ABX3 (A = Y, La; B = Sc, Y; and X =

S, Se) are evaluated to gain fundamental insight into

their suitability for optoelectronic applications. At first,

the electronic band structures of these chalcogenide per-

ovskites are calculated using the semilocal GGA-PBE xc

functional, both with and without inclusion of spin-orbit

coupling (SOC). The GGA-PBE xc functional is found to

underestimate the band gaps due to the self-interaction

error of electrons (see Table II). Furthermore, SOC has a

negligible effect on the band gap (see Table S5 of the SM

[42]), as expected for chalcogenide perovskites [15-17].

Subsequently, the band gaps are computed more ac-

curately using the hybrid HSE06 xc functional and the

many-body perturbation theory (MBPT)-based GW ap-

proach, specifically at the G0W0@PBE level. Figure 3

presents the band structures of these compounds, cal-

culated using the hybrid HSE06 functional. Our calcu-

lated electronic band structures explicitly demonstrate

that YScX3 (X = S, Se) are indirect band gap materials.

In these compounds, the valence band maximum (VBM)

is located at the Γ-point, whereas the conduction band

minimum (CBM) occurs at the S-point in the Brillouin

zone [see Fig. 3(a)-(b)]. This spatial separation of the

band extrema confirms the indirect nature of the funda-

mental band gap, implying that optical transitions near

the band edge are phonon-assisted. In contrast, all other

compounds investigated in this study exhibit direct band

gaps. For these systems, both the VBM and CBM are

located at the same high-symmetry k-point, specifically

at the Γ-point [see Fig. 3(c)-(f)]. As a result, the fun-

damental electronic transition is momentum-conserving,

leading to a stronger optical absorption onset compared

to the indirect-gap counterparts.

The band gaps of these compounds, as calculated us-

ing the HSE06 functional and the G0W0@PBE approach,

are summarized in Table II. The HSE06 band gaps of

these chalcogenide perovskites are found to lie in the

range of 2.17-3.45 eV, whereas the G0W0@PBE band

gaps are systematically larger, spanning 2.75-4.47 eV.

This trend reflects the well-known tendency of many-

body perturbation theory within the GW approximation

to yield improved quasiparticle energies by explicitly ac-

counting for electron-electron interactions, thereby cor-

recting the band gap underestimation inherent to stan-

dard and hybrid density functional approaches. Impor-

tantly, the G0W0@PBE results obtained in this work are

in good agreement with previously reported theoretical

studies [19, 22], confirming the reliability of the present

computational framework. The absence of exact quanti-

tative agreement with previous reports can be attributed

to the sensitivity of G0W0 calculations to the choice of

starting functional, convergence parameters, and struc-

tural inputs. For the benchmark compound LaScS3, the

experimentally measured band gap (2.62 eV) is closer to

the HSE06 value (2.80 eV) than to the G0W0@PBE value

(3.72 eV) [18]. This discrepancy is likely attributable to

the inherent starting-point dependence of the single-shot

<!-- image -->

6

G0W0 approximation, the absence of self-consistency in

the GW calculations, residual convergence limitations,

and the neglect of finite-temperature and excitonic ef-

fects. Although G0W0 calculations based on an HSE06

starting point or self-consistent GW schemes could fur-

ther reduce the starting-point dependence and improve

the quantitative accuracy of the quasiparticle energies,

such calculations are computationally prohibitive for the

large unit cells considered here. Nevertheless, the good

agreement with previous theoretical studies supports the

reliability of the present G0W0 results. Overall, the cal-

culated band gaps place these chalcogenide perovskites

in the visible-to-ultraviolet wide-band-gap regime, high-

lighting their potential for optoelectronic applications.

Direct-gap compounds favor efficient light absorption and

emission (e.g., LEDs), whereas indirect-gap systems are

advantageous for longer carrier lifetime-based applica-

tions such as photodetectors and photocatalysis.

To gain deeper insight into the electronic structure, the

density of states (DOS) is calculated using the HSE06 xc

functional, as shown in Fig. S3 of the SM [42]. For

YScS3, the VBM is predominantly derived from S-3p or-

bitals, whereas the CBM is mainly contributed by Sc-3d

orbitals. As expected, the CBM also exhibits hybridiza-

tion between Y-4d and Sc-3d states. Similarly, in YScSe3,

the VBM is primarily composed of Se-4p orbitals, while

the CBM shows a noticeable downward shift due to en-

hanced hybridization between Se-4p and transition-metal

d states, leading to the observed reduction in the band

gap. In contrast, for LaScX3 (X= S, Se), the CBM arises

from hybridized La-5d and Sc-3d states. The direct-to-

indirect band gap transition primarily arises from the in-

terplay between d-d orbital hybridization and structural

distortions. In YScX3, stronger Y-4d-Sc-3d coupling

and larger octahedral tilting stabilize the CBM at the

S-point, resulting in an indirect gap. In contrast, weaker

La-5d-Sc-3d coupling and reduced tilting in LaScX3 shift

the conduction band upward at S-point and favor a min-

imum at Γ-point, leading to a direct band gap [18]. Fur-

thermore, upon replacing Sc with Y (LaScX3 → LaYX3),

the direct band gap nature is preserved, while the band

gap increases due to the higher energy and modified dis-

persion of Y-4d states relative to Sc-3d states, resulting

in an upward shift of the CBM in LaYX3.

To further substantiate the above interpretation, we

have included orbital-projected band structures near the

VBM and CBM in Fig. S4 of the SM [42]. These re-

sults explicitly identify the orbital character of the band-

edge states and confirm that the evolution from a direct

to an indirect band gap is governed by changes in the

hybridization between Y-4d/La-5d and Sc-3d orbitals,

together with the accompanying structural distortions.

The orbital-projected bands provide direct microscopic

evidence for the orbital interactions responsible for the

shift of the CBM between the Γ and S points, thereby

supporting the mechanism proposed from the DOS anal-

ysis.

FIG. 3. Electronic band structures of the rare-earth chalco-

genide perovskites (a) YScS3, (b) YScSe3, (c) LaScS3, (d)

LaScSe3, (e) LaYS3, and (f) LaYSe3, calculated using the

HSE06 xc functional. The Fermi level is set to be zero and

marked by the dashed line.

To gain insight into charge-carrier transport, we fur-

ther calculate the effective masses of electrons (m∗e ) and

holes (m∗h ) for all compounds by fitting the E-k disper-

sion obtained from PBE band structures using the for-

mula, m∗ = ℏ2 [∂ 2E(k)/∂k2 ]-1 , and the results are sum-

marized in Table II. For the direct band gap compounds,

the effective masses are evaluated as the harmonic mean

along the Γ-X, Γ-Y, and Γ-Z directions, with results

listed in Table S6 of the SM [42]. In contrast, for YScX3

(X = S, Se), the electron effective masses are obtained

by averaging along the S-X and S-Y directions, consis-

tent with the location of the CBM. From Table II, it is

evident that m∗e is significantly larger than m∗h in these

compounds, indicating that holes are expected to possess

higher mobility than electrons. This suggests that these

materials are more favorable for p-type transport.

C. Optical Properties:

Beyond the electronic structure, the optical response

provides key insight into the suitability of these materials

for optoelectronic applications. In this work, the optical

response is accurately described by capturing many-body

effects through the Bethe-Salpeter equation (BSE) built

upon G0W0@PBE quasiparticle energies, ensuring a re-

liable treatment of excitonic contributions to the optical

spectra. In this framework, GW calculations determine

the fundamental bandgap, which is directly comparable

to photoelectron (PES) and inverse photoelectron spec-

troscopy (IPES) [31, 32], whereas BSE yields the optical

bandgap consistent with experimental absorption mea-

surements [33, 34].

To evaluate the optical response of ABX3 (A = Y, La;

B = Sc, Y; and X = S, Se), we focus on the frequency-

dependent complex dielectric function, ε(ω) = [Re(ε)]

+ i[Im(ε)], which governs the interaction of electromag-

netic radiation with the material. The imaginary part,

<!-- image -->

7

TABLE II. Bandgap (in eV) of ABX3 (A = Y, La; B = Sc, Y; and X = S, Se) rare-earth chalcogenide perovskites calculated

using different methods as well as computed average effective mass of electron (m∗e) and hole (m∗h). Here, i, d, t, and e

represent indirect, direct, theoretical, and experimental bandgaps, respectively. All values of the effective mass are in terms of

free-electron mass (m0).

Configurations PBE

HSE06 G0W0@PBE Previous Work m∗e m∗h

YScS3

1.76i (1.88d ) 2.75i (2.96d ) 3.49i (3.75d ) 3.16t (G0W0) [22] 1.545 0.494

YScSe3

1.30i (1.43d ) 2.17i (2.39d ) 2.75i (3.00d )

1.622 0.375

LaScS3

1.69

2.80

3.72

2.62e [18]

0.916 0.457

LaScSe3

1.27

2.27

2.94

2.96t (G0W0) [19] 0.851 0.350

LaYS3

2.25

3.45

4.47

1.255 0.542

LaYSe3

1.79

2.87

3.70

1.180 0.419

[Im(ε)], describes interband optical absorption arising

from electronic transitions between occupied and unoc-

cupied states and is directly related to the absorption

spectrum and optical bandgap. In contrast, the real

part, [Re(ε)], represents the dispersive response and de-

termines key optical properties such as dielectric screen-

ing, refractive index, and polarization behavior. Notably,

the static limit ε∞ provides insight into the screening

strength, which influences excitonic effects and charge-

carrier interactions. Together, these components offer

a comprehensive description of light-matter interaction

and are essential for assessing the suitability of these ma-

terials for optoelectronic applications.

FIG. 4. Spatially averaged real [Re(ε)] and imaginary part

[Im(ε)] of the electronic dielectric function for rare-earth

chalcogenide perovskites (a) YScS3, (b) YScSe3, (c) LaScS3,

(d) LaScSe3, (e) LaYS3, and (f) LaYSe3, respectively, calcu-

lated using the BSE@G0W0@PBE method. Peaks with cyan

color represent the oscillator strength.

The imaginary part of the dielectric function, [Im(ε)],

for ABX3 (A = Y, La; B = Sc, Y; and X = S, Se)

perovskite compounds exhibits broad spectral coverage

from the visible to the ultraviolet region, as shown in

Figure 4. This response reflects the interplay of band

structure, momentum selection rules, and electron-hole

interactions, where direct gaps enable sharp absorption

edges, indirect gaps lead to phonon-assisted onset, and

excitonic effects renormalize the optical gap and enhance

near-edge spectral features. The oscillator strength spec-

tra further identify the optically allowed excitonic tran-

sitions. Strong oscillator strength indicates a large tran-

sition dipole moment and efficient light-matter coupling,

giving rise to intense absorption features, whereas weak

or nearly vanishing oscillator strength corresponds to op-

tically inactive (dark) excitonic states that contribute

negligibly to the optical response. The energy eigen-

value of the first optically active (bright) exciton, which

defines the optical band gap (Eo), spans 2.77-3.96 eV

across the series, highlighting the substantial influence of

excitonic effects. Since the lowest excitonic state is opti-

cally active for all compounds investigated in this work,

its eigenvalue directly corresponds to the optical absorp-

tion onset. Notably, for LaScS3, the experimentally mea-

sured optical gap is 2.62 eV [18], whereas the present

BSE optical gap value is 3.40 eV. This discrepancy can

be attributed to the idealized nature of the calculations,

which neglect temperature effects, carrier-phonon renor-

malization, and defect-induced band tailing that typi-

cally reduce the measured absorption onset. Overall,

the strong and compositionally tunable optical absorp-

tion highlights the potential of these materials for opto-

electronic applications, including photodetectors, light-

emitting diodes, and laser devices.

In addition to the optical spectra, the electronic dielec-

tric constant (ε∞), defined as the zero-frequency limit

of the real part of the dielectric function, is evaluated

as a key descriptor of the optoelectronic response. This

quantity governs the screening of Coulomb interactions,

where larger ε∞ values reduce electron-hole attraction

and suppress carrier recombination, thereby, enhancing

device performance [50]. The calculated ε∞ values for

ABX3 (A = Y, La; B = Sc, Y; and X = S, Se), obtained

within the BSE framework, span the range of 2.26-5.88,

as summarized in Table S13 of the SM [42]. These di-

electric constants also serve as essential input parameters

for evaluating excitonic and polaronic properties, as dis-

cussed in the following sections.

D. Excitonic Properties:

In addition to the aforementioned electronic and opti-

cal properties, excitonic properties such as, exciton bind-

ing energy (EB), excitonic temperature (Texc), exciton

radius (rexc), and the probability of the wavefunction for

the electron-hole (e-h) pair at zero separation (|ϕn(0)|2 ),

<!-- image -->

8

play a crucial role in determining the performance of

optoelectronic devices. An exciton is a Coulomb-bound

e - h pair formed upon optical excitation, which renor-

malizes the optical gap and governs near-edge absorption

features. The exciton binding energy (EB) quantifies the

energy required to dissociate the exciton into free charge

carriers, i.e., an electron in the conduction band and a

hole in the valence band. A lower EB facilitates efficient

charge separation at or near room temperature, thereby

promoting enhanced photoelectric conversion efficiency,

particularly in photovoltaic applications. In contrast,

a higher EB implies stronger Coulomb interaction be-

tween electrons and holes, leading to more stable and

tightly bound excitons. While this can hinder efficient

charge separation and reduce photocurrent generation in

photovoltaic devices, it is advantageous for applications

that rely on strong radiative recombination, such as light-

emitting diodes and laser devices, where enhanced exci-

tonic stability can improve emission efficiency.

The exciton binding energy (EB) is obtained from first-

principles Bethe-Salpeter equation (BSE) calculations as,

EB = Edir

g - Eo, where Edir

g is the direct quasiparti-

cle band gap from G0W0@PBE and Eo denotes the en-

ergy eigenvalue of the first optically active (bright) exci-

tonic state computed within BSE@G0W0@PBE [51, 52].

As summarized in Table III, the calculated EB val-

ues for these chalcogenide perovskites decrease from S-

to Se-containing counterparts and lie in the range of

0.148-0.517 eV. Such moderately large binding ener-

gies indicate pronounced excitonic effects arising from

reduced dielectric screening and enhanced electron-hole

interactions, which are favorable for efficient radiative re-

combination in light-emitting and photodetection appli-

cations. Notably, LaYX3 exhibits a clear deviation from

the overall trend, showing comparatively enhanced exci-

tonic binding. This behavior can be attributed to its re-

duced electronic dielectric screening (see Figure 4), which

strengthens the Coulomb interaction between electrons

and holes. While the absolute values of EB may be some-

what overestimated due to the use of G0W0@PBE and

the neglect of temperature- and phonon-induced screen-

ing effects, the overall trends and qualitative description

of excitonic behavior remain robust. In particular, the

systematic variation across the series and the identifica-

tion of intermediate excitonic character are expected to

be reliable, as they are primarily governed by dielectric

screening and carrier effective masses captured within the

present framework.

It is worth noting that when EB significantly exceeds

the longitudinal optical (LO) phonon energy (ℏωLO), di-

electric screening is dominated by the electronic contribu-

tion, while the ionic component becomes negligible. Con-

sequently, EB remains largely unaffected by lattice po-

larization effects [53]. As shown in Tables III and V, the

condition EB ≫ ℏωLO is satisfied for the present com-

pounds, justifying the neglect of ionic screening. This

behavior is further corroborated by estimates based on

the hydrogenic Wannier-Mott model (for details, see Sec.

XII of the SM [42]). From Table S13, it is observed that

the upper bounds (EBu = 0.102-1.009 eV) for these com-

pounds closely match the EB values obtained using the

BSE@G0W0@PBE method, whereas the lower bounds

(EBl) are significantly smaller. This indicates that the

ionic contribution to the dielectric constant is negligible,

leading to εeff → ε∞. Therefore, at high frequencies,

dielectric screening is governed primarily by electronic

effects.

TABLE III. Calculated exciton parameters of ABX3 (A =

Y, La; B = Sc, Y; and X = S, Se) rare-earth chalcogenide

perovskites.

Configurations Edir

g Eo EB Texc rexc

|ϕn(0)|2

(eV) (eV) (eV) (K) (nm) (10 27 m-3 )

YScS3

3.747 3.424 0.323 3745 0.69

0.97

YScSe3

3.005 2.772 0.233 2701 1.20

0.19

LaScS3

3.721 3.397 0.324 3757 0.58

1.61

LaScSe3 2.941 2.793 0.148 1716 0.86

0.50

LaYS3

4.472 3.955 0.517 5994 0.32

10.14

LaYSe3

3.701 3.286 0.415 4812 0.43

3.87

Further, the calculation of EB within the standard

first-principles BSE framework includes only electronic

screening in the e-h interaction kernel and neglects lat-

tice (phonon) contributions. Such a static treatment can

be inadequate for polar materials, where carrier-phonon

coupling plays a crucial role in screening Coulomb in-

teractions. To address this limitation, we adopt the ap-

proach of Filip et al. [54, 55], who introduced a correction

of phonon-screening under the assumption of isotropic

and parabolic band dispersion. The correction to the

exciton binding energy is given by

∆Eph

B = -2ωLO

(1 - ε∞

εs

) √1+ωLO/EB +3

(1 + √1 + ωLO/EB

)3 ,

(2)

where ωLO denotes the characteristic longitudinal op-

tical phonon frequency, and ε∞ and εs represent the elec-

tronic and static dielectric constants, respectively. The

effective ωLO is evaluated using the thermal "B" ap-

proach developed by Hellwarth et al. [36], which ac-

counts for the spectral contributions of multiple phonon

branches through an appropriate averaging scheme (for

details, see Sec. XIII of the SM [42]). Table IV shows

that phonon screening reduces EB by 3.20-9.26%, in-

dicating that the overall reduction is not substantial in

these rare-earth chalcogenide perovskites. After incor-

porating the phonon-screening correction, the renormal-

ized exciton binding energy (E′B ) spans 0.134-0.498 eV.

This behavior suggests that the electronic contribution

to dielectric screening dominates over the ionic (phonon-

mediated) component in these systems.

9

TABLE IV. Calculated exciton binding energy (EB), phonon

screening corrections (∆Eph

B ), percentage of phonon screening

contribution to the reduction of exciton binding energy (%),

and corrected values of exciton binding energy (E′B) for ABX3

(A = Y, La; B = Sc, Y; and X = S, Se) rare-earth chalcogenide

perovskites.

Configurations EB ∆Eph

B Reduction of EB E′B

(eV) (meV)

(%)

(eV)

YScS3

0.323 -19.20

5.94

0.304

YScSe3

0.233 -13.55

5.82

0.219

LaScS3

0.324 -19.41

5.99

0.305

LaScSe3 0.148 -13.70

9.26

0.134

LaYS3

0.517 -18.67

3.61

0.498

LaYSe3

0.415 -13.29

3.20

0.402

Next, several additional excitonic parameters, includ-

ing the excitonic temperature (Texc), exciton radius

(rexc), and the probability of the wavefunction for the

e - h pair at zero separation (|ϕn(0)|2 ), are evaluated

and summarized in Table III. The excitonic temperature

(Texc) serves as a useful metric to quantify the thermal

stability of bound e-h pairs in semiconductors and insu-

lators. It is defined by relating the exciton binding energy

(EB) to thermal energy via the Boltzmann constant (kB)

as Texc = EB/kB. Physically, Texc represents the charac-

teristic temperature above which excitons are thermally

ionized into free carriers. When Texc significantly exceeds

room temperature (∼ 300 K), excitons are expected to

remain stable under ambient conditions, giving rise to

pronounced excitonic features in optical absorption and

emission spectra. Conversely, if Texc is comparable to or

lower than room temperature, thermal dissociation be-

comes efficient, and the optoelectronic response is domi-

nated by free carriers. In our study, the rare-earth chalco-

genide perovskite compounds exhibit high excitonic tem-

peratures (1716-5994 K), reflecting strongly bound ex-

citons that remain thermally stable far above room tem-

perature and yield pronounced excitonic effects in their

optical response. Such robust excitonic stability is advan-

tageous for optoelectronic applications, particularly in

light-emitting devices and photodetectors, where strong

light-matter interaction and efficient exciton generation

are desirable.

The exciton radius (rexc) is evaluated within the hy-

drogenic Wannier-Mott model as [56, 57]:

rexc = m0

µ∗dir

εeffn2 rRy,

(3)

where µ∗dir is the reduced effective mass at the direct

band edge, εeff denotes the effective dielectric constant,

n is the exciton energy level, and rRy is the Bohr radius

(0.0529 nm). In this work, the high-frequency dielec-

tric constant (ε∞) is employed as the effective dielectric

screening (εeff), and n = 1 is considered, correspond-

ing to the ground-state exciton and yielding the mini-

mum exciton radius. The exciton radius serves as a key

descriptor of the spatial extent of the e - h pair, dis-

tinguishing between localized and delocalized excitonic

states. In our study, the obtained rexc values (∼ 3.2-12

Å) indicate moderately to strongly bound excitons with

spatial extents ranging from near unit-cell localization to

a few lattice constants, suggesting an intermediate char-

acter approaching the Wannier-Frenkel crossover regime.

Such excitons promote strong light-matter interaction,

highlighting the potential of these materials for opto-

electronic applications. Within this framework, LaYX3

stands out by exhibiting a comparatively smaller exciton

radius, reflecting enhanced localization of the electron-

hole pair. This behavior originates from its relatively

weak electronic screening, which strengthens Coulomb

interactions and stabilizes more tightly bound excitonic

states.

To qualitatively assess the radiative recombination

propensity of excitons, we evaluate the probability den-

sity of the e -h pair at zero separation, |ϕn(0)|2 , which

is given by [56, 57]:

|ϕn(0)|2 = 1

π(rexc) 3n3 .

(4)

Within the framework of radiative recombination, the

radiative decay rate is proportional to the e - h over-

lap, i.e., τ -1

rad ∝ |ϕn(0)|2 . Consequently, larger values of

|ϕn(0)|2 indicate stronger e - h overlap and a greater

propensity for radiative transitions. In the present case,

LaYX3 exhibits an enhanced |ϕn(0)|2 , consistent with its

reduced exciton radius, confirming stronger wavefunction

overlap and potentially larger oscillator strength. Since

neither radiative nor non-radiative exciton lifetimes are

explicitly calculated in this work, |ϕn(0)|2 is employed

only as a qualitative descriptor of the radiative recombi-

nation tendency rather than as a direct measure of the

exciton lifetime (τexc). These results indicate pronounced

light-matter interaction in the studied systems, which is

beneficial for optoelectronic and light-emitting applica-

tions.

E. Polaronic Properties:

Understanding the fundamental limits of carrier mo-

bility in these chalcogenide perovskites requires a rig-

orous treatment of carrier-phonon interactions within a

first-principles framework [58, 59]. In polar semiconduc-

tors, transport at ambient conditions is primarily limited

by scattering with longitudinal optical phonons, arising

from the macroscopic electric fields associated with lat-

tice polarization [15, 52]. This interaction leads to the

formation of polarons, wherein charge carriers become

dressed by lattice distortions, thereby altering their ef-

fective mass and transport dynamics. As a consequence,

mobility cannot be accurately described within a simple

band-like picture of free carriers.

The interaction between charge carriers and polar opti-

cal phonons can be effectively described within the frame-

work of the Fröhlich Hamiltonian, which is valid in the

10

low carrier-density regime [35]. The strength of this in-

teraction is quantified by the dimensionless Fröhlich cou-

pling constant, α, which incorporates the effects of dielec-

tric screening, carrier effective mass, and the longitudinal

optical phonon frequency. It is defined as [15, 60]:

α = 1

4πε0

1

2

( 1

ε∞

- 1

εs

) e2

ℏωLO

( 2m∗ωLO

ℏ

)1/2

(5)

The calculated carrier-phonon coupling constants (α)

for the investigated compounds are summarized in Table

V. In general, α &gt; 10 signifies strong carrier-phonon cou-

pling, whereas α ≪ 1 corresponds to the weak-coupling

regime [58]. Our results place these materials in the

intermediate-to-strong coupling regime, with α values

ranging from 1.92 to 10.72. Furthermore, the carrier-

phonon interaction is found to be stronger for electrons

than for holes, with this trend being particularly pro-

nounced in LaYX3 (X = S, Se), suggesting more signif-

icant polaronic renormalization of electron transport. It

should be emphasized that the present analysis is based

on the Fröhlich formalism, which provides a physically

meaningful description of the long-range interaction be-

tween charge carriers and longitudinal optical phonons

in polar materials using first-principles quantities, in-

cluding the dielectric constants, effective carrier masses,

and longitudinal optical phonon frequencies. Conse-

quently, the calculated Fröhlich coupling constants pro-

vide useful estimates of the strength of the long-range po-

lar electron-phonon interaction and the associated large-

polaron characteristics. However, this approach does not

explicitly evaluate the momentum- and mode-resolved

electron-phonon coupling matrix elements or identify the

individual phonon modes and electronic states contribut-

ing to the coupling. A comprehensive microscopic treat-

ment based on first-principles electron-phonon coupling

calculations using density-functional perturbation theory

together with Wannier interpolation would provide such

information but is beyond the scope of the present work

[61]. Nevertheless, the Fröhlich model remains a widely

adopted framework for describing large-polaron behav-

ior in polar semiconductors and is appropriate for the

objectives of the present study.

Polaron formation refers to the interaction of a charge

carrier, either an electron or a hole, with the surrounding

lattice, leading to a local structural distortion. This cou-

pling lowers the quasiparticle (QP) energies, so that both

electron and hole states are stabilized during polaron for-

mation. The polaron energy, Ep, can be estimated as

follows [15, 56]:

Ep = (-α - 0.0123α2 )ℏωLO.

(6)

The QP gap associated with the polaronic states, ob-

tained from the electron and hole polaron energies (Ta-

ble V), is compared with the exciton binding energies,

EB, listed in Table III. This comparison reveals that,

for most of the examined chalcogenide perovskites, the

energy of the charge-separated polaronic states is lower

than that of the bound exciton states, indicating that

the bound excitons are energetically more stable. How-

ever, in the case of La(Sc, Y)Se3, the charge-separated

polaronic states become more favorable than the bound

exciton states.

Feynman introduced a powerful variational approach

to address the Fröhlich Hamiltonian, which describes

the interaction between an electron (or hole) and a con-

tinuum of independent, harmonically oscillating phonon

modes within a quantum field theoretical framework [62].

As the electron (or hole) moves through the lattice, it

interacts with the polarization field it induces, which

evolves and decays over time. Within this formalism,

and in the weak-coupling limit (small α), the polaron

effective mass, mp, can be expressed as [17, 62]:

mp = m∗(1 + α6 + α2

40 + ...).

(7)

As shown in Table V, carrier-phonon coupling leads to

a substantial enhancement of the effective mass, with mp

increasing by approximately 41-466%. This significant

renormalization indicates the presence of intermediate to

strong carrier-lattice interactions in the examined sys-

tems.

To further assess the impact of the enhanced polaron

effective mass, the polaron mobility is estimated using

the Hellwarth polaron model as [36, 57]:

µp = (3√πe)

2πcωLOm∗α

sinh(β/2)

β5/2

w3

v3

1

K(a, b)

(8)

where e is the electronic charge, β = hcωLO/kBT, w

and v are temperature-dependent variational parameters,

and K(a, b) is a function of β, w, and v (for details, see

Sec. XIII of the SM [42]). The polaron mobility quan-

tifies the ease with which a polaron propagates through

the lattice and is governed by both its effective mass and

the strength of carrier-lattice interactions. As the ef-

fective mass increases due to strong carrier-phonon cou-

pling, the mobility correspondingly decreases, leading to

slower carrier transport. This behavior is evident in the

present systems (Table V), where hole polarons exhibit

significantly higher mobilities (2.12-39.94 cm 2 V-1 s-1 )

compared to electron polarons (0.21-3.87 cm 2 V-1 s-1 ).

This indicates stronger electron-phonon coupling and/or

larger effective masses for electrons, leading to more lo-

calized electron polarons and consequently reduced mo-

bility. In contrast, the relatively lighter and less strongly

coupled hole polarons enable more efficient charge trans-

port. Despite the relatively low electron mobility, the

favorable hole transport, combined with the structural

stability and non-toxicity of these materials, underscores

their potential for optoelectronic applications, particu-

larly in devices where hole conduction plays a dominant

role.

11

TABLE V. Calculated polaron parameters of ABX3 (A = Y, La; B = Sc, Y; and X = S, Se) rare-earth chalcogenide perovskites.

Configurations ωLO (THz)

α

Ep (meV) mp/m∗ µp (cm 2 V-1 s-1 )

e h

e

h

e h e

h

YScS3

6.50

4.39 2.48 124.55 68.79 2.21 1.57 2.18 19.04

YScSe3

4.86

3.99 1.92 84.25 39.56 2.06 1.41 2.94 39.94

LaScS3

5.92

5.56 3.93 145.63 101.01 2.70 2.04 2.27

9.67

LaScSe3

4.47

4.94 3.17 97.00 60.97 2.43 1.78 3.87 21.31

LaYS3

5.32

10.72 7.04 267.32 168.53 5.66 3.41 0.21

2.12

LaYSe3

3.87

10.58 6.30 191.63 108.79 5.56 3.04 0.34

5.05

A broader perspective can be obtained by comparing

the present III-III chalcogenide perovskites with the more

extensively studied II-IV systems ABX3 (A = Ca, Sr,

Ba; B = Ti, Zr, Sn, Hf; and X = S, Se). The lat-

ter typically exhibit smaller band gaps (∼ 1.0-2.5 eV),

larger dielectric screening, and correspondingly weaker

excitonic effects, resulting in more delocalized Wannier-

type excitons and longer carrier diffusion lengths that

are advantageous for photovoltaic applications [13-17].

In addition, relatively weaker carrier-phonon coupling in

these systems leads to lighter polarons and higher carrier

mobility. In contrast, the III-III compounds investigated

here display wider band gaps (2.75-4.47 eV), reduced di-

electric screening, and moderately large exciton binding

energies, giving rise to more localized excitons with en-

hanced electron-hole overlap. This enhanced localization

is further accompanied by stronger carrier-phonon cou-

pling, leading to heavier polaronic quasiparticles and re-

duced carrier mobility. While such polaronic effects may

limit efficient charge transport and charge separation,

they can simultaneously stabilize excitonic states and

suppress non-radiative recombination. Consequently, the

combination of strong excitonic binding and polaronic lo-

calization results in pronounced light-matter interaction

and enhanced radiative recombination, making these ma-

terials particularly promising for light-emitting and pho-

todetection applications, albeit less favorable for photo-

voltaic performance.

IV. CONCLUSION:

In summary, we have systematically investigated the

ground- and excited-state properties of III-III rare-earth

chalcogenide perovskites ABX3 (A = Y, La; B = Sc,

Y; and X = S, Se) using state-of-the-art density func-

tional theory, density functional perturbation theory, and

many-body perturbation theory. The calculated phonon

band structures and elastic constants confirm the dynam-

ical and mechanical stability of these compounds. Our

electronic structure analysis reveals quasiparticle band

gaps (G0W0@PBE) in the range of 2.75-4.47 eV, ac-

companied by lower hole effective masses compared to

electrons, indicating favorable p-type transport. The op-

tical properties, computed within the BSE framework,

exhibit a strong absorption onset spanning the visible to

ultraviolet region, highlighting their potential for opto-

electronic applications. Importantly, these compounds

exhibit pronounced excitonic effects, hosting stable ex-

citons as evidenced by their intermediate-to-large bind-

ing energies (0.148-0.517 eV), high excitonic tempera-

tures, Wannier-Frenkel crossover character, and strong

electron-hole wavefunction overlap, indicative of pro-

nounced light-matter interaction and favorable radia-

tive recombination characteristics. Fröhlich's mesoscopic

analysis indicates appreciable carrier-phonon coupling in

these systems, with electron-phonon interactions consis-

tently outweighing their hole counterparts. Remarkably,

bound excitonic states dominate over charge-separated

polaronic configurations in nearly all compounds, with

La(Sc, Y)Se3 as an exception, while hole polarons demon-

strate substantially higher mobilities (reaching up to ∼

40 cm 2 V-1 s-1 ) than electrons. Overall, the interplay

between strong excitonic effects and favorable polaronic

transport, combined with excellent structural stability

and lead-free composition, establishes rare-earth chalco-

genide perovskites ABX3 as promising candidates for

next-generation optoelectronic technologies. These ma-

terials are particularly attractive for applications in light-

emitting devices and photodetectors, and they offer a vi-

able platform for exploring excitonic optoelectronics in

environmentally benign systems.

ACKNOWLEDGMENTS

The authors would like to acknowledge the Coun-

cil of Scientific and Industrial Research (CSIR), Gov-

ernment of India [Grant No. 3WS(007)/2023-24/EMR-

II/ASPIRE] for financial support. The authors acknowl-

edge the High Performance Computing Cluster (HPCC)

'Magus' at Shiv Nadar Institution of Eminence for pro-

viding computational resources that have contributed to

the research results reported within this paper.

DATA AVAILABILITY

The data that support the findings of this article are

not publicly available. The data are available from the

authors upon reasonable request.

12

[1] A. Kojima, K. Teshima, Y. Shirai, and T. Miyasaka,

Organometal Halide Perovskites as Visible-Light Sensi-

tizers for Photovoltaic Cells, J. Am. Chem. Soc. 131,

6050 (2009).

[2] N.-G. Park, Organometal Perovskite Light Absorbers To-

ward a 20% Efficiency Low-Cost Solid-State Mesoscopic

Solar Cell, J. Phys. Chem. Lett. 4, 2423 (2013).

[3] J. Berry, T. Buonassisi, D. A. Egger, G. Hodes, L. Kro-

nik, Y.-L. Loo, I. Lubomirsky, S. R. Marder, Y. Mastai,

J. S. Miller, D. B. Mitzi, Y. Paz, A. M. Rappe, I. Riess,

B. Rybtchinski, O. Stafsudd, V. Stevanovic, M. F. Toney,

D. Zitoun, A. Kahn, D. Ginley, and D. Cahen, Hybrid

Organic-Inorganic Perovskites (HOIPs): Opportunities

and Challenges, Adv. Mater. 27, 5102 (2015).

[4] D. A. Egger, A. M. Rappe, and L. Kronik, Hybrid

Organic-Inorganic Perovskites on the Move, Acc. Chem.

Res. 49, 573 (2016).

[5] National Renewable Energy Laboratory (NREL), Best

Research Cell Efficiency Chart, https://www.nrel.gov/

pv/cell-efficiency.html, Accessed 2021-01-07 (2021).

[6] D. B. Straus, S. Guo, A. M. Abeykoon, and R. J.

Cava, Understanding the Instability of the Halide Per-

ovskite CsPbI3 through Temperature-Dependent Struc-

tural Analysis, Adv.Mater. 32, 2001069 (2020).

[7] A. Babayigit, A. Ethirajan, M. Muller, and B. Conings,

Toxicity of organometal halide perovskite solar cells, Nat.

Mater. 15, 247 (2016).

[8] D. Tiwari, O. S. Hutter, and G. Longo, Chalcogenide per-

ovskites for photovoltaics: current status and prospects,

J. Phys. Energy 3, 034010 (2021).

[9] S. Niu, H. Huyan, Y. Liu, M. Yeung, K. Ye, L. Blanke-

meier, T. Orvis, D. Sarkar, D. J. Singh, R. Kapadia, and

J. Ravichandran, Bandgap Control via Structural and

Chemical Tuning of Transition Metal Perovskite Chalco-

genides, Adv. Mater. 29, 1604733 (2017).

[10] X. Wu, W. Gao, J. Chai, C. Ming, M. Chen, H. Zeng,

P. Zhang, S. Zhang, and Y.-Y. Sun, Defect tolerance

in chalcogenide perovskite photovoltaic material BaZrS3,

Sci. China Mater. 64, 2976 (2021).

[11] Y.-Y. Sun, M. L. Agiorgousis, P. Zhang, and S. Zhang,

Chalcogenide Perovskites for Photovoltaics, Nano Lett.

15, 581 (2015).

[12] R. Lelieveld and D. J. W. IJdo, Sulphides with the

GdFeO3 structure, Acta Cryst. B 36, 2223 (1980).

[13] M. Kumar, A. Singh, D. Gill, and S. Bhattacharya, Op-

toelectronic Properties of Chalcogenide Perovskites by

Many-Body Perturbation Theory, J. Phys. Chem. Lett.

12, 5301 (2021).

[14] P. Basera and S. Bhattacharya, Chalcogenide Perovskites

(ABS3; A = Ba, Ca, Sr; B = Hf, Sn): An Emerging Class

of Semiconductors for Optoelectronics, J. Phys. Chem.

Lett. 13, 6439 (2022).

[15] S. Adhikari and P. Johari, Photovoltaic properties of

ABSe3 chalcogenide perovskites (A = Ca, Sr, Ba; B =

Zr, Hf), Phys. Rev. B 109, 174114 (2024).

[16] S. Adhikari, S. Das, and P. Johari, Post-transition metal

Sn-based chalcogenide perovskites: a promising lead-

free and transition metal alternative for stable, high-

performance photovoltaics, J. Mater. Chem. C 13, 7792

(2025).

[17] S. Adhikari and P. Johari, Optimizing lead-free chalco-

genide perovskites for high-efficiency photovoltaics via al-

loying, Phys. Rev. B 112, 085206 (2025).

[18] H. Zhang, Y. Pan, Z. Liu, B. Zeng, X. Wu, C. Ming,

G. Xin, W. Zhou, H. Zeng, S. Zhang, and Y.-Y. Sun,

Indirect-to-direct band gap transition induced by d-d

coupling between cations in rare-earth chalcogenide per-

ovskites, Phys. Rev. B 110, L041201 (2024).

[19] H. Zhang, X. Wu, K. Ding, L. Xie, K. Yang, C. Ming,

S. Bai, H. Zeng, S. Zhang, and Y.-Y. Sun, Prediction and

Synthesis of a Selenide Perovskite for Optoelectronics,

Chem. Mater. 35, 4128 (2023).

[20] K. Kuhar, A. Crovetto, M. Pandey, K. S. Thygesen,

B. Seger, P. C. K. Vesborg, O. Hansen, I. Chorkendorff,

and K. W. Jacobsen, Sulfide perovskites for solar en-

ergy conversion applications: computational screening

and synthesis of the selected compound LaYS3, Energy

Environ. Sci. 10, 2579 (2017).

[21] A. Crovetto, R. Nielsen, M. Pandey, L. Watts, J. G.

Labram, M. Geisler, N. Stenger, K. W. Jacobsen,

O. Hansen, B. Seger, I. Chorkendorff, and P. C. K. Ves-

borg, Shining Light on Sulfide Perovskites: LaYS3 Ma-

terial Properties and Solar Cells, Chem. Mater. 31, 3359

(2019).

[22] H. Zhang, C. Ming, K. Yang, H. Zeng, S. Zhang, and

Y.-Y. Sun, Chalcogenide Perovskite YScS3 as a Potential

p-Type Transparent Conducting Material, Chinese Phys.

Lett. 37, 097201 (2020).

[23] P. Hohenberg and W. Kohn, Inhomogeneous Electron

Gas, Phys. Rev. 136, B864 (1964).

[24] W. Kohn and L. J. Sham, Self-Consistent Equations In-

cluding Exchange and Correlation Effects, Phys. Rev.

140, A1133 (1965).

[25] M. Gajdoš, K. Hummer, G. Kresse, J. Furthmüller, and

F. Bechstedt, Linear optical properties in the projector-

augmented wave methodology, Phys. Rev. B 73, 045112

(2006).

[26] H. Jiang, P. Rinke, and M. Scheffler, Electronic proper-

ties of lanthanide oxides from the GW perspective, Phys.

Rev. B 86, 125115 (2012).

[27] F. Fuchs, C. Rödl, A. Schleife, and F. Bechstedt, Efficient

O(N 2 ) approach to solve the Bethe-Salpeter equation for

excitonic bound states, Phys. Rev. B 78, 085103 (2008).

[28] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized

Gradient Approximation Made Simple, Phys. Rev. Lett.

77, 3865 (1996).

[29] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vy-

drov, G. E. Scuseria, L. A. Constantin, X. Zhou, and

K. Burke, Restoring the Density-Gradient Expansion for

Exchange in Solids and Surfaces, Phys. Rev. Lett. 100,

136406 (2008).

[30] J. Heyd, G. E. Scuseria, and M. Ernzerhof, Hybrid func-

tionals based on a screened Coulomb potential, J. Chem.

Phys. 118, 8207 (2003).

[31] L. Hedin, New Method for Calculating the One-Particle

Green's Function with Application to the Electron-Gas

Problem, Phys. Rev. 139, A796 (1965).

[32] M. S. Hybertsen and S. G. Louie, First-Principles Theory

of Quasiparticles: Calculation of Band Gaps in Semicon-

ductors and Insulators, Phys. Rev. Lett. 55, 1418 (1985).

13

[33] S. Albrecht, L. Reining, R. Del Sole, and G. Onida,

Ab Initio Calculation of Excitonic Effects in the Opti-

cal Spectra of Semiconductors, Phys. Rev. Lett. 80, 4510

(1998).

[34] M. Rohlfing and S. G. Louie, Electron-Hole Excitations

in Semiconductors and Insulators, Phys. Rev. Lett. 81,

2312 (1998).

[35] H. Fröhlich, Electrons in lattice fields, Adv. Phys. 3, 325

(1954).

[36] R. W. Hellwarth and I. Biaggio, Mobility of an electron in

a multimode polar lattice, Phys. Rev. B 60, 299 (1999).

[37] G. Kresse and J. Furthmüller, Efficient iterative schemes

for ab initio total-energy calculations using a plane-wave

basis set, Phys. Rev. B 54, 11169 (1996).

[38] G. Kresse and J. Furthm¨uller, Efficiency of Ab-initio To-

tal Energy Calculations for Metals and Semiconductors

Using a Plane-wave Basis Set, Comput. Mater. Sci. 6, 15

(1996).

[39] P. E. Blöchl, Projector augmented-wave method, Phys.

Rev. B 50, 17953 (1994).

[40] K. Momma and F. Izumi, VESTA3 for three-dimensional

visualization of crystal, volumetric and morphology data,

J. Appl. Crystallogr. 44, 1272 (2011).

[41] A. Togo, L. Chaput, T. Tadano, and I. Tanaka, Imple-

mentation strategies in phonopy and phono3py, J. Phys.

Condens. Matter 35, 353001 (2023).

[42] See Supplemental Material (SM) at [URL will be inserted

by publisher] for details of distortion parameters, decom-

position energy, convex hull, phonon dispersion curves,

mechanical properties, electronic DOS, effect of spin-

orbit coupling on bandgap, orbital projected band struc-

tures, effective masses of charge carriers, convergence of

G0W0 and BSE calculations, exciton binding energy ob-

tained using the Wannier-Mott model, calculation of sin-

gle phonon angular frequency and polaron mobility pa-

rameters for rare-earth chalcogenide perovskites ABX3

(A = Y, La; B = Sc, Y; and X = S, Se).

[43] A. M. Ganose, A. J. Jackson, and D. O. Scanlon, sumo:

Command-line tools for plotting and analysis of peri-

odic ab initio calculations, J. Open Source Softw. 3, 717

(2018).

[44] V. Wang, N. Xu, J.-C. Liu, G. Tang, and W.-T. Geng,

VASPKIT: A user-friendly interface facilitating high-

throughput computing and analysis using VASP code,

Comput. Phys. Commun. 267, 108033 (2021).

[45] A. Chakravorty, S. Adhikari, and P. Johari, Unlocking

the optoelectronic potential of AGeX3 (A = Ca, Sr, Ba;

X = S, Se): A sustainable alternative in chalcogenide

perovskites, J. Chem. Phys. 163, 234708 (2025).

[46] F. Mouhat and F.-X. Coudert, Necessary and sufficient

elastic stability conditions in various crystal systems,

Phys. Rev. B 90, 224104 (2014).

[47] Z.-j. Wu, E.-j. Zhao, H.-p. Xiang, X.-f. Hao, X.-j. Liu,

and J. Meng, Crystal structures and elastic properties of

superhard IrN2 and IrN3 from first principles, Phys. Rev.

B 76, 054115 (2007).

[48] R. Hill, The Elastic Behaviour of a Crystalline Aggregate,

Proc. Phys. Soc. A 65, 349 (1952).

[49] S. Pugh, XCII. Relations between the elastic moduli

and the plastic properties of polycrystalline pure met-

als, London, Edinburgh Dublin Philos. Mag. J. Sci. 45,

823 (1954).

[50] X. Liu, B. Xie, C. Duan, Z. Wang, B. Fan, K. Zhang,

B. Lin, F. J. M. Colberts, W. Ma, R. A. J. Janssen,

F. Huang, and Y. Cao, A high dielectric constant non-

fullerene acceptor for efficient bulk-heterojunction or-

ganic solar cells, J. Mater. Chem. A 6, 395 (2018).

[51] S. Adhikari and P. Johari, Theoretical insights into

monovalent-metal-cation transmutation effects on lead-

free halide double perovskites for optoelectronic applica-

tions, Phys. Rev. Mater. 7, 075401 (2023).

[52] S. Adhikari and P. Johari, Capturing optoelectronic

properties of Cs2AgSbBr 6-xClx (x = 0 - 6) double

perovskites using many-body perturbation theory, Phys.

Rev. B 110, 014101 (2024).

[53] M. Bokdam, T. Sander, A. Stroppa, S. Picozzi, D. D.

Sarma, C. Franchini, and G. Kresse, Role of Polar

Phonons in the Photo Excited State of Metal Halide Per-

ovskites, Sci. Rep. 6, 28618 (2016).

[54] M. R. Filip, J. B. Haber, and J. B. Neaton, Phonon

Screening of Excitons in Semiconductors: Halide Per-

ovskites and Beyond, Phys. Rev. Lett. 127, 067401

(2021).

[55] S. Adhikari, S. S. Padelkar, J. J. Jasieniak, A. N. Si-

monov, and A. Alam, Harnessing Linear and Nonlinear

Optical Responses in Ferroelectric LaMoN3 for Enhanced

Photovoltaic Efficiency, Chem. Mater. 38, 6271 (2026).

[56] S. Adhikari and P. Johari, Unveiling the impact of triva-

lent metal cation transmutation on Cs2AgM(III)Cl 6 dou-

ble perovskites using many-body perturbation theory,

Phys. Rev. B 112, 195208 (2025).

[57] S. Adhikari, A. Chakravorty, and P. Johari, Optical

and polaronic properties of vacancy-ordered double per-

ovskites: A first-principles investigation, Phys. Rev. B

113, 045204 (2026).

[58] J. M. Frost, Calculating polaron mobility in halide per-

ovskites, Phys. Rev. B 96, 195202 (2017).

[59] L. M. Herz, Charge-Carrier Mobilities in Metal Halide

Perovskites: Fundamental Mechanisms and Limits, ACS

Energy Lett. 2, 1539 (2017).

[60] S. Adhikari and P. Johari, Probing Optoelectronic Prop-

erties of Stable Vacancy-Ordered Double Perovskites: In-

sights from Many-Body Perturbation Theory, Adv. The-

ory Simul. 8, 2400921 (2025).

[61] F. Giustino, Electron-phonon interactions from first prin-

ciples, Rev. Mod. Phys. 89, 015003 (2017).

[62] R. P. Feynman, Slow Electrons in a Polar Crystal, Phys.

Rev. 97, 660 (1955).