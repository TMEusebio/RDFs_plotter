# Radial Distribution Function (RDF) Plotting Script  

## 📌 Description  
This script reads and plots **Radial Distribution Function (RDF)** data for xenon (Xe) interacting with different atomic groups in ethanol. The data is read from a space-separated text file and visualized using `matplotlib`. The script saves the resulting plot as an image.  

## 📂 File Structure  
- `RDFs_A-X.txt` → Input file containing RDF data (ensure correct column names).  
- `RDFs_A-X.png` → Output image of the RDF plot.  
- `RDFs_plot.py` → This script (rename accordingly).  

## 🚀 Usage  
### **1. Install Dependencies**  
Ensure you have the required Python libraries installed:  
```bash
pip install pandas matplotlib
```

### **2. Run the Script
Execute the script in a Python environment:
```bash
python RDFs_plot.py
```

### **3. Output
The script reads RDFs_A-X.txt, extracts RDF functions obtained for A as the reference atom reatively to B, C, D and E, and plots them.
The plot is saved as RDFs_A-X.png.

## 📊 Plot Details
X-axis (r / nm) → Distance in nanometers.
Y-axis (g(r)) → RDF values.
Color & Transparency
A - B: Blue (solid, α=1.0)
A - C: Blue (α=0.5)
A - D: Blue (α=0.3)
A - E: Black (solid)

## ⚠️ Notes
Ensure RDFs_A-X.txt follows the correct format (whitespace-separated).
Modify sep=r'\s+' in pd.read_csv() if needed for different delimiters.
Adjust plot limits (plt.xlim(), plt.ylim()) as needed.

### **4. Multiple plots
For multiple plots on the same .png file run: 
```bash
python Multiple_RDF_plots.py
```
Ensure that the .txt files are well alocated to data1 or data2 lists.

## 🛠️ Author
TEusebio

##License
This project is licensed under the GPL License (aka GNU General Public License v3.0).

