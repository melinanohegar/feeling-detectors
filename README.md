# feeling-detectors
تحلیل احساسات از روی متن
# Persian-English Sentiment Analyzer

This is a simple sentiment analysis tool that supports both **Persian (Farsi) and English text input. It is built using Python with a graphical user interface (GUI) implemented via Tkinter.

The main goal of the project is to allow users to enter short text in either Persian or English, and detect the emotional sentiment behind it — whether the text is Positive, Negative, or Neutral.

---

#How It Works

- The user enters text into the GUI input box.
- If the input is in Persian:
  - The program first checks for certain known negative Persian expressions.
  - If none are found, the text is automatically translated into English using Google Translate (`googletrans`).
- The translated (or original English) text is analyzed using the **VADER Sentiment Analyzer, which scores the sentence for positivity, negativity, and neutrality.
- The result is displayed on screen with a sentiment label and a confidence score.

---

# Features

- Supports both Persian and English input
- Automatically translates Persian to English for sentiment analysis
- Detects emotion using rule-based sentiment scoring (VADER)
- GUI-based: user-friendly interface with no command-line required
- Color-coded output (green for positive, red for negative, orange for neutral)

---

# Requirements

To run this project, make sure you have the following installed:
- Python 3.8 or newer
Install the required Python libraries using pip:
```bash
-pip install googletrans==4.0.0-rc1
-pip install vaderSentiment

Tkinter is included by default with most Python installations.

---
 How to Run

1. Clone this repository or download the ZIP.

2. Open the feeling.py file in your Python IDE (e.g., PyCharm).

3. Run the script.

4. A GUI window will open. Type a sentence and click "تحلیل احساس" (Analyze Sentiment).


---

Developers

This project was developed by:
Hananeh Mirza Hosseini
Golestan Nohegar

