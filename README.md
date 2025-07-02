# SEO Week 2 Project: SmartSearch

### Problem Statement

- A lot of students feel stuck when trying to get help on assignments. There's so much information online that it's hard to tell what's actually helpful. According to the Education Data Initiative, more than 60% of students spend over 3 hours a week just looking for academic help. That's time they could be learning, but instead they're lost in a sea of videos, forums, and outdated resources.

### Our Solution

- We built a simple command-line tool to make that search process smarter and faster. Using Gemini AI, we help students turn confusing questions into better search prompts. Then, we use the YouTube API to find videos that actually explain the topic well. Everything gets saved in a SQLite database, so if a student wants to revisit a video later, it's all there.

### Technology Used

- Gemini API
- Youtube API
- SQLite Database

### Design Overview

SmartSearch CLI is built around a simple but powerful flow:

1. User enters a topic or question in the command-line interface.
2. Gemini API refines it into a smarter search prompt.
3. YouTube API finds clear, relevant videos.
4. Results are shown in the terminal and stored in an SQLite database.
5. Students can view or revisit past results anytime.

👉 **[Read the full Design Document](./design.md)** for technical details, schema, and implementation breakdown.

---

## Setup Instructions

### 1. Clone the repository  
Run `git clone https://github.com/rubyoliveira/seoweek2.git` then `cd seoweek2`

### 2. Create a virtual environment (optional but recommended)  
Run `python -m venv venv`  

- On **Windows** run: `venv\Scripts\activate`  
- On **macOS/Linux** run: `source venv/bin/activate`

### 3. Install dependencies  
Run `pip install -r requirements.txt`

### 4. Set up your `.env` file  
Create a `.env` file in the root directory and add:  
- GEMINI_API_KEY=your_gemini_api_key
- YOUTUBE_API_KEY=your_youtube_api_key


### 5. Run the application  
Run `python SmartSearch.py`

### 6. Run tests  
- To run all unit tests: `pytest tests/`  
- To run local mock tests without hitting real APIs: `python -m unittest discover -s tests_local`

---
