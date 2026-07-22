import streamlit as st
import time
from few_shot import FewShotPosts
from post_generator import generate_post

st.set_page_config(
    page_title="AI Content Studio",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CSS ----------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


def main():

    fs = FewShotPosts()
    tags = fs.get_tags()

    # ---------- Sidebar ----------
    with st.sidebar:

        st.title("🤖 AI Content Studio")

        st.markdown("---")

        st.write("### Features")

        st.success("AI Generated Content")

        st.info("Multiple Topics")

        st.info("Multiple Languages")

        st.info("Download Output")

        st.markdown("---")

        st.caption("Powered by Groq + Streamlit")

    # ---------- Hero ----------
    st.markdown("""
<div class="hero">

<h1>🚀 AI Content Studio</h1>

<p>Create engaging AI-generated social media content in seconds.</p>

</div>
""", unsafe_allow_html=True)

    st.write("")

    # ---------- Settings ----------
    st.subheader("⚙️ Content Settings")

    c1, c2, c3 = st.columns(3)

    with c1:
        topic = st.selectbox("Topic", tags)

    with c2:
        length = st.selectbox("Length", length_options)

    with c3:
        language = st.selectbox("Language", language_options)

    st.write("")

    generate = st.button(
        "✨ Generate Content",
        use_container_width=True
    )

    if generate:

        start = time.time()

        with st.spinner("🤖 AI is generating your content..."):

            post = generate_post(
                length,
                language,
                topic
            )

        end = time.time()

        st.success("Content generated successfully!")

        st.write("")

        st.subheader("📄 Generated Content")

        st.text_area(
            "",
            post,
            height=320
        )

        st.download_button(
            "📥 Download",
            post,
            file_name="generated_post.txt",
            use_container_width=True
        )

        st.write("")

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric(
                "Words",
                len(post.split())
            )

        with m2:
            st.metric(
                "Characters",
                len(post)
            )

        with m3:
            st.metric(
                "Generation Time",
                f"{round(end-start,2)} sec"
            )

    st.markdown("---")

    st.caption(
        "Built with Python • Streamlit • Groq"
    )


if __name__ == "__main__":
    main()