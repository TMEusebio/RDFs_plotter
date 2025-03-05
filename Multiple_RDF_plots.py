import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Replace 'your_file.txt' with the actual file path
# Use 'delimiter' to specify spaces or tabs
data = pd.read_csv('RDFs_A-X.txt', sep=r'\s+')
data1 = pd.read_csv('RDFs_A-Y.txt', sep=r'\s+')

# Extracting the data from data file
r = data['r']
rdf1 = data['B']
rdf2 = data['C']
rdf3 = data['D']
rdf4 = data['E']
rdf5 = data['F']

fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns

# Extracting the data from data1 file
r = data1['r']
rdf6 = data1['G']
rdf7 = data1['H']


# Plotting the RDFs (same as before)
# First subplot
axes[0].plot(r, rdf1, label='A - B', color='green', linestyle='-', linewidth=2)
axes[0].plot(r, rdf2, label='A - C', color='blue', linestyle='-', linewidth=2)
axes[0].plot(r, rdf3, label='A - D', color='red', linestyle='-', linewidth=2)

axes[0].set_title('RDFs(A-X1)', fontsize=12)
axes[0].set_xlabel('r / nm', fontsize=12)
axes[0].set_ylabel('g(r)', fontsize=12)
axes[0].legend(fontsize=8)
axes[0].grid(True)
axes[0].set_xlim(0, 2)
axes[0].set_ylim(0, 8)

# Second subplot
axes[1].plot(r, rdf4, label= "A - E" , color='green', alpha = 1, linestyle='-', linewidth=2)
axes[1].plot(r, rdf5, label='A - F', color='green', alpha = 0.9, linestyle='-',  linewidth=2)

axes[1].set_title('RDFs(A-X2', fontsize=12)
axes[1].set_xlabel('r / nm', fontsize=12)
axes[1].set_xlim(0, 2)
axes[1].set_ylim(0, 8)
axes[1].set_ylabel('g(r)', fontsize=12)
axes[1].legend(fontsize=8)
axes[1].grid(True)

# Third subplot
axes[2].plot(r, rdf6, label='A - G', color='blue', alpha = 1, linestyle='-', linewidth=2)
axes[2].plot(r, rdf7, label='A - H', color='blue', alpha= 0.5, linestyle='-', linewidth=2)

axes[2].set_title('RDFs(A-Y)', fontsize=12)
axes[2].set_xlabel('r / nm', fontsize=12)
axes[2].set_ylabel('g(r)', fontsize=12)
axes[2].legend(fontsize=8)
axes[2].grid(True)
axes[2].set_xlim(0, 2)
axes[2].set_ylim(0, 8)


# Set decimal places for each subplot
axes[0].xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))  # 2 decimal places for x-axis
axes[0].yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))  # 3 decimal places for y-axis

axes[1].xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))  # 1 decimal place for x-axis
axes[1].yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))  # 2 decimal places for y-axis

axes[2].xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))  # 1 decimal place for x-axis
axes[2].yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))  # 2 decimal places for y-axis

plt.savefig('RDFs_A-multiple.png')
plt.show()
