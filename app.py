import streamlit as st
import pandas as pd

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

st.info(
    "This is an early prototype. All uploaded information should be "
    "fictional test data, not real client or financial records."
)

st.header("Invoice Upload")

uploaded_file = st.file_uploader(
    "Upload an invoice CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        invoices = pd.read_csv(uploaded_file)

        st.success("File uploaded successfully!")

        st.subheader("Invoice Records")
        st.dataframe(invoices, use_container_width=True)

        st.write(f"**Total records uploaded:** {len(invoices)}")

    except Exception as error:
        st.error(f"Unable to read this file: {error}")

else:
    st.write("No invoice file uploaded yet.")

st.header("Invoice Review")

sample_data = {
    "Invoice Number": ["INV-001", "INV-002", "INV-003"],
    "Supplier": ["ABC Supplies", "Office Solutions", "XYZ Services"],
    "Invoice Total": [1250.00, 875.50, 2100.00],
    "Review Status": ["Matched", "Needs Review", "Pending"]
}

review_data = pd.DataFrame(sample_data)

st.dataframe(review_data, use_container_width=True)

st.caption(
    "Future features: invoice matching, duplicate detection, "
    "discrepancy alerts and human approval."
)
