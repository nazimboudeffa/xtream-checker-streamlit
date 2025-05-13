import streamlit as st
import streamlit.components.v1 as components
import xtream

components.html('''<script defer data-domain="xtream-checker.com" src="https://plausible.codewithadu.de/js/script.js"></script>''')

st.set_page_config(
    page_title="Xtream UI API",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Xtream Checker")
st.sidebar.title("Xtream Checker")
st.sidebar.image("logo-back.png", width=200)
st.sidebar.markdown(
    """
    ## Xtream UI API Checker
    This is a simple Streamlit app to interact with the Xtream UI API.
    """
)
st.sidebar.markdown(
    """
    ### Authentication
    - **Username**: Your Xtream UI username
    - **Password**: Your Xtream UI password
    - **Server**: Your Xtream UI server URL (e.g., http://example.com:8080)
    """
)
st.sidebar.markdown(
    """
    ### Stream types to check
    - **Live**: Live TV streams
    - **VoD**: TODO
    - **Series**: TODO
    """
)
st.sidebar.markdown(
    """
    ### DONATION
    If you find this app useful, consider donating to support its development.
    [GitHub](https://www.github.com/nazimboudeffa)
    """
)

username = st.text_input("Username", key="username")
password = st.text_input("Password", type="password", key="password")
server = st.text_input("Server", key="server")

check = st.button("Check", key="check")

if check:
    x = xtream

    # login details
    x.username = username
    x.password = password
    x.server = server

    if not username or not password or not server:
        st.error("Please enter your Username, Password, and Server before checking.")
    else:
        try:
            x.authenticate()
            st.success("Authenticated successfully!")
            
            total_streams = 0

            r = x.categories(x.liveType)

            try:
                live_category_data = r.json() 

                s = x.streams(x.liveType)
                live_stream_data = s.json() 

                # live_category_data is list of dict
                live_names = []
                live_IDs = []
                pos = 0
                while pos <= len(live_category_data) - 1:
                    cat_streams_data = [item for item in live_stream_data if item['category_id'] == live_category_data[pos]['category_id']]
                    total_streams += len(cat_streams_data)
                    pos += 1
                live_names.sort()

                if len(live_category_data) > 0:

                    st.write("Total Live Streams: {}".format(total_streams))

            except ValueError as err:
                st.error("Error: {}".format(err))
        except Exception as e:
            st.error("Authentication failed")

