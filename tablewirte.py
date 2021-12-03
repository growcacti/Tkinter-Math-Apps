awg_str="""--+-----+--------+--------+----------+----------+-----------+--------------+------------+
|    |  A  |   B    |   C    |    D     |    E     |     F     |      G       |     H      |
+----+-----+--------+--------+----------+----------+-----------+--------------+------------+
|  1 | AWG |        |        | Ohms     | Ohms     | I chassis | Transmission |            |
|  2 |     | Dia in | Dia mm | 1000ft   | km       | AMPs      | AMPs         | Freq skin  |
|  3 | 0   | 0.46   | 11.68  | 0.05     | 0.16     | 380       | 302          | 125 Hz     |
|  4 | 0   | 0.41   | 10.40  | 0.06     | 0.20     | 328       | 239          | 160 Hz     |
|  5 | 0   | 0.36   | 9.27   | 0.08     | 0.26     | 283       | 190          | 200 Hz     |
|  6 | 0   | 0.32   | 8.25   | 0.10     | 0.32     | 245       | 150          | 250 Hz     |
|  7 | 1   | 0.29   | 7.35   | 0.12     | 0.41     | 211       | 119          | 325 Hz     |
|  8 | 2   | 0.26   | 6.54   | 0.16     | 0.51     | 181       | 94           | 410 Hz     |
|  9 | 3   | 0.23   | 5.83   | 0.20     | 0.65     | 158       | 75           | 500 Hz     |
| 10 | 4   | 0.20   | 5.19   | 0.25     | 0.82     | 135       | 60           | 650 Hz     |
| 11 | 5   | 0.18   | 4.62   | 0.31     | 1.03     | 118       | 47           | 810 Hz     |
| 12 | 6   | 0.16   | 4.11   | 0.40     | 1.30     | 101       | 37           | 1100 Hz    |
| 13 | 7   | 0.14   | 3.67   | 0.50     | 1.63     | 89        | 30           | 1300 Hz    |
| 14 | 8   | 0.13   | 3.26   | 0.63     | 2.06     | 73        | 24           | 1650 Hz    |
| 15 | 9   | 0.11   | 2.91   | 0.79     | 2.60     | 64        | 19           | 2050 Hz    |
| 16 | 10  | 0.10   | 2.59   | 1.00     | 3.28     | 55        | 15           | 2600 Hz    |
| 17 | 11  | 0.09   | 2.30   | 1.26     | 4.13     | 47        | 12           | 3200 Hz    |
| 18 | 12  | 0.08   | 2.05   | 1.59     | 5.21     | 41        | 9.3          | 4150 Hz    |
| 19 | 13  | 0.07   | 1.83   | 2.00     | 6.57     | 35        | 7.4          | 5300 Hz    |
| 20 | 14  | 0.06   | 1.63   | 2.53     | 8.28     | 32        | 5.9          | 6700 Hz    |
| 21 | 15  | 0.06   | 1.45   | 3.18     | 10.44    | 28        | 4.7          | 8250 Hz    |
| 22 | 16  | 0.05   | 1.29   | 4.02     | 13.17    | 22        | 3.7          | 11 k Hz    |
| 23 | 17  | 0.05   | 1.15   | 5.06     | 16.61    | 19        | 2.9          | 13 k Hz    |
| 24 | 18  | 0.04   | 1.02   | 6.39     | 20.94    | 16        | 2.3          | 17 kHz     |
| 25 | 19  | 0.04   | 0.91   | 8.05     | 26.41    | 14        | 1.8          | 21 kHz     |
| 26 | 20  | 0.03   | 0.81   | 10.15    | 33.29    | 11        | 1.5          | 27 kHz     |
| 27 | 21  | 0.03   | 0.72   | 12.80    | 41.98    | 9         | 1.2          | 33 kHz     |
| 28 | 22  | 0.03   | 0.65   | 16.14    | 52.94    | 7         | 0.92         | 42 kHz     |
| 29 | 23  | 0.02   | 0.57   | 20.36    | 66.78    | 4.7       | 0.729        | 53 kHz     |
| 30 | 24  | 0.02   | 0.51   | 25.67    | 84.20    | 3.5       | 0.577        | 68 kHz     |
| 31 | 25  | 0.02   | 0.45   | 32.37    | 106.17   | 2.7       | 0.457        | 85 kHz     |
| 32 | 26  | 0.02   | 0.40   | 40.81    | 133.86   | 2.2       | 0.361        | 107 kHz    |
| 33 | 27  | 0.01   | 0.36   | 51.47    | 168.82   | 1.7       | 0.288        | 130 kHz    |
| 34 | 28  | 0.01   | 0.32   | 64.90    | 212.87   | 1.4       | 0.226        | 170 kHz    |
| 35 | 29  | 0.01   | 0.29   | 81.83    | 268.40   | 1.2       | 0.182        | 210 kHz    |
| 36 | 30  | 0.01   | 0.25   | 103.20   | 338.50   | 0.86      | 0.142        | 270 kHz    |
| 37 | 31  | 0.01   | 0.23   | 130.10   | 426.73   | 0.7       | 0.113        | 340 kHz    |
| 38 | 33  | 0.01   | 0.18   | 206.90   | 678.63   | 0.43      | 0.072        | 540 kHz    |
| 39 | 34  | 0.01   | 0.16   | 260.90   | 855.75   | 0.33      | 0.056        | 690 kHz    |
| 40 | 35  | 0.01   | 0.14   | 329.00   | 1,079.12 | 0.27      | 0.044        | 870 kHz    |
| 41 | 37  | 0.00   | 0.11   | 523.10   | 1,715.00 | 0.17      | 0.0289       | 1350 kHz   |
| 42 | 38  | 0.00   | 0.10   | 659.60   | 2,163.00 | 0.13      | 0.0228       | 1750 kHz   |
| 43 | 39  | 0.00   | 0.09   | 831.80   | 2,728.00 | 0.11      | 0.0175       | 2250 kHz   |
| 44 | 40  | 0.00   | 0.08   | 1,049.00 | 3,440.00 | 0.09      | 0.0137       | 2900 kHz   |
+----+-----+--------+--------+----------+----------+-----------+--------------+------------+
"""
awgtab = tk.Label(f10, text=awg_str)