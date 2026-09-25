import streamlit as st
from dataclasses import dataclass
from typing import Optional, List, Dict, Set

# ============================================================
# المرشد الأكاديمي الذكي — دفعة 2025/2026
# الواجهة الجديدة لا تغيّر محرك القواعد الأكاديمية.
# ============================================================

st.set_page_config(
    page_title="المرشد الأكاديمي الذكي",
    page_icon="🎓",
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

.block-container {
    max-width: 1240px;
    padding-top: 1.4rem;
    padding-bottom: 3.5rem;
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
    box-shadow: 0 8px 20px rgba(29,78,216,.18);
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
add_course("EM1.8", "مبادئ العلاقات العامة", 2, 1, "إجباري تخصص", program="عام")
add_course("EM1.9", "أدب الطفل", 2, 1, "إجباري تخصص", program="عام")
add_course("EM1.10", "التربية الإعلامية", 2, 1, "إجباري تخصص", program="عام")
add_course("EME1.5", "الإعلام النفسي", 2, 1, "اختياري تخصص", program="عام")
add_course("EME1.6", "الإعلام وقضايا المجتمع", 2, 1, "اختياري تخصص", program="عام")
add_course("EME1.7", "التربية المسرحية", 2, 1, "اختياري تخصص", program="عام")
add_course("EME1.8", "الترجمة الإعلامية", 2, 1, "اختياري تخصص", program="عام")

# ============================================================
# المستوى الأول — خاص
# ============================================================
add_course("Sp1.1", "مدخل إلى التربية الخاصة", 2, 1, "تربية خاصة", program="خاص")
add_course("Sp1.2", "إعاقات بسيطة", 2, 1, "تربية خاصة", program="خاص")
add_course("EMS1.1", "نشأة وسائل الإعلام وتطورها", 2, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.2", "مبادئ علم الصحافة", 2, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.3", "الاتصال بالجماهير", 2, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.4", "مبادئ علوم المسرح", 2, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.5", "الإعلام والتنمية", 2, 1, "إجباري تخصص", program="خاص")
add_course("EMSE1.1", "مبادئ الإعلام التربوي", 1, 1, "اختياري تخصص", program="خاص")
add_course("EMSE1.2", "جماليات العرض المسرحي", 1, 1, "اختياري تخصص", program="خاص")
add_course("EMSE1.3", "مفاهيم ومصطلحات إعلامية", 1, 1, "اختياري تخصص", program="خاص")
add_course("EMSE1.4", "مبادئ الاقتصاد والسياسة", 1, 1, "اختياري تخصص", program="خاص")
add_course("Sp1.3", "التوعية بميدان الأطفال ذوي الاحتياجات الخاصة", 2, 1, "تربية خاصة", program="خاص")
add_course("Sp1.4", "القياس النفسي", 2, 1, "تربية خاصة", program="خاص")
add_course("EMS1.6", "الخبر في وسائل الإعلام", 1, 1, "إجباري تخصص", program="خاص")
add_course("EMS1.7", "مبادئ الراديو والتليفزيون", 1, 1, "إجباري تخصص", program="خاص")
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
add_course("UG3.2", "اللغة العربية", None, 2, "متطلبات الجامعة", program="خاص", clearance=True)
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
    for code in get_level2_courses(program):
        prerequisite = COURSES[code].prerequisite
        if prerequisite:
            prerequisites.add(prerequisite)
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
    }

    result["clearance"] = get_clearance_courses(failed_courses, program)
    result["clearance_hours"] = calculate_clearance_hours(result["clearance"])

    threshold = LEVEL_2_THRESHOLD[program]
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
        return result

    # الحالة 3
    if len(failed_courses) == 0 and 1.6 <= gpa < 2.0:
        result["case"] = 3
        result["title"] = "الحالة الثالثة"
        result["reason"] = "أنت ناجح في جميع المقررات، لكن التقدير التراكمي بين 1.60 وأقل من 2.00."
        result["available"] = get_available_level2_courses(failed_courses, program)
        result["warnings"].append("يجب العمل على رفع التقدير التراكمي إلى 2.00 وتجنب استمرار انخفاضه.")
        return result

    # الحالة 8
    case8_prerequisites = (
        {"EDU1.1", "EM1.2", "EM1.4", "EDU1.4"}
        if program == "عام"
        else {"EDU1.1", "EMS1.2", "EMS1.4", "EDU1.4"}
    )

    if gpa < 1.6 and case8_prerequisites.issubset(failed_courses):
        result["case"] = 8
        result["title"] = "الحالة الثامنة"
        result["reason"] = "التقدير التراكمي أقل من 1.60، ومقررات المتطلبات المحددة لهذه الحالة كلها ضمن المقررات الراسب فيها."
        result["regular_limit"] = TWELVE_HOUR_LIMIT
        result["blocked"] = get_blocked_level2_courses(failed_courses, program)
        result["available"] = get_available_level2_courses(failed_courses, program)
        result["replacement"] = get_replacement_courses(failed_courses, program)
        result["summer"] = list(failed_courses)
        if "EDU2.7" not in result["blocked"]:
            result["blocked"].append("EDU2.7")
        if "EDU2.7" in result["available"]:
            result["available"].remove("EDU2.7")
        result["warnings"].append("حد التسجيل الأساسي في هذه الحالة هو 12 ساعة.")
        result["warnings"].append("الأولوية هي العمل على رفع التقدير التراكمي وتجنب استمرار انخفاضه.")
        result["notes"].append("مواد الاجتياز، مثل اللغة العربية أو الإنجليزية إذا كانت ضمن مقررات الرسوب، لا تُخصم من حد الـ12 ساعة.")
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
        result["notes"].append("تكون الأولوية عند بناء خطة التسجيل لمقرر علم النفس للنمو وأساسيات الحاسب الآلي، ثم اختيار مقررات أخرى مناسبة وفق حالة الطالب.")
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
                result["notes"].append("عند الوصول إلى تقدير تراكمي 2.00 فأكثر، يمكن التعامل مع التدريس المصغر وفق خطة الصيف والقواعد المطبقة.")
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
        return result

    # الحالة 4
    if len(failed_courses) > 0 and not has_failed_prerequisite(failed_courses, program) and gpa >= 1.6:
        result["case"] = 4
        result["title"] = "الحالة الرابعة"
        result["reason"] = "لديك مقررات راسب فيها، لكن هذه المقررات ليست من المتطلبات التي تمنع فتح مقررات المستوى الثاني وفق علاقات المتطلبات المدخلة."
        result["available"] = get_available_level2_courses(failed_courses, program)
        result["summer"] = list(failed_courses)
        result["warnings"].append("يجب العمل على رفع التقدير التراكمي إلى 2.00 والمحافظة عليه.")
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
        return result

    result["title"] = "البيانات تحتاج إلى مراجعة"
    result["reason"] = "البيانات التي تم إدخالها لا تكفي لتحديد موقف دراسي مؤكد وفق القواعد المدخلة."
    result["warnings"].append("لا تختار موقفًا دراسيًا بنفسك ولا نعتمد على التخمين.")
    result["notes"].append("راجع البيانات المدخلة، وإذا كان الموقف غير موجود ضمن القواعد الحالية، يجب الرجوع إلى المرشد الأكاديمي.")
    return result


# ============================================================
# عرض المقررات — أسماء فقط للطالب، بلا أكواد
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
            extra = "يمكن وضعه ضمن خطة الصيف وفق قواعد الصيف والتسجيل الفعلية"
        elif style == "clearance":
            badge = "<span class='badge badge-green'>اجتياز</span>"
            extra = "لا يستهلك حد الـ12 ساعة الأساسي في المواقف التي ينطبق عليها هذا الحد"
        else:
            badge = "<span class='badge badge-blue'>مقرر متاح</span>"
            extra = course.category
            if course.prerequisite:
                extra += f" — المتطلب السابق: {course_name(course.prerequisite)}"

        st.markdown(
            f"""
            <div class="course-card">
                <div class="course-name">{badge} {course.name}</div>
                <div class="course-meta">{hours_text} &nbsp; • &nbsp; {extra}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# الواجهة الرئيسية
# ============================================================

st.markdown(
    """
    <div class="hero" dir="rtl">
        <div class="hero-content">
            <div class="hero-badge">دفعة 2025/2026 • نظام الساعات المعتمدة</div>
            <h1 class="hero-title">🎓 المرشد الأكاديمي الذكي</h1>
            <div class="hero-subtitle">
                أداة أكاديمية تساعدك على فهم موقفك الدراسي، ومعرفة المقررات المتاحة لك،
                والمتطلبات المرتبطة بها، والتنبيهات المهمة قبل التسجيل.
            </div>
            <div class="hero-meta">
                <span>قسم الإعلام التربوي</span>
                <span>برنامج عام / خاص</span>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="intro-card" dir="rtl">
        <div class="intro-title">مرحبًا بك 👋</div>
        <div class="intro-text">
            أدخل بياناتك الدراسية، وسيقوم المرشد بتحليل موقفك الأكاديمي وتحديد المقررات
            المتاحة لك والتنبيهات الخاصة بالتسجيل، وفق القواعد المطبقة في النظام.
        </div>
    </div>

    <div class="steps" dir="rtl">
        <div class="step-card step-active"><div class="step-no">01</div><div class="step-text">بياناتك الدراسية</div></div>
        <div class="step-card"><div class="step-no">02</div><div class="step-text">موقفك الدراسي</div></div>
        <div class="step-card"><div class="step-no">03</div><div class="step-text">التحليل والنتيجة</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# البيانات الأساسية
# ============================================================
st.markdown('<div class="section-title">📝 بياناتك الدراسية</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    student_name = st.text_input("اسم الطالب", placeholder="اكتب اسمك هنا")
with col2:
    program = st.selectbox("نوع البرنامج", ["عام", "خاص"], index=0)

st.caption("اختيار البرنامج مهم لأن المقررات وعلاقات المتطلبات وحدود الانتقال تختلف حسب البرنامج.")

# ============================================================
# الموقف الدراسي
# ============================================================
st.markdown('<div class="section-title">📊 موقفك الدراسي</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="field-label">📈 التقدير التراكمي (GPA)</div>', unsafe_allow_html=True)
    gpa = st.number_input(
        "التقدير التراكمي (GPA)",
        min_value=0.0,
        max_value=4.0,
        value=2.00,
        step=0.01,
        format="%.2f",
        help="المعدل التراكمي هو متوسط تقديرك الأكاديمي على مقياس من 0 إلى 4.",
        label_visibility="collapsed",
    )
    st.caption("المعدل من 0 إلى 4، ويُستخدم ضمن قواعد التحليل الأكاديمي.")

with c2:
    st.markdown('<div class="field-label">🎓 الساعات المعتمدة المجتازة</div>', unsafe_allow_html=True)
    passed_hours = st.number_input(
        "عدد الساعات المعتمدة المجتازة",
        min_value=0,
        max_value=200,
        value=0,
        step=1,
        help="أدخل عدد الساعات التي اجتزتها بالفعل حتى الآن.",
        label_visibility="collapsed",
    )
    threshold = LEVEL_2_THRESHOLD[program]
    status_class = "threshold-ok" if passed_hours >= threshold else "threshold-low"
    status_text = "تجاوزت الحد المذكور للانتقال" if passed_hours >= threshold else "أقل من الحد المذكور للانتقال"
    st.markdown(
        f"""
        <div class="threshold-card">
            <div class="threshold-value">{threshold} ساعة</div>
            <div class="threshold-label">الحد المذكور للانتقال إلى المستوى الثاني — برنامج {program}</div>
            <div class="{status_class}" style="margin-top:6px;">{status_text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# ملاحظة داخلية لمحرك الحالة السادسة
# ============================================================
# لا نعرض سؤالًا منفصلًا عن الفصل الدراسي الأول للمستخدم؛
# حالة 6A تعتمد أصلًا على أن المقرر غير المجتاز الوحيد هو "طرق تدريس عامة".
# لذلك تظل قيمة المتغير الداخلية ثابتة دون تغيير قواعد التحليل.
all_first_semester_passed = True

# ============================================================
# المقررات غير المجتازة
# ============================================================
st.markdown('<div class="section-title">📖 المقررات التي لم تجتزها</div>', unsafe_allow_html=True)
st.caption("اختر فقط المقررات التي لم تجتزها بالفعل. ستظهر لك أسماء المقررات فقط، بينما الأكواد تظل داخل النظام.")

available_failed_options = sorted(
    [
        code for code, course in COURSES.items()
        if course_belongs_to_program(course, program)
    ],
    key=lambda x: (COURSES[x].level, COURSES[x].name),
)

failed_courses = st.multiselect(
    "حدد المقررات غير المجتازة",
    options=available_failed_options,
    format_func=lambda code: COURSES[code].name,
    placeholder="ابدأ بكتابة اسم المقرر أو اختر من القائمة...",
)

st.markdown(
    f"""
    <div class="counter-card" dir="rtl">
        <div>
            <div class="counter-label">المقررات التي لم تجتزها</div>
            <div class="counter-number">{len(failed_courses)}</div>
        </div>
        <div style="font-size:26px;">📚</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if "EDU1.4" in failed_courses:
    st.info(
        "طرق تدريس عامة من المقررات التي لها أثر على بعض المقررات المرتبطة بها، لذلك سيأخذ النظام هذا الارتباط في التحليل تلقائيًا."
    )

# ============================================================
# مراجعة البيانات قبل التحليل
# ============================================================
st.markdown('<div class="section-title">🔎 مراجعة بياناتك</div>', unsafe_allow_html=True)
st.markdown(
    f"""
    <div class="review-card" dir="rtl">
        <div class="review-title">تأكد من بياناتك قبل بدء التحليل</div>
        <div class="review-item"><strong>البرنامج:</strong> {program}</div>
        <div class="review-item"><strong>المعدل التراكمي:</strong> {gpa:.2f}</div>
        <div class="review-item"><strong>ساعات النجاح:</strong> {passed_hours} ساعة</div>
        <div class="review-item"><strong>المقررات غير المجتازة:</strong> {len(failed_courses)} مقرر</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
analyze_button = st.button("🔍 تحليل موقفي الدراسي", type="primary", use_container_width=True)

# ============================================================
# تشغيل التحليل — نفس المحرك
# ============================================================
if analyze_button:
    data = {
        "name": student_name,
        "program": program,
        "gpa": gpa,
        "passed_hours": passed_hours,
        "failed_courses": failed_courses,
        "all_first_semester_passed": all_first_semester_passed,
    }
    result = analyze_student(data)
    st.session_state["analysis_result"] = result
    st.session_state["student_data"] = data
    st.session_state["analysis_ran"] = True

# ============================================================
# النتيجة
# ============================================================
if "analysis_result" in st.session_state:
    result = st.session_state["analysis_result"]
    data = st.session_state["student_data"]

    st.markdown('<div class="section-title">📋 موقفك الدراسي بعد التحليل</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    metrics = [
        (f"{data['gpa']:.2f}", "المعدل التراكمي"),
        (str(data["passed_hours"]), "ساعات النجاح"),
        (str(len(data["failed_courses"])), "المقررات غير المجتازة"),
        (data["program"], "نوع البرنامج"),
    ]
    for column, (number, label) in zip((c1, c2, c3, c4), metrics):
        with column:
            st.markdown(
                f"<div class='metric-box'><div class='metric-number'>{number}</div><div class='metric-label'>{label}</div></div>",
                unsafe_allow_html=True,
            )

    st.markdown(
        f"""
        <div class="result-card" dir="rtl">
            <div style="font-size:24px;font-weight:800;color:#14213d;margin-bottom:10px;">نتيجة التحليل</div>
            <div style="color:#64748b;font-size:13px;margin-bottom:12px;">تم تحليل بياناتك وفق القواعد الأكاديمية المدخلة في النظام.</div>
            <div class="reason-box">
                <strong>لماذا ظهرت لك هذه النتيجة؟</strong><br>
                {result['reason']}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if result["clearance"]:
        st.markdown('<div class="section-title">🎯 مقررات الاجتياز</div>', unsafe_allow_html=True)
        st.markdown(
            "<div class='blue-box'><strong>مهم:</strong> مقررات الاجتياز لا تُحسب ضمن حد الساعات الأساسي في المواقف التي ينطبق عليها هذا الحد.</div>",
            unsafe_allow_html=True,
        )
        display_course_list("مقررات الاجتياز الموجودة ضمن موادك غير المجتازة", result["clearance"], "clearance", set(data["failed_courses"]))

    if result["regular_limit"] is not None:
        st.markdown('<div class="section-title">⏱️ حد التسجيل الأساسي</div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="info-card" dir="rtl">
                <div style="font-size:23px;font-weight:800;color:#14213d;">{TWELVE_HOUR_LIMIT} ساعة أساسية</div>
                <div class="subtle-note">هذا الحد يخص الساعات الأساسية للتسجيل. مقررات الاجتياز لها معاملة منفصلة.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if result["available"]:
        st.markdown('<div class="section-title">🟢 المقررات المتاحة</div>', unsafe_allow_html=True)
        display_course_list("مقررات يمكنك النظر في تسجيلها", result["available"], "normal", set(data["failed_courses"]))

    if result["blocked"]:
        st.markdown('<div class="section-title">🔒 مقررات تحتاج إلى استيفاء متطلباتها</div>', unsafe_allow_html=True)
        st.markdown(
            "<div class='warning-box'>هذه المقررات مرتبطة بمتطلبات سابقة لم يتم اجتيازها وفق البيانات التي أدخلتها.</div>",
            unsafe_allow_html=True,
        )
        display_course_list("مقررات غير متاحة حاليًا", result["blocked"], "blocked", set(data["failed_courses"]))

    if result["replacement"]:
        st.markdown('<div class="section-title">🔁 مقررات يمكن إدخالها ضمن خطة المعالجة</div>', unsafe_allow_html=True)
        display_course_list("مقررات المستوى الأول المرتبطة بخطة المعالجة", result["replacement"], "replacement", set(data["failed_courses"]))

    if result["case"] in [7, 8]:
        st.markdown('<div class="section-title">🧭 تصور لخطة الـ12 ساعة</div>', unsafe_allow_html=True)
        regular_candidates = [
            code for code in result["available"]
            if code in COURSES and not COURSES[code].clearance and COURSES[code].hours is not None
        ]
        priority = {
            "EDU2.5": 0,
            ("EMS2.15" if data["program"] == "خاص" else "EM2.15"): 1,
        }
        regular_candidates = sorted(regular_candidates, key=lambda x: (priority.get(x, 10), x))
        selected_for_plan = []
        hours_used = 0
        for code in regular_candidates:
            h = COURSES[code].hours
            if h is not None and hours_used + h <= TWELVE_HOUR_LIMIT:
                selected_for_plan.append(code)
                hours_used += h

        st.markdown(
            f"<div class='info-card'><strong>الساعات الأساسية المقترحة:</strong> {hours_used} / {TWELVE_HOUR_LIMIT} ساعة<br><span class='subtle-note'>هذا الحساب يخص المقررات الأساسية فقط؛ مقررات الاجتياز لها معاملة منفصلة.</span></div>",
            unsafe_allow_html=True,
        )
        display_course_list("المقررات الأساسية المقترحة", selected_for_plan, "normal", set(data["failed_courses"]))

        if result["clearance"]:
            st.markdown(
                "<div class='success-box'><strong>بالإضافة إلى ذلك:</strong> يمكن إضافة مقررات الاجتياز المحددة دون اعتبارها جزءًا من حد الـ12 ساعة الأساسي.</div>",
                unsafe_allow_html=True,
            )

    if result["summer"]:
        st.markdown('<div class="section-title">☀️ مقررات يمكن وضعها ضمن خطة الصيف</div>', unsafe_allow_html=True)
        display_course_list("مقررات الصيف", result["summer"], "summer", set(data["failed_courses"]))
        st.caption("ظهور المقرر ضمن خطة الصيف يعني أنه من الخيارات التي تحتاج إلى مراجعة قواعد الصيف والتسجيل الفعلية، وليس أن تسجيله مضمون تلقائيًا.")

    if result["warnings"]:
        st.markdown('<div class="section-title">⚠️ تنبيهات مهمة</div>', unsafe_allow_html=True)
        for warning in result["warnings"]:
            st.markdown(f"<div class='warning-box'>⚠️ {warning}</div>", unsafe_allow_html=True)

    if result["notes"]:
        st.markdown('<div class="section-title">💡 ملاحظات المرشد</div>', unsafe_allow_html=True)
        for note in result["notes"]:
            st.markdown(f"<div class='blue-box'>💡 {note}</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-title">📚 مصطلحات مهمة</div>', unsafe_allow_html=True)
    glossary = {
        "GPA": "التقدير التراكمي للطالب.",
        "الساعات المعتمدة": "وحدة تُستخدم لقياس العبء الدراسي للمقرر.",
        "مادة المتطلب": "مادة يجب اجتيازها حتى يصبح من الممكن تسجيل مادة مرتبطة بها.",
        "Prerequisite": "المتطلب السابق؛ أي المادة التي يجب اجتيازها قبل فتح المادة المرتبطة بها.",
        "مقررات الاجتياز": "مقررات يمكن التعامل معها كمقررات اجتياز ولا تدخل ضمن حد الـ12 ساعة الأساسي في المواقف التي ينطبق عليها ذلك.",
        "المستوى": "المستوى الدراسي داخل نظام الساعات المعتمدة، وليس بالضرورة سنة دراسية كاملة.",
    }
    for term, explanation in glossary.items():
        st.markdown(
            f"<div class='info-card' dir='rtl'><div style='font-weight:800;font-size:16px;color:#14213d;'>{term}</div><div class='subtle-note' style='margin-top:6px;'>{explanation}</div></div>",
            unsafe_allow_html=True,
        )

    st.error(
        "⚠️ تنبيه نهائي: هذا المرشد مبني على القواعد والبيانات المدخلة في التطبيق. "
        "النتيجة تساعدك على فهم موقفك الدراسي وتكوين تصور عن التسجيل، لكنها لا تغني عن مراجعة المرشد الأكاديمي أو شؤون الطلاب عند وجود استثناء أو تعديل في اللائحة أو موقف غير مذكور في القواعد."
    )

else:
    st.markdown(
        "<div class='info-card' style='text-align:center;margin-top:22px;'>"
        "<div style='font-size:20px;font-weight:800;color:#14213d;'>جاهز تبدأ؟</div>"
        "<div class='subtle-note' style='margin-top:6px;'>أدخل بياناتك في الأقسام السابقة، ثم اضغط «تحليل موقفي الدراسي» لعرض موقفك والمقررات المرتبطة به.</div>"
        "</div>",
        unsafe_allow_html=True,
    )

# ============================================================
# Footer
# ============================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align:center;color:#7b8799;font-size:12px;line-height:2.1;">
        🎓 المرشد الأكاديمي الذكي<br>
        نظام الساعات المعتمدة • دفعة 2025/2026 • قسم الإعلام التربوي
    </div>
    """,
    unsafe_allow_html=True,
)
