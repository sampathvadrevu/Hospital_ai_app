# main.py
import os
import streamlit as st
from langchain.llms import OpenAI  # keeping your original import
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# -----------------------
# LLM
# -----------------------
os.environ["OPENAI_API_KEY"] = "Try_your_own_api_key"

llm = OpenAI(temperature=0)

# -----------------------
# Chains
# -----------------------
def generate_hospital_details(City: str):
    # 1) City intro about hospital facilities
    city_intro = PromptTemplate(
        input_variables=["City"],
        template="Give a very nice short introduction about the best hospital facilities in the {City} under 250 words"
    )
    city_chain = LLMChain(llm=llm, prompt=city_intro, output_key="city_intro")

    # 2) One best hospital in the city
    # Minimal fix: use City (not city_intro) so the model returns just a name
    hosp_name = PromptTemplate(
        input_variables=["City"],
        template="Suggest one best hospital in {City} for all sorts of emergencies. Return only the hospital name."
    )
    hospital_chain = LLMChain(llm=llm, prompt=hosp_name, output_key="hospital_name")

    # 3) Intro + top 3 doctors of that hospital
    hosp_details = PromptTemplate(
        input_variables=["hospital_name"],
        template=(
            "Give the introduction about {hospital_name} and list top 3 best doctors of {hospital_name}, "
            "their degrees and their specialisation. Return as an ordered list."
        )
    )
    details_chain = LLMChain(llm=llm, prompt=hosp_details, output_key="hospital_details")

    # Sequential chain: city -> hospital -> details
    chain = SequentialChain(
        chains=[city_chain, hospital_chain, details_chain],
        input_variables=["City"],
        output_variables=["city_intro", "hospital_name", "hospital_details"]
    )

    return chain({"City": City})


# -----------------------
# Streamlit UI
# -----------------------
City = st.sidebar.selectbox(
    "Pick a City in India",
    (
        "Hyderabad", "Chennai", "Bengaluru", "Visakhapatnam", "Coimbatore",
        "Kochi", "Thiruvananthapuram", "Mysuru", "Delhi", "Mumbai",
        "Kolkata", "Jaipur", "Lucknow", "Chandigarh", "Varanasi"
    )
)

if City:
    response = generate_hospital_details(City)

    # The ONLY page title
    st.title(f"✨ The Finest Healthcare Destination in {City}")

    # City intro
    if "city_intro" in response and response["city_intro"].strip():
        st.subheader("About Healthcare in the City")
        st.write(response["city_intro"].strip())

    # Hospital name as heading
    hospital_name = response["hospital_name"].strip()
    st.subheader(hospital_name)

    # Hospital details & top doctors
    details_lines = response["hospital_details"].strip().splitlines()
    for line in details_lines:
        line = line.strip()
        if line:
            st.write("-", line)
