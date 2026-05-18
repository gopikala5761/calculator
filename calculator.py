import streamlit as st
import math
# Set up the page layout
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮")
# Initialize session state for the calculator screen
if "expression" not in st.session_state:
    st.session_state.expression = ""
# Callback function to handle button clicks
def on_click(button):
    if button == "C":
        # Clear the screen
        st.session_state.expression = ""
    elif button == "DEL":
        # Delete the last character
        st.session_state.expression = st.session_state.expression[:-1]
        if st.session_state.expression == "Erro": # In case of "Error" message, clear completely
            st.session_state.expression = ""
    elif button == "=":
        # Evaluate the math expression
        try:
            expr = st.session_state.expression
            
            # Replace UI-friendly symbols with Python equivalents
            expr = expr.replace("^", "**")
            expr = expr.replace("π", str(math.pi))
            expr = expr.replace("e", str(math.e))
            
            # Safely evaluate using functions from the 'math' library
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            result = eval(expr, {"__builtins__": {}}, allowed_names)
            
            st.session_state.expression = str(result)
        except Exception:
            st.session_state.expression = "Error"
    else:
        # If it's a scientific function, append an open parenthesis automatically
        scientific_funcs = [
            "sin", "cos", "tan", "asin", "acos", "atan", 
            "sinh", "cosh", "tanh", "sqrt", "log", "log10", "factorial"
        ]
        if button in scientific_funcs:
            st.session_state.expression += f"{button}("
        else:
            st.session_state.expression += button
# --- UI Setup ---
st.title("🧮 Scientific Calculator")
# Custom CSS to make the display text larger and align to the right
st.markdown("""
    <style>
    div[data-baseweb="input"] input {
        font-size: 2rem !important;
        text-align: right !important;
    }
    </style>
""", unsafe_allow_html=True)
# Calculator Screen (disabled to prevent direct keyboard typing, forces button use)
st.text_input("Screen", value=st.session_state.expression, label_visibility="collapsed", disabled=True)
# Define the grid of buttons
buttons = [
    ["C", "DEL", "(", ")"],
    ["sin", "cos", "tan", "/"],
    ["asin", "acos", "atan", "*"],
    ["sqrt", "log", "log10", "-"],
    ["7", "8", "9", "+"],
    ["4", "5", "6", "^"],
    ["1", "2", "3", "="],
    ["0", ".", "π", "e"]
]
# Render the buttons in a grid
for row in buttons:
    cols = st.columns(4)
    for i, button in enumerate(row):
        # We assign an on_click callback to update state before the app re-runs
        cols[i].button(
            button, 
            use_container_width=True, 
            on_click=on_click, 
            args=(button,)
        )
