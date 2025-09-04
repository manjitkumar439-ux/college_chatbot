import difflib
import string


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
    "hod mechanical": "The HOD of MECHANICAL branch is Prof. Nikhil patel 👨‍🏫.",
    "hod electronics":"The HOD of ELECTRONICS branch is Prof. Chandraprakash sir 👨‍🏫.",
    "hod civil":"The HOD of CIVIL branch is Prof. Arbind sir 👨‍🏫.",
    "hod textile":"The HOD of TEXTILE branch is Prof. s.n chaudhary 👨‍🏫.",
    "hod printing":"The HOD of PRINTING branch is Prof. beer bahadur singh 👨‍🏫.",
    "hod ceramics":"The HOD of CERAMICS branch is prof. Abhay kumar 👨‍🏫.",
    "training and placement officers": "The TRAINING & PLACEMENT Officers are --> Brajendra kumar, Saurav suman and Ajay kumar 👨‍🏫."
}

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
    "hod mechanical": ["hod mechanical", "mechanical hod", "hod of mehanical", "mechanical department hod", "me hod", "mechanical engineering", "mechanical engineering department", "mechanical branch"],
    "hod electronics": ["hod electronics", "electronics hod", "hod of electronics", "electronics department hod", "electronic hod", "electronics engineering", "electronic engineering", "head of electronics", "electronics branch"],
    "hod civil": ["hod civil", "civil hod", "hod of civil", "civil department hod", "civil enginnering hod", "civil engineering", "head of civil", "civil branch",],
    "hod textile": ["hod textile", "textile hod", "hod of textile", "textile department hod", "textile engineering hod", "textile engineering", "head of textile", "textile branch",],
    "hod printing": ["hod printing", "printing hod", "hod of printing", "printing department hod", "printing tecnology hod", "printing engineering", "head of printing", "printing branch", "printing tecnology"],
    "hod ceramics": ["hod ceramics", "hod ceramic", "ceramic hod", "ceramics hod", "hod of ceramics", "ceramics department hod", "ceramics engineering hod", "ceramics engineering", "head of ceramics", "ceramics branch", "ceramic", "ceramics"],
    "training and placement officers": ["tpo", "training and placement officer", "training & placement officers"],


}
bad_words = ["fuck", "shit", "bitch", "damn", "ass", "idiot", "love you",]

def contains_bad_word(user_input):
    # Normalize input
    clean_input = user_input.lower()
    clean_input = clean_input.translate(str.maketrans("", "", string.punctuation))
    words = clean_input.split()

    for bad_word in bad_words:
        # if the bad word has spaces (like "love you"), check substring
        if " " in bad_word:
            if bad_word in clean_input:
                return True
        else:
            if bad_word in words:
                return True
    return False

def get_bot_reply(user_input):
    # Normalize input
    clean_input = user_input.lower().translate(str.maketrans("", "", string.punctuation))

    # 0️⃣ Check for bad words
    for bad_word in bad_words:
        if " " in bad_word:  # multi-word
            if bad_word in clean_input:
                return "⚠️ Please use polite language."
        else:
            if bad_word in clean_input.split():
                return "⚠️ Please use polite language."

    # 1️⃣ Check keywords by substring match
    for answer_key, keywords in faq_keywords.items():
        for kw in keywords:
            if kw in clean_input:
                return faq_answers[answer_key]

    # 2️⃣ Fuzzy matching fallback
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

    # 3️⃣ Default fallback
    return "Sorry, I don’t have information on that. Please contact the office 📌."
