import streamlit as st
from supabase import create_client, Client

# Supabase configuration
SUPABASE_URL = 'https://kidbzlespbhlseivcosi.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtpZGJ6bGVzcGJobHNlaXZjb3NpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTk4MzQzMjksImV4cCI6MjAzNTQxMDMyOX0.9GraLP8enw7jJhgUyD8A0_bL8sSGRF5h-5tByvo5ceY'
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Set up the form
st.title('User_Registration_Info')

with st.form(key='user_form'):
    name = st.text_input('Name')
    phone_number = st.text_input('Phone Number')
    email_id = st.text_input('Email ID')
    field = st.checkbox('Field')
    location = st.text_input('Location')
    domain = st.selectbox('Domain', ['ML', 'DS', 'AI', 'DL', 'Other'])
    
    
    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# Display the submitted form data and store it in Supabase
if submit_button:
    st.write('Form submitted successfully!')
    st.write('Name:', name)
    st.write('Phone Number:', phone_number)
    st.write('Email ID:', email_id)
    st.write('Field:', field)
    st.write('Location:', location)
    st.write('Domain:', domain) 
    
    # Insert data into Supabase
    data = {
        'name': name,
        'phone_number': phone_number,
        'email_id': email_id,
        'field': field,
        'location': location,
        'domain': domain
    }
    
    try:
    # Insert data into a table
        response = supabase.table('your_table_name').insert(data).execute()

    # Check for successful insertion (Supabase may not return status_code)
        if response.status == 201:
           print("Insertion successful:", response.get('data'))
        else:
           print("Insertion failed:", response.get('status'), response.get('error'))

    except Exception as e:
        print("Error:", e)