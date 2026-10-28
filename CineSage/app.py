import json
import html
import streamlit as st
from core import model, prompt, parser

# ==================================================
# PAGE CONFIGURATION
# ==================================================
st.set_page_config(
    page_title="CineSage | Movie Intelligence",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# PREMIUM CINEMATIC THEME
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --bg: #080911;
    --panel: #10121e;
    --border: #24263a;
    --purple: #a78bfa;
    --cyan: #67e8f9;
    --muted: #969bb3;
    --white: #f6f5ff;
}

.stApp {
    background:
        radial-gradient(ellipse at 15% 0%, #21133b 0%, transparent 38%),
        radial-gradient(ellipse at 95% 20%, #102535 0%, transparent 30%),
        var(--bg);
    color: var(--white);
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1250px;
    padding: 2rem 2rem 4rem;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--white) !important;
}

p, label, li {
    color: #c4c6d8;
}

.brand {
    display: flex;
    align-items: center;
    gap: 11px;
    font-size: 15px;
    letter-spacing: 2px;
    font-weight: 700;
    color: white;
}

.brand-icon {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
    border-radius: 13px;
    background: linear-gradient(135deg, #8b5cf6, #4338ca);
    box-shadow: 0 0 30px #8b5cf633;
    font-size: 21px;
}

.brand span {
    color: var(--purple);
}

.status {
    display: inline-block;
    border: 1px solid #28594f;
    color: #86efac;
    background: #10251f;
    border-radius: 30px;
    padding: 7px 12px;
    font-size: 11px;
    letter-spacing: 1px;
    font-weight: 700;
}

.hero {
    padding: 65px 0 42px;
}

.eyebrow {
    color: var(--cyan);
    font-size: 11px;
    letter-spacing: 3px;
    font-weight: 700;
    margin-bottom: 18px;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(42px, 6vw, 72px);
    font-weight: 700;
    line-height: 1.06;
    letter-spacing: -3px;
    color: white;
    margin: 0;
}

.gradient-text {
    background: linear-gradient(90deg, #c4b5fd, #a78bfa 45%, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-description {
    max-width: 620px;
    color: var(--muted);
    font-size: 16px;
    line-height: 1.9;
    margin-top: 20px;
}

.section-kicker {
    color: var(--purple);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    margin: 15px 0;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(16,18,30,.78);
    border: 1px solid var(--border);
    border-radius: 20px;
}

div[data-testid="stTextArea"] textarea {
    background: #0b0d17 !important;
    color: #f5f3ff !important;
    border: 1px solid #30334c !important;
    border-radius: 13px !important;
    line-height: 1.7;
}

div[data-testid="stTextArea"] textarea:focus {
    border-color: var(--purple) !important;
    box-shadow: 0 0 0 1px var(--purple);
}

div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(100deg, #7c3aed, #8b5cf6 55%, #6366f1);
    color: white;
    border: 0;
    border-radius: 12px;
    height: 49px;
    font-weight: 700;
    transition: all .2s ease;
}

div[data-testid="stButton"] > button[kind="primary"]:hover {
    box-shadow: 0 8px 30px #8b5cf644;
    transform: translateY(-2px);
}

div[data-testid="stButton"] > button:not([kind="primary"]) {
    background: #141626;
    color: #d9d5f3;
    border: 1px solid #30334c;
    border-radius: 11px;
}

.feature {
    padding: 15px 0;
    border-bottom: 1px solid #25273a;
}

.feature:last-child {
    border-bottom: none;
}

.feature-icon {
    font-size: 21px;
    margin-bottom: 8px;
}

.feature-title {
    color: white;
    font-weight: 700;
    font-size: 14px;
    margin-bottom: 5px;
}

.feature-description {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.7;
}

.result-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 35px;
    font-weight: 700;
    color: white;
    letter-spacing: -1px;
    margin-bottom: 8px;
}

.result-meta {
    color: var(--muted);
    font-size: 13px;
    margin-bottom: 22px;
}

.metric-card {
    background: linear-gradient(145deg, #17192a, #10121e);
    border: 1px solid #292c43;
    border-radius: 16px;
    padding: 20px;
    min-height: 112px;
}

.metric-label {
    color: #9b9eb7;
    font-size: 10px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.metric-value {
    color: white;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 27px;
    font-weight: 700;
    margin-top: 14px;
}

.genre-tag {
    display: inline-block;
    padding: 7px 12px;
    margin: 4px 5px 4px 0;
    background: #211a37;
    color: #d4c4ff;
    border: 1px solid #48376c;
    border-radius: 30px;
    font-size: 12px;
}

.cast-card {
    background: #141626;
    border: 1px solid #292c43;
    border-radius: 12px;
    padding: 12px 14px;
    margin: 7px 0;
    color: #e4e4f4;
    font-size: 13px;
}

div[data-testid="stTabs"] button {
    color: #a9abc1;
}

div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #c4b5fd;
}

div[data-testid="stExpander"] {
    background: #10121e;
    border: 1px solid #292c43;
    border-radius: 12px;
}

div[data-testid="stDownloadButton"] button {
    background: #17192a;
    color: white;
    border: 1px solid #484064;
    border-radius: 11px;
    min-height: 43px;
}

hr {
    border-color: #26283a;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

@media (max-width: 700px) {
    .block-container {
        padding: 1rem 1rem 3rem;
    }

    .hero {
        padding: 35px 0 25px;
    }

    .hero-title {
        letter-spacing: -1.5px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==================================================
# NAVIGATION HEADER
# ==================================================
header_left, header_right = st.columns([3, 1])

with header_left:
    st.markdown("""
    <div class="brand">
        <div class="brand-icon">🎬</div>
        CINE<span>SAGE</span>
        <span style="color:#72758e;font-size:10px;letter-spacing:1px;">
            &nbsp; AI STUDIO
        </span>
    </div>
    """, unsafe_allow_html=True)

with header_right:
    st.markdown(
        '<div style="text-align:right;padding-top:10px;">'
        '<span class="status">● SYSTEM READY</span></div>',
        unsafe_allow_html=True
    )

st.markdown("""
<div class="hero">
    <div class="eyebrow">INTELLIGENCE BEHIND EVERY FRAME</div>
    <div class="hero-title">
        Stories in.<br>
        <span class="gradient-text">Insights out.</span>
    </div>
    <div class="hero-description">
        Turn unstructured movie descriptions into structured intelligence.
        Extract movie metadata, discover cast and genres, and transform
        plain text into clean, validated JSON with Generative AI.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==================================================
# INPUT WORKSPACE
# ==================================================
st.markdown(
    '<div class="section-kicker">01 &nbsp; / &nbsp; EXTRACTION WORKSPACE</div>',
    unsafe_allow_html=True
)

input_col, info_col = st.columns([1.55, 0.85], gap="large")

sample = (
    "Inception is a science fiction action thriller released in 2010, "
    "directed by Christopher Nolan. The film stars Leonardo DiCaprio, "
    "Joseph Gordon-Levitt, Elliot Page, Tom Hardy, and Cillian Murphy. "
    "It follows a skilled thief who enters people's dreams to steal secrets "
    "and is given a mission to plant an idea inside someone's mind. "
    "The movie has an IMDb rating of 8.8 out of 10 and belongs to the "
    "science fiction, action, and thriller genres."
)

with input_col:
    with st.container(border=True):
        st.markdown("### Tell us the story")
        st.caption("Paste any movie description. Let AI handle the details.")

        if "movie_input" not in st.session_state:
            st.session_state["movie_input"] = sample

        paragraph = st.text_area(
            "Movie description",
            key="movie_input",
            height=220,
            placeholder="Paste your movie paragraph here...",
            label_visibility="collapsed"
        )

        b1, b2 = st.columns([2, 1])

        with b1:
            extract_clicked = st.button(
                "✦  Analyze Movie",
                type="primary",
                use_container_width=True
            )

        with b2:
            sample_clicked = st.button(
                "↻  Load Sample",
                use_container_width=True
            )

        if sample_clicked:
            st.session_state["movie_input"] = sample
            st.rerun()

with info_col:
    with st.container(border=True):
        st.markdown("### Your AI toolkit")
        st.caption("One paragraph. Multiple insights.")

        features = [
            ("🎞️", "Movie identification", "Title and release year"),
            ("🎭", "Genre intelligence", "Classify movie genres"),
            ("🌟", "Cast & crew", "Identify actors and directors"),
            ("📊", "Rating extraction", "Capture ratings when provided"),
            ("🧠", "Semantic understanding", "Extract a concise summary"),
            ("📦", "Structured output", "Validated data, ready to use"),
        ]

        for icon, title, desc in features:
            st.markdown(f"""
            <div class="feature">
                <div class="feature-icon">{icon}</div>
                <div class="feature-title">{title}</div>
                <div class="feature-description">{desc}</div>
            </div>
            """, unsafe_allow_html=True)


# ==================================================
# GROQ EXTRACTION
# ==================================================
if extract_clicked:
    if not paragraph.strip():
        st.warning("Enter a movie description before analyzing.")

    else:
        try:
            with st.spinner("✦ CineSage is analyzing your story..."):
                final_prompt = prompt.invoke({
                    "paragraph": paragraph,
                    "format_instructions": parser.get_format_instructions()
                })

                response = model.invoke(final_prompt)
                movie_data = parser.parse(response.content)

                st.session_state["movie_data"] = movie_data.model_dump()

        except Exception as e:
            st.error("Unable to extract movie information.")
            st.info(
                "Check your API key, model availability, internet connection, "
                "and the response format."
            )

            with st.expander("Technical error"):
                st.code(str(e))


# ==================================================
# RESULTS DASHBOARD
# ==================================================
if "movie_data" in st.session_state:
    movie = st.session_state["movie_data"]

    title = html.escape(str(movie.get("title") or "Untitled Movie"))
    director = html.escape(str(movie.get("director") or "Not specified"))
    year = movie.get("release_year")
    genres = movie.get("genre") or []
    cast = movie.get("cast") or []
    rating = movie.get("rating")
    summary = html.escape(str(movie.get("summary") or "No summary available."))

    st.markdown("---")
    st.markdown(
        '<div class="section-kicker">02 &nbsp; / &nbsp; INTELLIGENCE REPORT</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        st.markdown(
            f'<div class="result-title">{title}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="result-meta">'
            f'📅 &nbsp; {year if year is not None else "Year unknown"}'
            f' &nbsp;&nbsp; / &nbsp;&nbsp; 🎬 &nbsp; {director}'
            f'</div>',
            unsafe_allow_html=True
        )

        m1, m2, m3, m4 = st.columns(4)

        metrics = [
            (m1, "REPORTED RATING", f"⭐ {rating}" if rating is not None else "N/A"),
            (m2, "GENRES FOUND", str(len(genres))),
            (m3, "CAST MEMBERS", str(len(cast))),
            (m4, "RELEASE YEAR", str(year) if year is not None else "N/A"),
        ]

        for column, label, value in metrics:
            with column:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{html.escape(value)}</div>
                </div>
                """, unsafe_allow_html=True)

        st.write("")

        tab_overview, tab_cast, tab_json = st.tabs([
            "✧  Overview",
            "✧  Cast & Crew",
            "{ }  Raw JSON"
        ])

        with tab_overview:
            st.markdown("### The story, summarized")
            st.write(summary)

            st.markdown("### Genre profile")

            if genres:
                genre_html = "".join(
                    f'<span class="genre-tag">{html.escape(str(g))}</span>'
                    for g in genres
                )
                st.markdown(genre_html, unsafe_allow_html=True)
            else:
                st.caption("No genres were identified.")

        with tab_cast:
            st.markdown("### People behind the movie")

            if movie.get("director"):
                st.markdown(f"**Director:** {director}")

            if cast:
                cast_cols = st.columns(2)

                for index, actor in enumerate(cast):
                    with cast_cols[index % 2]:
                        st.markdown(
                            '<div class="cast-card">🎭 &nbsp; '
                            + html.escape(str(actor))
                            + '</div>',
                            unsafe_allow_html=True
                        )
            else:
                st.caption("No cast members were identified.")

        with tab_json:
            st.caption("Validated movie object generated by Pydantic")
            st.json(movie, expanded=True)

    st.write("")

    json_data = json.dumps(movie, indent=2, ensure_ascii=False)

    download_col, reset_col, _ = st.columns([1.2, 1.2, 2])

    with download_col:
        st.download_button(
            "↓  Export JSON",
            data=json_data,
            file_name="cinesage_movie.json",
            mime="application/json",
            use_container_width=True
        )

    with reset_col:
        if st.button("↻  Clear results", use_container_width=True):
            st.session_state.pop("movie_data", None)
            st.rerun()


# ==================================================
# FOOTER
# ==================================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")

footer_left, footer_right = st.columns(2)

with footer_left:
    st.markdown(
        '<div style="color:#777b96;font-size:12px;">'
        'CINESAGE © &nbsp; MOVIE INTELLIGENCE STUDIO'
        '</div>',
        unsafe_allow_html=True
    )

with footer_right:
    st.markdown(
        '<div style="color:#777b96;font-size:12px;text-align:right;">'
        'POWERED BY GROQ · LANGCHAIN · PYDANTIC'
        '</div>',
        unsafe_allow_html=True
    )