import streamlit as st
import pandas as pd
from invoice_validator import validate_invoices

st.set_page_config(
    page_title="AI Bookkeeping Review Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("AI Bookkeeping Review Assistant")

st.write(
    "An assistant designed to help bookkeeping teams review invoices, "
    "identify discrepancies and improve financial accuracy."
)

st.info("This is an early prototype. Use fictional test data only.")

st.header("Invoice Upload")

uploaded_file = st.file_uploader(
    "Upload an invoice CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        invoices = pd.read_csv(uploaded_file)

        st.success("File uploaded successfully!")

        st.subheader("Original Invoice Records")
        st.dataframe(invoices, use_container_width=True)

        st.header("Invoice Validation")

        reviewed_invoices = validate_invoices(invoices)

        total_invoices = len(reviewed_invoices)
        flagged_invoices = (
            reviewed_invoices["Review Status"] == "Needs Review"
        ).sum()
        ready_invoices = (
            reviewed_invoices["Review Status"] == "Ready for Review"
        ).sum()

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Invoices", total_invoices)
        col2.metric("Needs Review", int(flagged_invoices))
        col3.metric("Ready for Review", int(ready_invoices))

        st.subheader("Validation Results")
        st.dataframe(reviewed_invoices, use_container_width=True)

    except Exception as error:
        st.error(f"Unable to process this file: {error}")

else:
    st.write("Upload a CSV file to begin invoice validation.")

st.caption(
    "Future features: AI invoice extraction, transaction matching "
    "and human approval."
)
        
