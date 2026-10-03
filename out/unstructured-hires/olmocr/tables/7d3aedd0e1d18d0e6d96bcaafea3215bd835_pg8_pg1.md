n

Table 8—SDR-1000 Level Analysis Detail for the 10-Meter Band with 40dB of INA Gain

i

a

G

A

N

I

f

o

B

d

0

4

h

t

i

w

d

n

a

B

r

e

t

e

M

-

0

1

e

h

t

r

o

f

l

i

a

t

e

D

s

i

s

y

l

a

n

A

l

e

v

e

L

0

0

0

1

-

R

D

S

—

8

e

l

b

a

T

Digital Output S/N Ratio Gain Required in BW2 (dB) (dB)

Noise in Quantizing Total A/D Input Noise in BW2 Noise of inBW2- A/Din BW2 (dBm) (dBm) (dBm)

A/D Signal Level (dBm)

Sound Card’ Noise at Antenna Total Overload Analog AGC A/D Input Reduction in BW1 (dBm) Gain Level (dBm) (AB) (aB)

T

a

n

n

e

t

n

A

O

t

NA Antenna Signal Output Level (dBm) Level (dBm)

A

N

I

a

n

n

e

t

n

A

S

L

(

86.0 76.0 66.0 56.0 46.0 36.0 26.0 16.0 9.4 9.4 9.4 9.4 9.4 9.4 6.0 —4.0 -14.0

9.1 1 9.1 | | | | | 2 82.2 29 39 49 59 69 78 82.9 83 .O 0 3.0 83 8 86.4 9 6.4 106.4

—81.1 -81.1 -81.1 -81.1 -81.1 -81.1 -81.1 -81.1 -83.6 —87.6 -88.3 —88.4 -88.4 —88.4 -88.4 —88.4 -88.4

—88.4 —-88.4 —88.4 —88.4 —88.4 —88.4 —88.4 —88.4 -88.4 —88.4 -88.4 —88.4 -88.4 —88.4 —88.4 —88.4 —88.4

—82.0 -82.0 —82.0 -82.0 -82.0 -82.0 -82.0 -82.0 —85.4 -95.4 -105.4 —115.4 -125.4 -135.4 -142.0 -—142.0 -142.0

-82.0 -72.0 -62.0 —52.0 —42.0 —32.0 —22.0 -12.0 —5.4 5.4 —5.4 —5.4 5.4 —5.4 -2.0 8.0 18.0

-63.0 -63.0 -63.0 —63.0 —63.0 —63.0 —63.0 —63.0 —66.4 -76.4 —86.4 —96.4 -—106.4 —116.4 -123.0 -—123.0 -123.0

0.0 0.0 0.0

-3.3 -13.3 —23.3 —33.3 —43.3 —53.3 —60.0 —60.0 —60.0

46.0 46.0 46.0 46.0 46.0 46.0 46.0 46.0 42.7 32.7 7 2.7 2.7 -7.3 -14.0 -14.0 -14.0

4

1

–

6

6

6

6

6

16 26 36 46

1

3

2

4

2

2

2

2

2

2

2

2

—82 -72 —62 —52 —42 —32 -22 -12 -2

8

–

2

–

8

8

8

8

8

8

8

8

18 28 38 48 58 68 78

7

4

1

2

8

8

8

-128 -118 -108 -98 —88 -78 -68 —58 —48 —38 -28 -18 -8

2

1

–

8

–

2

2

2

2

12 22 32

1

2

3

to the quantizing level or dither noise would have to be added outside the passband. Fig 6 illustrates the signal- to-noise ratio curve with external noise for the 10-m band and 40 dB of INA gain. Fig 5 shows the same curve without external noise and with INA gain of 60 dB. This much gain would not improve the sensitivity in the pres- ence of external noise but would re- duce blocking and IMD dynamic range by 20 dB. On the lower bands, 20 dB or lower INA gain is perfectly accept- able given the higher external noise.

# Frequency Control

Fig 7 illustrates the Analog Devices AD9854 quadrature DDS circuitry for driving the QSD/QSE. Quadrature lo- cal-oscillator signals allow the elimi- nation of the divide-by-four Johnson counter, described in Part 1, so that the DDS runs at the carrier frequency instead of its fourth harmonic. I have chosen to use the 200-MHz version of the part to minimize heat dissipation, and because it easily meets my fre- quency coverage requirements of dc- 60 MHz. The DDS outputs are con- nected to seventh-order elliptical low-pass filters that also provide a dc reference for the high-speed compara- tors. The AD9854 may be controlled either through a SPI port or a paral- lel interface. There are timing issues in SPI mode that require special care in programming. Analog Devices have developed a protocol that allows the chip to be put into external I/O update mode to work around the serial

# About Intel Performance Primitives

Many readers have inquired about Intel’s replacement of its Signal Pro- cessing Library (SPL) with the Intel Performance Primatives (IPP). The SPL was a free distribution, but the Intel Web site states that IPP re- quires payment of a $199 fee after a 30 day evaluation period. A fully functional trial version of IPP may be downloaded from the Intel site at www.intel.com/software/prod- ucts/global/eval.htm. The author has confirmed with Intel Product Management that no license fee is required for amateur experimenta- tion using IPP, and there is no limit on the evaluation period for such use. Intel actually encourages this type of experimental use. Payment of the license fee is required if and only if there is a commercial distribution of the DLL code.—Gerald Youngblood

# Mar/Apr 2003 27
