# 📄 Resume Review Bot

An AI-powered resume reviewer that gives structured, honest feedback for engineering students. I built it to solve a real problem rather than just as a tutorial exercise.

## WHY I BUILT THIS

After learning the basics of LangChain and working with LLM APIs on my Astro Bot project, I wanted to build something actually useful. Many students don't have anyone to give them direct, specific feedback on their resume, so this bot does that: paste your resume, get a structured review and a rating out of 10.

## WHAT I BUILT MYSELF

The core logic is mine: the review prompt (a 7-point rubric covering overall impression, skills, projects, education, what's missing, what to improve, and a score), the Groq + LangChain integration, and the logic that ties it together.

I used Claude to help build the UI (layout, feedback buttons, session state flow), since I'm still learning frontend patterns and wanted to focus on the review logic.

## HOW IT WORKS

1. Paste your resume text into the box
2. Click "Review My Resume"
3. Get feedback across 7 categories, plus a score out of 10
4. Mark the review as helpful or not, with an optional comment

## TECHNICAL STACK

- Streamlit
- LangChain (`langchain-groq`, `langchain-core`)
- Groq API (LLaMA 3.1 8B Instant)

## Running it locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file (see `.env.example`) and add your own Groq API key:
   ```
   GROQ_API_KEY=your_key_here
   ```
   Get a free key at [console.groq.com](https://console.groq.com).

3. Run the app:
   ```bash
   streamlit run YOUR_FILE_NAME.py
   ```

## What's next

- Support for PDF/DOCX uploads instead of pasted text
- Feedback tailored to the target role (SDE, data science, core engineering)
- Saving feedback ratings permanently instead of only in session state