import tkinter as tk
from tkinter import messagebox
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# ترجمه و تحلیل احساسات
translator = Translator()
analyzer = SentimentIntensityAnalyzer()


# تابع تشخیص احساسات
def analyze_sentiment():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("هشدار", "لطفاً متن خود را وارد کنید!")
        return

    # بررسی دستی برای برخی عبارات منفی فارسی
    negative_phrases = ["حالم بده", "احساس بدی دارم", "افسرده‌ام", "ناراحتم", "غمگینم", "دلم گرفته"]
    for phrase in negative_phrases:
        if phrase in text:
            result_label.config(text="نتیجه: منفی (کلمه کلیدی)", fg="red")
            return

    # ترجمه متن فارسی به انگلیسی
    translated_text = translator.translate(text, src='fa', dest='en').text

    # تحلیل احساسات با VADER
    sentiment = analyzer.polarity_scores(translated_text)
    compound_score = sentiment['compound']

    # نتیجه احساسات
    if compound_score >= 0.05:
        result_label.config(text=f"نتیجه: مثبت (اعتماد: {compound_score:.2f})", fg="green")
    elif compound_score <= -0.05:
        result_label.config(text=f"نتیجه: منفی (اعتماد: {compound_score:.2f})", fg="red")
    else:
        result_label.config(text=f"نتیجه: خنثی (اعتماد: {compound_score:.2f})", fg="orange")


# رابط گرافیکی با Tkinter
window = tk.Tk()
window.title("تشخیص احساسات ")
window.geometry("400x400")
window.config(bg="#f7f7f7")
header_label = tk.Label(window, text="تحلیل احساسات AI ", font=("Tahoma", 16, "bold"),
                        bg="#f7f7f7",anchor="center")
header_label.pack(pady=20)

# ورودی متن
tk.Label(window, text="متن خود را وارد کنید:", font=("Tahoma", 12), bg="#f7f7f7", anchor="e").pack(pady=10, padx=10,
                                                                                                   fill='x')

text_entry = tk.Text(window, height=6, font=("Tahoma", 12), wrap="word", bg="#ffffff", bd=2, relief="solid", padx=10,
                     pady=10)
text_entry.pack(padx=20, pady=10, fill='x')
text_entry.tag_configure("right", justify="right")
text_entry.insert("1.0", "")  # اینجا هیچ متنی به صورت پیش‌فرض وارد نمی‌شود
text_entry.tag_add("right", "1.0", "end")  # تگ راست‌چین به متن اضافه می‌شود

# دکمه
analyze_button = tk.Button(window, text="تحلیل احساس", command=analyze_sentiment, bg="#4CAF50", fg="white",
                           font=("Tahoma", 12, "bold"), relief="raised", bd=2)
analyze_button.pack(pady=20)

# نمایش نتیجه تحلیل
result_label = tk.Label(window, text="", font=("Tahoma", 14), bg="#f7f7f7", anchor="e")
result_label.pack(pady=20, padx=20, fill='x')

window.mainloop()
