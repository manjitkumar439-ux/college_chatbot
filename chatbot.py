import difflib
import string

# ---------------- FAQs ---------------- #
faq_answers = {
    "exam date": "Your next exam is scheduled for last November 2025 📅. The detailed timetable will be shared soon.",
    "leave application": "To apply for leave 📝, visit the office and fill out a form, or apply online via the portal.",
    "hostel rules": "Hostel rules 🏫: return before 9:30 PM, daily attendance, no visitors inside rooms.",
    "syllabus": "The syllabus 📚 is available on the college website or your department office.",
    "library": "Our library is open from 1:00 PM 📖. You can borrow 2 books for 14 days with your library card.",
    "principal": "Our Principal is Dr. Bhagwan Singh 👨‍🏫. Meet him during office hours with prior permission.",
    "sports": "Sports 🏅: cricket, football, basketball, indoor games. Annual Sports Week happens in February.",
    "canteen": "The canteen 🍴 is open from 8:30 AM to 6:00 PM with affordable meals and snacks.",
    "greeting": "Hello 👋, I am the chatbot of your college Government Polytechnic Patna-07. What can I help you with today?",
    "hod cse": "The HOD of CSE branch is Prof. Neha Rani Ma'am 👩‍🏫.",
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

# ---------------- Keywords ---------------- #
faq_keywords = {
    "exam date": ["exam", "exam date", "next exam", "when is exam", "exam timetable"],
    "leave application": ["leave", "leave application", "how to apply leave", "leave form"],
    "hostel rules": ["hostel", "rules of hostel", "hostel rules"],
    "syllabus": ["syllabus", "subjects", "course syllabus"],
    "library": ["library", "books", "reading room"],
    "principal": ["principal", "head of college", "college principal"],
    "sports": ["sports", "games", "playground", "athletics"],
    "canteen": ["canteen", "food", "mess", "dining", "food in hostel"],
    "greeting": ["hello", "hi", "hii", "hey", "how are you"],
    "hod cse": ["hod cse", "cse hod", "computer science hod", "head of cse", "cs hod", "computer science & engineering", "cse", "cse branch"],
    "hod electrical": ["hod electrical", "electrical hod", "head of electrical", "electrical department hod", "ee hod", "electrical engineering", "electrical branch"],
    "hod mechanical": ["hod mechanical", "mechanical hod", "mechanical department hod", "me hod", "mechanical engineering", "mechanical branch"],
    "hod electronics": ["hod electronics", "electronics hod", "electronics department hod", "electronics engineering", "electronics branch"],
    "hod civil": ["hod civil", "civil hod", "civil department hod", "civil engineering", "civil branch"],
    "hod textile": ["hod textile", "textile hod", "textile department hod", "textile engineering", "textile branch"],
    "hod printing": ["hod printing", "printing hod", "printing department hod", "printing engineering", "printing branch"],
    "hod ceramics": ["hod ceramics", "ceramic hod", "ceramics engineering", "ceramics branch"],
    "training and placement officers": ["tpo", "training and placement officer", "placement officers", "training officers"]
}

# ---------------- Bad words ---------------- #
bad_words = ["fuck", "shit", "bitch", "damn", "ass", "idiot", "love you"]

# ---------------- Holiday handler ---------------- #
def get_holiday_reply(user_input):
    clean_input = user_input.lower().translate(str.maketrans("", "", string.punctuation)).strip()
    words = clean_input.split()

    # Check festivals first
    for month, events in holidays.items():
        for fest, date in events.items():
            fest_words = fest.lower().split()
            # Check if all words of festival are in the user input
            if all(word in words for word in fest_words):
                return f"The holiday for {fest.title()} is on {date}"

    # Then check months
    for month, events in holidays.items():
        if month in words:
            reply = f"There are {len(events)} holidays in {month.capitalize()}:<br>"
            for fest, date in events.items():
                reply += f"• {date} → {fest.title()}<br>"
            return reply.strip()

    return None




# ---------------- Bot reply ---------------- #
def get_bot_reply(user_input):
    clean_input = user_input.lower().translate(str.maketrans("", "", string.punctuation))

    # Check for bad words
    for bad_word in bad_words:
        if " " in bad_word:
            if bad_word in clean_input:
                return "⚠️ Please use polite language."
        else:
            if bad_word in clean_input.split():
                return "⚠️ Please use polite language."

    # Check holidays
    holiday_reply = get_holiday_reply(clean_input)
    if holiday_reply:
        return holiday_reply

    # Check FAQs
    for answer_key, keywords in faq_keywords.items():
        for kw in keywords:
            if kw in clean_input:
                return faq_answers[answer_key]

    # Fuzzy match fallback
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

    return "Sorry, I don’t have information on that. Please contact the office 📌."
