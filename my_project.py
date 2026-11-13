import streamlit as st

# Page Configuration
st.set_page_config(page_title="NexusAI Studio Pro", page_icon="🚀", layout="wide")

# Initialize Session State
if "generation_count" not in st.session_state:
    st.session_state.generation_count = 0
if "is_licensed" not in st.session_state:
    st.session_state.is_licensed = False

# Sidebar Navigation
st.sidebar.title("🚀 Navigation")
app_mode = st.sidebar.selectbox("Choose Mode", ["Website Generator", "User Dashboard", "Export & Monetize", "Settings"])

VALID_LICENSE_KEY = "VISHAL-PRO-2026"

# 1. Website Generator Page
if app_mode == "Website Generator":
    st.title("🤖 NexusAI Studio Pro")
    st.markdown("Apni pasand ki website ka idea yahan dalein aur AI se turant generate karein.")
    
    FREE_LIMIT = 3
    remaining_trials = FREE_LIMIT - st.session_state.generation_count
    
    if not st.session_state.is_licensed:
        if remaining_trials > 0:
            st.warning(f"⚠️ Aapke paas **{remaining_trials} Free Trials** bache hain. Unlimited use ke liye Pro License kharidein!")
        else:
            st.error("❌ Aapki free trial limit khatam ho chuki hai! Website generate karne ke liye pehle Pro License activate karein.")

    prompt = st.text_area("Apni website ka description yahan likhein:")
    
    if st.button("🚀 Generate Website Now", key="final_unique_generate_btn"):
        if not st.session_state.is_licensed and st.session_state.generation_count >= FREE_LIMIT:
            st.error("Free limit over! 'Export & Monetize' page par jakar payment karein.")
        elif not prompt.strip():
            st.warning("Kripya kuch description darj karein.")
        else:
            if not st.session_state.is_licensed:
                st.session_state.generation_count += 1
            st.success("🎉 Aapki AI website safalata-pūrvak generate ho gayi hai!")
            st.code(f"<!-- Generated Code for: {prompt} -->\n<html>\n<head><title>AI Website</title></head>\n<body>\n  <h1>Welcome!</h1>\n</body>\n</html>", language="html")

# 2. User Dashboard Page
elif app_mode == "User Dashboard":
    st.title("📊 User Dashboard")
    st.metric(label="Total Generations Used", value=f"{st.session_state.generation_count} / 3")
    st.metric(label="License Status", value="Pro Active" if st.session_state.is_licensed else "Free Trial Active")

# 3. Export & Monetize Page (PayPal Integration)
elif app_mode == "Export & Monetize":
    st.title("💸 Monetization & Export Hub")
    st.markdown("Apni generated websites ko sell karne ke liye package export karein.")
    
    st.markdown("---")
    st.subheader("📦 Pro License Pricing: $10 USD")
    st.markdown("Unlimited AI Website Generations ke liye niche diye gaye button par click karke **$10 USD** payment karein:")
    
    # PayPal Link Integration
    paypal_url = "https://paypal.me/VishalAI"
    st.markdown(f'<a href="{paypal_url}" target="_blank"><button style="background-color:#0070ba; color:white; padding:12px 24px; border:none; border-radius:5px; font-size:16px; cursor:pointer; font-weight:bold;">Pay $10 via PayPal (PayPal.Me/VishalAI)</button></a>', unsafe_allow_html=True)
    
    st.info("Payment ke baad license key ke liye sampark karein.")

# 4. Settings Page
elif app_mode == "Settings":
    st.title("⚙️ License Activation")
    license_input = st.text_input("Enter Pro License Key:", type="password", key="final_settings_key")
    
    if st.button("Activate License", key="final_activate_btn"):
        if license_input == VALID_LICENSE_KEY:
            st.session_state.is_licensed = True
            st.success("🎉 Pro License activate ho gaya hai!")
        else:
            st.error("❌ Galat License Key hai.")