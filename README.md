# 🧠 MoodDecode – NLP API Project

#### 👩‍💻 By Sthuthi for MoodDecode Developer Challenge

---

## ✅ Overview

MoodDecode is an emotion-aware NLP API built using **Flask** and **Gemini 2.5 Flash** via Google’s Generative AI SDK. It includes three endpoints that detect emotion, identify mental health crises, and summarize emotional content.

The project demonstrates real-world backend applications for emotional analysis, crisis detection, and summarization, suitable for use in mental health tools, journaling apps, or smart assistants.

---

## 🚀 API Endpoints

### 🔹 POST `/analyze_mood`
**Input:**
```json
{
  "text": "I feel amazing today!"
}
```
**Output:**
```json
{
  "emotion": "joyful"
}
```
**Description:** Detects the primary emotion in the input text using Gemini 2.5 Flash. Returns a single emotion label.

---

### 🔹 POST `/detect_crisis`
**Input:**
```json
{
  "text": "I'm feeling hopeless and might hurt myself"
}
```
**Output:**
```json
{
  "crisis_detected": true
}
```
**Description:** Checks for signs of emotional crisis or suicidal ideation. Returns true if such a pattern is detected.

---

### 🔹 POST `/summarize`
**Input:**
```json
{
  "text": "Lately, I've been feeling exhausted and disconnected from people around me. Even simple tasks feel overwhelming, and I can't focus on anything."
}
```
**Output:**
```json
{
  "summary": "The user feels emotionally drained and overwhelmed."
}
```
**Description:** Generates a concise emotional summary using Gemini 2.5 Flash.

---

## 🔧 Tools, Models & APIs Used

- **Backend**: Python 3, Flask
- **Model**: Gemini 2.5 Flash via `google-generativeai`
- **API Platform**: Google Generative AI Python SDK
- **Hosting**: [Render](https://mooddecode-7mmq.onrender.com/)
- **Environment**: `.env` file used for storing the Gemini API key securely

---

## 🧪 Sample Usage

You can test the API using Postman, cURL, or any HTTP client.

**Example:**
```bash
curl -X POST https://mooddecode-7mmq.onrender.com/analyze_mood \
  -H "Content-Type: application/json" \
  -d '{"text": "I am really frustrated with everything lately."}'
```

---