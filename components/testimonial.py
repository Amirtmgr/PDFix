import streamlit as st

def testimonial():
    # Apply custom CSS for styling
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #d0efff, #ffffff);
            color: #000000;
            text-align: center;
            font-family: Arial, sans-serif;
        }
        .title {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 0;
        }
        .subtitle {
            font-size: 18px;
            color: #666666;
            margin-bottom: 40px;
        }
        .icon-bar {
            margin-top: 20px;
            margin-bottom: 30px;
        }
        .icon-bar a {
            text-decoration: none;
            font-size: 24px;
            margin: 0 10px;
            color: #0073b1;
            transition: color 0.3s ease;
        }
        .icon-bar a:hover {
            color: #005682;
        }
        .download-btn {
            font-size: 20px;
            font-weight: bold;
            background-color: #00aaff;
            color: #ffffff;
            padding: 12px 24px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .download-btn:hover {
            background-color: #008ecc;
        }
        .gradient-text {
                    -webkit-text-size-adjust: 100%;
        tab-size: 4;
        font-feature-settings: normal;
        font-variation-settings: normal;
        -webkit-tap-highlight-color: transparent;
        -webkit-font-smoothing: antialiased;
        --rem: 16;
        --background: 210 20% 96%;
        --foreground: 230 20% 18%;
        --card: 210 36% 92%;
        --card-foreground: 230 20% 18%;
        --popover: 210 36% 92%;
        --popover-foreground: 230 20% 18%;
        --primary: 190 100% 40%;
        --primary-foreground: 0 0% 100%;
        --secondary: 50 100% 60%;
        --secondary-foreground: 230 20% 18%;
        --muted: 210 16% 80%;
        --muted-foreground: 230 20% 18%;
        --accent: 210 36% 92%;
        --accent-foreground: 0 0% 100%;
        --destructive: 0 80% 60%;
        --destructive-foreground: 0 0% 100%;
        --border: 210 16% 80%;
        --input: 210 16% 80%;
        --ring: 190 100% 80%;
        --radius: 0.5rem;
        cursor: default;
        font-style: normal;
        text-align: center;
        font-weight: 500;
        letter-spacing: -.05em;
        font-size: 3.75rem;
        line-height: 1;
        box-sizing: border-box;
        border: 0 solid #e5e7eb;
        border-color: hsl(var(--border));
        --tw-border-spacing-x: 0;
        --tw-border-spacing-y: 0;
        --tw-translate-x: 0;
        --tw-translate-y: 0;
        --tw-rotate: 0;
        --tw-skew-x: 0;
        --tw-skew-y: 0;
        --tw-scale-x: 1;
        --tw-scale-y: 1;
        --tw-pan-x: ;
        --tw-pan-y: ;
        --tw-pinch-zoom: ;
        --tw-scroll-snap-strictness: proximity;
        --tw-gradient-from-position: ;
        --tw-gradient-via-position: ;
        --tw-gradient-to-position: ;
        --tw-ordinal: ;
        --tw-slashed-zero: ;
        --tw-numeric-figure: ;
        --tw-numeric-spacing: ;
        --tw-numeric-fraction: ;
        --tw-ring-inset: ;
        --tw-ring-offset-width: 0px;
        --tw-ring-offset-color: #fff;
        --tw-ring-color: rgba(59,130,246,.5);
        --tw-ring-offset-shadow: 0 0 #0000;
        --tw-ring-shadow: 0 0 #0000;
        --tw-shadow: 0 0 #0000;
        --tw-shadow-colored: 0 0 #0000;
        --tw-blur: ;
        --tw-brightness: ;
        --tw-contrast: ;
        --tw-grayscale: ;
        --tw-hue-rotate: ;
        --tw-invert: ;
        --tw-saturate: ;
        --tw-sepia: ;
        --tw-drop-shadow: ;
        --tw-backdrop-blur: ;
        --tw-backdrop-brightness: ;
        --tw-backdrop-contrast: ;
        --tw-backdrop-grayscale: ;
        --tw-backdrop-hue-rotate: ;
        --tw-backdrop-invert: ;
        --tw-backdrop-opacity: ;
        --tw-backdrop-saturate: ;
        --tw-backdrop-sepia: ;
        --tw-contain-size: ;
        --tw-contain-layout: ;
        --tw-contain-paint: ;
        --tw-contain-style: ;
        font-family: ClashGrotesk-Variable,sans-serif;
        background-image: linear-gradient(to bottom right,var(--tw-gradient-stops));
        --tw-gradient-from: hsl(var(--primary)) var(--tw-gradient-from-position);
        --tw-gradient-stops: var(--tw-gradient-from),var(--tw-gradient-to);
        --tw-gradient-to: hsl(var(--secondary)) var(--tw-gradient-to-position);
        background-clip: text;
        color: transparent;
                }
        </style>
    """, unsafe_allow_html=True)

    # Title and Subtitle
    st.markdown(f"<h1 class='title'>Let's craft your vision into <span class='gradient-text'>reality.</span></h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>I'm currently available for hiring and freelance work.</p>", unsafe_allow_html=True)

    # Icon Bar
    st.markdown("""
        <div class="icon-bar">
            <a href="https://www.linkedin.com/in/amir" target="_blank">&#x1F465;</a>
            <a href="https://www.xing.com/profile/Amir" target="_blank">&#x1F4F1;</a>
            <a href="https://github.com/amir" target="_blank">&#x1F4BB;</a>
            <a href="mailto:amir@example.com" target="_blank">&#x2709;</a>
        </div>
    """, unsafe_allow_html=True)

    # Download Resume Button
    st.markdown("""
        <a href="https://amir-portfolio.com/resume.pdf" target="_blank">
            <button class="download-btn">Download Resume</button>
        </a>
    """, unsafe_allow_html=True)
