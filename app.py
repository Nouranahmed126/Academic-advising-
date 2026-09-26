import streamlit as st
from dataclasses import dataclass
from typing import Optional, List, Dict, Set

# ============================================================
# المرشد الأكاديمي الذكي — دفعة 2025/2026
# الواجهة الجديدة لا تغيّر محرك القواعد الأكاديمية.
# ============================================================

st.set_page_config(
    page_title="المرشد الأكاديمي الذكي",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# الهوية البصرية — RTL
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: "Cairo", sans-serif;
    direction: rtl;
}

.stApp {
    background:
        radial-gradient(circle at 90% 0%, rgba(29, 78, 216, .09), transparent 28%),
        radial-gradient(circle at 5% 35%, rgba(13, 148, 136, .07), transparent 25%),
        #f5f7fb;
}

/* إزالة المساحة البيضاء الكبيرة التي يتركها رأس Streamlit */
header[data-testid="stHeader"] {
    height: 0 !important;
    min-height: 0 !important;
    background: transparent !important;
}
header[data-testid="stHeader"] > div {
    height: 0 !important;
}
[data-testid="stAppViewContainer"] {
    margin-top: 0 !important;
}
[data-testid="stToolbar"] {
    display: none !important;
}
main[data-testid="stMain"] {
    padding-top: 0 !important;
}
section[data-testid="stMain"] {
    padding-top: 0 !important;
}
footer {
    visibility: hidden;
    height: 0 !important;
}

.block-container {
    max-width: 1240px;
    padding-top: 0.45rem !important;
    padding-bottom: 2.5rem;
}

/* ---------- Hero ---------- */
.hero {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #0f1f3d 0%, #173765 55%, #1f4f7a 100%);
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 28px;
    padding: 34px 38px 30px;
    margin-bottom: 22px;
    box-shadow: 0 18px 50px rgba(15, 31, 61, .16);
    color: white;
}

.hero:before {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    border-radius: 50%;
    left: -95px;
    top: -115px;
    background: rgba(203, 166, 76, .13);
}

.hero:after {
    content: "";
    position: absolute;
    width: 180px;
    height: 180px;
    border-radius: 50%;
    right: -70px;
    bottom: -90px;
    background: rgba(45, 212, 191, .10);
}

.hero-content { position: relative; z-index: 2; }

.hero-badge {
    display: inline-block;
    padding: 7px 13px;
    border: 1px solid rgba(255,255,255,.20);
    background: rgba(255,255,255,.08);
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 14px;
}

.hero-title {
    font-size: clamp(30px, 4vw, 48px);
    line-height: 1.25;
    font-weight: 800;
    margin: 0;
    letter-spacing: -.5px;
}

.hero-subtitle {
    color: #e6edf7;
    font-size: 17px;
    line-height: 1.9;
    margin: 10px 0 18px;
    max-width: 780px;
}

.hero-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.hero-meta span {
    padding: 7px 12px;
    border-radius: 10px;
    background: rgba(255,255,255,.08);
    color: #f4f7fb;
    font-size: 12px;
    font-weight: 600;
}

/* ---------- Intro / steps ---------- */
.intro-card {
    background: rgba(255,255,255,.94);
    border: 1px solid #e2e8f0;
    border-radius: 22px;
    padding: 22px 24px;
    margin: 0 0 18px;
    box-shadow: 0 8px 26px rgba(15,23,42,.05);
}

.intro-title { font-size: 19px; font-weight: 800; color: #14213d; }
.intro-text { color: #52627a; line-height: 1.95; font-size: 15px; margin-top: 6px; }

.steps {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin: 18px 0 28px;
}

.step-card {
    background: #fff;
    border: 1px solid #e3e8f0;
    border-radius: 16px;
    padding: 13px 15px;
    display: flex;
    align-items: center;
    gap: 10px;
    box-shadow: 0 5px 18px rgba(15,23,42,.035);
}

.step-no {
    width: 34px;
    height: 34px;
    border-radius: 10px;
    display: grid;
    place-items: center;
    background: #edf3ff;
    color: #1d4ed8;
    font-weight: 800;
    font-size: 12px;
    flex: 0 0 34px;
}

.step-text { color: #334155; font-weight: 700; font-size: 13px; }
.step-active { border-color: #b9cbed; background: linear-gradient(180deg,#fff,#f7faff); }

/* ---------- Sections ---------- */
.section-title {
    background: linear-gradient(135deg, #11213f, #1e3a62);
    color: white;
    padding: 14px 20px;
    border-radius: 17px;
    margin-top: 24px;
    margin-bottom: 16px;
    font-size: 20px;
    font-weight: 800;
    box-shadow: 0 7px 20px rgba(17,33,63,.10);
}

.subtle-note {
    color: #64748b;
    font-size: 13px;
    line-height: 1.9;
}

.info-card, .result-card {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 7px 24px rgba(15,23,42,.045);
}

.result-card { margin-top: 18px; }

.reason-box {
    background: #f8fbff;
    border-right: 4px solid #1d4ed8;
    padding: 17px 18px;
    border-radius: 14px;
    line-height: 2;
    color: #334155;
}

.warning-box, .danger-box, .success-box, .blue-box {
    padding: 16px 18px;
    border-radius: 14px;
    margin: 10px 0;
    line-height: 1.9;
}

.warning-box { background:#fff8ed; border-right:4px solid #d97706; color:#713f12; }
.danger-box { background:#fff5f5; border-right:4px solid #dc2626; color:#7f1d1d; }
.success-box { background:#f0fdf8; border-right:4px solid #059669; color:#065f46; }
.blue-box { background:#eff6ff; border-right:4px solid #2563eb; color:#1e3a8a; }

.metric-box {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 17px;
    padding: 16px 10px;
    text-align: center;
    box-shadow: 0 5px 18px rgba(15,23,42,.035);
}
.metric-number { font-size: 26px; font-weight: 800; color:#14213d; }
.metric-label { color:#64748b; font-size:12px; margin-top:2px; }

.threshold-card {
    background: linear-gradient(135deg,#f8fbff,#f2f7ff);
    border: 1px solid #d8e4f7;
    border-radius: 17px;
    padding: 15px 17px;
    margin-top: 12px;
}
.threshold-value { font-size: 25px; font-weight: 800; color:#1d4ed8; }
.threshold-label { color:#64748b; font-size:12px; }
.threshold-ok { color:#047857; font-weight:700; }
.threshold-low { color:#b45309; font-weight:700; }

.counter-card {
    background: linear-gradient(135deg,#f7fbff,#ffffff);
    border: 1px solid #dce7f5;
    border-radius: 17px;
    padding: 15px 18px;
    margin: 12px 0 4px;
    display:flex;
    align-items:center;
    justify-content:space-between;
}
.counter-number { font-size: 27px; font-weight: 800; color:#1d4ed8; }
.counter-label { color:#64748b; font-size:13px; }

.review-card {
    background: linear-gradient(135deg,#fbfcfe,#f5f8fc);
    border: 1px solid #dde5ef;
    border-radius: 20px;
    padding: 20px;
    margin-top: 18px;
}
.review-title { font-weight:800; color:#14213d; font-size:18px; margin-bottom:12px; }
.review-item { padding:8px 0; border-bottom:1px solid #e8edf3; color:#475569; }
.review-item:last-child { border-bottom:0; }
.review-item strong { color:#172033; }

.course-card {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 15px;
    padding: 14px 16px;
    margin: 8px 0;
    box-shadow: 0 3px 12px rgba(15,23,42,.025);
}
.course-name { font-weight:800; color:#172033; font-size:15px; }
.course-meta { color:#64748b; font-size:12px; margin-top:4px; line-height:1.8; }

.badge {
    display:inline-block;
    padding:5px 10px;
    border-radius:999px;
    font-size:11px;
    font-weight:700;
    margin-left:5px;
}
.badge-blue { background:#e8f0ff; color:#1d4ed8; }
.badge-green { background:#e8f8f1; color:#047857; }
.badge-amber { background:#fff4d8; color:#92400e; }
.badge-red { background:#feecec; color:#b91c1c; }

.stButton > button[kind="primary"] {
    min-height: 50px;
    border-radius: 15px;
    font-size: 16px;
    font-weight: 800;
    box-shadow: 0 8px 20px rgba(5,150,105,.18);
    background: #059669;
    border-color: #059669;
}

/* Streamlit inputs — Arabic RTL */
.stApp,
.stApp * {
    direction: rtl;
}

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] *,
.stMarkdown,
.stCaption,
.stAlert,
[data-testid="stRadio"] label,
[data-testid="stSelectbox"] label,
[data-testid="stMultiSelect"] label,
[data-testid="stTextInput"] label,
[data-testid="stNumberInput"] label {
    direction: rtl !important;
    text-align: right !important;
}

div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input,
div[data-testid="stSelectbox"] div[data-baseweb="select"],
div[data-testid="stMultiSelect"] div[data-baseweb="select"] {
    border-radius: 12px;
    direction: rtl !important;
    text-align: right !important;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div {
    direction: rtl !important;
    text-align: right !important;
}

.field-label {
    color: #172033;
    font-size: 15px;
    font-weight: 800;
    margin: 0 0 8px 0;
    text-align: right;
    direction: rtl;
}

/* عناوين الاختيارات تكون ظاهرة بجوار دوائر الاختيار */
div[data-testid="stRadio"] > label {
    display: block !important;
    color: #172033 !important;
    font-size: 15px !important;
    font-weight: 800 !important;
    margin-bottom: 10px !important;
    visibility: visible !important;
}
div[data-testid="stRadio"] [role="radiogroup"] label {
    color: #172033 !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    background: #ffffff;
    border: 1px solid #dfe7f1;
    border-radius: 14px;
    padding: 11px 14px;
    margin: 4px 0 !important;
}
div[data-testid="stRadio"] [role="radiogroup"] label p {
    color: #172033 !important;
    font-weight: 700 !important;
}

/* عناوين الـcheckbox والاختيارات لا تختفي */
div[data-testid="stCheckbox"] label,
div[data-testid="stCheckbox"] label p {
    color: #172033 !important;
    font-size: 14px !important;
    font-weight: 700 !important;
}

@media (max-width: 700px) {
    .hero { padding: 25px 20px; border-radius:22px; }
    .hero-title { font-size:31px; }
    .hero-subtitle { font-size:14px; }
    .steps { grid-template-columns: 1fr; }
    .block-container { padding-left: 1rem; padding-right: 1rem; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# بيانات المقررات
# ============================================================

@dataclass
class Course:
    code: str
    name: str
    hours: Optional[int]
    level: int
    category: str
    program: str = "مشترك"
    prerequisite: Optional[str] = None
    clearance: bool = False


COURSES: Dict[str, Course] = {}


def add_course(code, name, hours, level, category, program="مشترك", prerequisite=None, clearance=False):
    COURSES[code] = Course(
        code=code,
        name=name,
        hours=hours,
        level=level,
        category=category,
        program=program,
        prerequisite=prerequisite,
        clearance=clearance,
    )


# ============================================================
# المستوى الأول — عام
# ============================================================
add_course("UG1.1", "اللغة الإنجليزية", None, 1, "متطلبات الجامعة", program="مشترك", clearance=True)
add_course("EDU1.1", "مدخل إلى العلوم التربوية", 2, 1, "متطلبات الكلية", program="مشترك")
add_course("EDU1.2", "المناهج وتنظيماتها", 2, 1, "متطلبات الكلية", program="مشترك")
add_course("EM1.1", "نشأة وسائل الإعلام وتطورها", 2, 1, "إجباري تخصص", program="عام")
add_course("EM1.2", "مبادئ علم الصحافة", 2, 1, "إجباري تخصص", program="عام")
add_course("EM1.3", "الاتصال بالجماهير", 2, 1, "إجباري تخصص", program="عام")
add_course("EM1.4", "مبادئ علوم المسرح", 2, 1, "إجباري تخصص", program="عام")
add_course("EM1.5", "الإعلام والتنمية", 2, 1, "إجباري تخصص", program="عام")
add_course("EME1.1", "مبادئ الإعلام التربوي", 2, 1, "اختياري تخصص", program="عام")
add_course("EME1.2", "جماليات العرض المسرحي", 2, 1, "اختياري تخصص", program="عام")
add_course("EME1.3", "مفاهيم ومصطلحات إعلامية", 2, 1, "اختياري تخصص", program="عام")
add_course("EME1.4", "مبادئ الاقتصاد والسياسة", 2, 1, "اختياري تخصص", program="عام")
add_course("EDU1.3", "مدخل إلى العلوم النفسية", 2, 1, "متطلبات الكلية", program="مشترك")
add_course("EDU1.4", "طرق تدريس عامة", 2, 1, "متطلبات الكلية", program="مشترك")
add_course("EM1.6", "الخبر في وسائل الإعلام", 2, 1, "إجباري تخصص", program="عام")
add_course("EM1.7", "مبادئ الراديو والتليفزيون", 2, 1, "إجباري تخصص", program="عام")
add_course("EM1.8", "مبادئ العلاقات العامة", 1, 1, "إجباري تخصص", program="عام")
add_course("EM1.9", "أدب الطفل", 2, 1, "إجباري تخصص", program="عام")
add_course("EM1.10", "التربية الإعلامية", 2, 1, "إجباري تخصص", program="عام")
add_course("EME1.5", "الإعلام النفسي", 2, 1, "اختياري تخصص", program="عام")
add_course("EME1.6", "الإعلام وقضايا المجتمع", 2, 1, "اختياري تخصص", program="عام")
add_course("EME1.7", "التربية المسرحية", 2, 1, "اختياري تخصص", program="عام")
add_course("EME1.8", "الترجمة الإعلامية", 2, 1, "اختياري تخصص", program="عام")

# ============================================================
# المستوى الأول — خاص
# ============================================================
add_course("Sp1.1", "مدخل إلى التربية الخاصة", 1, 1, "تربية خاصة", program="خاص")
add_course("Sp1.2", "إعاقات بسيطة", 1, 1, "تربية خاصة", program="خاص")
add_course("EMS1.1", "نشأة وسائل الإعلام وتطورها", 2, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.2", "مبادئ علم الصحافة", 2, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.3", "الاتصال بالجماهير", 2, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.4", "مبادئ علوم المسرح", 2, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.5", "الإعلام والتنمية", 1, 1, "إجباري تخصص", program="خاص")
add_course("EMSE1.1", "مبادئ الإعلام التربوي", 1, 1, "اختياري تخصص", program="خاص")
add_course("EMSE1.2", "جماليات العرض المسرحي", 1, 1, "اختياري تخصص", program="خاص")
add_course("EMSE1.3", "مفاهيم ومصطلحات إعلامية", 1, 1, "اختياري تخصص", program="خاص")
add_course("EMSE1.4", "مبادئ الاقتصاد والسياسة", 1, 1, "اختياري تخصص", program="خاص")
add_course("Sp1.3", "التوعية بميدان الأطفال ذوي الاحتياجات الخاصة", 1, 1, "تربية خاصة", program="خاص")
add_course("Sp1.4", "القياس النفسي", 2, 1, "تربية خاصة", program="خاص")
add_course("EMS1.6", "الخبر في وسائل الإعلام", 2, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.7", "مبادئ الراديو والتليفزيون", 2, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.8", "مبادئ العلاقات العامة", 1, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.9", "أدب الطفل", 2, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.10", "التربية الإعلامية", 1, 1, "إجباري تخصص", program="خاص")
add_course("EMSE1.5", "الإعلام النفسي", 1, 1, "اختياري تخصص", program="خاص")
add_course("EMSE1.6", "الإعلام وقضايا المجتمع", 1, 1, "اختياري تخصص", program="خاص")
add_course("EMSE1.7", "التربية المسرحية", 1, 1, "اختياري تخصص", program="خاص")
add_course("EMSE1.8", "الترجمة الإعلامية", 1, 1, "اختياري تخصص", program="خاص")

# ============================================================
# المستوى الثاني — عام
# ============================================================
add_course("UG2.2", "اللغة العربية", None, 2, "متطلبات الجامعة", program="مشترك", clearance=True)
add_course("EDU2.5", "علم النفس للنمو", 2, 2, "متطلبات الكلية", program="مشترك")
add_course("EDU2.6", "تاريخ التربية ونظام التعليم في مصر", 2, 2, "متطلبات الكلية", program="مشترك", prerequisite="EDU1.1")
add_course("EDU2.7", "التدريس المصغر", 2, 2, "متطلبات الكلية", program="مشترك", prerequisite="EDU1.4")
add_course("EM2.11", "تكنولوجيا الاتصال والمعلومات", 2, 2, "إجباري تخصص", program="عام")
add_course("EM2.12", "المسرح المصري", 2, 2, "إجباري تخصص", program="عام", prerequisite="EM1.4")
add_course("EM2.13", "إعلام الطفل", 2, 2, "إجباري تخصص", program="عام")
add_course("EM2.14", "أنشطة الصحافة والإذاعة المدرسية", 2, 2, "إجباري تخصص", program="عام", prerequisite="EM1.2")
add_course("EM2.15", "أساسيات الحاسب الآلي", 2, 2, "إجباري تخصص", program="عام")
add_course("EME2.9", "التوثيق الإعلامي", 2, 2, "اختياري تخصص", program="عام")
add_course("EME2.10", "التلفزيون التعليمي", 2, 2, "اختياري تخصص", program="عام")
add_course("EME2.11", "الصحافة الاستقصائية", 2, 2, "اختياري تخصص", program="عام")
add_course("EME2.12", "مسرحة المناهج التعليمية", 2, 2, "اختياري تخصص", program="عام")
add_course("EDU2.8", "سيكولوجية ذوي الاحتياجات الخاصة", 2, 2, "متطلبات الكلية", program="مشترك")
add_course("EDU2.9", "علم نفس تعليمي (نظريات تعلم)", 2, 2, "متطلبات الكلية", program="مشترك", prerequisite="EDU1.3")
add_course("EM2.16", "الأصول العلمية للإعلان", 2, 2, "إجباري تخصص", program="عام")
add_course("EM2.17", "نظم سياسية وسياسات الإعلام", 2, 2, "إجباري تخصص", program="عام")
add_course("EM2.18", "الرأي العام وطرق قياسه", 2, 2, "إجباري تخصص", program="عام")
add_course("EM2.19", "تشريعات الإعلام وأخلاقياته", 2, 2, "إجباري تخصص", program="عام")
add_course("EM2.20", "مسرح الطفل", 3, 2, "إجباري تخصص", program="عام")
add_course("EME2.13", "صحافة المواطن", 1, 2, "اختياري تخصص", program="عام")
add_course("EME2.14", "تيارات فكرية وثقافية معاصرة", 1, 2, "اختياري تخصص", program="عام")
add_course("EME2.15", "الإحصاء والحاسب الآلي", 1, 2, "اختياري تخصص", program="عام", prerequisite="EM2.15")
add_course("EME2.16", "المذاهب المسرحية", 1, 2, "اختياري تخصص", program="عام")

# ============================================================
# المستوى الثاني — خاص
# ============================================================
# اللغة العربية في المستوى الثاني كودها UG2.2 في كلا المسارين، وهي مقرّر اجتياز مشترك.
add_course("EDU2.5", "علم النفس للنمو", 2, 2, "متطلبات الكلية", program="مشترك")
add_course("EDU2.6", "تاريخ التربية ونظام التعليم في مصر", 2, 2, "متطلبات الكلية", program="مشترك", prerequisite="EDU1.1")
add_course("EDU2.7", "التدريس المصغر (تخصص)", 2, 2, "متطلبات الكلية", program="مشترك", prerequisite="EDU1.4")
add_course("Sp2.5", "تقييم أطفال ذوي الاحتياجات الخاصة", 2, 2, "تربية خاصة", program="خاص")
add_course("Sp2.6", "مهارات تواصل ذوي الاحتياجات الخاصة", 2, 2, "تربية خاصة", program="خاص")
add_course("EMS2.11", "تكنولوجيا الاتصال والمعلومات", 1, 2, "إجباري تخصص", program="خاص")
add_course("EMS2.12", "المسرح المدرسي", 2, 2, "إجباري تخصص", program="خاص", prerequisite="EMS1.4")
add_course("EMS2.13", "إعلام الطفل", 2, 2, "إجباري تخصص", program="خاص")
add_course("EMS2.14", "أنشطة الصحافة والإذاعة المدرسية", 2, 2, "إجباري تخصص", program="خاص", prerequisite="EMS1.2")
add_course("EMS2.15", "أساسيات الحاسب الآلي", 2, 2, "إجباري تخصص", program="خاص")
add_course("EMSE2.9", "التوثيق الإعلامي", 1, 2, "اختياري تخصص", program="خاص")
add_course("EMSE2.10", "التلفزيون التعليمي", 1, 2, "اختياري تخصص", program="خاص")
add_course("EMSE2.11", "الصحافة الاستقصائية", 1, 2, "اختياري تخصص", program="خاص")
add_course("EMSE2.12", "مسرحة المناهج التعليمية", 1, 2, "اختياري تخصص", program="خاص")
add_course("EDU2.8", "سيكولوجية ذوي الاحتياجات الخاصة", 2, 2, "متطلبات الكلية", program="مشترك")
add_course("EDU2.9", "علم نفس تعليمي (نظريات تعلم)", 2, 2, "متطلبات الكلية", program="مشترك", prerequisite="EDU1.3")
add_course("Sp2.7", "الاضطرابات الانفعالية والسلوكية لأطفال ذوي الاحتياجات الخاصة", 2, 2, "تربية خاصة", program="خاص")
add_course("Sp2.8", "التربية الترويحية لذوي الاحتياجات الخاصة", 2, 2, "تربية خاصة", program="خاص")
add_course("EMS2.16", "الأصول العلمية للإعلان", 2, 2, "إجباري تخصص", program="خاص")
add_course("EMS2.17", "نظم سياسية وسياسات الإعلام", 2, 2, "إجباري تخصص", program="خاص")
add_course("EMS2.18", "الرأي العام وطرق قياسه", 2, 2, "إجباري تخصص", program="خاص")
add_course("EMS2.19", "تشريعات الإعلام وأخلاقياته", 2, 2, "إجباري تخصص", program="خاص")
add_course("EMS2.20", "مسرح الطفل", 2, 2, "إجباري تخصص", program="خاص")
add_course("EMSE2.13", "صحافة المواطن", 1, 2, "اختياري تخصص", program="خاص")
add_course("EMSE2.14", "تيارات فكرية وثقافية معاصرة", 1, 2, "اختياري تخصص", program="خاص")
add_course("EMSE2.15", "الإحصاء والحاسب الآلي", 1, 2, "اختياري تخصص", program="خاص", prerequisite="EMS2.15")
add_course("EMSE2.16", "المذاهب المسرحية", 1, 2, "اختياري تخصص", program="خاص")

# ============================================================
# قواعد النظام — كما هي داخليًا
# ============================================================
LEVEL_2_THRESHOLD = {"عام": 35, "خاص": 32}
TWELVE_HOUR_LIMIT = 12

# مقررات المستوى الثاني للفصل الدراسي الأول كما هي معرفة في قاعدة المقررات.
# لا نخلط بينها وبين مقررات الفصل الدراسي الثاني.
FIRST_TERM_PLAN = {
    "عام": {
        "required": [
            "UG2.2", "EDU2.5", "EDU2.6", "EDU2.7",
            "EM2.11", "EM2.12", "EM2.13", "EM2.14", "EM2.15",
        ],
        "electives": ["EME2.9", "EME2.10", "EME2.11", "EME2.12"],
        "elective_count": 2,
    },
    "خاص": {
        "required": [
            "UG2.2", "EDU2.5", "EDU2.6", "EDU2.7",
            "Sp2.5", "Sp2.6",
            "EMS2.11", "EMS2.12", "EMS2.13", "EMS2.14", "EMS2.15",
        ],
        "electives": ["EMSE2.9", "EMSE2.10", "EMSE2.11", "EMSE2.12"],
        "elective_count": 1,
    },
}

# مقررات المتطلب الخمسة المذكورة صراحةً في الاجتماع للحالة الثامنة.
CASE8_PREREQUISITES = {
    "عام": {"EDU1.1", "EDU1.2", "EM1.2", "EM1.4", "EDU1.4"},
    "خاص": {"EDU1.1", "EDU1.2", "EMS1.2", "EMS1.4", "EDU1.4"},
}

def _available_by_prerequisite(codes, failed_courses):
    return [c for c in codes if c in COURSES and c not in failed_courses and not (COURSES[c].prerequisite and COURSES[c].prerequisite in failed_courses)]

def build_first_term_plan(program: str, failed_courses: Set[str]):
    spec = FIRST_TERM_PLAN[program]
    required = list(spec["required"])
    available_required = _available_by_prerequisite(required, failed_courses)
    elective_available = _available_by_prerequisite(spec["electives"], failed_courses)
    selected_electives = elective_available[:spec["elective_count"]]
    selected = available_required + selected_electives
    blocked = [c for c in required + spec["electives"] if c in COURSES and COURSES[c].prerequisite and COURSES[c].prerequisite in failed_courses]
    failed_required = [c for c in required if c in failed_courses]
    return selected, blocked, failed_required, selected_electives

def verify_first_term_level2(program: str, passed_hours: int, failed_courses: Set[str]):
    threshold = LEVEL_2_THRESHOLD[program]
    spec = FIRST_TERM_PLAN[program]
    selected, blocked, failed_required, selected_electives = build_first_term_plan(program, failed_courses)
    official_required = [c for c in spec["required"] if c in COURSES]
    official_electives = [c for c in spec["electives"] if c in COURSES]
    expected_hours = calculate_regular_hours(official_required) + sum((COURSES[c].hours or 0) for c in official_electives[:spec["elective_count"]])
    available_hours = calculate_regular_hours(selected)
    clearance = [c for c in selected if COURSES[c].clearance]
    eligible = passed_hours >= threshold
    complete_plan = not failed_required and len(selected_electives) == spec["elective_count"] and all(c not in blocked for c in official_required)
    exact = eligible and complete_plan and available_hours == expected_hours
    return {
        "threshold": threshold, "expected": official_required + official_electives[:spec["elective_count"]],
        "expected_hours": expected_hours, "available": selected, "available_hours": available_hours,
        "blocked": blocked, "failed_required": failed_required, "elective_options": official_electives,
        "selected_electives": selected_electives, "clearance": clearance, "eligible": eligible, "exact": exact,
    }


def normalize_gpa(gpa):
    try:
        return float(gpa)
    except Exception:
        return 0.0


def course_name(code):
    return COURSES[code].name if code in COURSES else code


def course_hours(code):
    return COURSES[code].hours if code in COURSES else None


def course_belongs_to_program(course: Course, program: str):
    return course.program == "مشترك" or course.program == program


def get_course_list(program: str, level: Optional[int] = None):
    result = []
    for code, course in COURSES.items():
        if not course_belongs_to_program(course, program):
            continue
        if level is not None and course.level != level:
            continue
        result.append(code)
    return result


def get_clearance_courses(failed_courses: Set[str], program: str):
    return [
        code for code in failed_courses
        if code in COURSES
        and COURSES[code].clearance
        and course_belongs_to_program(COURSES[code], program)
    ]


def get_level2_courses(program: str):
    return [
        code for code, course in COURSES.items()
        if course.level == 2 and course_belongs_to_program(course, program)
    ]


def get_failed_prerequisites(failed_courses: Set[str], program: str):
    prerequisites = set()
    for code, course in COURSES.items():
        if not course_belongs_to_program(course, program):
            continue
        if course.prerequisite:
            prerequisites.add(course.prerequisite)
    return failed_courses.intersection(prerequisites)


def has_failed_prerequisite(failed_courses: Set[str], program: str):
    return bool(get_failed_prerequisites(failed_courses, program))


def get_blocked_level2_courses(failed_courses: Set[str], program: str):
    blocked = []
    for code in get_level2_courses(program):
        prerequisite = COURSES[code].prerequisite
        if prerequisite and prerequisite in failed_courses:
            blocked.append(code)
    return blocked


def get_available_level2_courses(failed_courses: Set[str], program: str):
    available = []
    for code in get_level2_courses(program):
        prerequisite = COURSES[code].prerequisite
        if prerequisite and prerequisite in failed_courses:
            continue
        available.append(code)
    return available


def get_replacement_courses(failed_courses: Set[str], program: str):
    replacements = []
    for code in failed_courses:
        if code not in COURSES:
            continue
        course = COURSES[code]
        if course.level != 1 or not course_belongs_to_program(course, program):
            continue
        if course.clearance or course.hours is None:
            continue
        replacements.append(code)
    return replacements


def calculate_regular_hours(course_codes: List[str]):
    total = 0
    for code in course_codes:
        if code not in COURSES:
            continue
        course = COURSES[code]
        if not course.clearance and course.hours is not None:
            total += course.hours
    return total


def calculate_failed_credit_hours(course_codes: List[str]):
    """إجمالي الساعات الفعلية للمقررات غير المجتازة؛ مقررات الاجتياز = صفر."""
    return calculate_regular_hours(course_codes)


def calculate_clearance_hours(course_codes: List[str]):
    total = 0
    for code in course_codes:
        if code not in COURSES:
            continue
        course = COURSES[code]
        if course.clearance and course.hours is not None:
            total += course.hours
    return total


def determine_case_6(failed_courses: Set[str], gpa: float, all_first_semester_passed: bool, program: str):
    teaching_failed = "EDU1.4" in failed_courses
    curriculum_failed = "EDU1.2" in failed_courses

    program_prerequisites = {
        code for code in [
            "EDU1.1",
            "EM1.2" if program == "عام" else "EMS1.2",
            "EM1.4" if program == "عام" else "EMS1.4",
        ] if code in COURSES
    }

    first_level_prereq_failed = bool(failed_courses.intersection(program_prerequisites))

    if not teaching_failed:
        return None

    if gpa >= 1.6 and all_first_semester_passed and failed_courses == {"EDU1.4"}:
        return "6A"

    if gpa >= 1.6 and first_level_prereq_failed and not curriculum_failed:
        return "6B"

    if gpa >= 1.6:
        return "6C"

    return None


# ============================================================
# محرك الحالات — لا يظهر رقم الحالة للطالب
# ============================================================

def analyze_student(data):
    gpa = normalize_gpa(data["gpa"])
    program = data["program"]
    failed_courses = set(data["failed_courses"])
    all_first_semester_passed = data["all_first_semester_passed"]
    passed_hours = data["passed_hours"]

    result = {
        "case": None,
        "subcase": None,
        "title": "",
        "reason": "",
        "available": [],
        "blocked": [],
        "replacement": [],
        "warnings": [],
        "summer": [],
        "clearance": [],
        "regular_limit": None,
        "regular_hours": 0,
        "clearance_hours": 0,
        "notes": [],
        "first_term_check": None,
    }

    result["clearance"] = get_clearance_courses(failed_courses, program)
    result["clearance_hours"] = calculate_clearance_hours(result["clearance"])

    threshold = LEVEL_2_THRESHOLD[program]
    failed_hours = calculate_failed_credit_hours(list(failed_courses))
    remaining_to_threshold = max(threshold - passed_hours, 0)
    transition_conflict = passed_hours < threshold and failed_hours > remaining_to_threshold
    result["transition_conflict"] = transition_conflict
    result["passed_hours_remaining"] = remaining_to_threshold
    result["failed_credit_hours"] = failed_hours
    result["first_term_check"] = verify_first_term_level2(program, passed_hours, failed_courses)
    if transition_conflict:
        result["warnings"].append(
            f"لا يمكن اعتماد هذه البيانات للانتقال: لديك {passed_hours} ساعة نجاح، والمتبقي للوصول إلى حد {threshold} ساعة هو {remaining_to_threshold} ساعة فقط، بينما إجمالي ساعات المقررات غير المجتازة المختارة {failed_hours} ساعة. لا تُستخدم ساعات المقرر غير المجتاز لتجاوز حد الانتقال."
        )
    if passed_hours < threshold:
        result["notes"].append(
            f"عدد ساعات النجاح المدخل هو {passed_hours} ساعة، بينما الحد المذكور للانتقال للمستوى الثاني في برنامج «{program}» هو {threshold} ساعة."
        )

    # الحالة 1
    if len(failed_courses) == 0 and gpa >= 2.0:
        result["case"] = 1
        result["title"] = "الحالة الأولى"
        result["reason"] = "أنت ناجح في جميع المقررات، والتقدير التراكمي يساوي 2.00 أو أكثر."
        result["available"] = get_available_level2_courses(failed_courses, program)
        result["notes"].append("سجّل مقررات المستوى الثاني وفق خطة الفصل المتاحة، مع الحفاظ على تقدير تراكمي 2.00 فأعلى لتجنب الإنذار أو الفصل.")
        return result

    # الحالة 3
    if len(failed_courses) == 0 and 1.6 <= gpa < 2.0:
        result["case"] = 3
        result["title"] = "الحالة الثالثة"
        result["reason"] = "أنت ناجح في جميع المقررات، لكن التقدير التراكمي بين 1.60 وأقل من 2.00."
        result["available"] = get_available_level2_courses(failed_courses, program)
        result["warnings"].append("يجب العمل على رفع التقدير التراكمي إلى 2.00 وتجنب استمرار انخفاضه.")
        result["notes"].append("سجّل مقررات المستوى الثاني المتاحة، ويفضّل وضع المقررات الراسب فيها ضمن خطة الصيف إذا أمكن.")
        return result

    # الحالة 8
    case8_prerequisites = CASE8_PREREQUISITES[program]

    if gpa < 1.6 and case8_prerequisites.issubset(failed_courses):
        result["case"] = 8
        result["title"] = "الحالة الثامنة"
        result["reason"] = "التقدير التراكمي أقل من 1.60، ومقررات المتطلبات المحددة لهذه الحالة كلها ضمن المقررات الراسب فيها."
        result["regular_limit"] = TWELVE_HOUR_LIMIT
        result["blocked"] = get_blocked_level2_courses(failed_courses, program)
        result["available"] = get_available_level2_courses(failed_courses, program)
        result["replacement"] = get_replacement_courses(failed_courses, program)
        result["summer"] = sorted(case8_prerequisites)
        if "EDU2.7" not in result["blocked"]:
            result["blocked"].append("EDU2.7")
        if "EDU2.7" in result["available"]:
            result["available"].remove("EDU2.7")
        result["warnings"].append("حد التسجيل الأساسي في هذه الحالة هو 12 ساعة.")
        result["warnings"].append("الأولوية هي العمل على رفع التقدير التراكمي وتجنب استمرار انخفاضه.")
        result["notes"].append("في هذه الحالة تُسجَّل 12 ساعة فقط، مع أولوية علم النفس للنمو وأساسيات الحاسب الآلي ثم ما يلائم القدرة على الدراسة.")
        result["notes"].append("مبادئ علوم المسرح تُعاد الآن، وتُترك بقية مقررات المتطلب الخمسة لخطة الصيف بإجمالي 8 ساعات.")
        result["notes"].append("مقررات الاجتياز مثل العربية والإنجليزية لا تُحتسب كساعات تسجيل أساسية.")
        return result

    # الحالة 7
    if gpa < 1.6 and len(failed_courses) > 0:
        result["case"] = 7
        result["title"] = "الحالة السابعة"
        result["reason"] = "التقدير التراكمي أقل من 1.60 مع وجود مقررات راسب فيها، لكن شروط الحالة الأكثر تقييدًا لا تنطبق على البيانات المدخلة."
        result["regular_limit"] = TWELVE_HOUR_LIMIT
        result["available"] = get_available_level2_courses(failed_courses, program)
        result["blocked"] = get_blocked_level2_courses(failed_courses, program)
        result["replacement"] = get_replacement_courses(failed_courses, program)
        result["summer"] = list(failed_courses)
        result["warnings"].append("حد التسجيل الأساسي في هذه الحالة هو 12 ساعة.")
        result["warnings"].append("الأولوية هي رفع التقدير التراكمي وتجنب استمرار انخفاضه.")
        priority_courses = ["EDU2.5", "EMS2.15" if program == "خاص" else "EM2.15"]
        result["available"] = sorted(result["available"], key=lambda x: (0 if x in priority_courses else 1, x))
        result["notes"].append("الأولوية في خطة التسجيل لعلم النفس للنمو وأساسيات الحاسب الآلي، ثم باقي المقررات الأكثر ملاءمة لإمكانية الدراسة.")
        return result

    # الحالة 6
    if "EDU1.4" in failed_courses:
        subcase = determine_case_6(failed_courses, gpa, all_first_semester_passed, program)
        if subcase is not None:
            result["case"] = 6
            result["subcase"] = subcase
            result["title"] = f"الحالة السادسة — {subcase}"

            if subcase == "6A":
                result["reason"] = "أنت ناجح في جميع مقررات الفصل الدراسي الأول، ولديك رسوب في طرق تدريس عامة فقط، والتقدير التراكمي 1.60 فأكثر."
                result["available"] = [c for c in get_available_level2_courses(failed_courses, program) if c != "EDU2.7"]
                result["blocked"] = ["EDU2.7"]
                result["warnings"].append("التدريس المصغر لا يتم تسجيله حاليًا لأن طرق تدريس عامة لم تُجتز.")
                result["notes"].append("قد يكون عدد الساعات المسجلة أقل من زملائك بسبب طبيعة هذا الموقف الدراسي.")
                result["summer"].append("EDU2.7")

            elif subcase == "6B":
                result["reason"] = "لديك رسوب في طرق تدريس عامة بالإضافة إلى مقرر أو مقررات من مقررات المستوى الأول ذات أثر مباشر على مقررات المستوى الثاني."
                result["blocked"] = get_blocked_level2_courses(failed_courses, program)
                if "EDU2.7" not in result["blocked"]:
                    result["blocked"].append("EDU2.7")
                result["available"] = [c for c in get_available_level2_courses(failed_courses, program) if c != "EDU2.7"]
                result["replacement"] = get_replacement_courses(failed_courses, program)
                result["summer"] = list(failed_courses)
                if "EDU2.7" not in result["summer"]:
                    result["summer"].append("EDU2.7")

            else:
                result["reason"] = "لديك رسوب في طرق تدريس عامة مع المناهج وتنظيماتها أو مع مقررات أخرى من المستوى الأول، ولذلك تختلف خطة التسجيل."
                result["blocked"] = get_blocked_level2_courses(failed_courses, program)
                if "EDU2.7" not in result["blocked"]:
                    result["blocked"].append("EDU2.7")
                result["available"] = [c for c in get_available_level2_courses(failed_courses, program) if c != "EDU2.7"]
                result["replacement"] = get_replacement_courses(failed_courses, program)
                result["summer"] = list(failed_courses)
                if "EDU2.7" not in result["summer"]:
                    result["summer"].append("EDU2.7")
                result["notes"].append("المناهج وتنظيماتها لها دور في تحديد البديل عند ارتباطها بهذه الحالة.")

            if gpa >= 2.0:
                result["notes"].append("الأولوية هي الحفاظ على التقدير التراكمي 2.00 فأعلى وتجنب النزول عنه.")
            else:
                result["warnings"].append("الأولوية هي رفع التقدير التراكمي والوصول إلى 2.00.")
            return result

    # الحالة 2
    if len(failed_courses) > 0 and has_failed_prerequisite(failed_courses, program) and gpa >= 2.0:
        result["case"] = 2
        result["title"] = "الحالة الثانية"
        failed_prereqs = get_failed_prerequisites(failed_courses, program)
        prereq_names = "، ".join(course_name(code) for code in failed_prereqs)
        result["reason"] = (
            "لديك مقررات راسب فيها، ومن بينها مواد متطلبات غير مجتازة "
            f"({prereq_names}) تؤثر على فتح مقررات أخرى، بينما التقدير التراكمي 2.00 أو أكثر."
        )
        result["blocked"] = get_blocked_level2_courses(failed_courses, program)
        result["available"] = get_available_level2_courses(failed_courses, program)
        result["replacement"] = get_replacement_courses(failed_courses, program)
        result["summer"] = list(failed_courses)
        result["notes"].append("سجّل مقررات المستوى الثاني المتاحة، واستبدل المقرر الذي يمنعه المتطلب بمقرر المتطلب من المستوى الأول، ويمكن وضع المقررات الراسب فيها ضمن خطة الصيف عند توافرها.")
        return result

    # الحالة 4
    if len(failed_courses) > 0 and not has_failed_prerequisite(failed_courses, program) and gpa >= 1.6:
        result["case"] = 4
        result["title"] = "الحالة الرابعة"
        result["reason"] = "لديك مقررات راسب فيها، لكن هذه المقررات ليست من المتطلبات التي تمنع فتح مقررات المستوى الثاني وفق علاقات المتطلبات المدخلة."
        result["available"] = get_available_level2_courses(failed_courses, program)
        result["summer"] = list(failed_courses)
        result["warnings"].append("يجب العمل على رفع التقدير التراكمي إلى 2.00 والمحافظة عليه.")
        result["notes"].append("سجّل مقررات المستوى الثاني المتاحة، وسجّل المقررات الراسب فيها في الفصل الصيفي عند توافرها.")
        return result

    # الحالة 5
    if len(failed_courses) > 0 and has_failed_prerequisite(failed_courses, program) and 1.6 <= gpa < 2.0:
        result["case"] = 5
        result["title"] = "الحالة الخامسة"
        failed_prereqs = get_failed_prerequisites(failed_courses, program)
        prereq_names = "، ".join(course_name(code) for code in failed_prereqs)
        result["reason"] = (
            "لديك مقررات راسب فيها، ومن بينها مواد متطلبات غير مجتازة "
            f"({prereq_names})، والتقدير التراكمي بين 1.60 وأقل من 2.00."
        )
        result["blocked"] = get_blocked_level2_courses(failed_courses, program)
        result["available"] = get_available_level2_courses(failed_courses, program)
        result["replacement"] = get_replacement_courses(failed_courses, program)
        result["summer"] = list(failed_courses)
        result["warnings"].append("هذه الحالة تحتاج إلى رفع التقدير التراكمي وتجنب استمرار انخفاضه.")
        result["notes"].append("سجّل مقررات المستوى الثاني غير المتأثرة بالمتطلبات، واستبدل المقررات المغلقة بمقررات المتطلب من المستوى الأول، مع وضع المقررات الراسب فيها في خطة الصيف عند توافرها.")
        return result

    result["title"] = "البيانات تحتاج إلى مراجعة"
    result["reason"] = "البيانات التي تم إدخالها لا تكفي لتحديد موقف دراسي مؤكد وفق القواعد المدخلة."
    result["warnings"].append("لا تختار موقفًا دراسيًا بنفسك ولا نعتمد على التخمين.")
    result["notes"].append("راجع البيانات المدخلة، وإذا كان الموقف غير موجود ضمن القواعد الحالية، يجب الرجوع إلى المرشد الأكاديمي.")
    return result


# ============================================================
# عرض المقررات — الاسم + الكود + الساعات
# ============================================================
def display_course_list(title: str, course_codes: List[str], style: str = "normal", failed_courses: Optional[Set[str]] = None):
    if not course_codes:
        st.info("لا توجد مقررات في هذه القائمة وفق البيانات المدخلة.")
        return

    st.markdown(f"#### {title}")
    failed_courses = failed_courses or set()

    for code in course_codes:
        if code not in COURSES:
            continue
        course = COURSES[code]

        if course.hours is None:
            hours_text = "اجتياز — لا تُحسب كساعات تسجيل"
        else:
            hours_text = f"{course.hours} ساعة"

        if style == "blocked":
            badge = "<span class='badge badge-red'>غير متاح حاليًا</span>"
            if course.prerequisite:
                prerequisite_text = course_name(course.prerequisite)
                if course.prerequisite in failed_courses:
                    extra = f"المتطلب السابق: {prerequisite_text} غير مجتاز"
                else:
                    extra = f"مرتبط بمتطلب سابق: {prerequisite_text}"
            else:
                extra = "مرتبط بقواعد الموقف الدراسي"
        elif style == "replacement":
            badge = "<span class='badge badge-amber'>خطة معالجة</span>"
            extra = "مقرر من المستوى الأول يمكن إدخاله ضمن خطة المعالجة وفق القواعد"
        elif style == "summer":
            badge = "<span class='badge badge-blue'>الصيف</span>"
            extra = "مقرر مقترح ضمن خطة الترم الصيفي"
        elif style == "clearance":
            badge = "<span class='badge badge-green'>اجتياز</span>"
            extra = "مقرر اجتياز منفصل ولا يُحتسب ضمن الساعات الأساسية"
        else:
            badge = "<span class='badge badge-blue'>مقرر متاح</span>"
            extra = course.category
            if course.prerequisite:
                extra += f" — المتطلب السابق: {course_name(course.prerequisite)}"

        st.markdown(
            f"""
            <div class="course-card">
                <div class="course-name">{badge} {course.name} <span class='course-code'>— {course.code}</span></div>
                <div class="course-meta">{hours_text} &nbsp; • &nbsp; {extra}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# CSS إضافي لتجربة الصفحات المنفصلة
# ============================================================
st.markdown("""
<style>
/* ---------- الهوية العلوية والواجهة الافتتاحية ---------- */
.app-topbar { display:flex; align-items:center; justify-content:space-between; gap:16px; background:rgba(255,255,255,.94); border:1px solid #e2e8f0; border-radius:14px; padding:9px 15px; margin:0 0 16px; box-shadow:0 4px 16px rgba(15,23,42,.035); }
.app-topbar-name { color:#14213d !important; font-size:14px; font-weight:800; }
.app-topbar-meta { color:#64748b !important; font-size:11px; font-weight:600; }
.cover-page { position:relative; overflow:hidden; min-height:610px; display:flex; align-items:center; justify-content:center; text-align:center; border-radius:30px; background:linear-gradient(135deg,#0b1730 0%,#102a50 52%,#174c72 100%); border:1px solid rgba(255,255,255,.10); box-shadow:0 24px 70px rgba(15,31,61,.20); padding:46px 24px 52px; }
.cover-inner { position:relative; z-index:2; width:min(900px,100%); }
.cover-illustration { width:min(410px,72vw); height:auto; margin:0 auto 18px; display:block; filter:drop-shadow(0 18px 35px rgba(0,0,0,.20)); }
.cover-kicker { color:#e6d3a3 !important; font-size:13px; font-weight:700; }
.cover-title { color:#f7f8fb !important; font-size:clamp(34px,5vw,58px); font-weight:800; line-height:1.25; margin-top:7px; }
.cover-subtitle { color:#dce6f4 !important; font-size:17px; line-height:1.9; margin-top:7px; }
.cover-line { width:76px; height:3px; border-radius:999px; background:#e6d3a3; margin:20px auto 16px; }
.cover-tagline { color:#eef4fb !important; font-size:14px; line-height:2; }
.cover-orbit { position:absolute; border-radius:50%; pointer-events:none; }
.cover-orbit-one { width:390px; height:390px; left:-150px; top:-175px; border:1px solid rgba(230,211,163,.15); }
.cover-orbit-two { width:300px; height:300px; right:-115px; bottom:-145px; border:1px solid rgba(45,212,191,.14); }
.cover-action { max-width:430px; margin:14px auto 0; }
.cover-action button { min-height:54px !important; font-size:16px !important; }
.section-title { color:#ffffff !important; font-weight:800 !important; }
.field-label, .counter-label, .page-title, .page-kicker { color:#14213d !important; }
.page-kicker { color:#64748b !important; }
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 { color:#14213d !important; }

.page-shell {
    background: transparent !important;
    border: 0 !important;
    border-radius: 0 !important;
    padding: 4px 0 0 !important;
    margin: 0 !important;
    box-shadow: none !important;
    min-height: 0 !important;
    height: auto !important;
    overflow: visible !important;
}
.page-kicker { color:#64748b; font-size:12px; font-weight:700; margin-bottom:7px; }
.page-title { color:#14213d; font-size:30px; font-weight:800; line-height:1.45; margin:0; }
.page-description { color:#64748b; font-size:14px; line-height:2; margin:7px 0 20px; }
.progress-wrap { display:flex; gap:7px; margin:0 0 22px; }
.progress-dot { height:6px; flex:1; border-radius:999px; background:#e5e7eb; }
.progress-dot.active { background:#0f2f57; }
.progress-dot.done { background:#0f9f76; }
.nav-label { text-align:center; color:#94a3b8; font-size:11px; margin-top:8px; }
.welcome-logo { width:104px; height:104px; border-radius:30px; margin:0 auto 18px; display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg,#0f1f3d,#1f4f7a); color:#d8b56a; font-size:52px; box-shadow:0 14px 30px rgba(15,31,61,.18); border:1px solid rgba(216,181,106,.35); }
.center-page { text-align:center; }
.center-page .page-description { max-width:720px; margin:8px auto 22px; }
.name-page { max-width:720px; margin:24px auto 0; }
.name-page-title { color:#14213d !important; font-size:26px; font-weight:800; text-align:right; margin:0 0 10px; }
.name-page input { min-height:52px !important; font-size:16px !important; }
.name-nav { margin-top:14px; padding-top:0; border-top:0; }
.required-note { background:#f8fafc; border:1px solid #e2e8f0; border-radius:15px; padding:13px 15px; color:#475569; font-size:12px; line-height:1.9; margin-top:10px; }
.knowledge-card { background:linear-gradient(135deg,#fbfcfe,#f5f8fc); border:1px solid #e1e8f0; border-radius:18px; padding:16px; margin:9px 0; }
.knowledge-title { color:#14213d; font-size:15px; font-weight:800; margin-bottom:5px; }
.knowledge-text { color:#64748b; font-size:13px; line-height:1.9; }
.infer-card { background:#f0fdf8; border:1px solid #bfe9d9; border-right:4px solid #059669; border-radius:16px; padding:15px 17px; margin-top:13px; }
.infer-title { color:#065f46; font-weight:800; }
.infer-text { color:#475569; font-size:13px; line-height:1.9; margin-top:5px; }
.review-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:10px; }
.review-mini { background:#f8fafc; border:1px solid #e2e8f0; border-radius:15px; padding:13px 15px; }
.review-mini-label { color:#64748b; font-size:11px; }
.review-mini-value { color:#14213d; font-size:16px; font-weight:800; margin-top:3px; }
.course-code { color:#1d4ed8; font-size:12px; font-weight:800; }
.page-nav { margin-top:25px; padding-top:18px; border-top:1px solid #edf1f5; }
.back-note { color:#94a3b8; font-size:11px; text-align:center; margin-top:7px; }

.info-card, .info-card * { color:#172033 !important; }
.course-card { color:#172033; }
.course-card .course-name { color:#172033 !important; }
.course-card .course-meta { color:#64748b !important; }
.course-card .badge-blue { color:#1d4ed8 !important; }
.course-card .badge-green { color:#047857 !important; }
.course-card .badge-amber { color:#92400e !important; }
.course-card .badge-red { color:#b91c1c !important; }
.page-title, .page-kicker, .field-label, .counter-label, .knowledge-title, .review-title { color:#14213d !important; }
.section-title { color:#ffffff !important; }

@media (max-width:700px) {
 .page-shell { padding:4px 0 0 !important; border-radius:0; min-height:0 !important; height:auto !important; }
 .page-title { font-size:25px; }
 .review-grid { grid-template-columns:1fr; }
 .welcome-logo { display:none; }
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# الحالة والتنقل بين الصفحات
# ============================================================
if "wizard_page" not in st.session_state:
    st.session_state["wizard_page"] = 1
if "student_name" not in st.session_state:
    st.session_state["student_name"] = ""
if "gpa_input" not in st.session_state:
    st.session_state["gpa_input"] = None
if "passed_hours_input" not in st.session_state:
    st.session_state["passed_hours_input"] = None
if "program_input" not in st.session_state:
    st.session_state["program_input"] = None
if "failed_courses_input" not in st.session_state:
    st.session_state["failed_courses_input"] = []
if "no_failed_courses_confirmed" not in st.session_state:
    st.session_state["no_failed_courses_confirmed"] = False

page = st.session_state["wizard_page"]

st.markdown("<div class='app-topbar'><div class='app-topbar-name'>المرشد الأكاديمي الذكي</div><div class='app-topbar-meta'>نظام الساعات المعتمدة • قسم الإعلام التربوي • 2025/2026</div></div>", unsafe_allow_html=True)

# الصفحة 1 — واجهة افتتاحية
if page == 1:
    compass_svg = """
    <svg class='cover-illustration' viewBox='0 0 520 360' xmlns='http://www.w3.org/2000/svg' aria-label='بوصلة أكاديمية وخريطة طريق'>
      <defs>
        <linearGradient id='g1' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#e6d3a3'/><stop offset='1' stop-color='#8ee5d7'/></linearGradient>
        <linearGradient id='g2' x1='0' y1='1' x2='1' y2='0'><stop offset='0' stop-color='#ffffff'/><stop offset='1' stop-color='#9fc8e8'/></linearGradient>
      </defs>
      <circle cx='260' cy='170' r='122' fill='rgba(255,255,255,.045)' stroke='rgba(230,211,163,.38)' stroke-width='2'/>
      <circle cx='260' cy='170' r='91' fill='rgba(15,31,61,.35)' stroke='rgba(255,255,255,.18)'/>
      <path d='M260 62 L282 164 L260 278 L238 164 Z' fill='url(#g1)' opacity='.95'/>
      <path d='M190 170 L260 148 L330 170 L260 192 Z' fill='url(#g2)' opacity='.92'/>
      <circle cx='260' cy='170' r='15' fill='#0f1f3d' stroke='#e6d3a3' stroke-width='4'/>
      <path d='M68 276 C128 242 158 300 214 270 S316 222 364 258 S438 274 468 232' fill='none' stroke='#2dd4bf' stroke-width='6' stroke-linecap='round'/>
      <circle cx='68' cy='276' r='9' fill='#e6d3a3'/><circle cx='214' cy='270' r='9' fill='#e6d3a3'/><circle cx='364' cy='258' r='9' fill='#e6d3a3'/><circle cx='468' cy='232' r='11' fill='#2dd4bf'/>
      <path d='M382 76 l44 0 0 58 -44 0z' fill='rgba(255,255,255,.08)' stroke='rgba(255,255,255,.28)' rx='10'/>
      <path d='M392 94 h24 M392 107 h31 M392 120 h18' stroke='#dce6f4' stroke-width='5' stroke-linecap='round'/>
      <path d='M108 82 h54 v38 h-54z' fill='rgba(255,255,255,.07)' stroke='rgba(230,211,163,.3)' rx='8'/>
      <path d='M121 101 l12 -10 11 8 12 -13' fill='none' stroke='#2dd4bf' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'/>
    </svg>
    """
    st.markdown(f"<div class='cover-page'><div class='cover-orbit cover-orbit-one'></div><div class='cover-orbit cover-orbit-two'></div><div class='cover-inner'>{compass_svg}<div class='cover-kicker'>نظام الساعات المعتمدة</div><div class='cover-title'>المرشد الأكاديمي الذكي</div><div class='cover-subtitle'>قسم الإعلام التربوي — دفعة 2025/2026</div><div class='cover-line'></div><div class='cover-tagline'>افهم موقفك الدراسي • اعرف المقررات المتاحة • خطط لتسجيلك بثقة</div></div></div>", unsafe_allow_html=True)
    st.markdown("<div class='cover-action'>", unsafe_allow_html=True)
    if st.button("ابدأ الآن →", type="primary", use_container_width=True):
        st.session_state["wizard_page"] = 2
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# الصفحة 2
elif page == 2:
    st.markdown("<div class='page-shell center-page name-page'>", unsafe_allow_html=True)
    st.markdown("<div class='name-page-title'>اسم الطالب</div>", unsafe_allow_html=True)
    student_name = st.text_input("اسم الطالب", value=st.session_state["student_name"], placeholder="اكتب اسمك هنا", key="student_name_field", label_visibility="collapsed")
    st.session_state["student_name"] = student_name.strip()
    st.markdown("<div class='page-nav name-nav'>", unsafe_allow_html=True)
    if st.button("تأكيد →", type="primary", use_container_width=True, disabled=not bool(st.session_state["student_name"])):
        st.session_state["wizard_page"] = 3
        st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)

# الصفحة 3
elif page == 3:
    st.markdown("<div class='page-shell'>", unsafe_allow_html=True)
    st.markdown("<div class='page-kicker'>02 / بياناتك الأكاديمية</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='page-title'>مرحبًا {st.session_state['student_name']} 👋</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-description'>أدخل بياناتك الأكاديمية كما هي مسجلة في المنصة الجامعية. هذه البيانات أساسية لعمل المرشد بدقة.</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='field-label'>📈 التقدير التراكمي (GPA)</div>", unsafe_allow_html=True)
        gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, value=st.session_state["gpa_input"], step=0.01, format="%.2f", key="gpa_field", label_visibility="collapsed")
        st.session_state["gpa_input"] = gpa
    with c2:
        st.markdown("<div class='field-label'>الساعات المعتمدة المجتازة</div>", unsafe_allow_html=True)
        passed_hours = st.number_input("ساعات النجاح", min_value=0, max_value=200, value=st.session_state["passed_hours_input"], step=1, key="hours_field", label_visibility="collapsed")
        st.session_state["passed_hours_input"] = passed_hours

    st.markdown("<div class='field-label'>تأكيد البيانات</div>", unsafe_allow_html=True)
    data_confirmation = st.radio(
        "هل أدخلت التقدير التراكمي وساعات النجاح كما هي مسجلة في المنصة الجامعية؟",
        ["نعم، البيانات صحيحة", "لا، أحتاج إلى مراجعتها"],
        index=None,
        key="academic_data_confirmation",
    )
    know_data = data_confirmation == "نعم، البيانات صحيحة"
    dont_know = data_confirmation == "لا، أحتاج إلى مراجعتها"
    if dont_know:
        st.markdown("<div class='warning-box'>راجعي بيانات التقدير التراكمي وساعات النجاح من المنصة الجامعية ثم عودي إلى هذه الصفحة لإدخالها بدقة.</div>", unsafe_allow_html=True)

    valid = gpa is not None and passed_hours is not None and know_data
    st.markdown("<div class='required-note'>التقدير التراكمي وساعات النجاح لا يمكن للنظام استنتاجهما من اسم الطالب، لذلك يجب إدخالهما بدقة.</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-nav'>", unsafe_allow_html=True)
    b1, b2 = st.columns(2)
    with b1:
        if st.button("← رجوع", use_container_width=True):
            st.session_state["wizard_page"] = 2; st.rerun()
    with b2:
        if st.button("تأكيد →", type="primary", use_container_width=True, disabled=not valid):
            st.session_state["wizard_page"] = 4; st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)

# الصفحة 4
elif page == 4:
    st.markdown("<div class='page-shell'>", unsafe_allow_html=True)
    st.markdown("<div class='page-kicker'>03 / برنامجك الدراسي</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-title'>اختر برنامجك الدراسي</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-description'>اختاري نوع البرنامج الذي تنتمين إليه. سيستخدم المرشد هذا الاختيار لتحديد المقررات والقواعد المناسبة تلقائيًا.</div>", unsafe_allow_html=True)
    program = st.radio(
        "نوع البرنامج",
        ["عام", "خاص"],
        index=None,
        horizontal=False,
        key="program_field",
        help="عام = برنامج الإعلام التربوي العام، خاص = برنامج تربية خاصة / ذوي الاحتياجات الخاصة.",
    )
    st.session_state["program_input"] = program

    if program == "عام":
        st.markdown("<div class='success-box'><strong>البرنامج المختار: عام</strong><br><span class='subtle-note'>مسار الإعلام التربوي العام.</span></div>", unsafe_allow_html=True)
    elif program == "خاص":
        st.markdown("<div class='blue-box'><strong>البرنامج المختار: خاص</strong><br><span class='subtle-note'>مسار تربية خاصة / ذوي الاحتياجات الخاصة.</span></div>", unsafe_allow_html=True)

    if program:
        threshold = LEVEL_2_THRESHOLD[program]
        passed = st.session_state["passed_hours_input"]
        if passed is not None and passed >= threshold:
            text = f"استوفيت شرط الانتقال للمستوى الثاني في برنامج {program} وفق حد {threshold} ساعة."
            cls = "infer-card"
        else:
            text = f"لم تستوفِ بعد شرط الانتقال للمستوى الثاني في برنامج {program}؛ الحد المذكور هو {threshold} ساعة، وساعاتك الحالية {passed} ساعة."
            cls = "warning-box"
        st.markdown(f"<div class='{cls}'><div class='infer-title'>🧠 المرشد استنتج مستواك</div><div class='infer-text'>{text}</div></div>", unsafe_allow_html=True)

    st.markdown("<div class='page-nav'>", unsafe_allow_html=True)
    b1,b2=st.columns(2)
    with b1:
        if st.button("← رجوع", use_container_width=True): st.session_state["wizard_page"]=3; st.rerun()
    with b2:
        if st.button("تأكيد →", type="primary", use_container_width=True, disabled=not bool(program)):
            st.session_state["wizard_page"]=5; st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)

# الصفحة 5
elif page == 5:
    st.markdown("<div class='page-shell'>", unsafe_allow_html=True)
    st.markdown("<div class='page-kicker'>04 / المقررات غير المجتازة</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-title'>ما المقررات التي لم تجتزها؟</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-description'>اختر المقررات التي لم تجتزها فقط. يظهر اسم المقرر وكوده وساعاته حتى يكون الاختيار واضحًا.</div>", unsafe_allow_html=True)

    program = st.session_state["program_input"]
    available_failed_options = sorted([code for code, course in COURSES.items() if course_belongs_to_program(course, program)], key=lambda x: (COURSES[x].level, COURSES[x].name))
    failed = st.multiselect("المقررات", options=available_failed_options, format_func=lambda code: f"{COURSES[code].name} — {COURSES[code].code} — {('اجتياز' if COURSES[code].hours is None else str(COURSES[code].hours) + ' ساعة')}", default=st.session_state["failed_courses_input"], placeholder="اختر المقرر أو ابدأ بكتابة اسمه...", key="failed_field", label_visibility="collapsed")
    st.session_state["failed_courses_input"] = failed

    st.markdown(f"<div class='counter-card'><div><div class='counter-label'>عدد المقررات التي لم تجتزها</div><div class='counter-number'>{len(failed)}</div></div><div style='font-size:26px;'>📚</div></div>", unsafe_allow_html=True)
    if "EDU1.4" in failed:
        st.markdown("<div class='blue-box'>ℹ️ «طرق تدريس عامة» لها أثر على بعض المقررات المرتبطة بها، وسيأخذ النظام هذا الارتباط في التحليل تلقائيًا.</div>", unsafe_allow_html=True)

    no_failed = st.checkbox("أؤكد أنه لا توجد لدي مقررات غير مجتازة", key="no_failed_confirm") if not failed else False
    st.session_state["no_failed_courses_confirmed"] = no_failed
    valid = bool(failed) or no_failed

    # تحقق فوري من عدم تجاوز حد الانتقال بساعات مقرر غير مجتاز.
    program_for_check = st.session_state.get("program_input")
    passed_for_check = st.session_state.get("passed_hours_input")
    transition_conflict = False
    if program_for_check and passed_for_check is not None and failed:
        threshold_for_check = LEVEL_2_THRESHOLD[program_for_check]
        failed_hours_for_check = calculate_failed_credit_hours(failed)
        remaining_for_check = max(threshold_for_check - passed_for_check, 0)
        transition_conflict = passed_for_check < threshold_for_check and failed_hours_for_check > remaining_for_check
        if transition_conflict:
            st.markdown(
                f"<div class='danger-box'><strong>⚠️ تنبيه: الساعات المختارة لا تتوافق مع حد الانتقال</strong><br>لديك {passed_for_check} ساعة نجاح، والمتبقي لحد {threshold_for_check} ساعة هو {remaining_for_check} ساعة فقط، بينما المقرر/المقررات غير المجتازة المختارة مجموعها {failed_hours_for_check} ساعة.<br>لا يمكن اعتبار مقرر غير مجتاز بساعتين كأنه ساعة واحدة متبقية، ولا يجوز أن تتجاوز خطة الانتقال حد الساعات المطلوب.</div>",
                unsafe_allow_html=True,
            )

    st.markdown("<div class='page-nav'>", unsafe_allow_html=True)
    b1,b2=st.columns(2)
    with b1:
        if st.button("← رجوع", use_container_width=True): st.session_state["wizard_page"]=4; st.rerun()
    with b2:
        if st.button("تأكيد →", type="primary", use_container_width=True, disabled=(not valid or transition_conflict)): st.session_state["wizard_page"]=6; st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)

# الصفحة 6
elif page == 6:
    st.markdown("<div class='page-shell'>", unsafe_allow_html=True)
    st.markdown("<div class='page-kicker'>05 / المراجعة النهائية</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-title'>راجع بياناتك قبل التحليل</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-description'>تأكد من أن البيانات مطابقة لما هو مسجل لديك قبل أن يبدأ المرشد التحليل.</div>", unsafe_allow_html=True)
    failed = st.session_state["failed_courses_input"]
    program = st.session_state["program_input"]
    gpa = st.session_state["gpa_input"]
    hours = st.session_state["passed_hours_input"]
    items = [("اسم الطالب",st.session_state["student_name"]),("البرنامج",program),("GPA",f"{gpa:.2f}"),("ساعات النجاح",f"{hours} ساعة"),("المقررات غير المجتازة",f"{len(failed)} مقرر")]
    html="<div class='review-grid'>"+"".join(f"<div class='review-mini'><div class='review-mini-label'>{a}</div><div class='review-mini-value'>{b}</div></div>" for a,b in items)+"</div>"
    st.markdown(html, unsafe_allow_html=True)
    if failed:
        names = "، ".join(f"{COURSES[c].name} ({c})" for c in failed if c in COURSES)
        st.markdown(f"<div class='required-note'><strong>المقررات غير المجتازة:</strong> {names}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='success-box'>✓ لا توجد مقررات غير مجتازة وفق اختيارك.</div>", unsafe_allow_html=True)

    threshold = LEVEL_2_THRESHOLD.get(program, 0)
    failed_credit_hours = calculate_failed_credit_hours(failed)
    remaining_to_threshold = max(threshold - hours, 0)
    transition_conflict = hours < threshold and failed_credit_hours > remaining_to_threshold
    if transition_conflict:
        st.markdown(
            f"<div class='danger-box'><strong>⚠️ لا يمكن اعتماد البيانات بهذه الصورة</strong><br>أنت أدخلت {hours} ساعة نجاح، أي يتبقى {remaining_to_threshold} ساعة فقط للوصول إلى حد الانتقال لبرنامج «{program}» ({threshold} ساعة). لكن المقرر/المقررات غير المجتازة المختارة مجموعها {failed_credit_hours} ساعة. لا يمكن استخدام ساعتين غير مجتازتين لتغطية ساعة واحدة متبقية أو لتجاوز حد الانتقال.<br><strong>راجِع ساعات النجاح أو المقررات غير المجتازة قبل المتابعة.</strong></div>",
            unsafe_allow_html=True,
        )

    st.markdown("<div class='page-nav'>", unsafe_allow_html=True)
    b1,b2=st.columns(2)
    with b1:
        if st.button("← رجوع", use_container_width=True): st.session_state["wizard_page"]=5; st.rerun()
    with b2:
        if st.button("إظهار النتيجة →", type="primary", use_container_width=True, disabled=transition_conflict):
            data={"name":st.session_state["student_name"],"program":program,"gpa":gpa,"passed_hours":hours,"failed_courses":failed,"all_first_semester_passed":True}
            st.session_state["student_data"]=data
            st.session_state["analysis_result"]=analyze_student(data)
            st.session_state["wizard_page"]=7
            st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)

# الصفحات 6-8: النتيجة وخطة التسجيل والنصيحة
elif page in [7,8]:
    result = st.session_state.get("analysis_result")
    data = st.session_state.get("student_data")
    if not result or not data:
        st.session_state["wizard_page"] = 1
        st.rerun()

    st.markdown("<div class='page-shell'>", unsafe_allow_html=True)
    if page == 7:
        st.markdown("<div class='page-kicker'>07 / النتيجة</div>", unsafe_allow_html=True)
        st.markdown("<div class='page-title'>موقفك الدراسي</div>", unsafe_allow_html=True)
        st.markdown("<div class='page-description'>حلّل المرشد بياناتك تلقائيًا وفق القواعد المسجلة في النظام.</div>", unsafe_allow_html=True)
        c1,c2,c3,c4=st.columns(4)
        metrics=[(f"{data['gpa']:.2f}","GPA"),(str(data['passed_hours']),"ساعات النجاح"),(str(len(data['failed_courses'])),"المقررات غير المجتازة"),(data['program'],"البرنامج")]
        for col,(num,label) in zip((c1,c2,c3,c4),metrics):
            with col: st.markdown(f"<div class='metric-box'><div class='metric-number'>{num}</div><div class='metric-label'>{label}</div></div>",unsafe_allow_html=True)
        st.markdown(f"<div class='result-card'><div style='font-size:22px;font-weight:800;color:#14213d;margin-bottom:10px;'>نتيجة التحليل</div><div class='reason-box'><strong>لماذا ظهرت لك هذه النتيجة؟</strong><br>{result['reason']}</div></div>",unsafe_allow_html=True)
        if result.get("transition_conflict"):
            st.markdown(
                f"<div class='danger-box'><strong>⚠️ تعارض في ساعات الانتقال</strong><br>المتبقي للوصول إلى الحد هو {result.get('passed_hours_remaining', 0)} ساعة، بينما ساعات المقررات غير المجتازة المختارة {result.get('failed_credit_hours', 0)} ساعة. هذه الساعات لا تُحتسب كساعات نجاح ولا يجوز بها تجاوز حد الانتقال.</div>",
                unsafe_allow_html=True,
            )
        check = result.get("first_term_check")
        if check:
            if check["eligible"]:
                if check["exact"]:
                    st.markdown(f"<div class='success-box'><strong>✓ تحقق المستوى الثاني للفصل الدراسي الأول</strong><br>برنامج «{data['program']}» — حد الانتقال: {check['threshold']} ساعة نجاح.<br>المقررات الأساسية المحسوبة: <strong>{len(check['expected'])}</strong> مقررًا بإجمالي <strong>{check['expected_hours']} ساعة</strong>، وجميعها متاحة وفق المتطلبات الحالية.</div>",unsafe_allow_html=True)
                else:
                    blocked_names = "، ".join(course_name(c) for c in check["blocked"]) or "لا يوجد"
                    st.markdown(f"<div class='warning-box'><strong>⚠️ تحقق المستوى الثاني يحتاج مراجعة</strong><br>برنامج «{data['program']}» استوفى حد الانتقال ({check['threshold']} ساعة)، لكن إجمالي مقررات الفصل الأول المعرفة في الخطة هو <strong>{check['expected_hours']} ساعة</strong>، والمتاح حاليًا <strong>{check['available_hours']} ساعة</strong>.<br>المقررات المتأثرة بمتطلبات غير مجتازة: {blocked_names}.</div>",unsafe_allow_html=True)
            else:
                remaining = max(check["threshold"] - data["passed_hours"], 0)
                st.markdown(f"<div class='info-card'><strong>حالة شرط الانتقال</strong><br>الحد لبرنامج «{data['program']}» هو <strong>{check['threshold']} ساعة</strong>، والمتبقي للوصول إليه <strong>{remaining} ساعة</strong>.</div>",unsafe_allow_html=True)
        if result.get("warnings"):
            for w in result["warnings"]: st.markdown(f"<div class='warning-box'>⚠️ {w}</div>",unsafe_allow_html=True)
        st.markdown("<div class='page-nav'>",unsafe_allow_html=True)
        b1,b2=st.columns(2)
        with b1:
            if st.button("← تعديل البيانات",use_container_width=True): st.session_state["wizard_page"]=6; st.rerun()
        with b2:
            if st.button("خطة التسجيل →",type="primary",use_container_width=True): st.session_state["wizard_page"]=8; st.rerun()
        st.markdown("</div>")
    elif page == 8:
        st.markdown("<div class='page-kicker'>08 / خطة التسجيل</div>", unsafe_allow_html=True)
        st.markdown("<div class='page-title'>خطة التسجيل المقترحة</div>", unsafe_allow_html=True)
        st.markdown("<div class='page-description'>المتاح والمغلق والبدائل، ثم خطة الترم الصيفي عند انطباق القاعدة.</div>",unsafe_allow_html=True)
        failed_set=set(data["failed_courses"])
        if result["available"]:
            display_course_list("🟢 المقررات المتاحة",result["available"],"normal",failed_set)
        if result["blocked"]:
            display_course_list("🔒 المقررات غير المتاحة حاليًا",result["blocked"],"blocked",failed_set)
        if result["replacement"]:
            display_course_list("🔁 مقررات خطة المعالجة",result["replacement"],"replacement",failed_set)

        selected=[]; regular_used=0
        first_check = result.get("first_term_check") or {}
        if first_check.get("eligible") and result.get("regular_limit") is None:
            selected = list(first_check.get("available", []))
            regular_used = calculate_regular_hours(selected)
            st.markdown(f"<div class='success-box'><strong>خطة الفصل الدراسي الأول للمستوى الثاني:</strong> {len(selected)} مقررًا بإجمالي {regular_used} ساعة أساسية.</div>",unsafe_allow_html=True)
            if selected:
                display_course_list("📘 مقررات المستوى الثاني — الفصل الدراسي الأول",selected,"normal",failed_set)
        elif result.get("regular_limit") is not None:
            first_term_candidates, _, _, _ = build_first_term_plan(data["program"], failed_set)
            candidates=[c for c in first_term_candidates if c in COURSES and not COURSES[c].clearance and COURSES[c].hours is not None]
            priority={"EDU2.5":0,("EMS2.15" if data["program"]=="خاص" else "EM2.15"):1}
            candidates=sorted(candidates,key=lambda x:(priority.get(x,10),x))
            for c in candidates:
                hh=COURSES[c].hours
                if regular_used+hh<=TWELVE_HOUR_LIMIT:
                    selected.append(c); regular_used+=hh
            if result.get("case")==8:
                now_course="EM1.4" if data["program"]=="عام" else "EMS1.4"
                if now_course in failed_set and now_course in COURSES:
                    selected=[now_course]
                    regular_used=COURSES[now_course].hours or 0
                    for c in candidates:
                        if c==now_course:
                            continue
                        hh=COURSES[c].hours
                        if hh is not None and regular_used+hh<=TWELVE_HOUR_LIMIT:
                            selected.append(c); regular_used+=hh
                            if regular_used>=TWELVE_HOUR_LIMIT:
                                break
            st.markdown(f"<div class='info-card'><strong>حد التسجيل الأساسي:</strong> {TWELVE_HOUR_LIMIT} ساعة<br><span class='subtle-note'>المقترح: {regular_used} ساعة أساسية.</span></div>",unsafe_allow_html=True)
            if selected:
                display_course_list("📘 المقررات الأساسية المقترحة",selected,"normal",failed_set)

        if result.get("clearance"):
            display_course_list("✓ مقررات الاجتياز — منفصلة عن الساعات الأساسية",result["clearance"],"clearance",failed_set)

        summer_codes=[]
        for c in result.get("summer",[]):
            if c in COURSES and COURSES[c].hours is not None and not COURSES[c].clearance and c not in summer_codes:
                summer_codes.append(c)
        if summer_codes:
            st.markdown("<div class='section-title'>☀️ خطة تسجيل الترم الصيفي</div>",unsafe_allow_html=True)
            if result.get("case")==8:
                summer_limit=8
                prereq_set=CASE8_PREREQUISITES[data["program"]]
                now_course="EM1.4" if data["program"]=="عام" else "EMS1.4"
                summer_selected=sorted([c for c in prereq_set if c in failed_set and c != now_course])
                summer_selected=[c for c in summer_selected if c in COURSES and COURSES[c].hours is not None]
                summer_used=calculate_regular_hours(summer_selected)
                if summer_used>summer_limit:
                    summer_selected=[]; summer_used=0
                now_note=f"تُعاد «{course_name(now_course)}» الآن، وتُترك المتطلبات الأربعة الأخرى للصيف بإجمالي {summer_used} ساعات."
                st.markdown(f"<div class='info-card'><strong>حد الترم الصيفي في هذه الحالة:</strong> {summer_limit} ساعات<br><span class='subtle-note'>{now_note}<br>خطة الصيف: {summer_used} من {summer_limit} ساعات.</span></div>",unsafe_allow_html=True)
                display_course_list("مقررات الصيف المقترحة",summer_selected,"summer",failed_set)
                st.session_state["summer_plan_codes"]=summer_selected
            else:
                display_course_list("مقررات يمكن وضعها ضمن خطة الصيف",summer_codes,"summer",failed_set)
                st.session_state["summer_plan_codes"]=summer_codes
        else:
            st.session_state["summer_plan_codes"]=[]

        st.session_state["registration_plan"]={"regular":selected,"regular_hours":regular_used,"summer":st.session_state.get("summer_plan_codes",[])}
        st.markdown("<div class='page-nav'>",unsafe_allow_html=True)
        b1,b2=st.columns(2)
        with b1:
            if st.button("← النتيجة",use_container_width=True): st.session_state["wizard_page"]=7; st.rerun()
        with b2:
            if st.button("النصيحة الأكاديمية →",type="primary",use_container_width=True): st.session_state["wizard_page"]=9; st.rerun()
        st.markdown("</div>")
    st.markdown("</div>")

elif page == 9:
    result = st.session_state.get("analysis_result")
    data = st.session_state.get("student_data")
    if not result or not data:
        st.session_state["wizard_page"] = 1
        st.rerun()
    st.markdown("<div class='page-shell'>", unsafe_allow_html=True)
    st.markdown("<div class='page-kicker'>09 / النصيحة الأكاديمية</div>",unsafe_allow_html=True)
    st.markdown("<div class='page-title'>نصيحتك من المرشد</div>",unsafe_allow_html=True)
    st.markdown("<div class='page-description'>أهم النقاط التي ينبغي الانتباه إليها بناءً على النتيجة وخطة التسجيل.</div>",unsafe_allow_html=True)
    for w in result["warnings"]: st.markdown(f"<div class='warning-box'>⚠️ {w}</div>",unsafe_allow_html=True)
    for n in result["notes"]: st.markdown(f"<div class='blue-box'>💡 {n}</div>",unsafe_allow_html=True)
    if not result["warnings"] and not result["notes"]:
        st.markdown("<div class='success-box'>✓ حافظ على استقرار مستواك الأكاديمي واستمر في متابعة متطلبات التسجيل.</div>",unsafe_allow_html=True)
    st.markdown("<div class='page-nav'>",unsafe_allow_html=True)
    b1,b2=st.columns(2)
    with b1:
        if st.button("← خطة التسجيل",use_container_width=True): st.session_state["wizard_page"]=8; st.rerun()
    with b2:
        if st.button("المصطلحات المهمة →",type="primary",use_container_width=True): st.session_state["wizard_page"]=10; st.rerun()
    st.markdown("</div>")
    st.markdown("</div>")

else:
    st.markdown("<div class='page-shell'>", unsafe_allow_html=True)
    st.markdown("<div class='page-kicker'>10 / المصطلحات المهمة</div>",unsafe_allow_html=True)
    st.markdown("<div class='page-title'>المصطلحات المهمة</div>",unsafe_allow_html=True)
    st.markdown("<div class='page-description'>مرجع سريع للمصطلحات التي يحتاج الطالب إلى فهمها أثناء استخدام المرشد.</div>",unsafe_allow_html=True)
    glossary={
        "نظام الساعات المعتمدة":"نظام يعتمد على الساعات التي يجتازها الطالب والمقررات التي أنجزها، وليس على اسم السنة فقط.",
        "مادة المتطلب":"مقرر يجب اجتيازه حتى يصبح مقرر آخر مرتبط به متاحًا للتسجيل.",
        "المستوى الدراسي":"المستوى الذي يصل إليه الطالب وفق ساعات النجاح وشروط الانتقال المطبقة على برنامجه.",
        "ساعات النجاح":"إجمالي الساعات التي اجتازها الطالب بالفعل، وتستخدم في فهم موقفه وشرط الانتقال.",
        "مقررات الاجتياز":"مثل العربية والإنجليزية، ولا تُحتسب كساعات تسجيل أساسية وفق قاعدة المشروع.",
        "حد التسجيل":"أقصى عدد من الساعات الأساسية التي تسمح بها القاعدة المطبقة على الحالة عندما يكون لها حد محدد.",
    }
    for term,explanation in glossary.items():
        st.markdown(f"<div class='knowledge-card'><div class='knowledge-title'>{term}</div><div class='knowledge-text'>{explanation}</div></div>",unsafe_allow_html=True)
    st.markdown("<div class='warning-box final-warning'>⚠️ <strong>تنبيه نهائي:</strong> النتيجة وخطة التسجيل مبنيتان على البيانات والقواعد المسجلة في التطبيق، ويجب مراجعة المرشد الأكاديمي أو شؤون الطلاب عند وجود استثناء أو تعديل في اللائحة.</div>",unsafe_allow_html=True)
    st.markdown("<div class='page-nav'>",unsafe_allow_html=True)
    b1,b2=st.columns(2)
    with b1:
        if st.button("← النصيحة",use_container_width=True): st.session_state["wizard_page"]=9; st.rerun()
    with b2:
        if st.button("بدء تحليل جديد ↻",type="primary",use_container_width=True):
            for k in ["analysis_result","student_data","gpa_input","passed_hours_input","program_input","failed_courses_input","no_failed_courses_confirmed","registration_plan"]: st.session_state.pop(k,None)
            st.session_state.pop("summer_plan_codes",None)
            st.session_state["wizard_page"]=1; st.session_state["student_name"]=""; st.rerun()
    st.markdown("</div>")

