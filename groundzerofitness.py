import streamlit as st
import pandas as pd

def save_schedule(schedule):
    # Function to save the schedule data
    # You can customize this function to save the data to a database or storage of your choice
    # For simplicity, we'll just save it to a CSV file
    df = pd.DataFrame([schedule], columns=['Client', 'Schedule'])
    df.to_csv('schedule_data.csv', mode='a', header=not st.session_state.schedule_data)

def load_schedule_data():
    # Function to load the schedule data
    # You can customize this function to load the data from your chosen storage
    # For simplicity, we'll load it from a CSV file
    try:
        df = pd.read_csv('schedule_data.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Client', 'Schedule'])
    return df

def main():
    st.title("Client Schedule Input")
    
    # Load existing schedule data
    df = load_schedule_data()
    
    # Display existing schedule data
    st.subheader("Existing Schedules")
    st.table(df)
    
    # Schedule input form
    st.subheader("Input New Schedule")
    client_name = st.text_input("Client Name")
    schedule = st.text_input("Schedule")
    if st.button("Submit"):
        if client_name and schedule:
            save_schedule({'Client': client_name, 'Schedule': schedule})
            st.success("Schedule submitted successfully.")
            # Clear input fields
            st.session_state.client_name = ''
            st.session_state.schedule = ''
        else:
            st.error("Please enter both Client Name and Schedule.")

if __name__ == '__main__':
    main()
