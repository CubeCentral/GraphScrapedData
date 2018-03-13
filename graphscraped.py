import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# This is a temporary measure
# This is the path to the output of scrapentpmon.py (which creates this file)
tempargs_o = "./IndexedOutput.csv"

# This is code that will validate the path/filename for the input file, used later
IndexedDataFilePath = Path(tempargs_o)
IndexedDataFilePath = IndexedDataFilePath.expanduser()
print("Using:",IndexedDataFilePath)

# Read in Indexed Output file
IndexedDataFile = open(str(IndexedDataFilePath),'r')
IndexedData=pd.read_csv(IndexedDataFile,names=['ts_epoch','ts','offset','step','score','leap'])
IndexedDataFile.close()
lenIndexedData=len(IndexedData.index)
print("OK",lenIndexedData,"Rows read in")

# Check for existing header row in file
TestDupeHeader = IndexedData.columns == IndexedData.iloc[0]
if TestDupeHeader.all():
    # Drop that row containing header
    IndexedData.drop(IndexedData.head(1).index, inplace=True)

#
# Here is the start of the plotting
# Can't seem to get the y-axis formatting right
# also very slow for large datasets
#

fig = plt.figure()
ax = plt.axes()

x = IndexedData['ts']
y1 = IndexedData['offset']

plt.plot(x,y1)

plt.xlabel('Date')
plt.ylabel('offset')
plt.title('Date vs offset')

plt.xticks(rotation=90)

plt.show()

# raise SystemExit(1)