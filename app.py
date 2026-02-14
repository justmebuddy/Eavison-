# app.py
import streamlit as st
import pandas as pd
import sqlite3
from risk import score_url

# Configure the page
st.set_page_config(page_title="SecureStack Dashboard", layout="wide")

st.title("🛡️ SecureStack Scanner")
st.markdown("---")

# Sidebar for input
with st.sidebar:
    st.header("Scan Configuration")
    target_url = st.text_input("Enter Target URL", placeholder="https://example.com")
    scan_button = st.button("Start Scan")

# Main Dashboard Area
if scan_button and target_url:
    st.info(f"Initiating scan on: {target_url}")
    
    # --- Perform Scanning Logic ---
    # In a real scenario, this would import main.py and run the scan
    # For now, we simulate the results to demonstrate the UI
    
    with st.spinner("Analyzing attack surface and bypassing WAFs..."):
        # Placeholder for actual scanning logic
        import time
        time.sleep(2) 
        
    st.success("Scan Completed!")
    
    # --- Display Results ---
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Risk Assessment")
        risk = score_url(target_url)
        
        # Color coding the risk level
        if risk == "High Risk":
            st.error(f"## {risk}")
        elif risk == "Medium Risk":
            st.warning(f"## {risk}")
        else:
            st.success(f"## {risk}")
            
    with col2:
        st.subheader("Data Summary")
        # Simulating data fetching from SQLite
        data = {
            "URL": [target_url, f"{target_url}/login", f"{target_url}/search?q=test"],
            "Risk": ["Low", "High", "Medium"]
        }
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

    st.markdown("---")
    st.subheader("Detailed Findings")
    
    # Simulated Findings Table
    findings_data = {
        "URL": [f"{target_url}/login", f"{target_url}/search"],
        "Issue Type": ["SQL Injection indicator", "Possible XSS pattern"],
        "Severity": ["Critical", "High"]
    }
    findings_df = pd.DataFrame(findings_data)
    
    # Displaying findings with color coding
    st.dataframe(
        findings_df.style.map(
            lambda x: 'background-color: #ffcccc' if x == 'Critical' else 'background-color: #ffe6cc',
            subset=['Severity']
        ),
        use_container_width=True
    )

elif scan_button and not target_url:
    st.warning("Please enter a valid URL.")
