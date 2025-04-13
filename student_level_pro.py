import streamlit as st
from PIL import Image

# --- סיסמה ---
st.set_page_config(page_title="מערכת הערכת תלמידים", layout="centered")
if 'access_granted' not in st.session_state:
    st.session_state.access_granted = False

if not st.session_state.access_granted:
    st.title("🔐 התחברות למערכת")
    password = st.text_input("הכנס סיסמה:", type="password")
    if password == "15243":
        st.session_state.access_granted = True
        st.experimental_rerun()
    else:
        st.stop()

# --- עיצוב עמוד ---
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main {
        background-color: white;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .title {
        text-align: center;
        font-size: 36px;
        color: #2c3e50;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #7f8c8d;
        margin-bottom: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# --- לוגו ותמונה ---
st.image("https://i.imgur.com/Wq3qY7v.png", width=120)  # לוגו
st.image("https://i.imgur.com/A6l6tWm.jpg", use_column_width=True)  # כיתת למידה

st.markdown('<div class="title">📘 מערכת להערכת רמת תלמידים</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">אנגלית ומתמטיקה • קביעת יחידה מומלצת • ללא מבחן</div>', unsafe_allow_html=True)

# --- טופס פרטים ---
with st.form("student_form"):
    st.header("📝 פרטי תלמיד")
    name = st.text_input("שם התלמיד")
    grade = st.selectbox("כיתה", ["ז'", "ח'", "ט'", "י'", "יא'", "יב'"])
    subject = st.radio("מקצוע", ["אנגלית", "מתמטיקה"])

    st.header("📊 הערכת יכולות")
    participation = st.slider("השתתפות בשיעור", 1, 10, 5)
    homework = st.slider("הגשת שיעורים", 1, 10, 5)
    understanding = st.slider("הבנת החומר בכיתה", 1, 10, 5)
    test_avg = st.slider("ממוצע מבחנים אחרונים", 0, 100, 70)
    motivation = st.selectbox("רמת מוטיבציה", ["נמוכה", "בינונית", "גבוהה"])
    behavior = st.selectbox("התנהלות כללית", ["בעייתית", "סבירה", "טובה"])

    submitted = st.form_submit_button("חשב רמה")

# --- חישוב רמה ---
def calculate_level(p, h, u, t, m, b):
    score = (p + h + u) * 2 + (t / 10)
    if m == "גבוהה": score += 5
    if m == "נמוכה": score -= 5
    if b == "טובה": score += 5
    if b == "בעייתית": score -= 5

    if score >= 35:
        return 5
    elif score >= 30:
        return 4
    elif score >= 25:
        return 3
    elif score >= 20:
        return 2
    else:
        return 1

if submitted and name:
    unit = calculate_level(participation, homework, understanding, test_avg, motivation, behavior)
    
    st.success(f"🏅 התלמיד {name} מתאים ליחידה {unit} ב{subject}")
    
    # תעודה
    with st.expander("📄 לחץ לצפייה בתעודה"):
        st.markdown(f"""
        <div style='border: 2px solid #2980b9; padding: 20px; border-radius: 10px; background-color: #ecf0f1'>
            <h3 style='text-align: center;'>תעודת התאמה לרמת לימוד</h3>
            <p>שם התלמיד: <b>{name}</b></p>
            <p>כיתה: <b>{grade}</b></p>
            <p>מקצוע: <b>{subject}</b></p>
            <p>יחידת לימוד מומלצת: <b>{unit} יחידות</b></p>
            <p>___________________________</p>
            <p>חתימת מורה: _____________</p>
            <p>תאריך: __ / __ / ____</p>
        </div>
        """, unsafe_allow_html=True)

# --- מדריך שימוש ---
with st.expander("📘 מדריך שימוש"):
    st.markdown("""
    - יש להזין את פרטי התלמיד, לבחור מקצוע, ולמלא את הערכת היכולות לפי התרשמות המורה.
    - המערכת תחשב באופן חכם את רמת היחידה המתאימה (1–5).
    - ניתן להדפיס תעודת המלצה למורה או ליועץ/ת.
    """)

# --- קרדיט ---
st.markdown("""
<hr>
<p style='text-align: center; color: gray; font-size: 13px;'>
פותח עבור צוות חינוכי • כל הזכויות שמורות © 2025
</p>
""", unsafe_allow_html=True)
# טוען את קובץ השאלות
try:
import math_quiz
except ModuleNotFoundError:
    st.error("קובץ השאלות לא נטען. ודא שקובץ math_quiz.py קיים בתיקייה הראשית.")

st.header("🧠 שאלון קביעת רמה במתמטיקה")

# מציג את השאלות מהקובץ
if hasattr(math_quiz, "questions"):
    for i, q in enumerate(math_quiz.questions, 1):
        st.markdown(f"**שאלה {i}:** {q['question']}")
        if q['type'] == 'multiple_choice':
            st.radio("בחר תשובה:", q['options'], key=f"q{i}")
        elif q['type'] == 'open':
            st.text_input("התשובה שלך:", key=f"q{i}")
else:
    st.warning("אין שאלות בקובץ. ודא שקובץ math_quiz.py בנוי נכון.")
import streamlit as st
from PIL import Image

def show_math_quiz_image():
    st.header("🧮 שאלון מתמטי לקביעת רמת התלמיד")

    try:
        image = Image.open("images/math_level_test.jpg")
        st.image(image, caption="פתרו את התרגילים וכתבו במחברת", use_column_width=True)
        
        with open("images/math_level_test.jpg", "rb") as file:
            btn = st.download_button(
                label="📥 הורד את שאלון התרגילים",
                data=file,
                file_name="שאלון_רמת_מתמטיקה.jpg",
                mime="image/jpeg"
            )
    except FileNotFoundError:
        st.error("התמונה לא נמצאה. ודא שהקובץ נמצא בתיקייה images עם השם הנכון.")

# קרא לפונקציה איפה שאתה רוצה שהשאלון יופיע
show_math_quiz_image()


