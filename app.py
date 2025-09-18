#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 15:50:09 2025

@author: cb_ash
"""

# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Page configuration
# ---------------------------
st.set_page_config(
    page_title="AI$Disco: AI-Powered BGC Discovery",
    page_icon="🧬",
    layout="wide"
)

# ---------------------------
# Custom CSS for font sizes
# ---------------------------
st.markdown("""
    <style>
    .big-font {
        font-size:28px !important;
        font-weight: bold;
    }
    .medium-font {
        font-size:22px !important;
    }
    .small-font {
        font-size:18px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Landing / Hero Section
# ---------------------------
st.markdown('<p class="big-font">🧬 AI-Powered BGC Discovery Platform</p>', unsafe_allow_html=True)

st.markdown("""
<p class="medium-font"><b>Problem:</b> The world is running out of effective antibiotics and anticancer drugs.</p>
<p class="medium-font"><b>Solution:</b> Our platform uses AI to scan microbial genomes, detect biosynthetic gene clusters (BGCs), and prioritize top candidates for new drugs.</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------
# Mock Genome Upload Section
# ---------------------------
st.markdown('<p class="big-font">Upload Genome (Demo)</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload microbial genome (FASTA/GenBank)", type=["fasta", "gbk"])

if uploaded_file:
    st.success("Genome uploaded successfully! Running AI pipeline...")
    st.info("Showing mock results for demo purposes.")

# ---------------------------
# Mock BGC Results
# ---------------------------
st.markdown('<p class="big-font">Detected Biosynthetic Gene Clusters (BGCs)</p>', unsafe_allow_html=True)

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
st.markdown('<p class="big-font">Novelty vs Drug-likeness</p>', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(8,5))
ax.scatter(clusters["Novelty"], clusters["Drug-likeness"], c="green", s=120)

for i, row in clusters.iterrows():
    ax.text(row["Novelty"] + 0.01, row["Drug-likeness"], row["Cluster ID"], fontsize=12)

ax.set_xlabel("Novelty Score", fontsize=14)
ax.set_ylabel("Drug-likeness Score", fontsize=14)
ax.set_title("Cluster Prioritization", fontsize=16)
ax.tick_params(axis="both", labelsize=12)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
st.pyplot(fig)

# ---------------------------
# How It Works Section
# ---------------------------
st.markdown('<p class="big-font">How It Works</p>', unsafe_allow_html=True)
st.markdown("""
<p class="medium-font">1. <b>Genome Scanning:</b> Upload microbial genomes.</p>
<p class="medium-font">2. <b>BGC Detection:</b> AntiSMASH detects biosynthetic gene clusters.</p>
<p class="medium-font">3. <b>Clustering & Analysis:</b> BiG-SCAPE groups similar clusters and calculates novelty.</p>
<p class="medium-font">4. <b>AI Prioritization:</b> Machine learning ranks top candidates based on novelty and drug potential.</p>
<p class="medium-font">5. <b>Result Dashboard:</b> View top clusters, novelty score, and drug-likeness for each BGC.</p>
""", unsafe_allow_html=True)

# ---------------------------
# Partnerships / Impact
# ---------------------------
st.markdown('<p class="big-font">🌍 Partnerships & Impact</p>', unsafe_allow_html=True)
st.markdown("""
<p class="medium-font">- Collaborate with <b>pharma, biotech startups, and government research institutes</b></p>
<p class="medium-font">- Accelerate <b>drug discovery from natural products</b></p>
<p class="medium-font">- Reduce <b>R&D costs and failure rates</b></p>
<p class="medium-font">- Focus research on <b>high-priority, novel biosynthetic clusters</b></p>
""", unsafe_allow_html=True)

# ---------------------------
# Footer / Call to Action
# ---------------------------
st.markdown("---")
st.markdown('<p class="small-font">💡 <i>This is a demo prototype for the Smart India Hackathon. In the full version, antiSMASH and BiG-SCAPE run in the backend, and AI ranks clusters in real-time.</i></p>', unsafe_allow_html=True)
