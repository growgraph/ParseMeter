|Digital<br>Gain<br>Required<br>(dB)|86.0<br>76.0<br>66.0<br>56.0<br>46.0<br>36.0<br>26.0<br>16.0<br>9.4|9.4|9.4<br>9.4<br>9.4<br>9.4|6.0|–4.0|–14.0|
|---|---|---|---|---|---|---|
|Output<br>S/N Ratio<br>in BW2<br>(dB)|–0.9<br>9.1<br>19.1<br>29.1<br>39.1<br>49.1<br>59.1<br>69.1<br>78.2|82.2|82.9<br>83.0<br>83.0<br>83.0|86.4|96.4|106.4|
|Total<br>Noise<br>in BW2<br>(dBm)|–81.1<br>–81.1<br>–81.1<br>–81.1<br>–81.1<br>–81.1<br>–81.1<br>–81.1<br>–83.6|–87.6|–88.3<br>–88.4<br>–88.4<br>–88.4|–88.4|–88.4|–88.4|
|Quantizing<br>Noise of<br>A/D in BW2<br>(dBm)|–88.4<br>–88.4<br>–88.4<br>–88.4<br>–88.4<br>–88.4<br>–88.4<br>–88.4<br>–88.4|–88.4|–88.4<br>–88.4<br>–88.4<br>–88.4|–88.4|–88.4|–88.4|
|Noise in<br>A/D Input<br>in BW2<br>(dBm)|–82.0<br>–82.0<br>–82.0<br>–82.0<br>–82.0<br>–82.0<br>–82.0<br>–82.0<br>–85.4|–95.4|–105.4<br>–115.4<br>–125.4<br>–135.4|–142.0|–142.0|–142.0|
|A/D<br>Signal<br>Level<br>(dBm)|–82.0<br>–72.0<br>–62.0<br>–52.0<br>–42.0<br>–32.0<br>–22.0<br>–12.0<br>–5.4|–5.4|–5.4<br>–5.4<br>–5.4<br>–5.4|–2.0|8.0|18.0|
|Noise at<br>A/D Input<br>in BW1<br>(dBm)|–63.0<br>–63.0<br>–63.0<br>–63.0<br>–63.0<br>–63.0<br>–63.0<br>–63.0<br>–66.4|–76.4|–86.4<br>–96.4<br>–106.4<br>–116.4|–123.0|–123.0|–123.0|
|Sound Card<br>AGC<br>Reduction<br>(dB)|0.0<br>0.0<br>0.0<br>0.0<br>0.0<br>0.0<br>0.0<br>0.0<br>–3.3|–13.3|–23.3<br>–33.3<br>–43.3<br>–53.3|–60.0|–60.0|–60.0|
|Total<br>Analog<br>Gain<br>(dB)|46.0<br>46.0<br>46.0<br>46.0<br>46.0<br>46.0<br>46.0<br>46.0<br>42.7|32.7|22.7<br>12.7<br>2.7<br>–7.3|–14.0|–14.0|–14.0|
|Antenna<br>Overload<br>Level<br>(dBm)|||6<br>16|26|36|46|
|INA<br>Output<br>Level<br>(dBm)|–82<br>–72<br>–62<br>–52<br>–42<br>–32<br>–22<br>–12<br>–2|8|18<br>28<br>38<br>48|58|68|78|
|Antenna<br>Signal<br>Level<br>(dBm)|–128<br>–118<br>–108<br>–98<br>–88<br>–78<br>–68<br>–58<br>–48|–38|–28<br>–18<br>–8<br>2|12|22|32|



to the quantizing level or dither noise would have to be added outside the passband. Fig 6 illustrates the signalto-noise ratio curve with external noise for the 10-m band and 40 dB of INA gain. Fig 5 shows the same curve without external noise and with INA gain of 60 dB. This much gain would not improve the sensitivity in the presence of external noise but would reduce blocking and IMD dynamic range by 20 dB. On the lower bands, 20 dB or lower INA gain is perfectly acceptable given the higher external noise. 

## **Frequency Control** 

Fig 7 illustrates the Analog Devices AD9854 quadrature DDS circuitry for driving the QSD/QSE. Quadrature local-oscillator signals allow the elimination of the divide-by-four Johnson counter, described in Part 1, so that the DDS runs at the carrier frequency instead of its fourth harmonic. I have chosen to use the 200-MHz version of the part to minimize heat dissipation, and because it easily meets my frequency coverage requirements of dc60 MHz. The DDS outputs are connected to seventh-order elliptical low-pass filters that also provide a dc reference for the high-speed comparators. The AD9854 may be controlled either through a SPI port or a parallel interface. There are timing issues in SPI mode that require special care in programming. Analog Devices have developed a protocol that allows the chip to be put into external I/O update mode to work around the serial 

# **About Intel Performance Primitives** 

Many readers have inquired about Intel’s replacement of its Signal Processing Library (SPL) with the Intel Performance Primatives (IPP). The SPL was a free distribution, but the Intel Web site states that IPP requires payment of a $199 fee after a 30 day evaluation period. A fully functional trial version of IPP may be downloaded from the Intel site at **www.intel.com/software/products/global/eval.htm** . The author has confirmed with Intel Product Management that no license fee is required for amateur experimentation using IPP, and there is no limit on the evaluation period for such use. Intel actually encourages this type of experimental use. Payment of the license fee is required if and only if there is a commercial distribution of the DLL code.—Gerald Youngblood 

**Mar/Apr  2003  27** 

