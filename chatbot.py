import difflib
import string
import re

# ---------------- FAQs ---------------- #
faq_answers = {
    "exam date": "Your next exam is scheduled from 02 December 2025 to 12 December 2025 📅.",
    "hostel rules": "Hostel rules 🏫: return before 9:30 PM, no visitors inside rooms.",
    "library": "Our library is open from 1:00 PM 📖. You can borrow 2 books for 14 days with your library card.",
    "principal": "Our Principal is Dr. Bhagwan Singh 👨‍🏫. Meet him during office hours with prior permission.",
    "greeting": "Hello 👋, I am the chatbot of your college Government Polytechnic Patna-07. What can I help you with today?",
    "hod cse": "The HOD of CSE branch is Prof. Neha Ma'am 👩‍🏫.",
    "hod electrical": "The HOD of ELECTRICAL branch is Prof. Rabindra sir 👨‍🏫.",
    "hod mechanical": "The HOD of MECHANICAL branch is Prof. Nikhil Patel 👨‍🏫.",
    "hod electronics": "The HOD of ELECTRONICS branch is Prof. Chandraprakash sir 👨‍🏫.",
    "hod civil": "The HOD of CIVIL branch is Prof. Arbind sir 👨‍🏫.",
    "hod textile": "The HOD of TEXTILE branch is Prof. S.N Chaudhary 👨‍🏫.",
    "hod printing": "The HOD of PRINTING branch is Prof. Beer Bahadur Singh 👨‍🏫.",
    "hod ceramics": "The HOD of CERAMICS branch is Prof. Abhay Kumar 👨‍🏫.",
    "training and placement officers": "The TRAINING & PLACEMENT Officers are Brajendra Kumar, Saurav Suman and Ajay Kumar 👨‍🏫."
}

# ---------------- Holiday list ---------------- #
holidays = {
    "january": {
        "new year": "01 January 2025",
        "guru gobind singh jayanti": "06 January 2025",
        "makar sankranti": "14 January 2025",
        "republic day": "26 January 2025"
    },
    "february": {
        "saraswati puja": "03 February 2025",
        "sant ravidas jayanti": "12 February 2025",
        "shab e barat": "14 February 2025",
        "mahashivratri": "26 February 2025"
    },
    "march": {
        "holi": "13 March 2025 - 15 March 2025",
        "bihar divas": "22 March 2025",
        "eid-ul-fitar (eid)": "31 March 2025"
    },
    "april": {
        "smart ashok jayanti": "05 April 2025",
        "ramnavami": "06 April 2025",
        "mahavir jayanti": "10 April 2025",
        "dr. bhimrao ambedkar jayanti": "14 April 2025",
        "good friday": "18 April 2025",
        "veer kunwar singh jayanti": "23 April 2025"
    },
    "may": {
        "may divas/shram divas": "01 May 2025",
        "janki navami": "06 May 2025",
        "buddha purnima": "12 May 2025"
    },
    "june": {
        "summer leave": "01 June 2025 - 30 June 2025"
    },
    "july": {
        "muharram": "06 July 2025"
    },
    "august": {
        "rakshabandhan": "09 August 2025",
        "independence day": "15 August 2025",
        "shree krishna janmashtami": "16 August 2025"
    },
    "september": {
        "hazrat muhammad sahab janamdin": "05 September 2025",
        "durga puja": "29 September 2025 - 02 October 2025",
        "mahatma gandhi jayanti": "02 October 2025"
    },
    "october": {
        "dipawali/chitragupt puja/bhai dooj/chhath puja": "20 October 2025 - 28 October 2025"
    },
    "november": {
        "gurunanak jayanti/kartik purnima": "05 November 2025"
    },
    "december": {
        "christmas day/guru govind singh jayanti": "25 December 2025 - 31 December 2025"
    }
}

# ---------------- Keywords (for FAQ fallback) ---------------- #
faq_keywords = {
    "exam date": ["exam", "exam date", "next exam", "when is exam", "exam timetable"],
    "leave application": ["leave", "leave application", "how to apply leave", "leave form"],
    "hostel rules": ["hostel", "rules of hostel", "hostel rules"],
    "library": ["library", "books", "reading room"],
    "principal": ["principal", "head of college", "college principal"],
    "greeting": ["hello", "hi", "hii", "hey", "how are you"],
}

# Branch names list for HOD 
BRANCHES = ["cse", "electrical", "mechanical", "electronics", "civil", "textile", "printing", "ceramics"]

# ---------------- Utility helpers ---------------- #
def clean_text(text):
    return text.lower().translate(str.maketrans("", "", string.punctuation))


# ---------------- Holiday handler ---------------- #
def get_holiday_reply(user_input):
    clean = clean_text(user_input)
    words = clean.split()

    # festival exact match (multi-word)
    for month, events in holidays.items():
        for fest, date in events.items():
            fest_words = fest.lower().split()
            if all(w in words for w in fest_words):
                return f"The holiday for {fest.title()} is on {date}"
    # month query
    for month, events in holidays.items():
        if month in words:
            reply = f"There are {len(events)} holidays in {month.capitalize()}:<br>"
            for fest, date in events.items():
                reply += f"• {date} → {fest.title()}<br>"
            return reply.strip()
    return None

# ---------------- HOD handler ---------------- #
def get_hod_reply(user_input):
    clean = clean_text(user_input)
    # Only handle HOD if user explicitly asked about HOD / 'who is' with branch or 'head of'
    if ("hod" in clean) or ("head of" in clean) or re.search(r'\bwho is\b', clean):
        for branch in BRANCHES:
            if branch in clean:
                key = f"hod {branch}"
                # safe lookup
                return faq_answers.get(key, f"HOD information for {branch.upper()} not available.")
    return None



# ---------------- Bot reply (master) ---------------- #
def get_bot_reply(user_input):
    if not user_input or not user_input.strip():
        return "⚠️ Please type a message."

    clean_input = clean_text(user_input)

    # Holidays
    holiday_reply = get_holiday_reply(user_input)
    if holiday_reply:
        return holiday_reply

    # HOD queries (higher priority than syllabus)
    hod_reply = get_hod_reply(user_input)
    if hod_reply:
        return hod_reply

  

    #  FAQs by keywords
    for answer_key, keywords in faq_keywords.items():
        for kw in keywords:
            if kw in clean_input:
                return faq_answers[answer_key]

    # Fuzzy match fallback (try best keyword)
    all_keywords = []
    keyword_to_answer = {}
    for ans_key, keywords in faq_keywords.items():
        for k in keywords:
            all_keywords.append(k)
            keyword_to_answer[k] = ans_key

    best_match = difflib.get_close_matches(clean_input, all_keywords, n=1, cutoff=0.6)
    if best_match:
        matched_keyword = best_match[0]
        answer_key = keyword_to_answer[matched_keyword]
        return faq_answers[answer_key]

    # Default fallback
    return "Sorry, I don’t have information on that. Please contact the office 📌."