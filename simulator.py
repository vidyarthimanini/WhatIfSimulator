# ============================================================
#            📉 WHAT-IF CREDIT RISK SIMULATOR (UI)
# ============================================================

st.header("🧪 What-If Credit Risk Simulator")

st.write("""
Use this tool to instantly understand how changes in **DSCR**, **CIBIL**, **Turnover**, and 
**Net Worth** will affect the borrower’s financial health risk score.
""")

# ---------------------------
# Input Controls
# ---------------------------
base_score = st.number_input("Base Risk Score", min_value=0.0, max_value=100.0, value=70.0)

dscr = st.slider("DSCR Ratio", min_value=0.0, max_value=3.0, value=1.2, step=0.01)
cibil = st.slider("CIBIL Score", min_value=300, max_value=900, value=720, step=1)
turnover = st.number_input("Turnover (₹ Crores)", min_value=0.0, value=50.0)
networth = st.number_input("Net Worth (₹ Crores)", min_value=0.0, value=20.0)

# ---------------------------
# Impact Functions
# ---------------------------
def dscr_impact(dscr):
    if dscr < 1.0:
        return -15
    elif dscr < 1.2:
        return -10
    elif dscr < 1.5:
        return 0
    else:
        return +5

def cibil_impact(cibil):
    if cibil < 650:
        return -20
    elif cibil < 700:
        return -10
    elif cibil < 750:
        return +5
    elif cibil < 800:
        return +12
    else:
        return +15

def scale_impact(turnover, networth):
    combined = turnover + networth
    if combined < 20:
        return 0
    elif combined < 50:
        return 5
    elif combined < 100:
        return 8
    else:
        return 10

# ---------------------------
# Calculate Impacts
# ---------------------------
D = dscr_impact(dscr)
C = cibil_impact(cibil)
S = scale_impact(turnover, networth)

projected = base_score + D + C + S
projected = float(np.clip(projected, 0, 100))

# ---------------------------
# Risk Color Label
# ---------------------------
def risk_color(score):
    if score >= 75:
        return "🟢 Low Risk"
    elif score >= 50:
        return "🟡 Moderate Risk"
    else:
        return "🔴 High Risk"

# ---------------------------
# Display Results
# ---------------------------
st.subheader("📊 Simulation Result")

st.metric("Projected Risk Score", f"{projected:.2f}", delta=projected - base_score)

st.write(f"### Risk Band: **{risk_color(projected)}**")

st.write("### Impact Breakdown")
st.write(f"- **DSCR Impact**: `{D}`")
st.write(f"- **CIBIL Impact**: `{C}`")
st.write(f"- **Scale Impact (Turnover + Net Worth)**: `{S}`")

st.success("Simulation complete. Adjust the sliders above to see results instantly!")
