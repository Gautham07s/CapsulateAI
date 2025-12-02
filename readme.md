# 💡 Capsulate AI – Smart Meeting Summarizer

Capsulate AI is an intelligent and user-friendly meeting summarization tool designed to help users convert YouTube video content into concise, meaningful summaries. Built with Streamlit for the frontend and powered by **Google's Gemini 2.0 Flash** model for summarization, this project provides seamless video transcription, timestamped transcripts, and downloadable summaries in both .txt and .pdf formats.

## 🔍 Key Features
* **🎥 YouTube Video Support** – Paste any YouTube URL to get instant transcriptions.
* **✨ Gemini-powered Summarization** – Uses **Gemini 2.0 Flash** for fast, intelligent, context-aware summaries.
* **⏱️ Timestamps** – Clearly segmented transcripts with precise time markers.
* **📥 Downloadable Summaries** – Export summaries as `.txt` or `.pdf` instantly.
* **🎨 Modern UI** – Clean, professional interface built using Streamlit.
* **⚡ Optimized Performance** – Uses the latest `youtube-transcript-api` (v1.2+) for reliable fetching.

## ⚙️ Technologies Used
| Layer | Tools / Libraries |
| :--- | :--- |
| **Frontend** | Streamlit |
| **Backend** | Python, Google Generative AI (Gemini) |
| **Transcription** | YouTube Transcript API |
| **PDF Generation** | FPDF |
| **Environment** | Python-dotenv |

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/Gautham07s/CapsulateAI.git](https://github.com/Gautham07s/CapsulateAI.git)
cd CapsulateAI
```
### 2. Install dependencies
```Bash
pip install -r requirements.txt
```
### 3. Set up your API Key
Create a .env file in the root directory and add your Google Gemini API key:

```Bash
GOOGLE_API_KEY=your_api_key_here
```
### 4. Run the app
```Bash
streamlit run app.py
```
### 2. Push it to GitHub
Once you have saved the file, run these commands in your terminal to upload it:

```powershell
git add README.md
git commit -m "Added project documentation"
git push origin main
```
