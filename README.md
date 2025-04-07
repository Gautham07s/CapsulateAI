💡 Capsulate AI – Smart Meeting Summarizer
Capsulate AI is an intelligent and user-friendly meeting summarization tool designed to help users convert long audio and video meetings into concise, meaningful summaries. Built with Streamlit for the frontend and powered by Google's Gemini 1.5 Pro model for summarization, this project provides seamless audio/video transcription, timestamped transcripts, and downloadable summaries in both .txt and .pdf formats.

🔍 Key Features
🎥 Audio/Video Support – Upload MP4, MP3, WAV files and get transcriptions.

✨ Gemini-powered Summarization – Uses Gemini 1.5 Pro for intelligent, context-aware summaries.

⏱️ Timestamps in Transcripts – Clearly segmented transcripts with time markers.

📥 Downloadable Summaries – Export summaries as .txt or .pdf instantly.

🎨 Modern UI – Clean, professional interface built using Streamlit.

⚡ Optimized Performance – Designed for faster execution on machines without GPUs.

⚙️ Technologies Used
Layer	Tools / Libraries
Frontend	Streamlit
Backend	Python, Google Generative AI (Gemini)
Transcription	OpenAI Whisper
UI/UX	Streamlit Components, Custom CSS
File Export	FPDF, Text Generation


# 1. Clone the repository
git clone https://github.com/your-username/capsulate-ai.git
cd capsulate-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Gemini API key in a .env file
echo "GOOGLE_API_KEY=your_api_key_here" > .env

# 4. Run the app
streamlit run app.py
