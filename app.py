"""Contact Book - Streamlit App"""
import streamlit as st
from db_connection import insert_contact, search_contacts

st.title("📞 Contact Book")

# Add Contact Section
st.subheader("Add New Contact")
with st.form("add_contact"):
    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    submit = st.form_submit_button("Add Contact")
    
    if submit:
        if name and phone:
            try:
                insert_contact(name, phone)
                st.success(f"✓ Contact '{name}' added successfully!")
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill all fields")

st.divider()

# Search Contacts Section
st.subheader("Search Contacts")
search = st.text_input("Search by name", placeholder="Type name to search...")

if st.button("Search") or search:
    try:
        contacts = search_contacts(search)
        
        if contacts:
            st.write(f"Found {len(contacts)} contact(s)")
            
            for contact in contacts:
                with st.container():
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.write(f"**{contact[1]}**")
                    with col2:
                        st.write(f"📱 {contact[2]}")
                    st.caption(f"Added: {contact[3].strftime('%Y-%m-%d')}")
                    st.divider()
        else:
            st.info("No contacts found")
            
    except Exception as e:
        st.error(f"Error: {str(e)}")