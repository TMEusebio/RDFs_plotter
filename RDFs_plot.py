import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.txt' with the actual file path
# Use 'delimiter' to specify spaces or tabs
data = pd.read_csv('RDFs_A-X.txt', sep=r'\s+')

# Extracting the data
r = data['r']
rdf1 = data['B']
rdf2 = data['C']
rdf3 = data['D']
rdf4 = data['E']

# Plotting the RDFs (same as before)
plt.figure(figsize=(8, 6))
plt.plot(r, rdf1, label='A - B', color='blue', alpha = 1, linestyle='-', linewidth=2)
plt.plot(r, rdf2, label='A - C', color='blue', alpha= 0.5, linestyle='-', linewidth=2)
plt.plot(r, rdf3, label='A - D', color='blue', alpha = 0.3, linestyle='-', linewidth=2)
plt.plot(r, rdf4, label='A - E', color='black', linestyle='-', linewidth=2)
plt.title('Radial Distribution Function', fontsize=16)
plt.xlabel('r / nm', fontsize=14)
plt.xlim(0, 2)
plt.ylim(0, 4)
plt.ylabel('g(r)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)

plt.savefig('RDFs_A-X.png')
plt.show()
