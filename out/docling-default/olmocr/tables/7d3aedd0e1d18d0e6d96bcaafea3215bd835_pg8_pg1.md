| Digital Gain Required (dB)           | 86.0 76.0 66.0 56.0 46.0 36.0 26.0 16.0 9.4 9.4 9.4 9.4 9.4 9.4 6.0 -4.0 -14.0                               |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Output S/N Ratio in BW2 (dB)         | -0.9 9.1 19.1 29.1 39.1 49.1 59.1 69.1 78.2 82.2 82.9 83.0 83.0 83.0 86.4 96.4 106.4                         |
| Total Noise in BW2 (dBm)             | -81.1 -81.1 -81.1 -81.1 -81.1 -81.1 -81.1 -81.1 -83.6 -87.6 -88.3 -88.4 -88.4 -88.4 -88.4 -88.4 -88.4        |
| Quantizing Noise of A/D in BW2 (dBm) | -88.4 -88.4 -88.4 -88.4 -88.4 -88.4 -88.4 -88.4 -88.4 -88.4 -88.4 -88.4 -88.4 -88.4 -88.4 -88.4 -88.4        |
| Noise in A/D Input in BW2 (dBm)      | -82.0 -82.0 -82.0 -82.0 -82.0 -82.0 -82.0 -82.0 -85.4 -95.4 -105.4 -115.4 -125.4 -135.4 -142.0 -142.0 -142.0 |
| A/D Signal Level (dBm)               | -82.0 -72.0 -62.0 -52.0 -42.0 -32.0 -22.0 -12.0 -5.4 -5.4 -5.4 -5.4 -5.4 -5.4 -2.0 8.0 18.0                  |
| Noise at A/D Input in BW1 (dBm)      | -63.0 -63.0 -63.0 -63.0 -63.0 -63.0 -63.0 -63.0 -66.4 -76.4 -86.4 -96.4 -106.4 -116.4 -123.0 -123.0 -123.0   |
| Sound Card AGC Reduction (dB)        | 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 -3.3 -13.3 -23.3 -33.3 -43.3 -53.3 -60.0 -60.0 -60.0                         |
| Total Analog Gain (dB)               | 46.0 46.0 46.0 46.0 46.0 46.0 46.0 46.0 42.7 32.7 22.7 12.7 2.7 -7.3 -14.0 -14.0 -14.0                       |
| Antenna Overload Level (dBm)         | 6 16 26 36 46                                                                                                |
| INA Output Level (dBm)               | -82 -72 -62 -52 -42 -32 -22 -12 -2 8 18 28 38 48 58 68 78                                                    |
| Antenna Signal Level (dBm)           | -128 -118 -108 -98 -88 -78 -68 -58 -48 -38 -28 -18 -8 2 12 22 32                                             |

to the quantizing level or dither noise would have to be added outside the passband. Fig 6 illustrates the signalto-noise ratio curve with external noise for the 10-m band and 40 dB of INA gain. Fig 5 shows the same curve without external noise and with INA gain of 60 dB. This much gain would not improve the sensitivity in the presence of external noise but would reduce blocking and IMD dynamic range by 20 dB. On the lower bands, 20 dB or lower INA gain is perfectly acceptable given the higher external noise.

## Frequency Control

Fig 7 illustrates the Analog Devices AD9854 quadrature DDS circuitry for driving the QSD/QSE. Quadrature local-oscillator signals allow the elimination of the divide-by-four Johnson counter, described in Part 1, so that the DDS runs at the carrier frequency instead of its fourth harmonic. I have chosen to use the 200-MHz version of the part to minimize heat dissipation, and because it easily meets my frequency coverage requirements of dc60 MHz. The DDS outputs are connected to seventh-order elliptical low-pass filters that also provide a dc reference for the high-speed comparators. The AD9854 may be controlled either through a SPI port or a parallel interface. There are timing issues in SPI mode that require special care in programming. Analog Devices have developed a protocol that allows the chip to be put into external I/O update mode to work around the serial

## About Intel Performance Primitives

Many readers have inquired about Intel's replacement of its Signal Processing Library (SPL) with the Intel Performance Primatives (IPP). The SPL was a free distribution, but the Intel Web site states that IPP requires payment of a $199 fee after a 30 day evaluation period. A fully functional trial version of IPP may be downloaded from the Intel site at www. intel .com/sof tware/products/global/eval.htm. The author has confirmed with Intel Product Management that no license fee is required for amateur experimentation using IPP, and there is no limit on the evaluation period for such use. Intel actually encourages this type of experimental use. Payment of the license fee is required if and only if there is a commercial distribution of the DLL code.-Gerald Youngblood