## You can run this by typing the command 'streamlit run Stock_Dashboard.py' in terminal 

import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px

st.title('Company Insights')
ticker=st.sidebar.text_input('Ticker')

import streamlit as st

# Based on the insights and data provided to us by the llm model, we will now be generating visualiations and sharing our derived insights from the app
# Define the data
data = {
    'Metric': ['Revenue', 'Gross Margin', 'Operating Expenses', 'Net Income', 'Earnings Per Share', 'Cash and Cash Equivalents'],
    '2021': [365.8, 39.8, 43.9, 94.7, 5.67, 23.6],
    '2023': [383.3, 40.3, 54.8, 97.0, 6.13, 30.7]
}

# Convert data to a DataFrame for plotting
df = pd.DataFrame(data)

# Define a function to create a visualization with insights and a bar chart using Plotly
def visualize_data_with_insights_and_chart(df):
    st.title('Apple Financial Performance Visualization')

    for i, row in df.iterrows():
        st.subheader(row['Metric'])
        st.write(f"2021: ${row['2021']} billion")
        st.write(f"2023: ${row['2023']} billion")

        # Add insights
        if row['Metric'] == 'Revenue':
            growth = ((row['2023'] - row['2021']) / row['2021']) * 100
            st.write(f"Growth Rate: {growth:.2f}%")
            st.write("Key Drivers: Strong demand for products like iPhone, Mac, and iPad.")
        elif row['Metric'] == 'Gross Margin':
            st.write("Stable gross margin indicates pricing power and cost control.")
        elif row['Metric'] == 'Operating Expenses':
            increase = ((row['2023'] - row['2021']) / row['2021']) * 100
            st.write(f"Increase in Operating Expenses: {increase:.2f}%")
            st.write("Driven by higher research and development costs, and increased spending on marketing and sales.")
        elif row['Metric'] == 'Net Income':
            st.write("Steady growth in net income driven by strong revenue growth and stable gross margin.")
        elif row['Metric'] == 'Earnings Per Share':
            st.write("Growth in earnings per share due to strong net income growth and share buyback program.")
        elif row['Metric'] == 'Cash and Cash Equivalents':
            st.write("Significant increase in cash and cash equivalents due to strong cash flow from operations.")

        st.write('---')  # Add a separator between sections

    # Create a bar chart using Plotly
    st.subheader('Bar Chart')
    fig = px.bar(df, x='Metric', y=['2021', '2023'], title='Financial Metrics Comparison', barmode='group')
    st.plotly_chart(fig)
    st.write("- Apple has shown steady revenue growth, driven by strong demand for its products.")
    st.write("- The company has maintained a stable gross margin, indicating effective cost management.")
    st.write("- Operating expenses have increased, reflecting investments in research, marketing, and sales.")
    st.write("- Apple's net income and earnings per share have also grown steadily.")
    st.write("- The company has a strong cash position, with significant cash and cash equivalents.")


insights, financials = st.tabs(["Insights", "Fundamental Data"])

# Define the data for Microsoft Corporation
data_msft = {
    'Metric': ['Revenue Growth', 'Profitability', 'Financial Strength', 'Valuation', 'Risks'],
    '2021': [168088, 61271, 34704, 285.26, 'Competition, Cloud Market, Global Operations'],
    '2023': [211915, 72361, 34704, 333.19, 'Competition, Cloud Market, Global Operations']
}

# Convert data to a DataFrame for plotting
df_msft = pd.DataFrame(data_msft)

# Define a function to create a visualization with insights and a bar chart using Plotly
def visualize_msft_data_with_insights_and_chart(df):
    st.title('Microsoft Corporation Insights')

    for i, row in df.iterrows():
        st.subheader(row['Metric'])
        if row['Metric'] == 'Revenue Growth':
            growth_rate = ((row['2023'] - row['2021']) / row['2021']) * 100
            st.write(f"Revenue Growth Rate: {growth_rate:.2f}%")
            st.write(f"2021: ${row['2021']} million")
            st.write(f"2023: ${row['2023']} million")
        elif row['Metric'] == 'Profitability':
            increase = ((row['2023'] - row['2021']) / row['2021']) * 100
            st.write(f"Profitability Increase: {increase:.2f}%")
            st.write(f"Net Income 2021: ${row['2021']} million")
            st.write(f"Net Income 2023: ${row['2023']} million")
        elif row['Metric'] == 'Financial Strength':
            st.write(f"Cash and Cash Equivalents: ${row['2023']} million")
            st.write(f"Total Liabilities: ${row['2023']} million")
        elif row['Metric'] == 'Valuation':
            st.write(f"Stock Price 2021: ${row['2021']}")
            st.write(f"Stock Price 2023: ${row['2023']}")
            st.write(f"P/E Ratio: {row['2023'] / row['2021']:.1f}")
        elif row['Metric'] == 'Risks':
            st.write("Risks:")
            for risk in row['2023'].split(','):
                st.write(f"- {risk.strip()}")

        st.write('---')  # Add a separator between sections

    # Create a bar chart using Plotly
    st.subheader('Bar Chart')
    fig = px.bar(df.melt(id_vars='Metric', var_name='Year', value_name='Value'), x='Metric', y='Value', color='Year',
             title='Financial Metrics Comparison', barmode='group')
    st.plotly_chart(fig)
    # Relevant insights
    st.subheader('Relevant Insights')
    st.write("- Microsoft has shown significant revenue growth over the past three years, driven by strong demand for its cloud-based solutions.")
    st.write("- The company has successfully increased its profitability, focusing on cost optimization and high-margin cloud services.")
    st.write("- Microsoft maintains a strong financial position with substantial cash reserves and manageable debt levels.")
    st.write("- The stock's performance has been positive, with an increase in stock price and a relatively high P/E ratio.")
    st.write("- However, investors should consider the competitive landscape and risks associated with the technology sector.")

# Call the function to display the visualization with insights and a bar chart using Plotly for Microsoft data

financial_data = {
    'Metric': ['Cash and cash equivalents', 'Short-term investments', 'Accounts receivable, net', 'Inventories',
               'Other current assets', 'Total current assets', 'Property and equipment, net',
               'Operating lease right-of-use assets', 'Equity investments', 'Goodwill', 'Intangible assets, net',
               'Other long-term assets', 'Accounts payable', 'Current portion of long-term debt', 'Accrued compensation',
               'Short-term income taxes', 'Short-term unearned revenue', 'Other current liabilities',
               'Total current liabilities', 'Long-term debt', 'Long-term income taxes', 'Long-term unearned revenue',
               'Deferred income taxes', 'Operating lease liabilities', 'Other long-term liabilities',
               'Common stock and paid-in capital', 'Retained earnings', 'Accumulated other comprehensive income (loss)',
               'Total stockholders equity'],
    '2021': [13931, 90826, 44261, 3742, 16924, 169684, 74398, 13148, 6891, 67886, 11298, 21897,
             19000, 2749, 10661, 4067, 45538, 13067, 95082, 47032, 26069, 2912, 230, 11489, 15526,
             86939, 84281, 4678, 166542],
    '2023': [34704, 76558, 48688, 2500, 21807, 184257, 95641, 14346, 9879, 67886, 9366, 30601,
             18095, 5247, 11009, 4152, 50901, 14745, 104149, 41990, 25560, 2912, 433, 12728, 17981,
             93718, 118848, 6343, 206223]
}

# Convert data to a DataFrame for plotting
df_financial = pd.DataFrame(financial_data)

# Define a function to create a visualization with insights and a bar chart using Plotly
def visualize__msft_financial_data_with_insights_and_chart(df):
    st.title('Microsoft Company Financials Visualization')

    for i, row in df.iterrows():
        st.subheader(row['Metric'])
        st.write(f"2021: ${row['2021']} million")
        st.write(f"2023: ${row['2023']} million")

        # Add insights
        if row['Metric'] == 'Cash and cash equivalents':
            increase = ((row['2023'] - row['2021']) / row['2021']) * 100
            st.write(f"Increase: {increase:.2f}%")
            st.write("Driven by increase in cash reserves.")
        elif row['Metric'] == 'Short-term investments':
            decrease = ((row['2021'] - row['2023']) / row['2021']) * 100
            st.write(f"Decrease: {decrease:.2f}%")
            st.write("Reduction in short-term investments.")
        # Add insights for other metrics

        st.write('---')  # Add a separator between sections

    # Create a bar chart using Plotly
    st.subheader('Bar Chart')
    fig = px.bar(df, x='Metric', y=['2021', '2023'], title='Financial Metrics Comparison', barmode='group')
    st.plotly_chart(fig)

# Define the financial data for Apple
apple_financial_data = {
    'Metric': ['Cash and cash equivalents', 'Marketable securities', 'Accounts receivable, net', 'Vendor non-trade receivables',
               'Inventories', 'Other current assets', 'Marketable securities (Non-current)', 'Property, plant and equipment, net',
               'Other non-current assets', 'Accounts payable', 'Other current liabilities', 'Deferred revenue', 'Commercial paper',
               'Term debt (Current)', 'Term debt (Non-current)', 'Other non-current liabilities', 'Total shareholders equity'],
    '2021': [23646, 24658, 28184, 32748, 4946, 21223, 120805, 42117, 54428, 64115, 60845, 7912, 9982, 11128, 98959, 49142, 50672],
    '2023': [29965, 31590, 29508, 31477, 6331, 14695, 100544, 43715, 64758, 62611, 58829, 8061, 5985, 9822, 95281, 49848, 62146]
}

# Convert data to a DataFrame for plotting
df_apple = pd.DataFrame(apple_financial_data)

# Define a function to create a visualization with insights and a bar chart using Plotly
def visualize_apple_financial_data_with_insights_and_chart(df):
    st.title('Apple Financials Visualization')

    for i, row in df.iterrows():
        st.subheader(row['Metric'])
        st.write(f"2021: ${row['2021']} million")
        st.write(f"2023: ${row['2023']} million")

        # Add insights
        if row['Metric'] == 'Cash and cash equivalents':
            increase = ((row['2023'] - row['2021']) / row['2021']) * 100
            st.write(f"Increase: {increase:.2f}%")
            st.write("Driven by increase in cash reserves.")
        elif row['Metric'] == 'Marketable securities':
            increase = ((row['2023'] - row['2021']) / row['2021']) * 100
            st.write(f"Increase: {increase:.2f}%")
            st.write("Increase in marketable securities.")
        # Add insights for other metrics

        st.write('---')  # Add a separator between sections

    # Create a bar chart using Plotly
    st.subheader('Bar Chart')
    fig = px.bar(df, x='Metric', y=['2021', '2023'], title='Apple Financial Metrics Comparison', barmode='group')
    st.plotly_chart(fig)
    

# Call the function to display the visualization with insights and a bar chart using Plotly for Apple financial data

with insights:
    if ticker=="AAPL":
        i=visualize_data_with_insights_and_chart(df)
    elif ticker=="MSFT": 
        i=visualize_msft_data_with_insights_and_chart(df_msft)

with financials:
    if ticker=="AAPL":
        f=visualize_apple_financial_data_with_insights_and_chart(df_apple)
    elif ticker=="MSFT":
        f=visualize__msft_financial_data_with_insights_and_chart(df_financial)