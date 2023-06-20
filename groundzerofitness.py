import streamlit as st
import datetime

def main():
    st.title("Ground Zero Fitness")
    
    # Owner's Schedule
    st.subheader("Al's Schedule")
    
    owner_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    owner_schedule = {}
    
    for day in owner_days:
        st.write(f"**{day}:**")
        start_time = st.time_input("Start Time", key=f"owner_start_{day}", value=datetime.time(5, 0))
        end_time = st.time_input("End Time", key=f"owner_end_{day}", value=datetime.time(17, 0))
        
        if start_time < end_time:
            owner_schedule[day] = (start_time, end_time)
        else:
            st.error("Invalid time range. Start time must be before end time.")
    
    # Client's Schedule
    st.subheader("Fighter's Schedule")
    
    client_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    client_schedule = {}
    
    for day in client_days:
        st.write(f"**{day}:**")
        start_time = st.time_input("Start Time", key=f"client_start_{day}", value=datetime.time(5, 17))
        end_time = st.time_input("End Time", key=f"client_end_{day}", value=datetime.time(5, 17))
        
        if start_time < end_time:
            client_schedule[day] = (start_time, end_time)
        else:
            st.error("Invalid time range. Start time must be before end time.")
    
    # Check schedules
    st.subheader("Schedule Conflicts")
    
    conflicts = []
    
    for day in owner_schedule:
        if day in client_schedule:
            owner_start, owner_end = owner_schedule[day]
            client_start, client_end = client_schedule[day]
            
            if owner_start <= client_end and client_start <= owner_end:
                conflicts.append(day)
    
    if conflicts:
        st.write("Conflicts exist on the following days:")
        for day in conflicts:
            st.write(f"- {day}")
    else:
        st.write("No schedule conflicts.")
        
if __name__ == '__main__':
    main()
