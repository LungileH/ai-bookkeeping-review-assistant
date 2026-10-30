import pandas as pd


def validate_invoices(invoices):
    results = invoices.copy()

    results["Review Issues"] = ""

    required_fields = [
        "invoice_number",
        "supplier",
        "invoice_date",
        "subtotal",
        "vat",
        "invoice_total"
    ]

    for field in required_fields:
        if field not in results.columns:
            results["Review Issues"] += f"Missing column: {field}; "

    if any(field not in results.columns for field in required_fields):
        results["Review Status"] = "Needs Review"
        return results

    for index, row in results.iterrows():
        issues = []

        # Check for missing information
        for field in required_fields:
            if pd.isna(row[field]) or str(row[field]).strip() == "":
                issues.append(f"Missing {field}")

        # Check for duplicate invoices
        if pd.notna(row["invoice_number"]) and pd.notna(row["supplier"]):
            duplicates = (
                (results["invoice_number"] == row["invoice_number"]) &
                (results["supplier"] == row["supplier"])
            )

            if duplicates.sum() > 1:
                issues.append("Possible duplicate invoice")

        # Check whether the invoice total adds up
        try:
            calculated_total = float(row["subtotal"]) + float(row["vat"])
            actual_total = float(row["invoice_total"])

            if abs(calculated_total - actual_total) > 0.01:
                issues.append("Invoice total does not match subtotal + VAT")

        except (ValueError, TypeError):
            issues.append("Invalid amount")

        results.at[index, "Review Issues"] = "; ".join(issues)

    results["Review Status"] = results["Review Issues"].apply(
        lambda issues: "Needs Review" if issues else "Ready for Review"
    )

    return results
