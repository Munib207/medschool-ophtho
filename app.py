import streamlit as st
import random
from datetime import datetime

# ===== MEDICAL SCHOOL OPHTHALMOLOGY CURRICULUM =====
st.set_page_config(
    page_title="MedSchool Ophtho - Interactive Curriculum",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== CURRICULUM STRUCTURE =====
CURRICULUM_MODULES = {
    "ms1_foundations": {
        "name": "MS1: Ophthalmic Foundations",
        "icon": "🔬",
        "color": "#4CAF50",
        "description": "Basic anatomy, physiology, and examination skills",
        "prerequisites": [],
        "learning_objectives": [
            "Understand basic eye anatomy and physiology",
            "Perform fundamental eye examination",
            "Recognize normal vs. abnormal findings"
        ]
    },
    "ms2_pathologies": {
        "name": "MS2: Core Pathologies", 
        "icon": "📚",
        "color": "#2196F3",
        "description": "High-yield conditions for Step 1 preparation",
        "prerequisites": ["ms1_foundations"],
        "learning_objectives": [
            "Identify common ophthalmic conditions",
            "Understand pathophysiology of key diseases",
            "Develop differential diagnosis skills"
        ]
    },
    "ms3_clerkship": {
        "name": "MS3: Clinical Clerkship",
        "icon": "🏥", 
        "color": "#FF9800",
        "description": "Clinical cases for rotation readiness",
        "prerequisites": ["ms2_pathologies"],
        "learning_objectives": [
            "Manage common clinical presentations",
            "Develop patient assessment skills",
            "Formulate evidence-based management plans"
        ]
    },
    "ms4_advanced": {
        "name": "MS4: Advanced Care",
        "icon": "🚨",
        "color": "#F44336",
        "description": "Complex cases for internship preparation", 
        "prerequisites": ["ms3_clerkship"],
        "learning_objectives": [
            "Manage ophthalmic emergencies",
            "Coordinate multidisciplinary care",
            "Prepare for residency decision-making"
        ]
    },
    "boards_prep": {
        "name": "Boards Preparation",
        "icon": "🎯",
        "color": "#9C27B0",
        "description": "Integrated practice for USMLE/board examinations",
        "prerequisites": ["ms4_advanced"],
        "learning_objectives": [
            "Apply knowledge in exam-style questions",
            "Develop test-taking strategies", 
            "Integrate knowledge across specialties"
        ]
    }
}

# ===== MEDICAL SCHOOL CONTENT DATABASE =====
MEDICAL_CASES = {
    # MS1 Foundations
    "Eye Anatomy Basics": {
        "module": "ms1_foundations",
        "case_type": "conceptual",
        "question": "Which cranial nerve is responsible for eye adduction?",
        "options": ["CN II", "CN III", "CN IV", "CN VI"],
        "correct_answer": "CN III",
        "explanation": "Cranial Nerve III (oculomotor) controls adduction, elevation, and depression of the eye.",
        "learning_points": [
            "CN III: adduction, elevation, depression",
            "CN IV: intorsion", 
            "CN VI: abduction"
        ]
    },
    
    "Visual Acuity Assessment": {
        "module": "ms1_foundations", 
        "case_type": "clinical",
        "question": "A patient reads 20/40 on the Snellen chart. What does this mean?",
        "options": [
            "Patient sees at 20 feet what normal person sees at 40 feet",
            "Patient sees at 40 feet what normal person sees at 20 feet", 
            "Patient has 40% visual acuity",
            "Patient requires 40% magnification"
        ],
        "correct_answer": "Patient sees at 20 feet what normal person sees at 40 feet",
        "explanation": "20/40 means the patient must be at 20 feet to see what a person with normal vision can see at 40 feet.",
        "learning_points": [
            "20/20 is normal visual acuity",
            "First number: testing distance",
            "Second number: comparison to normal vision"
        ]
    },

    # MS2 Pathologies
    "Red Eye Differential": {
        "module": "ms2_pathologies",
        "case_type": "clinical",
        "question": "A patient presents with acute red eye, photophobia, and blurred vision. Pupil is constricted. What is the most likely diagnosis?",
        "options": [
            "Conjunctivitis",
            "Acute angle closure glaucoma", 
            "Anterior uveitis",
            "Subconjunctival hemorrhage"
        ],
        "correct_answer": "Anterior uveitis",
        "explanation": "Photophobia + blurred vision + constricted pupil suggests anterior uveitis. Conjunctivitis typically has discharge without vision changes.",
        "learning_points": [
            "Uveitis: pain, photophobia, vision loss",
            "Conjunctivitis: discharge, itching, minimal pain",
            "Angle closure: severe pain, nausea, fixed pupil"
        ]
    },

    # MS3 Clerkship
    "Diabetic Retinopathy": {
        "module": "ms3_clerkship",
        "case_type": "management",
        "question": "A diabetic patient with NPDR shows CSME on exam. What is the first-line treatment?",
        "options": [
            "Pan-retinal photocoagulation",
            "Anti-VEGF injections", 
            "Focal laser photocoagulation",
            "Observation with tight glycemic control"
        ],
        "correct_answer": "Anti-VEGF injections",
        "explanation": "For center-involving diabetic macular edema, anti-VEGF is first-line. Focal laser is for non-center involving edema.",
        "learning_points": [
            "CSME = clinically significant macular edema",
            "Anti-VEGF first line for center-involving DME",
            "Laser for non-center involving or non-responsive cases"
        ]
    }
}

# ===== INITIALIZE SESSION STATE =====
if "student_progress" not in st.session_state:
    st.session_state.student_progress = {}

if "current_module" not in st.session_state:
    st.session_state.current_module = "ms1_foundations"

if "current_case" not in st.session_state:
    st.session_state.current_case = None

# ===== MAIN APPLICATION =====
def main():
    # Header
    st.markdown("""
    <div style="text-align: center; background: linear-gradient(135deg, #1A237E, #1565C0); color: white; padding: 3rem; border-radius: 15px; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0; font-size: 3rem;">🎓 MedSchool Ophtho</h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.4rem;">Interactive Ophthalmology Curriculum</p>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.1rem; opacity: 0.9;">Medical Student Education Platform</p>
    </div>
    """, unsafe_allow_html=True)

    # Student Registration
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 👨‍🎓 Student Login")
        student_id = st.text_input("Enter Student ID:", placeholder="MS2024001")
        
        if student_id:
            initialize_student_progress(student_id)
            display_student_dashboard(student_id)
    
    with col2:
        st.markdown("### 🏫 Curriculum Overview")
        display_curriculum_progress(student_id if student_id else None)

    # Main Content Area
    if student_id:
        display_learning_interface(student_id)
    else:
        display_welcome_message()

# ===== APPLICATION FUNCTIONS =====
def initialize_student_progress(student_id):
    if student_id not in st.session_state.student_progress:
        st.session_state.student_progress[student_id] = {
            "current_module": "ms1_foundations",
            "modules_completed": [],
            "cases_completed": 0,
            "correct_answers": 0,
            "module_progress": {
                module: {"completed": False, "cases_attempted": 0, "correct": 0}
                for module in CURRICULUM_MODULES
            },
            "registration_date": datetime.now().strftime("%Y-%m-%d"),
            "last_active": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

def display_student_dashboard(student_id):
    student_data = st.session_state.student_progress[student_id]
    
    st.success(f"**Welcome, Medical Student {student_id}!**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        completed = len([m for m in student_data["module_progress"] if student_data["module_progress"][m]["completed"]])
        st.metric("Modules Completed", f"{completed}/{len(CURRICULUM_MODULES)}")
    
    with col2:
        st.metric("Cases Attempted", student_data["cases_completed"])
    
    with col3:
        accuracy = (student_data["correct_answers"] / student_data["cases_completed"] * 100) if student_data["cases_completed"] > 0 else 0
        st.metric("Overall Accuracy", f"{accuracy:.1f}%")

def display_curriculum_progress(student_id):
    for module_id, module_info in CURRICULUM_MODULES.items():
        # Check if module is available
        if student_id:
            student_data = st.session_state.student_progress[student_id]
            prerequisites_met = all(p in student_data["modules_completed"] for p in module_info["prerequisites"])
            module_available = prerequisites_met or module_id == student_data["current_module"]
        else:
            module_available = module_id == "ms1_foundations"
        
        # Display module card
        with st.container():
            st.markdown(f"""
            <div style="background: {module_info['color']}15; padding: 1rem; border-radius: 10px; border-left: 4px solid {module_info['color']}; margin: 0.5rem 0;">
                <h4 style="color: {module_info['color']}; margin: 0;">{module_info['icon']} {module_info['name']}</h4>
                <p style="margin: 0.5rem 0 0 0; color: #666; font-size: 0.9rem;">{module_info['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if not module_available:
                st.caption("🔒 Complete prerequisites to unlock")

def display_welcome_message():
    st.markdown("""
    ## 🎯 Welcome to MedSchool Ophtho!
    
    **Your dedicated ophthalmology learning platform designed specifically for medical students.**
    
    ### 📚 Curriculum Pathway:
    
    **MS1 Foundations** → **MS2 Pathologies** → **MS3 Clerkship** → **MS4 Advanced** → **Boards Prep**
    
    ### 🎓 Educational Features:
    
    - **Structured learning** following medical school curriculum
    - **Progressive difficulty** matching your training level
    - **Clinical cases** with immediate feedback
    - **Learning objectives** aligned with competencies
    - **Progress tracking** and achievement system
    
    ### 🚀 Get Started:
    
    1. **Enter your Student ID** in the sidebar
    2. **Begin with MS1 Foundations** 
    3. **Progress through curriculum** as you master each level
    4. **Prepare for boards** with integrated practice cases
    
    *Designed by medical educators for optimal learning progression.*
    """)

def display_learning_interface(student_id):
    student_data = st.session_state.student_progress[student_id]
    current_module_id = student_data["current_module"]
    current_module = CURRICULUM_MODULES[current_module_id]
    
    # Module Header
    st.markdown(f"""
    <div style="background: {current_module['color']}20; padding: 2rem; border-radius: 15px; border-left: 6px solid {current_module['color']}; margin: 1rem 0;">
        <h2 style="color: {current_module['color']}; margin: 0;">{current_module['icon']} {current_module['name']}</h2>
        <p style="margin: 0.5rem 0 0 0; color: #666;">{current_module['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Learning Objectives
    with st.expander("📖 Learning Objectives"):
        for i, objective in enumerate(current_module["learning_objectives"], 1):
            st.write(f"{i}. {objective}")
    
    # Case Interface
    st.markdown("### 💡 Interactive Cases")
    
    if st.button("🎯 Generate New Case", type="primary", use_container_width=True):
        generate_new_case(current_module_id)
    
    if st.session_state.current_case:
        display_current_case(student_id)

def generate_new_case(module_id):
    module_cases = [case for case_id, case in MEDICAL_CASES.items() if case["module"] == module_id]
    if module_cases:
        st.session_state.current_case = random.choice(module_cases)

def display_current_case(student_id):
    case = st.session_state.current_case
    student_data = st.session_state.student_progress[student_id]
    
    st.markdown("#### 📋 Clinical Scenario")
    st.info(f"**{case['question']}**")
    
    selected_option = st.radio("Select your answer:", case["options"])
    
    if st.button("📝 Submit Answer", type="secondary", use_container_width=True):
        # Update progress
        student_data["cases_completed"] += 1
        student_data["module_progress"][case["module"]]["cases_attempted"] += 1
        
        if selected_option == case["correct_answer"]:
            student_data["correct_answers"] += 1
            student_data["module_progress"][case["module"]]["correct"] += 1
            st.success("### ✅ Correct!")
        else:
            st.error(f"### ❌ Correct answer: **{case['correct_answer']}**")
        
        # Show explanation
        st.markdown("---")
        st.markdown("#### 📚 Explanation")
        st.write(case["explanation"])
        
        st.markdown("#### 🎓 Key Learning Points")
        for point in case["learning_points"]:
            st.write(f"• {point}")

# Run the application
if __name__ == "__main__":
    main()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p><strong>MedSchool Ophtho</strong> - Interactive Ophthalmology Curriculum for Medical Students</p>
    <p><small>MS1 Foundations → MS2 Pathologies → MS3 Clerkship → MS4 Advanced → Boards Preparation</small></p>
</div>
""", unsafe_allow_html=True)
