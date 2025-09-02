import difflib


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
}

faq_keywords = {
    "exam date": ["exam", "exam date", "next exam", "when is exam", "exam timetable"],
    "leave application": ["leave", "leave application", "how to apply leave", "leave form"],
    "hostel rules": ["hostel", "rules of hostel", "hostel rules"],
    "syllabus": ["syllabus", "subjects", "course syllabus"],
    "library": ["library", "books", "reading room"],
    "principal": ["principal", "head of college", "college principal"],
    "sports": ["sports", "games", "playground", "athletics"],
    "canteen": ["canteen", "food", "mess", "dining"],
    "greeting": ["hello", "hi", "hii", "hey", "how are you"],
    "hod cse": ["hod cse", "cse hod", "computer science hod", "head of cse", "cs hod", "computer science & engineering", "cse"],
    "hod electrical": ["hod electrical", "electrical hod", "head of electrical", "electrical department hod", "ee hod", "electrical engineering", "ee"],
    "hod mechanical": ["hod mechanical", "mechanical hod", "hod of mehanical", "mechanical department hod", "me hod", "mechanical engineering", "me", "mechanical engineering department"],
    "hod electronics": ["hod electronics", "electronics hod", "hod of electronics", "electronics department hod", "electronic hod", "electronics engineering", "electronic engineering", "head of electronics"]
}

def get_bot_reply_fixed(user_input):
    user_input = user_input.lower()
    words = set(user_input.split())  # split input into words

    # 1️⃣ Check keywords by word overlap
    for answer_key, keywords in faq_keywords.items():
        for kw in keywords:
            kw_words = set(kw.lower().split())
            if kw_words <= words:  # all words in keyword are in user input
                return faq_answers[answer_key]

    # 2️⃣ If no exact match, use fuzzy matching on keywords (optional)
    all_keywords = []
    keyword_to_answer = {}
    for ans_key, keywords in faq_keywords.items():
        for k in keywords:
            all_keywords.append(k)
            keyword_to_answer[k] = ans_key

    best_match = difflib.get_close_matches(user_input, all_keywords, n=1, cutoff=0.4)
    if best_match:
        matched_keyword = best_match[0]
        answer_key = keyword_to_answer[matched_keyword]
        return faq_answers[answer_key]

    # 3️⃣ Default fallback
    return "Sorry, I don’t have information on that. Please contact the office 📌."
