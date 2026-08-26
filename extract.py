import fitz
import os

base = r'C:\Users\chaya\Documents\Obsidian\Thesis'
papers = [
    'raw_sources/2023_Cheng_VMD_Prophet_LSTM.pdf',
    'raw_sources/2025_Vertical_Federated_Learning_Method_for_EV_Charging_Station_Load_Prediction.pdf',
    'raw_sources/2025_Deep_Learning_Predicts_Real_World_Electric_Vehicle_DC_Charging_Profiles_and_Durations.pdf',
    'raw_sources/2025_Multi_View_Graph_Contrastive_Representative_Learning_for_Intrusion_Detection_in_EV_Charging_Station.pdf',
    'raw_sources/2025_Personalized_Federated_Learning_for_Household_Electricity_Load_Prediction_with_Imbalanced_Historical_Data.pdf',
    'raw_sources/2026_PC_M3_Physics_Constrained_Mamba_MIMO_Aggregator_Real_Time_Energy_Management_EV_Clusters.pdf',
    'raw_sources/2026_When_Mamba_Meets_KAN_Hybrid_Learning_Network_EV_Charging_Demand_Prediction.pdf',
    'raw_sources/2026_Mamba_3_Improved_Sequence_Modeling_using_State_Space_Principles.pdf'
]

for i, p in enumerate(papers):
    filepath = os.path.join(base, p)
    try:
        doc = fitz.open(filepath)
        text = ''.join(page.get_text() for page in doc)
        with open(os.path.join(base, f'extract_{i}.txt'), 'w', encoding='utf-8') as f:
            f.write(text)
    except Exception as e:
        print(f"Error on {p}: {e}")

print("Extraction complete")
