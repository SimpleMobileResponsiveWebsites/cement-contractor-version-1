import streamlit as st
import pandas as pd
from datetime import datetime

# Application title
st.title("Cement Company Project Planner")

# Sidebar for user inputs
st.sidebar.header("Project Information")

# Project details
project_type = st.sidebar.selectbox(
    "Select Project Type", ["Driveway", "Walkway", "Patio", "Other"]
)

# Project dimensions
length = st.sidebar.number_input("Project Length (in feet)", min_value=0.0, step=1.0)
width = st.sidebar.number_input("Project Width (in feet)", min_value=0.0, step=1.0)
square_footage = length * width

# Materials selection and cost
material = st.sidebar.selectbox(
    "Select Material", ["Standard Cement", "Stamped Cement", "Exposed Aggregate"]
)

# Cost per square foot based on material
material_cost = {
    "Standard Cement": 10.0,         # Adjust these costs based on your actual pricing
    "Stamped Cement": 15.0,
    "Exposed Aggregate": 20.0
}
cost_per_sqft = material_cost[material]
total_material_cost = square_footage * cost_per_sqft

# Labor cost (this can be fixed or per square foot)
labor_rate_per_sqft = 8.0           # Example labor cost per square foot
total_labor_cost = square_footage * labor_rate_per_sqft
total_cost = total_material_cost + total_labor_cost

# Customer information
st.sidebar.header("Customer Information")
customer_name = st.sidebar.text_input("Customer Name")
customer_email = st.sidebar.text_input("Customer Email")
customer_phone = st.sidebar.text_input("Customer Phone Number")

# Display Project Summary
st.subheader("Project Summary")
st.write(f"**Project Type**: {project_type}")
st.write(f"**Dimensions**: {length} ft x {width} ft")
st.write(f"**Square Footage**: {square_footage:.2f} sq ft")
st.write(f"**Material**: {material}")
st.write(f"**Material Cost**: ${total_material_cost:.2f}")
st.write(f"**Labor Cost**: ${total_labor_cost:.2f}")
st.write(f"**Total Cost**: ${total_cost:.2f}")

# Invoice Generation
st.subheader("Generate Invoice")
if st.button("Create Invoice"):
    # Create an invoice as a DataFrame
    invoice_data = {
        "Item": ["Project Type", "Dimensions", "Square Footage", "Material", "Material Cost", "Labor Cost", "Total Cost"],
        "Description": [
            project_type,
            f"{length} ft x {width} ft",
            f"{square_footage:.2f} sq ft",
            material,
            f"${total_material_cost:.2f}",
            f"${total_labor_cost:.2f}",
            f"${total_cost:.2f}"
        ]
    }
    invoice_df = pd.DataFrame(invoice_data)
    
    # Display invoice
    st.write(f"**Customer Name**: {customer_name}")
    st.write(f"**Customer Email**: {customer_email}")
    st.write(f"**Customer Phone**: {customer_phone}")
    st.write("**Invoice Date**: ", datetime.now().strftime("%Y-%m-%d"))
    st.table(invoice_df)
    
    # Downloadable invoice (optional)
    csv = invoice_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Invoice as CSV",
        data=csv,
        file_name=f"invoice_{customer_name.replace(' ', '_').lower()}.csv",
        mime="text/csv",
    )
else:
    st.write("Fill out all fields and click 'Create Invoice' to generate.")
