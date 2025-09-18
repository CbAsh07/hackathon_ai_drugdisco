# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Page configuration
# ---------------------------
st.set_page_config(
    page_title="AI-Powered BGC Discovery",
    page_icon="🧬",
    layout="wide"
)

# ---------------------------
# Landing / Hero Section
# ---------------------------
st.title("🧬 AI4Disco: AI-Powered BGC Discovery Platform")
st.markdown("""
**Problem:** The world is running out of effective antibiotics and anticancer drugs.  
**Solution:** Our platform uses AI to scan microbial genomes, detect biosynthetic gene clusters (BGCs), and prioritize top candidates for new drugs.
""")

st.markdown("---")

# ---------------------------
# Mock Genome Upload Section
# ---------------------------
st.header("Upload Genome (Demo)")
uploaded_file = st.file_uploader("Upload microbial genome (FASTA/GenBank)", type=["fasta", "gbk"])

if uploaded_file:
    st.success("Genome uploaded successfully! Running AI pipeline...")
    st.info("Showing mock results for demo purposes.")

# ---------------------------
# Mock BGC Results
# ---------------------------
st.header("Detected Biosynthetic Gene Clusters (BGCs)")

clusters = pd.DataFrame([
    {"Cluster ID": "Cluster 1", "Type": "NRPS", "Novelty": 0.85, "Drug-likeness": 0.76},
    {"Cluster ID": "Cluster 2", "Type": "PKS", "Novelty": 0.92, "Drug-likeness": 0.89},
    {"Cluster ID": "Cluster 3", "Type": "RiPP", "Novelty": 0.40, "Drug-likeness": 0.55},
    {"Cluster ID": "Cluster 4", "Type": "Terpene", "Novelty": 0.70, "Drug-likeness": 0.65},
])

st.dataframe(clusters)

# ---------------------------
# Novelty vs Drug-likeness Chart
# ---------------------------
st.header("Novelty vs Drug-likeness")

fig, ax = plt.subplots(figsize=(8,5))
ax.scatter(clusters["Novelty"], clusters["Drug-likeness"], c="green", s=120)

for i, row in clusters.iterrows():
    ax.text(row["Novelty"] + 0.01, row["Drug-likeness"], row["Cluster ID"], fontsize=9)

ax.set_xlabel("Novelty Score")
ax.set_ylabel("Drug-likeness Score")
ax.set_title("Cluster Prioritization")
ax.set_xlim(0,1)
ax.set_ylim(0,1)
st.pyplot(fig)

# ---------------------------
# How It Works Section
# ---------------------------
st.header("How It Works")
st.markdown("""
1. **Genome Scanning:** Upload microbial genomes.  
2. **BGC Detection:** AntiSMASH detects biosynthetic gene clusters.  
3. **Clustering & Analysis:** BiG-SCAPE groups similar clusters and calculates novelty.  
4. **AI Prioritization:** Machine learning ranks top candidates based on novelty and drug potential.  
5. **Result Dashboard:** View top clusters, novelty score, and drug-likeness for each BGC.
""")

# ---------------------------
# Partnerships / Impact
# ---------------------------
st.header("🌍 Partnerships & Impact")
st.markdown("""
- Collaborate with **pharma, biotech startups, and government research institutes**  
- Accelerate **drug discovery from natural products**  
- Reduce **R&D costs and failure rates**  
- Focus research on **high-priority, novel biosynthetic clusters**
""")

# ---------------------------
# Footer / Call to Action
# ---------------------------
st.markdown("---")
st.markdown("💡 *This is a demo prototype for the Smart India Hackathon. In the full version, antiSMASH and BiG-SCAPE run in the backend, and AI ranks clusters in real-time.*")
