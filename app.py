import streamlit as st

# Set the title of the app
st.set_page_config(page_title="Mortgage Calculator", page_icon="🏡", layout="centered")

# Add a header image
st.image("https://thumbs.dreamstime.com/b/d-house-budget-concept-render-56759583.jpg", use_column_width=True)

# Add a title and a subtitle
st.title("🏡 Mortgage Calculator")
st.write("Calculate your monthly payments and total cost of your mortgage with ease!")

# Customize with some styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        h1 {
            color: #FF6347;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            font-size: 18px;
        }
    </style>
    """, unsafe_allow_html=True)

# Request input for mortgage loan principal
principal = st.number_input("🏠 Enter the mortgage loan principal ($):", min_value=0.0, format="%.2f")

# Request input for the annual interest rate
interest_rate = st.number_input("💵 Enter the annual interest rate (%):", min_value=0.0, format="%.2f")

# Request input for the number of years to repay the mortgage
years = st.number_input("⏳ Enter the number of years to repay the mortgage:", min_value=1, step=1)

# Add a calculate button
if st.button("Calculate"):
    # Calculate the monthly repayment
    monthly_repayment = principal * (interest_rate / 12 / 100 * (1 + interest_rate / 12 / 100)**(years * 12)) / \
                        ((1 + interest_rate / 12 / 100)**(years * 12) - 1)

    # Calculate the total amount paid over the life of the mortgage
    total_amount = monthly_repayment * years * 12

    # Display the mortgage information to the user
    st.success(f"For a {years}-year mortgage loan of $ {principal:,.2f}:")
    st.write(f"at an annual interest rate of {interest_rate:.2f}%:")
    st.write(f"💰 **Monthly Payment**: $ {monthly_repayment:,.2f}")
    st.write(f"💰 **Total Payment**: $ {total_amount:,.2f}")

    st.balloons()

# Add a footer
st.write("---")
st.write("💬 *Thank you for using the Mortgage Calculator!*")