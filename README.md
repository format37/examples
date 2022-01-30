### Merger
Python script, made for data aggregation from several Excel files to a new one.
### Requirements 
Every original Excel file must have columns:  
```
Patient_ID  
Filename  
```
Also, at least one of the following columns:  
```
AFL  
sinus  
Afib  
non.AFL  
non.sinus  
non.Afib  
```
Original Excel files should be in a folder without hierarchy, alone, without extra files.
### installation
Install required python libraries
```
python3 -m pip install -r requirements.txt
```
### Usage
1. Place the original Excel files in an empty folder.
2. Run the script, specifying the path to the file and the name of the output file. 
```
python3 merger.py in/ out.xlsx
```
3. After the script finishes running, a new file will appear next to it. If a file with the same name already existed before, it will be replaced with a new one.

### Code explanation
- The script receives two parameters as input:
1. Path to original files
2. Name of the resulting file
- All files in the folder are read.
- Records on the first sheet of each file are grouped by the Filename column. For all columns, the Average value in the group is calculated. It turns out the average value for each Filename
- Groups derived from these Excel files are added to a new single Dataframe. 
Different files present different columns of data. In one file it can be sinus and AFL, and in another AFL and non.AFL. Therefore, after adding to the general frame, some cells take on the value of NAN.
- The columns listed below would be renamed accordingly:
```
AFL -> F  
sinus -> S  
Afib -> A  
non.AFL -> NF  
non.sinus -> NS  
non.Afib -> NA  
```
- Entries are again grouped by Filename, with the calculation of the maximum value.
- Added empty columns: 
```
class3
class2
Afib
non.Afib
class2_actual
class2_predicted
```
- The columns will be ordered according to the requirements:
Patient_ID, Filename, SDRR, SDPR, MPv, MRR, SDRR_ratio, SDPR_ratio, MPv_ratio, SDVm130_ratio, MRR_ratio, class3, class2, Afib, non.Afib, class2_actual, class2_predicted, F, S, A, NF, NS, NA  
Only the listed columns are included in the result.
- Sorting by columns:
```
Patient_ID, Filename
```
- Dataframe would be saved to output Excel file
