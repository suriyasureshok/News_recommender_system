import streamlit as st
import requests

API_BASE = "https://news-recommender-system-o7n3.onrender.com"

# ---------------- Session State Initialization ----------------
if "token" not in st.session_state:
    st.session_state.token = None
if "page" not in st.session_state:
    st.session_state.page = "Login"

# ------------------ API Call Helpers ------------------

def login_api(email, password):
    res = requests.post(f"{API_BASE}/login", json={"email": email, "password": password})
    return res.json(), res.status_code

def register_api(username, email, password):
    res = requests.post(f"{API_BASE}/register", json={
        "username": username,
        "email": email,
        "password": password
    })
    return res.json(), res.status_code

def get_news():
    headers = {"Authorization": f"Bearer {st.session_state.token}"}
    res = requests.get(f"{API_BASE}/news", headers=headers)
    return res.json()

def get_recommendations():
    headers = {"Authorization": f"Bearer {st.session_state.token}"}
    res = requests.get(f"{API_BASE}/recommend", headers=headers)
    return res.json()

def like_article(news_id):
    headers = {"Authorization": f"Bearer {st.session_state.token}"}
    res = requests.post(f"{API_BASE}/like/{news_id}", headers=headers)
    return res.json()

# ------------------ Page Functions ------------------

def login():
    st.title("🔐 Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        data, code = login_api(email, password)
        if code == 200:
            st.session_state.token = data['token']
            st.session_state.page = "Articles"
            st.success("Login successful!")
            st.rerun()
        else:
            st.error(data.get("error", "Login failed"))

def register():
    st.title("📝 Register")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        data, code = register_api(username, email, password)
        if code == 201:
            st.session_state.token = data['token']
            st.session_state.page = "Articles"
            st.success("Registration successful!")
            st.rerun()
        else:
            st.error(data.get("error", "Registration failed"))

def show_articles(news_list):
    st.title("📰 Your News Feed")

    # Initialize liked_news in session state
    if "liked_news" not in st.session_state:
        st.session_state.liked_news = set()

    for article in news_list:
        with st.container():
            st.subheader(article['title'])
            st.write(article['description'])
            st.caption(f"Category: {article['category']}")

            # Disable like button if already liked
            if article['id'] in st.session_state.liked_news:
                st.button("✅ Liked", key=f"liked_{article['id']}", disabled=True)
            else:
                if st.button("👍 Like", key=f"like_{article['id']}"):
                    like_article(article['id'])  # Call API to like
                    st.session_state.liked_news.add(article['id'])  # Track locally
                    st.success("Liked!")

def articles_page():
    news_list = get_news()
    if not news_list:
        st.info("No news found.")
        return
    show_articles(news_list)


# ------------------ Main Navigation Logic ------------------

def main():
    st.sidebar.title("🧭 Navigation")

    # Ensure session state variables are initialized
    if "token" not in st.session_state:
        st.session_state.token = None
    if "page" not in st.session_state:
        st.session_state.page = "Login"

    if st.session_state.token:  # User is logged in
        nav_options = ["Articles", "Recommendations", "Logout"]

        if st.session_state.page not in nav_options:
            st.session_state.page = "Articles"

        choice = st.sidebar.radio("Go to", nav_options, index=nav_options.index(st.session_state.page))

        if choice == "Articles":
            st.session_state.page = "Articles"
            articles_page()

        elif choice == "Recommendations":
            st.session_state.page = "Recommendations"
            news_list = get_recommendations()
            show_articles(news_list)


        elif choice == "Logout":
            st.session_state.token = None
            st.session_state.page = "Login"
            st.success("✅ Logged out successfully.")
            st.rerun()

    else:  # User is not logged in
        nav_options = ["Login", "Register"]

        if st.session_state.page not in nav_options:
            st.session_state.page = "Login"

        choice = st.sidebar.radio("Go to", nav_options, index=nav_options.index(st.session_state.page))

        if choice == "Login":
            st.session_state.page = "Login"
            login()

        elif choice == "Register":
            st.session_state.page = "Register"
            register()

# ------------- Entry Point -------------
if __name__ == "__main__":
    main()