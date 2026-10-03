to the quantizing level or dither noise
would have to be added outside the
passband. Fig 6 illustrates the signalto-noise ratio curve with external
noise for the 10-m band and 40 dB of
INA gain. Fig 5 shows the same curve
without external noise and with INA
gain of 60 dB. This much gain would
not improve the sensitivity in the presence of external noise but would reduce blocking and IMD dynamic range
by 20 dB. On the lower bands, 20 dB
or lower INA gain is perfectly acceptable given the higher external noise.


**Frequency Control**

Fig 7 illustrates the Analog Devices
AD9854 quadrature DDS circuitry for
driving the QSD/QSE. Quadrature local-oscillator signals allow the elimination of the divide-by-four Johnson
counter, described in Part 1, so that
the DDS runs at the carrier frequency
instead of its fourth harmonic. I have
chosen to use the 200-MHz version of
the part to minimize heat dissipation,
and because it easily meets my frequency coverage requirements of dc60 MHz. The DDS outputs are connected to seventh-order elliptical
low-pass filters that also provide a dc
reference for the high-speed comparators. The AD9854 may be controlled
either through a SPI port or a parallel interface. There are timing issues
in SPI mode that require special care
in programming. Analog Devices have
developed a protocol that allows the
chip to be put into external I/O update
mode to work around the serial


**About Intel Performance**
**Primitives**

Many readers have inquired about
Intel’s replacement of its Signal Processing Library (SPL) with the Intel
Performance Primatives (IPP). The
SPL was a free distribution, but the
Intel Web site states that IPP requires payment of a $199 fee after a
30 day evaluation period. A fully
functional trial version of IPP may be
downloaded from the Intel site at
**www.intel.com/software/prod-**
**ucts/global/eval.htm** . The author
has confirmed with Intel Product
Management that no license fee is
required for amateur experimentation using IPP, and there is no limit
on the evaluation period for such
use. Intel actually encourages this
type of experimental use. Payment of
the license fee is required if and only
if there is a commercial distribution of
the DLL code.—Gerald Youngblood


**Mar/Apr 2003 27**


