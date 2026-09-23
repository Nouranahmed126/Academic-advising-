import streamlit as st
from dataclasses import dataclass
from typing import Optional, List, Dict, Set


# ============================================================
# 🎓 المرشد الأكاديمي الذكي
# دفعة 2025/2026 — قسم الإعلام التربوي
# نظام الساعات المعتمدة
# ============================================================


# ------------------------------------------------------------
# إعداد الصفحة
# ------------------------------------------------------------

st.set_page_config(
    page_title="المرشد الأكاديمي الذكي",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ------------------------------------------------------------
# CSS — تصميم عربي RTL
# ------------------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: "Cairo", sans-serif;
    direction: rtl;
}

.stApp {
    background:
        radial-gradient(circle at top right, rgba(37, 99, 235, 0.08), transparent 30%),
        radial-gradient(circle at bottom left, rgba(16, 185, 129, 0.07), transparent 30%),
        #f7f9fc;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    color: #172033;
    margin-bottom: 5px;
}

.main-subtitle {
    text-align: center;
    color: #64748b;
    font-size: 18px;
    margin-bottom: 25px;
}

.section-title {
    background: linear-gradient(135deg, #172033, #263b63);
    color: white;
    padding: 14px 20px;
    border-radius: 16px;
    margin-top: 20px;
    margin-bottom: 18px;
    font-size: 21px;
    font-weight: 800;
}

.info-card {
    background: white;
    border: 1px solid #e5eaf2;
    border-radius: 18px;
    padding: 20px;
    margin: 10px 0;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.05);
}

.result-card {
    background: white;
    border-radius: 22px;
    padding: 25px;
    margin-top: 20px;
    border: 1px solid #e5eaf2;
    box-shadow: 0 8px 28px rgba(15, 23, 42, 0.07);
}

.case-card {
    background: linear-gradient(135deg, #eef6ff, #ffffff);
    border: 2px solid #93c5fd;
    border-radius: 22px;
    padding: 25px;
    margin: 20px 0;
}

.case-number {
    font-size: 17px;
    color: #2563eb;
    font-weight: 700;
}

.case-title {
    font-size: 30px;
    font-weight: 800;
    color: #172033;
    margin-top: 5px;
}

.reason-box {
    background: #f8fafc;
    border-right: 5px solid #2563eb;
    padding: 18px;
    border-radius: 14px;
    margin-top: 15px;
}

.warning-box {
    background: #fff7ed;
    border-right: 5px solid #f97316;
    padding: 18px;
    border-radius: 14px;
    margin: 12px 0;
}

.danger-box {
    background: #fef2f2;
    border-right: 5px solid #dc2626;
    padding: 18px;
    border-radius: 14px;
    margin: 12px 0;
}

.success-box {
    background: #f0fdf4;
    border-right: 5px solid #16a34a;
    padding: 18px;
    border-radius: 14px;
    margin: 12px 0;
}

.blue-box {
    background: #eff6ff;
    border-right: 5px solid #2563eb;
    padding: 18px;
    border-radius: 14px;
    margin: 12px 0;
}

.course-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 15px;
    padding: 15px;
    margin: 8px 0;
}

.course-name {
    font-weight: 800;
    color: #172033;
    font-size: 16px;
}

.course-meta {
    color: #64748b;
    font-size: 13px;
}

.pill {
    display: inline-block;
    padding: 5px 11px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    margin: 3px;
}

.pill-green {
    background: #dcfce7;
    color: #166534;
}

.pill-yellow {
    background: #fef9c3;
    color: #854d0e;
}

.pill-red {
    background: #fee2e2;
    color: #991b1b;
}

.pill-blue {
    background: #dbeafe;
    color: #1e40af;
}

.step-container {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin: 20px 0 30px 0;
    flex-wrap: wrap;
}

.step {
    padding: 8px 15px;
    border-radius: 999px;
    background: #e2e8f0;
    color: #64748b;
    font-size: 13px;
    font-weight: 700;
}

.step-active {
    background: #2563eb;
    color: white;
}

.small-note {
    color: #64748b;
    font-size: 13px;
    line-height: 1.9;
}

.metric-box {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 17px;
    text-align: center;
}

.metric-number {
    font-size: 28px;
    font-weight: 800;
    color: #172033;
}

.metric-label {
    color: #64748b;
    font-size: 13px;
}

hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 25px 0;
}

</style>
""", unsafe_allow_html=True)


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


# ============================================================
# قاعدة المقررات النهائية
# ============================================================

COURSES: Dict[str, Course] = {}


def add_course(
    code,
    name,
    hours,
    level,
    category,
    program="مشترك",
    prerequisite=None,
    clearance=False
):
    COURSES[code] = Course(
        code=code,
        name=name,
        hours=hours,
        level=level,
        category=category,
        program=program,
        prerequisite=prerequisite,
        clearance=clearance
    )


# ============================================================
# المستوى الأول — عام
# ============================================================

add_course(
    "UG1.1",
    "اللغة الإنجليزية",
    None,
    1,
    "متطلبات الجامعة",
    program="مشترك",
    clearance=True
)

add_course(
    "EDU1.1",
    "مدخل إلى العلوم التربوية",
    2,
    1,
    "متطلبات الكلية",
    program="مشترك"
)

add_course(
    "EDU1.2",
    "المناهج وتنظيماتها",
    2,
    1,
    "متطلبات الكلية",
    program="مشترك"
)

add_course(
    "EM1.1",
    "نشأة وسائل الإعلام وتطورها",
    2,
    1,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM1.2",
    "مبادئ علم الصحافة",
    2,
    1,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM1.3",
    "الاتصال بالجماهير",
    2,
    1,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM1.4",
    "مبادئ علوم المسرح",
    2,
    1,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM1.5",
    "الإعلام والتنمية",
    2,
    1,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EME1.1",
    "مبادئ الإعلام التربوي",
    2,
    1,
    "اختياري تخصص",
    program="عام"
)

add_course(
    "EME1.2",
    "جماليات العرض المسرحي",
    2,
    1,
    "اختياري تخصص",
    program="عام"
)

add_course(
    "EME1.3",
    "مفاهيم ومصطلحات إعلامية",
    2,
    1,
    "اختياري تخصص",
    program="عام"
)

add_course(
    "EME1.4",
    "مبادئ الاقتصاد والسياسة",
    2,
    1,
    "اختياري تخصص",
    program="عام"
)

# الفصل الدراسي الثاني — عام

add_course(
    "EDU1.3",
    "مدخل إلى العلوم النفسية",
    2,
    1,
    "متطلبات الكلية",
    program="مشترك"
)

add_course(
    "EDU1.4",
    "طرق تدريس عامة",
    2,
    1,
    "متطلبات الكلية",
    program="مشترك"
)

add_course(
    "EM1.6",
    "الخبر في وسائل الإعلام",
    2,
    1,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM1.7",
    "مبادئ الراديو والتليفزيون",
    2,
    1,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM1.8",
    "مبادئ العلاقات العامة",
    2,
    1,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM1.9",
    "أدب الطفل",
    2,
    1,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM1.10",
    "التربية الإعلامية",
    2,
    1,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EME1.5",
    "الإعلام النفسي",
    2,
    1,
    "اختياري تخصص",
    program="عام"
)

add_course(
    "EME1.6",
    "الإعلام وقضايا المجتمع",
    2,
    1,
    "اختياري تخصص",
    program="عام"
)

add_course(
    "EME1.7",
    "التربية المسرحية",
    2,
    1,
    "اختياري تخصص",
    program="عام"
)

add_course(
    "EME1.8",
    "الترجمة الإعلامية",
    2,
    1,
    "اختياري تخصص",
    program="عام"
)


# ============================================================
# المستوى الأول — خاص
# ============================================================

add_course(
    "Sp1.1",
    "مدخل إلى التربية الخاصة",
    2,
    1,
    "تربية خاصة",
    program="خاص"
)

add_course(
    "Sp1.2",
    "إعاقات بسيطة",
    2,
    1,
    "تربية خاصة",
    program="خاص"
)

add_course(
    "EMS1.1",
    "نشأة وسائل الإعلام وتطورها",
    2,
    1,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS1.2",
    "مبادئ علم الصحافة",
    2,
    1,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS1.3",
    "الاتصال بالجماهير",
    2,
    1,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS1.4",
    "مبادئ علوم المسرح",
    2,
    1,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS1.5",
    "الإعلام والتنمية",
    2,
    1,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMSE1.1",
    "مبادئ الإعلام التربوي",
    1,
    1,
    "اختياري تخصص",
    program="خاص"
)

add_course(
    "EMSE1.2",
    "جماليات العرض المسرحي",
    1,
    1,
    "اختياري تخصص",
    program="خاص"
)

add_course(
    "EMSE1.3",
    "مفاهيم ومصطلحات إعلامية",
    1,
    1,
    "اختياري تخصص",
    program="خاص"
)

add_course(
    "EMSE1.4",
    "مبادئ الاقتصاد والسياسة",
    1,
    1,
    "اختياري تخصص",
    program="خاص"
)

# الفصل الدراسي الثاني — خاص

add_course(
    "Sp1.3",
    "التوعية بميدان الأطفال ذوي الاحتياجات الخاصة",
    2,
    1,
    "تربية خاصة",
    program="خاص"
)

add_course(
    "Sp1.4",
    "القياس النفسي",
    2,
    1,
    "تربية خاصة",
    program="خاص"
)

add_course(
    "EMS1.6",
    "الخبر في وسائل الإعلام",
    1,
    1,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS1.7",
    "مبادئ الراديو والتليفزيون",
    1,
    1,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS1.8",
    "مبادئ العلاقات العامة",
    1,
    1,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS1.9",
    "أدب الطفل",
    2,
    1,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS1.10",
    "التربية الإعلامية",
    1,
    1,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMSE1.5",
    "الإعلام النفسي",
    1,
    1,
    "اختياري تخصص",
    program="خاص"
)

add_course(
    "EMSE1.6",
    "الإعلام وقضايا المجتمع",
    1,
    1,
    "اختياري تخصص",
    program="خاص"
)

add_course(
    "EMSE1.7",
    "التربية المسرحية",
    1,
    1,
    "اختياري تخصص",
    program="خاص"
)

add_course(
    "EMSE1.8",
    "الترجمة الإعلامية",
    1,
    1,
    "اختياري تخصص",
    program="خاص"
)


# ============================================================
# المستوى الثاني — عام
# ============================================================

add_course(
    "UG2.2",
    "اللغة العربية",
    None,
    2,
    "متطلبات الجامعة",
    program="عام",
    clearance=True
)

add_course(
    "EDU2.5",
    "علم النفس للنمو",
    2,
    2,
    "متطلبات الكلية",
    program="مشترك"
)

add_course(
    "EDU2.6",
    "تاريخ التربية ونظام التعليم في مصر",
    2,
    2,
    "متطلبات الكلية",
    program="مشترك",
    prerequisite="EDU1.1"
)

add_course(
    "EDU2.7",
    "التدريس المصغر",
    2,
    2,
    "متطلبات الكلية",
    program="مشترك",
    prerequisite="EDU1.4"
)

add_course(
    "EM2.11",
    "تكنولوجيا الاتصال والمعلومات",
    2,
    2,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM2.12",
    "المسرح المصري",
    2,
    2,
    "إجباري تخصص",
    program="عام",
    prerequisite="EM1.4"
)

add_course(
    "EM2.13",
    "إعلام الطفل",
    2,
    2,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM2.14",
    "أنشطة الصحافة والإذاعة المدرسية",
    2,
    2,
    "إجباري تخصص",
    program="عام",
    prerequisite="EM1.2"
)

add_course(
    "EM2.15",
    "أساسيات الحاسب الآلي",
    2,
    2,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EME2.9",
    "التوثيق الإعلامي",
    2,
    2,
    "اختياري تخصص",
    program="عام"
)

add_course(
    "EME2.10",
    "التليفزيون التعليمي",
    2,
    2,
    "اختياري تخصص",
    program="عام"
)

add_course(
    "EME2.11",
    "الصحافة الاستقصائية",
    2,
    2,
    "اختياري تخصص",
    program="عام"
)

add_course(
    "EME2.12",
    "مسرحة المناهج التعليمية",
    2,
    2,
    "اختياري تخصص",
    program="عام"
)

# الفصل الدراسي الثاني — عام

add_course(
    "EDU2.8",
    "سيكولوجية ذوي الاحتياجات الخاصة",
    2,
    2,
    "متطلبات الكلية",
    program="مشترك"
)

add_course(
    "EDU2.9",
    "علم نفس تعليمي (نظريات تعلم)",
    2,
    2,
    "متطلبات الكلية",
    program="مشترك",
    prerequisite="EDU1.3"
)

add_course(
    "EM2.16",
    "الأصول العلمية للإعلان",
    2,
    2,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM2.17",
    "نظم سياسية وسياسات الإعلام",
    2,
    2,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM2.18",
    "الرأي العام وطرق قياسه",
    2,
    2,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM2.19",
    "تشريعات الإعلام وأخلاقياته",
    2,
    2,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EM2.20",
    "مسرح الطفل",
    3,
    2,
    "إجباري تخصص",
    program="عام"
)

add_course(
    "EME2.13",
    "صحافة المواطن",
    1,
    2,
    "اختياري تخصص",
    program="عام"
)

add_course(
    "EME2.14",
    "تيارات فكرية وثقافية معاصرة",
    1,
    2,
    "اختياري تخصص",
    program="عام"
)

add_course(
    "EME2.15",
    "الإحصاء والحاسب الآلي",
    1,
    2,
    "اختياري تخصص",
    program="عام",
    prerequisite="EM2.15"
)

add_course(
    "EME2.16",
    "المذاهب المسرحية",
    1,
    2,
    "اختياري تخصص",
    program="عام"
)


# ============================================================
# المستوى الثاني — خاص
# ============================================================

add_course(
    "UG3.2",
    "اللغة العربية",
    None,
    2,
    "متطلبات الجامعة",
    program="خاص",
    clearance=True
)

add_course(
    "SP2.5",
    "تقييم أطفال ذوي الاحتياجات الخاصة",
    2,
    2,
    "تربية خاصة",
    program="خاص"
)

add_course(
    "SP2.6",
    "مهارات تواصل ذوي الاحتياجات الخاصة",
    2,
    2,
    "تربية خاصة",
    program="خاص"
)

add_course(
    "EMS2.11",
    "تكنولوجيا الاتصال والمعلومات",
    1,
    2,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS2.12",
    "المسرح المدرسي",
    2,
    2,
    "إجباري تخصص",
    program="خاص",
    prerequisite="EMS1.4"
)

add_course(
    "EMS2.13",
    "إعلام الطفل",
    2,
    2,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS2.14",
    "أنشطة الصحافة والإذاعة المدرسية",
    2,
    2,
    "إجباري تخصص",
    program="خاص",
    prerequisite="EMS1.2"
)

add_course(
    "EMS2.15",
    "أساسيات الحاسب الآلي",
    2,
    2,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMSE2.9",
    "التوثيق الإعلامي",
    1,
    2,
    "اختياري تخصص",
    program="خاص"
)

add_course(
    "EMSE2.10",
    "التليفزيون التعليمي",
    1,
    2,
    "اختياري تخصص",
    program="خاص"
)

add_course(
    "EMSE2.11",
    "الصحافة الاستقصائية",
    1,
    2,
    "اختياري تخصص",
    program="خاص"
)

add_course(
    "EMSE2.12",
    "مسرحة المناهج التعليمية",
    1,
    2,
    "اختياري تخصص",
    program="خاص"
)

# الفصل الدراسي الثاني — خاص

add_course(
    "Sp2.7",
    "الاضطرابات الانفعالية والسلوكية لأطفال ذوي الاحتياجات الخاصة",
    2,
    2,
    "تربية خاصة",
    program="خاص"
)

add_course(
    "Sp2.8",
    "التربية الترويحية لذوي الاحتياجات الخاصة",
    2,
    2,
    "تربية خاصة",
    program="خاص"
)

add_course(
    "EMS2.16",
    "الأصول العلمية للإعلان",
    2,
    2,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS2.17",
    "نظم سياسية وسياسات الإعلام",
    2,
    2,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS2.18",
    "الرأي العام وطرق قياسه",
    2,
    2,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS2.19",
    "تشريعات الإعلام وأخلاقياته",
    2,
    2,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMS2.20",
    "مسرح الطفل",
    2,
    2,
    "إجباري تخصص",
    program="خاص"
)

add_course(
    "EMSE2.13",
    "صحافة المواطن",
    1,
    2,
    "اختياري تخصص",
    program="خاص"
)

add_course(
    "EMSE2.14",
    "تيارات فكرية وثقافية معاصرة",
    1,
    2,
    "اختياري تخصص",
    program="خاص"
)

add_course(
    "EMSE2.15",
    "الإحصاء والحاسب الآلي",
    1,
    2,
    "اختياري تخصص",
    program="خاص",
    prerequisite="EMS2.15"
)

add_course(
    "EMSE2.16",
    "المذاهب المسرحية",
    1,
    2,
    "اختياري تخصص",
    program="خاص"
)


# ============================================================
# قواعد النظام
# ============================================================

LEVEL_2_THRESHOLD = {
    "عام": 35,
    "خاص": 32
}

TWELVE_HOUR_LIMIT = 12


# ============================================================
# أدوات مساعدة
# ============================================================

def normalize_gpa(gpa):
    try:
        return float(gpa)
    except Exception:
        return 0.0


def course_name(code):
    if code in COURSES:
        return COURSES[code].name
    return code


def course_hours(code):
    if code in COURSES:
        return COURSES[code].hours
    return None


def course_belongs_to_program(course: Course, program: str):
    return (
        course.program == "مشترك"
        or course.program == program
    )


def get_course_list(
    program: str,
    level: Optional[int] = None
):
    result = []

    for code, course in COURSES.items():

        if not course_belongs_to_program(course, program):
            continue

        if level is not None and course.level != level:
            continue

        result.append(code)

    return result


def get_clearance_courses(
    failed_courses: Set[str],
    program: str
):
    clearance = []

    for code in failed_courses:

        if code not in COURSES:
            continue

        course = COURSES[code]

        if course.clearance and course_belongs_to_program(
            course,
            program
        ):
            clearance.append(code)

    return clearance


def get_level2_courses(program: str):

    result = []

    for code, course in COURSES.items():

        if course.level != 2:
            continue

        if not course_belongs_to_program(course, program):
            continue

        result.append(code)

    return result


def get_failed_prerequisites(
    failed_courses: Set[str],
    program: str
):
    """
    يحدد المتطلبات التي رسب فيها الطالب فقط إذا كانت
    مرتبطة فعلًا بمقررات المستوى الثاني الخاصة ببرنامجه.
    """

    prerequisites = set()

    for code in get_level2_courses(program):

        course = COURSES[code]

        if course.prerequisite:
            prerequisites.add(course.prerequisite)

    return failed_courses.intersection(prerequisites)


def has_failed_prerequisite(
    failed_courses: Set[str],
    program: str
):
    return bool(
        get_failed_prerequisites(
            failed_courses,
            program
        )
    )


def get_blocked_level2_courses(
    failed_courses: Set[str],
    program: str
):

    blocked = []

    for code in get_level2_courses(program):

        course = COURSES[code]

        if (
            course.prerequisite
            and course.prerequisite in failed_courses
        ):
            blocked.append(code)

    return blocked


def get_available_level2_courses(
    failed_courses: Set[str],
    program: str
):

    available = []

    for code in get_level2_courses(program):

        course = COURSES[code]

        if (
            course.prerequisite
            and course.prerequisite in failed_courses
        ):
            continue

        available.append(code)

    return available


def get_replacement_courses(
    failed_courses: Set[str],
    program: str
):
    """
    يعرض مقررات المستوى الأول الراسب فيها الطالب
    والتي يمكن أن تدخل في خطة التعامل مع المقررات المغلقة.
    """

    replacements = []

    for code in failed_courses:

        if code not in COURSES:
            continue

        course = COURSES[code]

        if course.level != 1:
            continue

        if not course_belongs_to_program(
            course,
            program
        ):
            continue

        if course.clearance:
            continue

        if course.hours is None:
            continue

        replacements.append(code)

    return replacements


def calculate_regular_hours(
    course_codes: List[str]
):

    total = 0

    for code in course_codes:

        if code not in COURSES:
            continue

        course = COURSES[code]

        if course.clearance:
            continue

        if course.hours is not None:
            total += course.hours

    return total


def calculate_clearance_hours(
    course_codes: List[str]
):

    total = 0

    for code in course_codes:

        if code not in COURSES:
            continue

        course = COURSES[code]

        if not course.clearance:
            continue

        if course.hours is not None:
            total += course.hours

    return total


def format_course(code):

    if code not in COURSES:
        return code

    course = COURSES[code]

    if course.hours is None:
        hours_text = "اجتياز — لا تُحسب كساعات تسجيل"
    else:
        hours_text = f"{course.hours} ساعة"

    return f"{course.name} — {hours_text}"


# ============================================================
# الحالة السادسة
# ============================================================

def determine_case_6(
    failed_courses: Set[str],
    gpa: float,
    all_first_semester_passed: bool,
    program: str
):

    teaching_failed = "EDU1.4" in failed_courses
    curriculum_failed = "EDU1.2" in failed_courses

    program_prerequisites = {
        code for code in [
            "EDU1.1",
            "EM1.2" if program == "عام" else "EMS1.2",
            "EM1.4" if program == "عام" else "EMS1.4"
        ]
        if code in COURSES
    }

    first_level_prereq_failed = bool(
        failed_courses.intersection(
            program_prerequisites
        )
    )

    if not teaching_failed:
        return None

    # 6A
    if (
        gpa >= 1.6
        and all_first_semester_passed
        and failed_courses == {"EDU1.4"}
    ):
        return "6A"

    # 6B
    if (
        gpa >= 1.6
        and first_level_prereq_failed
        and not curriculum_failed
    ):
        return "6B"

    # 6C
    if gpa >= 1.6:
        return "6C"

    return None


# ============================================================
# محرك الحالات الثمانية
# ============================================================

def analyze_student(data):

    gpa = normalize_gpa(data["gpa"])
    program = data["program"]

    failed_courses = set(data["failed_courses"])

    all_first_semester_passed = data[
        "all_first_semester_passed"
    ]

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

    # --------------------------------------------------------
    # مواد الاجتياز
    # --------------------------------------------------------

    result["clearance"] = get_clearance_courses(
        failed_courses,
        program
    )

    result["clearance_hours"] = calculate_clearance_hours(
        result["clearance"]
    )

    # --------------------------------------------------------
    # شرط الانتقال للمستوى الثاني
    # --------------------------------------------------------

    threshold = LEVEL_2_THRESHOLD[program]

    if passed_hours < threshold:

        result["notes"].append(
            f"عدد ساعات النجاح المدخل هو {passed_hours} ساعة، "
            f"بينما الحد المذكور للانتقال للمستوى الثاني في برنامج "
            f"«{program}» هو {threshold} ساعة."
        )

    # --------------------------------------------------------
    # CASE 1
    # --------------------------------------------------------

    if len(failed_courses) == 0 and gpa >= 2.0:

        result["case"] = 1
        result["title"] = "الحالة الأولى"

        result["reason"] = (
            "أنت ناجح في جميع المقررات، والتقدير التراكمي "
            "يساوي 2.00 أو أكثر."
        )

        result["available"] = get_available_level2_courses(
            failed_courses,
            program
        )

        return result

    # --------------------------------------------------------
    # CASE 3
    # --------------------------------------------------------

    if len(failed_courses) == 0 and 1.6 <= gpa < 2.0:

        result["case"] = 3
        result["title"] = "الحالة الثالثة"

        result["reason"] = (
            "أنت ناجح في جميع المقررات، لكن التقدير التراكمي "
            "بين 1.60 وأقل من 2.00."
        )

        result["available"] = get_available_level2_courses(
            failed_courses,
            program
        )

        result["warnings"].append(
            "يجب العمل على رفع التقدير التراكمي إلى 2.00 "
            "وتجنب استمرار انخفاضه."
        )

        return result

    # --------------------------------------------------------
    # CASE 8
    # --------------------------------------------------------

    if program == "عام":

        case8_prerequisites = {
            "EDU1.1",
            "EM1.2",
            "EM1.4",
            "EDU1.4"
        }

    else:

        case8_prerequisites = {
            "EDU1.1",
            "EMS1.2",
            "EMS1.4",
            "EDU1.4"
        }

    all_case8_prerequisites_failed = (
        case8_prerequisites.issubset(
            failed_courses
        )
    )

    if (
        gpa < 1.6
        and all_case8_prerequisites_failed
    ):

        result["case"] = 8
        result["title"] = "الحالة الثامنة"

        result["reason"] = (
            "التقدير التراكمي أقل من 1.60، "
            "ومواد المتطلبات المحددة للحالة الثامنة كلها "
            "ضمن المقررات الراسب فيها."
        )

        result["regular_limit"] = TWELVE_HOUR_LIMIT

        result["blocked"] = get_blocked_level2_courses(
            failed_courses,
            program
        )

        result["available"] = get_available_level2_courses(
            failed_courses,
            program
        )

        result["replacement"] = get_replacement_courses(
            failed_courses,
            program
        )

        result["summer"] = list(failed_courses)

        if "EDU2.7" not in result["blocked"]:
            result["blocked"].append("EDU2.7")

        if "EDU2.7" in result["available"]:
            result["available"].remove("EDU2.7")

        result["warnings"].append(
            "حد التسجيل الأساسي في هذه الحالة هو 12 ساعة."
        )

        result["warnings"].append(
            "الأولوية هي العمل على رفع التقدير التراكمي "
            "وتجنب استمرار انخفاضه."
        )

        result["notes"].append(
            "مواد الاجتياز، مثل اللغة العربية أو الإنجليزية "
            "إذا كانت ضمن مقررات الرسوب، لا تُخصم من حد الـ12 ساعة."
        )

        return result

    # --------------------------------------------------------
    # CASE 7
    # --------------------------------------------------------

    if gpa < 1.6 and len(failed_courses) > 0:

        result["case"] = 7
        result["title"] = "الحالة السابعة"

        result["reason"] = (
            "التقدير التراكمي أقل من 1.60 مع وجود مقررات "
            "راسب فيها، لكن شروط الحالة الثامنة الكاملة "
            "لا تنطبق على البيانات المدخلة."
        )

        result["regular_limit"] = TWELVE_HOUR_LIMIT

        result["available"] = get_available_level2_courses(
            failed_courses,
            program
        )

        result["blocked"] = get_blocked_level2_courses(
            failed_courses,
            program
        )

        result["replacement"] = get_replacement_courses(
            failed_courses,
            program
        )

        result["summer"] = list(failed_courses)

        result["warnings"].append(
            "حد التسجيل الأساسي في هذه الحالة هو 12 ساعة."
        )

        result["warnings"].append(
            "الأولوية هي رفع التقدير التراكمي وتجنب استمرار انخفاضه."
        )

        priority_courses = [
            "EDU2.5",
            "EMS2.15" if program == "خاص" else "EM2.15"
        ]

        result["available"] = sorted(
            result["available"],
            key=lambda x: (
                0 if x in priority_courses else 1,
                x
            )
        )

        result["notes"].append(
            "تكون الأولوية عند بناء خطة التسجيل لـ«علم النفس للنمو» "
            "و«أساسيات الحاسب الآلي»، ثم اختيار مقررات أخرى مناسبة "
            "وفق حالة الطالب."
        )

        return result

    # --------------------------------------------------------
    # CASE 6
    # --------------------------------------------------------

    if "EDU1.4" in failed_courses:

        subcase = determine_case_6(
            failed_courses,
            gpa,
            all_first_semester_passed,
            program
        )

        if subcase is not None:

            result["case"] = 6
            result["subcase"] = subcase
            result["title"] = f"الحالة السادسة — {subcase}"

            if subcase == "6A":

                result["reason"] = (
                    "أنت ناجح في جميع مقررات الفصل الدراسي الأول، "
                    "ولديك رسوب في «طرق تدريس عامة» فقط، "
                    "والتقدير التراكمي 1.60 فأكثر."
                )

                result["available"] = [
                    code
                    for code in get_available_level2_courses(
                        failed_courses,
                        program
                    )
                    if code != "EDU2.7"
                ]

                result["blocked"] = ["EDU2.7"]

                result["warnings"].append(
                    "التدريس المصغر لا يتم تسجيله حاليًا "
                    "لأن «طرق تدريس عامة» لم تُجتز."
                )

                result["notes"].append(
                    "قد يكون عدد الساعات المسجلة أقل من زملائك "
                    "بسبب طبيعة هذه الحالة."
                )

                result["summer"].append("EDU2.7")

            elif subcase == "6B":

                result["reason"] = (
                    "لديك رسوب في «طرق تدريس عامة» بالإضافة إلى "
                    "مقرر أو مقررات من مقررات المستوى الأول "
                    "ذات أثر مباشر على مقررات المستوى الثاني."
                )

                result["blocked"] = get_blocked_level2_courses(
                    failed_courses,
                    program
                )

                if "EDU2.7" not in result["blocked"]:
                    result["blocked"].append("EDU2.7")

                result["available"] = [
                    code
                    for code in get_available_level2_courses(
                        failed_courses,
                        program
                    )
                    if code != "EDU2.7"
                ]

                result["replacement"] = get_replacement_courses(
                    failed_courses,
                    program
                )

                result["summer"] = list(failed_courses)

                if "EDU2.7" not in result["summer"]:
                    result["summer"].append("EDU2.7")

            else:

                result["reason"] = (
                    "لديك رسوب في «طرق تدريس عامة» مع "
                    "«المناهج وتنظيماتها» أو مع مقررات أخرى "
                    "من المستوى الأول، ولذلك تختلف خطة التسجيل."
                )

                result["blocked"] = get_blocked_level2_courses(
                    failed_courses,
                    program
                )

                if "EDU2.7" not in result["blocked"]:
                    result["blocked"].append("EDU2.7")

                result["available"] = [
                    code
                    for code in get_available_level2_courses(
                        failed_courses,
                        program
                    )
                    if code != "EDU2.7"
                ]

                result["replacement"] = get_replacement_courses(
                    failed_courses,
                    program
                )

                result["summer"] = list(failed_courses)

                if "EDU2.7" not in result["summer"]:
                    result["summer"].append("EDU2.7")

            if gpa >= 2.0:
                result["notes"].append(
                    "عند الوصول إلى تقدير تراكمي 2.00 فأكثر، "
                    "يمكن التعامل مع التدريس المصغر وفق خطة الصيف "
                    "والقواعد المطبقة."
                )
            else:
                result["warnings"].append(
                    "الأولوية هي رفع التقدير التراكمي والوصول إلى 2.00."
                )

            return result

    # --------------------------------------------------------
    # CASE 2
    # --------------------------------------------------------

    if (
        len(failed_courses) > 0
        and has_failed_prerequisite(
            failed_courses,
            program
        )
        and gpa >= 2.0
    ):

        result["case"] = 2
        result["title"] = "الحالة الثانية"

        failed_prereqs = get_failed_prerequisites(
            failed_courses,
            program
        )

        prereq_names = "، ".join(
            course_name(code)
            for code in failed_prereqs
        )

        result["reason"] = (
            "لديك مقررات راسب فيها، ومن بينها مواد متطلبات "
            f"غير مجتازة ({prereq_names}) تؤثر على فتح "
            "مقررات أخرى، بينما التقدير التراكمي 2.00 أو أكثر."
        )

        result["blocked"] = get_blocked_level2_courses(
            failed_courses,
            program
        )

        result["available"] = get_available_level2_courses(
            failed_courses,
            program
        )

        result["replacement"] = get_replacement_courses(
            failed_courses,
            program
        )

        result["summer"] = list(failed_courses)

        return result

    # --------------------------------------------------------
    # CASE 4
    # --------------------------------------------------------

    if (
        len(failed_courses) > 0
        and not has_failed_prerequisite(
            failed_courses,
            program
        )
        and gpa >= 1.6
    ):

        result["case"] = 4
        result["title"] = "الحالة الرابعة"

        result["reason"] = (
            "لديك مقررات راسب فيها، لكن هذه المقررات "
            "ليست من المتطلبات التي تمنع فتح مقررات المستوى "
            "الثاني وفق علاقات المتطلبات المدخلة."
        )

        result["available"] = get_available_level2_courses(
            failed_courses,
            program
        )

        result["summer"] = list(failed_courses)

        result["warnings"].append(
            "يجب العمل على رفع التقدير التراكمي إلى 2.00 "
            "والمحافظة عليه."
        )

        return result

    # --------------------------------------------------------
    # CASE 5
    # --------------------------------------------------------

    if (
        len(failed_courses) > 0
        and has_failed_prerequisite(
            failed_courses,
            program
        )
        and 1.6 <= gpa < 2.0
    ):

        result["case"] = 5
        result["title"] = "الحالة الخامسة"

        failed_prereqs = get_failed_prerequisites(
            failed_courses,
            program
        )

        prereq_names = "، ".join(
            course_name(code)
            for code in failed_prereqs
        )

        result["reason"] = (
            "لديك مقررات راسب فيها، ومن بينها مواد متطلبات "
            f"غير مجتازة ({prereq_names})، والتقدير التراكمي "
            "بين 1.60 وأقل من 2.00."
        )

        result["blocked"] = get_blocked_level2_courses(
            failed_courses,
            program
        )

        result["available"] = get_available_level2_courses(
            failed_courses,
            program
        )

        result["replacement"] = get_replacement_courses(
            failed_courses,
            program
        )

        result["summer"] = list(failed_courses)

        result["warnings"].append(
            "هذه الحالة تحتاج إلى رفع التقدير التراكمي "
            "وتجنب استمرار انخفاضه."
        )

        return result

    # --------------------------------------------------------
    # لا توجد حالة مؤكدة
    # --------------------------------------------------------

    result["title"] = "البيانات تحتاج إلى مراجعة"

    result["reason"] = (
        "البيانات التي تم إدخالها لا تكفي لتحديد إحدى الحالات "
        "الثماني بصورة مؤكدة وفق القواعد المدخلة."
    )

    result["warnings"].append(
        "لا تختار حالة بنفسك ولا نعتمد على التخمين."
    )

    result["notes"].append(
        "راجع البيانات المدخلة، وإذا كانت الحالة غير موجودة ضمن "
        "القواعد الحالية، يجب الرجوع إلى المرشد الأكاديمي."
    )

    return result


# ============================================================
# عرض المقررات
# ============================================================

def display_course_list(
    title: str,
    course_codes: List[str],
    style: str = "normal",
    failed_courses: Optional[Set[str]] = None
):

    if not course_codes:
        st.info(
            "لا توجد مقررات في هذه القائمة وفق البيانات المدخلة."
        )
        return

    st.markdown(f"### {title}")

    failed_courses = failed_courses or set()

    for code in course_codes:

        if code not in COURSES:

            st.markdown(
                f"""
                <div class="course-card">
                    <div class="course-name">{code}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            continue

        course = COURSES[code]

        if course.hours is None:
            hours = "اجتياز — لا تُحسب كساعات تسجيل"
        else:
            hours = f"{course.hours} ساعة"

        if style == "blocked":

            icon = "🔒"

            if course.prerequisite:

                prerequisite_text = course_name(
                    course.prerequisite
                )

                if course.prerequisite in failed_courses:

                    extra = (
                        f"مغلق — المتطلب السابق: "
                        f"{prerequisite_text} "
                        f"({course.prerequisite}) غير مجتاز"
                    )

                else:

                    extra = (
                        f"مغلق بسبب المتطلب السابق: "
                        f"{prerequisite_text}"
                    )

            else:

                extra = "مغلق وفق الحالة الدراسية"

        elif style == "replacement":

            icon = "🔄"
            extra = (
                "مقرر مستوى أول ضمن المقررات التي يمكن "
                "إدخالها في خطة المعالجة"
            )

        elif style == "summer":

            icon = "☀️"
            extra = (
                "يمكن وضعه ضمن خطة الصيف وفق قواعد "
                "الصيف والتسجيل الفعلية"
            )

        elif style == "clearance":

            icon = "🟦"
            extra = (
                "مادة اجتياز — لا تستهلك حد الـ12 ساعة"
            )

        else:

            icon = "📘"
            extra = course.category

            if course.prerequisite:

                extra += (
                    f" | المتطلب السابق: "
                    f"{course_name(course.prerequisite)}"
                )

        st.markdown(
            f"""
            <div class="course-card">
                <div class="course-name">
                    {icon} {course.name}
                </div>
                <div class="course-meta">
                    الكود: {course.code}
                    &nbsp; | &nbsp;
                    الساعات: {hours}
                    &nbsp; | &nbsp;
                    {extra}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# واجهة التطبيق
# ============================================================

st.markdown(
    '<div class="main-title">🎓 المرشد الأكاديمي الذكي</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'دفعة 2025/2026 — قسم الإعلام التربوي — نظام الساعات المعتمدة'
    '</div>',
    unsafe_allow_html=True
)


# ------------------------------------------------------------
# خطوات الاستخدام
# ------------------------------------------------------------

st.markdown(
    """
    <div class="step-container">
        <div class="step step-active">1. بياناتك الدراسية</div>
        <div class="step">2. مواد الرسوب</div>
        <div class="step">3. تحليل المتطلبات</div>
        <div class="step">4. نتيجة الحالة</div>
        <div class="step">5. خطة التسجيل</div>
        <div class="step">6. النصيحة</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# مقدمة
# ------------------------------------------------------------

st.markdown("### 💡 قبل ما تبدأ")

st.markdown(
    """
    المرشد لا يطلب منك اختيار رقم الحالة.

    أنت فقط تدخل بياناتك الدراسية ومقررات الرسوب،
    والنظام يحلل البيانات ويحدد الحالة الأقرب وفق القواعد
    المدخلة.
    """
)

st.caption(
    "لو البيانات غير كافية أو الحالة لا يمكن تحديدها بدقة، "
    "سيخبرك النظام بذلك بدلًا من إعطاء نتيجة مبنية على التخمين."
)
# ============================================================
# بيانات الطالب
# ============================================================

st.markdown(
    '<div class="section-title">📝 أولًا: بياناتك الدراسية</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    student_name = st.text_input(
        "اسم الطالب",
        placeholder="اكتب اسمك"
    )

with col2:
    program = st.selectbox(
        "نوع البرنامج",
        ["عام", "خاص"]
    )

with col3:
    gpa = st.number_input(
        "التقدير التراكمي GPA",
        min_value=0.0,
        max_value=4.0,
        value=2.0,
        step=0.01,
        format="%.2f"
    )

col4, col5 = st.columns(2)

with col4:
    passed_hours = st.number_input(
        "عدد ساعات النجاح حتى الآن",
        min_value=0,
        max_value=200,
        value=0,
        step=1
    )

with col5:
    all_first_semester_passed = st.radio(
        "هل اجتزت جميع مقررات الفصل الدراسي الأول؟",
        ["نعم", "لا"],
        horizontal=True
    )

all_first_semester_passed = (
    all_first_semester_passed == "نعم"
)


# ============================================================
# مواد الرسوب
# ============================================================

st.markdown(
    '<div class="section-title">📚 ثانيًا: حدد المقررات التي رسبت فيها</div>',
    unsafe_allow_html=True
)

st.info(
    "اختَر كل مقرر رسبت فيه فعلًا. "
    "النظام هو الذي سيحدد تأثير المتطلبات والحالة الدراسية."
)


available_failed_options = []

for code, course in COURSES.items():

    if not course_belongs_to_program(
        course,
        program
    ):
        continue

    available_failed_options.append(code)


available_failed_options = sorted(
    available_failed_options,
    key=lambda x: (
        COURSES[x].level,
        COURSES[x].name
    )
)


failed_courses = st.multiselect(
    "المقررات الراسب فيها",
    options=available_failed_options,
    format_func=lambda code: (
        f"{COURSES[code].name}"
        + (
            f" — {COURSES[code].hours} ساعة"
            if COURSES[code].hours is not None
            else " — اجتياز"
        )
    )
)


# ------------------------------------------------------------
# تنبيه طرق التدريس
# ------------------------------------------------------------

if "EDU1.4" in failed_courses:

    st.warning(
        "تم تسجيل «طرق تدريس عامة» ضمن مقررات الرسوب، "
        "ولذلك سيقوم النظام بفحص الحالة السادسة تلقائيًا "
        "عند انطباق شروطها."
    )


# ============================================================
# زر التحليل
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

analyze_button = st.button(
    "🔍 تحليل حالتي الدراسية",
    type="primary",
    use_container_width=True
)


# ============================================================
# النتيجة
# ============================================================

if analyze_button:

    data = {
        "name": student_name,
        "program": program,
        "gpa": gpa,
        "passed_hours": passed_hours,
        "failed_courses": failed_courses,
        "all_first_semester_passed": all_first_semester_passed
    }

    result = analyze_student(data)

    st.session_state["analysis_result"] = result
    st.session_state["student_data"] = data


# ============================================================
# عرض النتيجة
# ============================================================

if "analysis_result" in st.session_state:

    result = st.session_state["analysis_result"]
    data = st.session_state["student_data"]

    st.markdown(
        '<div class="section-title">🎯 ثالثًا: نتيجة التحليل</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # معلومات سريعة
    # --------------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-number">{data["gpa"]:.2f}</div>
                <div class="metric-label">التقدير التراكمي</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-number">{data["passed_hours"]}</div>
                <div class="metric-label">ساعات النجاح</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-number">
                    {len(data["failed_courses"])}
                </div>
                <div class="metric-label">مقررات الرسوب</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:

        if result["case"] is None:

            case_display = "—"

        elif result["subcase"]:

            case_display = (
                f'{result["case"]}{result["subcase"]}'
            )

        else:

            case_display = str(result["case"])

        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-number">
                    {case_display}
                </div>
                <div class="metric-label">الحالة</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # بطاقة الحالة
    # --------------------------------------------------------

    if result["case"] is not None:

        # بطاقة الحالة الرئيسية فقط
        st.markdown(
            f"""
            <div class="case-card">
                <div class="case-number">نتيجة التحليل</div>
                <div class="case-title">
                    {result["title"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # تم تحويل صندوق السبب إلى Streamlit مباشرة
        # حتى لا يظهر HTML كنص على الشاشة.
        st.markdown("### 📌 لماذا ظهرت لك هذه الحالة؟")

        st.markdown(
            f"""
            <div class="reason-box">
                {result["reason"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="warning-box">
                <h3>⚠️ لم يتم تحديد الحالة بشكل مؤكد</h3>
                <p>{result["reason"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # شرط الانتقال
    # --------------------------------------------------------

    threshold = LEVEL_2_THRESHOLD[
        data["program"]
    ]

    if data["passed_hours"] >= threshold:

        st.markdown(
            f"""
            <div class="success-box">
                <strong>✅ شرط ساعات الانتقال:</strong>
                لديك {data["passed_hours"]} ساعة نجاح،
                والحد المذكور لبرنامج «{data["program"]}»
                هو {threshold} ساعة.
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="warning-box">
                <strong>⚠️ ملاحظة مهمة بخصوص ساعات النجاح:</strong>
                لديك {data["passed_hours"]} ساعة نجاح،
                بينما الحد المذكور لبرنامج «{data["program"]}»
                هو {threshold} ساعة.
            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # مواد الاجتياز
    # ========================================================

    if result["clearance"]:

        st.markdown(
            '<div class="section-title">🟦 مواد الاجتياز</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="blue-box">
                <strong>مهم جدًا:</strong>
                مواد الاجتياز لا تُحسب ضمن حد التسجيل الأساسي
                البالغ 12 ساعة في الحالات التي ينطبق عليها هذا الحد.
            </div>
            """,
            unsafe_allow_html=True
        )

        display_course_list(
            "المواد التي تدخل ضمن الاجتياز",
            result["clearance"],
            "clearance",
            set(data["failed_courses"])
        )


    # ========================================================
    # الحالات ذات حد 12 ساعة
    # ========================================================

    if result["regular_limit"] is not None:

        st.markdown(
            '<div class="section-title">⏱️ حد التسجيل الأساسي</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="info-card">
                <h3>
                    الحد الأساسي:
                    {TWELVE_HOUR_LIMIT} ساعة
                </h3>

                <p>
                هذا الحد يخص الساعات الأساسية للتسجيل.
                أما مواد الاجتياز فلا تُخصم من هذا الحد.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # المقررات المفتوحة
    # ========================================================

    if result["available"]:

        st.markdown(
            '<div class="section-title">📗 المقررات المتاحة</div>',
            unsafe_allow_html=True
        )

        display_course_list(
            "مقررات يمكن النظر في تسجيلها",
            result["available"],
            "normal",
            set(data["failed_courses"])
        )


    # ========================================================
    # المقررات المغلقة
    # ========================================================

    if result["blocked"]:

        st.markdown(
            '<div class="section-title">🔒 المقررات التي لا يمكن فتحها حاليًا</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="warning-box">
                المقرر هنا مرتبط بمتطلب سابق لم يتم اجتيازه
                وفق البيانات التي أدخلتها.
            </div>
            """,
            unsafe_allow_html=True
        )

        display_course_list(
            "مقررات مغلقة بسبب المتطلبات",
            result["blocked"],
            "blocked",
            set(data["failed_courses"])
        )


    # ========================================================
    # البدائل
    # ========================================================

    if result["replacement"]:

        st.markdown(
            '<div class="section-title">🔄 المقررات البديلة</div>',
            unsafe_allow_html=True
        )

        display_course_list(
            "مقررات المستوى الأول الموجودة ضمن مقررات الرسوب",
            result["replacement"],
            "replacement",
            set(data["failed_courses"])
        )


    # ========================================================
    # خطة الـ12 ساعة
    # ========================================================

    if result["case"] in [7, 8]:

        st.markdown(
            '<div class="section-title">📋 كيف نفهم حد الـ12 ساعة؟</div>',
            unsafe_allow_html=True
        )

        regular_candidates = []

        for code in result["available"]:

            if code not in COURSES:
                continue

            course = COURSES[code]

            if course.clearance:
                continue

            if course.hours is None:
                continue

            regular_candidates.append(code)

        priority = {
            "EDU2.5": 0,
            "EMS2.15" if data["program"] == "خاص" else "EM2.15": 1
        }

        regular_candidates = sorted(
            regular_candidates,
            key=lambda x: (
                priority.get(x, 10),
                x
            )
        )

        selected_for_plan = []
        hours_used = 0

        for code in regular_candidates:

            h = COURSES[code].hours

            if h is None:
                continue

            if hours_used + h <= TWELVE_HOUR_LIMIT:

                selected_for_plan.append(code)
                hours_used += h

        st.markdown(
            f"""
            <div class="info-card">
                <h3>خطة أساسية مقترحة داخل حد الـ12 ساعة</h3>

                <p>
                الساعات الأساسية المستخدمة:
                <strong>
                    {hours_used} / {TWELVE_HOUR_LIMIT}
                </strong>
                </p>

                <p class="small-note">
                هذا الحساب يخص المقررات الأساسية فقط.
                مواد الاجتياز لها معاملة منفصلة.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        display_course_list(
            "المقررات الأساسية المقترحة",
            selected_for_plan,
            "normal",
            set(data["failed_courses"])
        )

        if result["clearance"]:

            st.markdown(
                """
                <div class="success-box">
                    <strong>➕ بالإضافة إلى ذلك:</strong>
                    يمكن إضافة مواد الاجتياز المحددة أعلاه
                    دون اعتبارها جزءًا من حد الـ12 ساعة الأساسي.
                </div>
                """,
                unsafe_allow_html=True
            )


    # ========================================================
    # الصيف
    # ========================================================

    if result["summer"]:

        st.markdown(
            '<div class="section-title">☀️ مقررات يمكن وضعها في خطة الصيف</div>',
            unsafe_allow_html=True
        )

        display_course_list(
            "مقررات الصيف",
            result["summer"],
            "summer",
            set(data["failed_courses"])
        )

        st.markdown(
            """
            <div class="small-note">
            عرض المقرر ضمن خطة الصيف يعني أنه يدخل ضمن الخيارات
            التي تحتاج إلى مراجعة قواعد الصيف والتسجيل الفعلية،
            وليس أن تسجيله مضمون تلقائيًا.
            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # التحذيرات
    # ========================================================

    if result["warnings"]:

        st.markdown(
            '<div class="section-title">⚠️ تنبيهات مهمة</div>',
            unsafe_allow_html=True
        )

        for warning in result["warnings"]:

            st.markdown(
                f"""
                <div class="warning-box">
                    ⚠️ {warning}
                </div>
                """,
                unsafe_allow_html=True
            )


    # ========================================================
    # الملاحظات
    # ========================================================

    if result["notes"]:

        st.markdown(
            '<div class="section-title">💡 ملاحظات المرشد</div>',
            unsafe_allow_html=True
        )

        for note in result["notes"]:

            st.markdown(
                f"""
                <div class="blue-box">
                    💡 {note}
                </div>
                """,
                unsafe_allow_html=True
            )


    # ========================================================
    # قاموس المصطلحات
    # ========================================================

    st.markdown(
        '<div class="section-title">📖 قاموس المصطلحات</div>',
        unsafe_allow_html=True
    )

    glossary = {

        "GPA":
            "التقدير التراكمي للطالب.",

        "الساعات المعتمدة":
            "وحدة تُستخدم لقياس العبء الدراسي للمقرر.",

        "مادة المتطلب":
            "مادة يجب اجتيازها حتى يصبح من الممكن تسجيل "
            "مادة مرتبطة بها.",

        "Prerequisite":
            "المتطلب السابق؛ أي المادة التي يجب اجتيازها "
            "قبل فتح المادة المرتبطة بها.",

        "مواد الاجتياز":
            "مواد يمكن التعامل معها كمواد اجتياز ولا تدخل "
            "ضمن حد الـ12 ساعة الأساسي في الحالات التي "
            "ينطبق عليها ذلك.",

        "المستوى":
            "المستوى الدراسي داخل نظام الساعات المعتمدة، "
            "وليس بالضرورة سنة دراسية كاملة."
    }

    # ========================================================
    # تم تعديل عرض المصطلحات ليكون Native Streamlit
    # بدل HTML حتى لا يظهر الكود للمستخدم.
    # ========================================================

    for term, explanation in glossary.items():

        st.markdown(f"**{term}**")
        st.markdown(explanation)
        st.divider()


    # ========================================================
    # تنبيه ختامي
    # ========================================================

    # تم تغيير طريقة العرض إلى Streamlit مباشرة
    # حتى لا يظهر HTML كنص.

    st.error(
        """
        **📌 تنبيه نهائي:**

        هذا المرشد مبني على قواعد وبيانات النظام التي تم
        إدخالها في التطبيق. النتيجة تساعدك على فهم موقفك
        الدراسي وتكوين تصور عن التسجيل، لكنها لا تُغني
        عن مراجعة المرشد الأكاديمي أو شؤون الطلاب عند وجود
        استثناء، تعديل في اللائحة، أو حالة غير مذكورة
        في القواعد.
        """
    )

# ============================================================
# إذا لم يتم الضغط على التحليل
# ============================================================

else:

    st.markdown("### 🚀 ابدأ من هنا")

    st.markdown(
        """
        أدخل التقدير التراكمي، وساعات النجاح، ونوع البرنامج،
        ثم حدد المقررات التي رسبت فيها.

        بعد ذلك اضغط على:
        **«تحليل حالتي الدراسية»**
        """
    )

    st.caption(
        "لا تحتاج إلى معرفة رقم الحالة مسبقًا. "
        "النظام يحاول تحديدها من بياناتك."
    )

# ============================================================
# Footer
# ============================================================

st.markdown(
    """
    <hr>

    <div style="
        text-align:center;
        color:#94a3b8;
        font-size:13px;
        line-height:2;
    ">
        🎓 المرشد الأكاديمي الذكي<br>
        دفعة 2025/2026 — قسم الإعلام التربوي<br>
        نظام الساعات المعتمدة
    </div>
    """,
    unsafe_allow_html=True
)
