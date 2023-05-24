# Spectrum of the Given Data

In this project, I draw spectrums of the given data using $Discrete Fourier Transforms$. The type of data file should be **'.xlsx'** or **'.xls'**. Due to the limitation of time, file of **'.xml'** can't be processed. The output picture contains four subpictures. They represent for the original data, spectrum which y-axis means modulus value, spectrum which y-axis means real part value, spectrum which y-axis means imaginary part value in turn.

The main program is named **'drawspec.py'** and there are three hyperparameters as followed.
```
file: the name of the given data.
aim:  data in which column of the file needs to be shift. (it starts from 0)
f: the frequency of sampling.
```
You can change the value of them in the raw program. If you want to process a new file, remember to add the ***aim sheet*** to the mapping variable named **'mp'**. You'd better rename the file in English. Otherwise, there will be some unexpected problems.

The required packets are as followed.
```
xlrd==1.2.0
numpy
matplotlib
```
If you have any questions, please contact me: <michaelzhangziniu@gmail.com>.

Thanks very much!
