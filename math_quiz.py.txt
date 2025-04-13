import streamlit as st

def run_math_quiz():
    st.image("https://images.unsplash.com/photo-1577896851231-70ef18881754?auto=format&fit=crop&w=1050&q=80", caption="כיתת לימוד", use_column_width=True)
    st.header("🔢 שאלון מתמטי לקביעת רמת לימוד")

    st.markdown("""
    > ענה על השאלות הבאות. לפי התשובות שלך, המערכת תציע רמה מתאימה בין 2 ל־5 יחידות.
    """)

    answers = {}
    score = 0

    with st.form("quiz_form"):
        # שאלה 1
        q1 = st.text_input("1. פתר את המשוואה: x + 3 = 4")
        answers['q1'] = q1.strip()
        
        # שאלה 2
        q2 = st.text_input("2. ציין את הפתרון של הביטוי: (a² - 36) / (a - 6)")
        answers['q2'] = q2.strip()

        # שאלה 3
        q3 = st.text_input("3. מהו הפתרון של: 2x - 10 = 0")
        answers['q3'] = q3.strip()

        # שאלה 4
        q4 = st.text_input("4. מה הפתרון של: 3(x - 1) = 3x - 3")
        answers['q4'] = q4.strip()

        # שאלה 5
        q5 = st.text_input("5. פתר: x² - 4x + 4 = 0")
        answers['q5'] = q5.strip()

        submitted = st.form_submit_button("🔍 בדוק רמה")

    if submitted:
        correct_answers = {
            'q1': ['1', 'x=1'],
            'q2': ['a+6 / a-6', '(a+6)/(a-6)', 'a+6 / a-2', '(a+6)/(a-2)'],
            'q3': ['5', 'x=5'],
            'q4': ['אין פתרון', '0=0', 'אינסוף פתרונות', 'אין סוף'],
            'q5': ['(x-2)²=0', 'x=2']
        }

        for key, user_ans in answers.items():
            correct_list = correct_answers[key]
            if any(correct in user_ans.replace(" ", "") for correct in correct_list):
                score += 1

        st.success(f"✅ ענית נכון על {score} מתוך 5 שאלות.")

        # המלצת רמה
        if score == 5:
            st.info("המערכת ממליצה: 5 יחידות")
        elif score >= 3:
            st.info("המערכת ממליצה: 4 יחידות")
        elif score >= 2:
            st.info("המערכת ממליצה: 3 יחידות")
        else:
            st.info("המערכת ממליצה: 2 יחידות")

        st.markdown("---")
        st.markdown("📄 **תעודה**")
        student_name = st.text_input("שם התלמיד")
        student_class = st.text_input("כיתה")
        if st.button("📥 הורד תעודה להדפסה"):
            st.markdown(f"""
            ### תעודה
            **שם:** {student_name}  
            **כיתה:** {student_class}  
            **רמת לימוד מוצעת:** {score + 1} יחידות  
            """)
questions = [
    {
        "question": "פתור את המשוואה: x + 3 = 4",
        "type": "open",
        "answer": "1"
    },
    {
        "question": "פשט את הביטוי: (a+3)/(a-2) + 3/(a-2)",
        "type": "open",
        "answer": "(a+6)/(a-2)"
    },
    {
        "question": "פתור: x^2 - 6x + 25 = x^2 - x",
        "type": "open",
        "answer": "x = 5"
    },
    {
        "question": "פתור: 5x + 3 = 5x + 3",
        "type": "open",
        "answer": "אין פתרון יחיד, אינסוף פתרונות"
    },
    {
        "question": "פשט את הביטוי: 2x + 5 - x + 3",
        "type": "open",
        "answer": "x + 8"
    }
]

