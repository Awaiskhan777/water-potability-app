# Water Potability Prediction System
**An Engineered Machine Learning Pipeline for Safety-Critical Classification**

!
Python
https://img.shields.io/badge/Python−3.8+−blue.svg

!
Scikit−Learn
https://img.shields.io/badge/Scikit−−Learn−ML−orange.svg

!
Streamlit
https://img.shields.io/badge/Streamlit−Deployment−red.svg

!
Status
https://img.shields.io/badge/Status−Complete−brightgreen.svg

## 1. Project Overview
This project presents a robust, end-to-end Machine Learning application designed to predict the potability of water based on nine physiochemical metrics 
pH,Hardness,Solids,Chloramines,Sulfate,Conductivity,OrganicCarbon,Trihalomethanes,andTurbidity
.

Rather than treating this as a standard dataset exercise, this project approaches the problem from a Software Engineering perspective. It features a strictly decoupled backend/frontend architecture, rigorous data profiling, and a deep-dive analysis into the consequences of Class Imbalance and Data Leakage.

## 2. Architecture & Parallel Development Strategy
To ensure efficient development without bottlenecks, the project was divided into two distinct, parallel tracks that merged only during final integration:

* **Role 1: Data & AI Engineer 
TheBrain
**
* Focused entirely on Jupyter Notebooks for data profiling, cleaning, feature scaling, and model optimization.
* *Deliverable:* Serialized .pkl files containing the trained algorithm and scaling parameters.
* **Role 2: Full-Stack/MLOps Engineer 
TheFace
**
* Focused entirely on building the Streamlit Web Interface.
* *Deliverable:* A deployed, interactive web application. Utilized a "Dummy Function" backend during development to prevent blocking while the ML pipeline was being trained.

## 3. Methodology & Key Engineering Decisions
The development of the ML pipeline followed a strict, documented 3-Act structure to ensure scientific rigor:

### Phase 1: Data Profiling & Integrity
Initial analysis revealed massive data sparsity 
missingvaluesinpH,Sulfate,andTrihalomethanes
 and severe feature scale discrepancies 
pH:0−14vs.Solids:20k−60k
.
* **Decision:* `StandardScaler` was implemented as a mandatory Data Transformation step to normalize the feature space for the distance-based SVM. Missing values were resolved via Median Imputation to preserve data volume without introducing outlier skew.

### Phase 2: The Class Imbalance Challenge
The target variable was heavily skewed 
61
, rendering standard "Accuracy" a deceptive metric.
* **Experiment A 
SMOTE
:* Synthetic upsampling successfully balanced the report metrics but introduced synthetic noise into the decision boundary, ultimately degrading real-world generalizability.
* **Experiment B 
Downsampling
:* Random undersampling discarded real data but preserved the authentic physical distribution of the water features.
* **Final Decision:* **Data Integrity supersedes Metric Symmetry.** Given the safety-critical nature of water consumption, generating synthetic water profiles 
SMOTE
 was deemed an unacceptable domain risk. The Downsampled SVM was selected as the final production model.

### Phase 3: Model Optimization & Bias-Variance Trade-off
To maximize the performance of the Downsampled SVM, a 5-Fold Cross-Validated Grid Search was utilized to empirically determine the optimal `C` 
Regularization
 and `Gamma` 
KernelCoefficient
 parameters, optimizing strictly for the **F1-Score**.

## 4. Tech Stack
* **Data Manipulation:* Pandas, NumPy
* **Visualization:* Matplotlib, Seaborn
* **Machine Learning:* Scikit-Learn 
SVM,StandardScaler,GridSearchCV
, Imbalanced-Learn 
SMOTE,RandomUnderSampler

* **MLOps/Deployment:* Streamlit, Joblib, Git/GitHub

### 5. Repository Structure
All project files are kept in the root directory for simple integration with the Streamlit deployment.

```text
├── app.py # Streamlit Frontend Application
├── svm_model.pkl # Serialized SVM Brain (Downsampled)
├── scaler.pkl # Serialized StandardScaler Parameters
├── water_potability.csv # Raw Dataset
├── cleaned_water_data.csv # Processed Dataset (Imputed)
├── requirements.txt # Python dependencies
└── README.md # Project Documentation
```

## 6. Local Installation & Execution
To run this project locally, ensure you have Python 3.8+ installed.

**Step 1: Clone the repository**
```bash
git clone https://github.com/<your-username>/Water-Quality-Engine.git
cd Water-Quality-Engine
```

**Step 2: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Run the Streamlit Application**
```bash
streamlit run app.py
```
*
Note:Becauseoftheflatstructure,app.pywillautomaticallydetectandloadthe.pklfilesfromthesamedirectoryuponuserinput.
*

## 7. Live Deployment
The application is actively deployed and can be accessed via Streamlit Community Cloud:

👉 **
FQy4HArVdBbZ87AHrbfdhSXRgyE5NUbrh6GaL8enMUeh
**

**Developed by:* Muhammad Obaidullah & Awais Khan

**Course:* BS-AI 
4thSemester - Machine Learning