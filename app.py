import streamlit as st
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
from fpdf import FPDF

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

def extract_video_id(youtube_url):
    """
    Extracts the video ID from various YouTube URL formats.
    """
    try:
        parsed_url = urlparse(youtube_url)
        if "youtube.com" in parsed_url.netloc:
            return parse_qs(parsed_url.query).get("v", [None])[0]
        elif "youtu.be" in parsed_url.netloc:
            return parsed_url.path.lstrip("/")
        else:
            return None
    except Exception:
        return None

def extract_transcript_details(video_id):
    """
    Fetches the transcript using the new v1.2+ object-based API.
    """
    try:
        # 1. Create an instance of the API
        yt = YouTubeTranscriptApi()
        
        # 2. List all available transcripts
        transcript_list = yt.list(video_id)
        
        # 3. Find the best English transcript (Manual or Auto-generated)
        transcript = transcript_list.find_transcript(['en'])
        
        # 4. Fetch the actual data (Returns a FetchedTranscript object)
        transcript_data = transcript.fetch()
        
        # 5. Format the text with timestamps
        # FIX: Use dot notation (.start, .text)
        transcript_text = "\n".join([f"[{item.start:.2f}s] {item.text}" for item in transcript_data])
        
        return transcript_text

    except TranscriptsDisabled:
        st.error("❌ Transcripts are disabled for this video.")
        return None
    except NoTranscriptFound:
        st.error("❌ No English transcript found for this video.")
        return None
    except Exception as e:
        st.error(f"❌ Error retrieving transcript: {e}")
        return None

def generate_gemini_content(transcript_text):
    """
    Sends the transcript to Google Gemini for summarization.
    """
    try:
        # CHANGED: "gemini-2.0-flash" is in your list and excellent for free usage
        model = genai.GenerativeModel("gemini-2.0-flash")
        
        prompt = "Summarize the transcript in bullet points within 350 words:\n\n"
        response = model.generate_content(prompt + transcript_text)
        return response.text if response else "No summary generated."
    except Exception as e:
        st.error(f"⚠️ Error generating summary: {e}")
        return None

def save_text_file(content):
    return content.encode("utf-8")

def save_pdf(content):
    """
    Generates a PDF file from the summary content.
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # multi_cell handles text wrapping automatically
    pdf.multi_cell(0, 10, content)
    return pdf.output(dest="S").encode("latin1")

# --- STREAMLIT UI SETUP ---
st.set_page_config(page_title="CapsulateAI - Transcript Summarizer", layout="wide")

st.markdown("""
    <style>
        body {background-color: #f8f9fa;}
        .main {background: white; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);}
        h1 {color: #007bff; text-align: center;}
        .stButton>button {background-color: #007bff; color: white; font-size: 18px; padding: 10px 20px; border-radius: 5px;}
        .stTextInput>div>div>input {font-size: 16px; padding: 10px;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("🎥 CapsulateAI - Transcript Summarizer")
st.markdown("<p style='text-align:center;'>Paste a YouTube video URL to get its transcript and summary.</p>", unsafe_allow_html=True)

youtube_link = st.text_input("🔗 Paste YouTube Video URL:")

if youtube_link:
    video_id = extract_video_id(youtube_link)
    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", caption="Video Thumbnail", use_container_width=True)
    else:
        st.warning("⚠️ Invalid YouTube link. Please enter a valid URL.")

if st.button("🚀 Get Summary & Transcript"):
    if not youtube_link:
        st.warning("⚠️ Please enter a YouTube URL.")
    elif not video_id:
        st.error("❌ Could not extract video ID. Please check your link.")
    else:
        if not GOOGLE_API_KEY:
            st.error("❌ Google API Key is missing. Check your .env file.")
        else:
            with st.spinner("⏳ Fetching transcript..."):
                transcript_text = extract_transcript_details(video_id)
            
            if transcript_text:
                with st.spinner("🤖 Generating summary..."):
                    summary = generate_gemini_content(transcript_text)
                
                if summary:
                    st.markdown("## ✨ Video Summary:")
                    st.write(summary)
                    
                    st.markdown("## 📜 Full Transcript:")
                    st.text_area("Transcript with Timestamps:", transcript_text, height=300)
                    
                    # Download Buttons
                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button("📥 Download Summary (TXT)", save_text_file(summary), "summary.txt", "text/plain")
                        st.download_button("📥 Download Transcript (TXT)", save_text_file(transcript_text), "transcript.txt", "text/plain")
                    with col2:
                        try:
                            pdf_data = save_pdf(summary)
                            st.download_button("📥 Download Summary (PDF)", pdf_data, "summary.pdf", "application/pdf")
                        except Exception as e:
                            st.error(f"PDF Generation Error: {e}")
                else:
                    st.error("⚠️ Failed to generate summary.")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<footer style='text-align:center; margin-top:20px;'>Created by CapsulateAI Team.</footer>", unsafe_allow_html=True)