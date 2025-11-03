from gtts import gTTS
import pandas as pd
from datetime import datetime
import os
 
# ---- Step 1: Load Your Dataset ----
# Replace 'your_data.csv' with your actual file"C:\Users\Administrator\Music\Status\PowerBI\Tracmed\hospital_management_analytics 3.xlsx"
df = pd.read_csv()  # or pd.read_excel("clinical_data.xlsx")
 
# ---- Step 2: Data Summary Logic ----
# Total patients
total_patients = df['Patient_ID'].nunique()
 
# Average length of stay
df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])
df['Discharge_Date'] = pd.to_datetime(df['Discharge_Date'])
df['Stay_Days'] = (df['Discharge_Date'] - df['Admission_Date']).dt.days
avg_stay = round(df['Stay_Days'].mean(), 1)
 
# Mortality rate
mortality_rate = round((df['Mortality'].sum() / total_patients) * 100, 1)
 
# Complication rate
complication_rate = round((df['Complications'].sum() / total_patients) * 100, 1)
 
# Patient satisfaction
avg_satisfaction = round(df['Satisfaction_Score'].mean(), 1)
 
# Treatment with most complications
top_complication_treatment = df.groupby("Treatment_Type")["Complications"].sum().idxmax()
 
# Protocol compliance
avg_compliance = round(df['Compliance'].mean(), 2)
 
# Readmission risk by condition (if column exists)
if 'Condition' in df.columns and 'Readmitted' in df.columns:
    high_risk_conditions = df[df['Readmitted'] == 1]['Condition'].value_counts().head(3).index.tolist()
    readmission_risks = ', '.join(high_risk_conditions)
else:
    readmission_risks = "N/A"
 
# ---- Step 3: Narrative Construction ----
summary = f"""
Welcome to the Clinical Outcomes and Patient Safety Dashboard.
 
From the dataset, a total of {total_patients} patients were treated with an average stay of {avg_stay} days and a low mortality rate of {mortality_rate}%.
The complication rate stands at {complication_rate}%, and patient satisfaction averages {avg_satisfaction} out of 5.
 
The highest number of complications occurred in {top_complication_treatment} treatments.
Protocol compliance is {avg_compliance}%, with the best adherence observed in medication and vaccination-related procedures.
 
The top conditions with highest readmission risks include {readmission_risks}.
 
This dashboard highlights critical care gaps, supports adherence improvements, and aims to reduce readmissions through actionable data insights.
"""
 
# ---- Step 4: Convert to Audio ----
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
audio_filename = f"Clinical_Outcome_Summary_{timestamp}.mp3"
 
tts = gTTS(text=summary, lang='en')
tts.save(audio_filename)
 
print("✅ Audio summary saved as:", audio_filename)
 
# Optional: Play audio
try:
    from playsound import playsound
    playsound(audio_filename)
except:
    print("🔊 Install 'playsound' to hear the audio.")