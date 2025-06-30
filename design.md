# **Design Document: SmartSearch CLI – AI Academic Resource Finder**

---

## 1. **Project Overview**

**SmartSearch CLI** is a command-line tool that helps students quickly find high-quality, topic-specific video resources. By integrating Gemini (Google GenAI) and YouTube APIs, it turns vague queries into effective searches and stores results in a local SQLite database.

---

## 2. **Goals & Success Criteria**

- Minimize time spent searching for academic help.
- Provide relevant, accurate YouTube video links.
- Save query history for easy access.
- Fully functional CLI with unit tests and CI.

---

## 3. **System Components**

### a. **CLI Interface**

- Takes user input and displays results.
- Allows history viewing and repeat searches.

### b. **Gemini API**

- Converts user input into smarter search prompts.

### c. **YouTube API**

- Fetches video results using AI-enhanced prompt.

### d. **SQLite Database**

- Stores queries and video results.
- Supports basic history retrieval.

---

## 4. **Data Flow**

```
User Input → Gemini API → Optimized Prompt → YouTube API → Results → CLI Display + SQLite Save
```

---

## 5. **Database Schema**

**Table:** `search_history`

| Column      | Type     | Description                 |
| ----------- | -------- | --------------------------- |
| id          | INTEGER  | Primary Key                 |
| user_query  | TEXT     | Original input              |
| ai_prompt   | TEXT     | Gemini-processed query      |
| video_title | TEXT     | YouTube video title         |
| video_url   | TEXT     | Video link                  |
| timestamp   | DATETIME | Date and time of the search |

---

## 6. **APIs Used**

- **Gemini API:** Enhances user queries.
- **YouTube Data API:** Returns video results.
- **Both require API keys for authorization.**

---

## 7. **Testing Plan**

- **Unit Tests:**

  1. Gemini response handling (mocked)
  2. YouTube result parsing
  3. SQLite query/store functions

- **CI/CD:**
  - GitHub Actions to run tests and style checks.

---

## 8. **Error Handling**

| Scenario           | Handling                  |
| ------------------ | ------------------------- |
| No YouTube results | Show message, allow retry |
| Gemini API down    | Use user input as-is      |
| Empty input        | Prompt for valid input    |
| API quota exceeded | Show error, use history   |

---

## 9. **Risks**

- API rate limits
- Low-quality or irrelevant results
- Database read/write failures

---

## 10. **Future Improvements**

- Add video filters (duration, rating)
- Bookmark videos
- Optional GUI interface
- Add support for other content APIs (e.g., Khan Academy)
