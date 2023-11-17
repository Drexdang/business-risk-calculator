import streamlit as st

def calculate_debt_to_capital_ratio(debt, equity):
    total_capital = debt + equity
    return debt / total_capital if total_capital != 0 else 0.0

def calculate_debt_to_equity_ratio(debt, equity):
    return debt / equity if equity != 0 else float('inf')  # Handle infinite ratio for debt-to-equity

def calculate_interest_coverage_ratio(ebit, interest_expense):
    return ebit / interest_expense if interest_expense != 0 else float('inf')  # Handle infinite ratio for interest coverage

def calculate_degree_of_combined_leverage(percentage_change_eps, percentage_change_revenue):
    return percentage_change_eps / percentage_change_revenue

def calculate_percentage_change(current_value, previous_value):
    return ((current_value - previous_value) / previous_value) * 100 if previous_value != 0 else float('inf')


# Markdown and Headings
html_temp = """ 
<div style="background-color: gold; padding: 16px">
<h2 style="color: blue; text-align: center;">Financial Ratios Calculator</h2>
</div>
"""

st.markdown(html_temp, unsafe_allow_html=True)
st.write('')
st.write('')

# Streamlit UI
st.subheader("Financial Ratios For Business Risk Analysis")

# Information display
st.write("""
Financial ratios can be used to assess a company's capital structure and current risk levels. 
Some commonly used ratios include:
- Debt-to-Capital Ratio
- Debt-to-Equity Ratio (D/E)
- Interest Coverage Ratio
- Degree of Combined Leverage (DCL)

These ratios provide insights into a company's financial health, risk levels, and ability to manage its debt.

### Insights and Interpretation:

- **Debt-to-Capital Ratio:**
  - Measures the proportion of debt in a company's capital structure.
  - Lower ratios are preferred, indicating a higher proportion of equity financing.

- **Debt-to-Equity Ratio (D/E):**
  - Compares debt financing to equity financing.
  - Lower ratios suggest financing through own resources, which is preferable.

- **Interest Coverage Ratio:**
  - Indicates the company's ability to handle short-term financing costs.
  - Higher ratios indicate effective handling of interest payments.

- **Degree of Combined Leverage (DCL):**
  - Assesses total risk by considering both operating and financial leverage.
  - Higher DCL suggests more fixed costs, indicating higher risk.

### Percentage Change:
- **Percentage Change in EPS:**
  - Represents the percentage change in Earnings Per Share.
  - Positive values indicate growth, while negative values may indicate decline.

- **Percentage Change in Revenue:**
  - Reflects the percentage change in total revenue.
  - Positive values suggest sales growth.

""")

# User input layout
# User input layout
col1, col2 = st.columns(2)

with col1:
    debt = st.number_input("Total Debt:", value=0.0)
    equity = st.number_input("Shareholders' Equity:", value=0.0)
    ebit = st.number_input("EBIT:", value=0.0)
    interest_expense = st.number_input("Interest Expense:", value=0.0)

with col2:
    current_eps = st.number_input("Current EPS:", value=0.0)
    previous_eps = st.number_input("Previous EPS:", value=0.0)
    current_revenue = st.number_input("Current Gross Revenue:", value=0.0)
    previous_revenue = st.number_input("Previous Gross Revenue:", value=0.0)

# Calculate ratios
debt_to_capital_ratio = calculate_debt_to_capital_ratio(debt, equity)
debt_to_equity_ratio = calculate_debt_to_equity_ratio(debt, equity)
interest_coverage_ratio = calculate_interest_coverage_ratio(ebit, interest_expense)
percentage_change_eps = calculate_percentage_change(current_eps, previous_eps)
percentage_change_revenue = calculate_percentage_change(current_revenue, previous_revenue)
degree_of_combined_leverage = calculate_degree_of_combined_leverage(percentage_change_eps, percentage_change_revenue)

# Display results
st.subheader("Financial Ratios:")
st.write(f"- Debt-to-Capital Ratio: {debt_to_capital_ratio:.2%}")
st.write(f"- Debt-to-Equity Ratio (D/E): {debt_to_equity_ratio:.2%}")
st.write(f"- Interest Coverage Ratio: {interest_coverage_ratio:.2f}")
st.write(f"- Degree of Combined Leverage (DCL): {degree_of_combined_leverage:.2f}")

st.subheader("Percentage Change:")
st.write(f"- Percentage Change in EPS: {percentage_change_eps:.2f}%")
st.write(f"- Percentage Change in revenue: {percentage_change_revenue:.2f}%")



st.subheader("Thanks for visiting,hope the information and calculations here were helpful?")