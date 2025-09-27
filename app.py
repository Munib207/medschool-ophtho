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

# ===== COMPREHENSIVE CURRICULUM STRUCTURE =====
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
            "Recognize normal vs. abnormal findings",
            "Learn visual pathway anatomy",
            "Master pupillary examination techniques"
        ],
        "estimated_duration": "10-15 hours",
        "key_topics": ["Eye Anatomy", "Visual Acuity", "Pupil Exam", "Visual Fields", "Color Vision"]
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
            "Develop differential diagnosis skills",
            "Learn treatment principles",
            "Recognize ophthalmologic emergencies"
        ],
        "estimated_duration": "15-20 hours",
        "key_topics": ["Red Eye", "Cataracts", "Glaucoma", "Retinal Diseases", "Neuro-ophthalmology"]
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
            "Formulate evidence-based management plans",
            "Perform focused ophthalmic history",
            "Interpret basic ophthalmic findings"
        ],
        "estimated_duration": "20-25 hours",
        "key_topics": ["Clinical Reasoning", "Patient Workup", "Treatment Plans", "Surgical Indications", "Follow-up Care"]
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
            "Prepare for residency decision-making",
            "Handle complex diagnostic dilemmas",
            "Lead patient education efforts"
        ],
        "estimated_duration": "15-20 hours",
        "key_topics": ["Ophthalmic Emergencies", "Complex Cases", "Multi-system Disease", "Surgical Decisions", "Transition to Residency"]
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
            "Integrate knowledge across specialties", 
            "Manage testing time effectively",
            "Review high-yield content efficiently"
        ],
        "estimated_duration": "25-30 hours",
        "key_topics": ["Integrated Cases", "Step 2 CK Style", "Clinical Vignettes", "Rapid Recall", "Test Strategies"]
    }
}

# ===== COMPREHENSIVE MEDICAL SCHOOL CONTENT DATABASE =====
MEDICAL_CASES = {
    # ===== MS1 FOUNDATIONS =====
    "Eye Anatomy - Cranial Nerves": {
        "module": "ms1_foundations",
        "case_type": "basic_science",
        "question": "A patient presents with inability to adduct the eye. Which cranial nerve is most likely affected?",
        "options": ["Optic Nerve (CN II)", "Oculomotor Nerve (CN III)", "Trochlear Nerve (CN IV)", "Abducens Nerve (CN VI)"],
        "correct_answer": "Oculomotor Nerve (CN III)",
        "explanation": "CN III (oculomotor nerve) controls adduction, elevation, and depression of the eye. Damage results in impaired adduction and other eye movements.",
        "learning_points": [
            "CN III: adduction, elevation, depression",
            "CN IV: intorsion (superior oblique)",
            "CN VI: abduction (lateral rectus)",
            "Remember: LR6SO4 - Lateral Rectus CN6, Superior Oblique CN4"
        ],
        "difficulty": "basic",
        "usmle_relevance": "High - Step 1"
    },

    "Visual Acuity Interpretation": {
        "module": "ms1_foundations", 
        "case_type": "clinical_basics",
        "question": "A patient has visual acuity of 20/200 in the right eye. What does this mean clinically?",
        "options": [
            "Patient sees at 20 feet what normal person sees at 200 feet",
            "Patient has 200% better vision than normal",
            "Patient requires 200% magnification to see normally",
            "Patient sees at 200 feet what normal person sees at 20 feet"
        ],
        "correct_answer": "Patient sees at 20 feet what normal person sees at 200 feet",
        "explanation": "20/200 means the patient must be at 20 feet to see what a person with normal vision can see at 200 feet. This is the threshold for legal blindness.",
        "learning_points": [
            "20/20 is normal visual acuity",
            "First number: testing distance (always 20 feet in US)",
            "Second number: comparison distance for normal vision",
            "20/200 or worse = legal blindness"
        ],
        "difficulty": "basic",
        "usmle_relevance": "High - Step 1"
    },

    "Pupillary Examination": {
        "module": "ms1_foundations",
        "case_type": "clinical_skills", 
        "question": "During pupillary examination, you note that when light is shone in the right eye, both pupils constrict. When light is moved to the left eye, the right pupil dilates. This indicates:",
        "options": [
            "Normal pupillary response",
            "Afferent pupillary defect in the right eye",
            "Efferent pupillary defect in the right eye", 
            "Horner's syndrome"
        ],
        "correct_answer": "Afferent pupillary defect in the right eye",
        "explanation": "This is a Marcus Gunn pupil or relative afferent pupillary defect (RAPD). It indicates asymmetric optic nerve function, with the affected eye (right) having decreased afferent input.",
        "learning_points": [
            "RAPD indicates optic nerve or severe retinal disease",
            "Swinging flashlight test detects RAPD",
            "Afferent defect: impaired sensory input",
            "Efferent defect: impaired motor output"
        ],
        "difficulty": "intermediate", 
        "usmle_relevance": "High - Step 2 CK"
    },

    # ===== MS2 PATHOLOGIES =====
    "Red Eye Differential": {
        "module": "ms2_pathologies",
        "case_type": "clinical_diagnosis",
        "question": "A 25-year-old contact lens wearer presents with acute red eye, severe pain, photophobia, and purulent discharge. Vision is 20/100. What is the most likely diagnosis?",
        "options": [
            "Viral conjunctivitis",
            "Bacterial corneal ulcer",
            "Allergic conjunctivitis", 
            "Subconjunctival hemorrhage"
        ],
        "correct_answer": "Bacterial corneal ulcer",
        "explanation": "Contact lens wear + severe pain + purulent discharge + vision loss = high suspicion for bacterial corneal ulcer. This is an ophthalmologic emergency.",
        "learning_points": [
            "Corneal ulcers: pain, vision loss, discharge",
            "Contact lens wear major risk factor",
            "Requires immediate ophthalmology referral",
            "Never patch an infected corneal ulcer"
        ],
        "difficulty": "intermediate",
        "usmle_relevance": "High - Step 1 and Step 2 CK"
    },

    "Cataract Types": {
        "module": "ms2_pathologies",
        "case_type": "pathology",
        "question": "A 45-year-old diabetic patient presents with gradual vision loss and 'seeing halos around lights'. Slit lamp examination reveals snowflake-like opacities in the posterior cortex. What type of cataract is this?",
        "options": [
            "Nuclear sclerotic cataract",
            "Cortical cataract", 
            "Posterior subcapsular cataract",
            "Congenital cataract"
        ],
        "correct_answer": "Posterior subcapsular cataract",
        "explanation": "Posterior subcapsular cataracts are associated with diabetes, steroids, and trauma. They cause significant glare and visual impairment even when small.",
        "learning_points": [
            "Posterior subcapsular: diabetics, steroid use",
            "Nuclear sclerotic: aging process",
            "Cortical: spoke-like opacities",
            "Diabetics get cataracts 10-15 years earlier"
        ],
        "difficulty": "intermediate",
        "usmle_relevance": "High - Step 1"
    },

    "Glaucoma Diagnosis": {
        "module": "ms2_pathologies", 
        "case_type": "diagnostic_reasoning",
        "question": "A 60-year-old African American male with hypertension presents for routine physical. He has no visual complaints. Examination shows cup-to-disc ratio of 0.8 in both eyes with normal IOP. What is the most appropriate next step?",
        "options": [
            "Reassure and annual follow-up",
            "Refer to ophthalmology for visual field testing",
            "Start timolol eye drops",
            "Order MRI brain"
        ],
        "correct_answer": "Refer to ophthalmology for visual field testing",
        "explanation": "Large cup-to-disc ratio (>0.5) especially in high-risk patients (African American, hypertension) requires evaluation for normal tension glaucoma despite normal IOP.",
        "learning_points": [
            "Normal tension glaucoma: optic nerve damage with normal IOP",
            "African Americans have 4-5x higher glaucoma risk",
            "Cup-to-disc ratio >0.5 requires evaluation",
            "Visual fields essential for diagnosis"
        ],
        "difficulty": "advanced",
        "usmle_relevance": "High - Step 2 CK"
    },

    # ===== MS3 CLERKSHIP =====
    "Retinal Detachment": {
        "module": "ms3_clerkship",
        "case_type": "emergency_management",
        "question": "A 65-year-old highly myopic male presents with sudden onset of floaters, flashing lights, and a 'curtain' coming down over his vision. What is the most appropriate immediate action?",
        "options": [
            "Schedule ophthalmology appointment in 1 week",
            "Prescribe steroid eye drops",
            "Urgent referral to ophthalmology within 24 hours",
            "Order routine fundus photography"
        ],
        "correct_answer": "Urgent referral to ophthalmology within 24 hours",
        "explanation": "Classic symptoms of retinal detachment (floaters, flashes, curtain vision) require urgent ophthalmology evaluation. Time is vision - delays can lead to permanent vision loss.",
        "learning_points": [
            "Retinal detachment symptoms: floaters, flashes, curtain vision",
            "Myopia is major risk factor",
            "Treatment within 24-48 hours improves outcomes",
            "Surgical emergency requiring vitreoretinal specialist"
        ],
        "difficulty": "advanced",
        "usmle_relevance": "High - Step 2 CK"
    },

    "Diabetic Retinopathy Management": {
        "module": "ms3_clerkship",
        "case_type": "management_decision",
        "question": "A 55-year-old diabetic with non-proliferative diabetic retinopathy now shows clinically significant macular edema on examination. What is the first-line treatment?",
        "options": [
            "Pan-retinal photocoagulation",
            "Anti-VEGF intravitreal injections",
            "Focal laser photocoagulation",
            "Tight glycemic control alone"
        ],
        "correct_answer": "Anti-VEGF intravitreal injections",
        "explanation": "For center-involving diabetic macular edema, anti-VEGF injections (bevacizumab, ranibizumab) are first-line treatment. Laser is reserved for non-center involving edema.",
        "learning_points": [
            "Anti-VEGF first line for center-involving DME",
            "Laser for non-center involving macular edema",
            "Pan-retinal photocoagulation for proliferative DR",
            "CSME = clinically significant macular edema"
        ],
        "difficulty": "advanced",
        "usmle_relevance": "High - Step 2 CK"
    },

    # ===== MS4 ADVANCED =====
    "CRAO Management": {
        "module": "ms4_advanced",
        "case_type": "emergency_response",
        "question": "A 70-year-old with atrial fibrillation presents with sudden, painless loss of vision in one eye. Examination shows afferent pupillary defect and cherry red spot. What is the most urgent intervention?",
        "options": [
            "Immediate anterior chamber paracentesis",
            "Cardiology consultation for anticoagulation",
            "Ocular massage and timolol drops",
            "Emergent stroke evaluation and imaging"
        ],
        "correct_answer": "Emergent stroke evaluation and imaging",
        "explanation": "Central retinal artery occlusion (CRAO) is an ophthalmologic emergency and a stroke equivalent. Requires immediate stroke workup and possible thrombolysis within 4.5 hours.",
        "learning_points": [
            "CRAO: stroke equivalent, requires emergent evaluation",
            "Cherry red spot pathognomonic",
            "Time is vision: 4-6 hour window for intervention",
            "Often indicates carotid or cardiac emboli"
        ],
        "difficulty": "expert",
        "usmle_relevance": "High - Step 2 CK and Step 3"
    },

    "Angle Closure Glaucoma": {
        "module": "ms4_advanced", 
        "case_type": "critical_management",
        "question": "A 60-year-old female presents with severe eye pain, headache, nausea, vomiting, and blurred vision with halos. Eye is red and pupil is mid-dilated and non-reactive. IOP measures 55 mmHg. What is the most appropriate immediate treatment?",
        "options": [
            "Oral acetazolamide and topical medications",
            "Emergent laser iridotomy",
            "Observation with pain control",
            "Systemic steroids"
        ],
        "correct_answer": "Oral acetazolamide and topical medications",
        "explanation": "Acute angle closure glaucoma requires immediate IOP reduction with medical therapy (acetazolamide + topical agents) before definitive laser iridotomy.",
        "learning_points": [
            "Medical therapy first to lower IOP",
            "Then laser iridotomy for definitive treatment",
            "Symptoms: pain, nausea, halos, vision loss",
            "Pupil often mid-dilated and fixed"
        ],
        "difficulty": "expert",
        "usmle_relevance": "High - Step 2 CK and Step 3"
    },

    # ===== BOARDS PREP =====
    "Integrated Case - Elderly Female": {
        "module": "boards_prep",
        "case_type": "integrated_clinical",
        "question": "A 75-year-old female with hypertension and diabetes presents with gradual central vision loss over 6 months. She has difficulty reading and recognizing faces. Fundus exam shows drusen and geographic atrophy. What is the most likely diagnosis?",
        "options": [
            "Diabetic macular edema",
            "Dry age-related macular degeneration", 
            "Wet age-related macular degeneration",
            "Macular hole"
        ],
        "correct_answer": "Dry age-related macular degeneration",
        "explanation": "Gradual central vision loss + drusen + geographic atrophy = dry AMD. Wet AMD presents with rapid vision loss and subretinal fluid/hemorrhage.",
        "learning_points": [
            "Dry AMD: gradual loss, drusen, geographic atrophy",
            "Wet AMD: rapid loss, subretinal fluid, hemorrhage",
            "AREDS2 supplements may slow dry AMD progression",
            "Anti-VEGF for wet AMD"
        ],
        "difficulty": "expert",
        "usmle_relevance": "High - Step 2 CK and Step 3"
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
                module: {"completed": False, "cases_attempted": 0, "correct": 0, "started": False}
                for module in CURRICULUM_MODULES
            },
            "registration_date": datetime.now().strftime("%Y-%m-%d"),
            "last_active": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "achievements": []
        }

def display_student_dashboard(student_id):
    student_data = st.session_state.student_progress[student_id]
    
    st.success(f"**Welcome, Medical Student {student_id}!**")
    
    # Progress metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        completed = len([m for m in student_data["module_progress"] if student_data["module_progress"][m]["completed"]])
        st.metric("Modules Completed", f"{completed}/{len(CURRICULUM_MODULES)}")
    
    with col2:
        st.metric("Cases Attempted", student_data["cases_completed"])
    
    with col3:
        accuracy = (student_data["correct_answers"] / student_data["cases_completed"] * 100) if student_data["cases_completed"] > 0 else 0
        st.metric("Overall Accuracy", f"{accuracy:.1f}%")
    
    # Current module progress
    current_module = student_data["current_module"]
    module_data = student_data["module_progress"][current_module]
    if module_data["cases_attempted"] > 0:
        module_accuracy = (module_data["correct"] / module_data["cases_attempted"] * 100)
        st.write(f"**Current Module Progress:** {module_data['cases_attempted']} cases | **Accuracy:** {module_accuracy:.1f}%")
        st.progress(min(module_data["cases_attempted"] / 10, 1.0))

def display_curriculum_progress(student_id):
    st.markdown("#### 📚 Medical School Curriculum Pathway")
    
    for module_id, module_info in CURRICULUM_MODULES.items():
        # Check if module is available
        if student_id:
            student_data = st.session_state.student_progress[student_id]
            prerequisites_met = all(p in student_data["modules_completed"] for p in module_info["prerequisites"])
            module_available = prerequisites_met or module_id == student_data["current_module"]
            module_started = student_data["module_progress"][module_id]["started"]
        else:
            module_available = module_id == "ms1_foundations"
            module_started = False
        
        # Display module card
        with st.container():
            status_icon = "✅" if student_id and student_data["module_progress"][module_id]["completed"] else "🟡" if module_started else "🔵" if module_available else "🔒"
            
            st.markdown(f"""
            <div style="background: {module_info['color']}15; padding: 1.5rem; border-radius: 10px; border-left: 4px solid {module_info['color']}; margin: 1rem 0;">
                <h4 style="color: {module_info['color']}; margin: 0;">{status_icon} {module_info['icon']} {module_info['name']}</h4>
                <p style="margin: 0.5rem 0 0 0; color: #666;">{module_info['description']}</p>
                <p style="margin: 0.3rem 0 0 0; font-size: 0.9rem; color: #888;">Duration: {module_info['estimated_duration']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if module_available and student_id:
                if st.button(f"Study {module_info['name']}", key=f"btn_{module_id}", use_container_width=True):
                    st.session_state.student_progress[student_id]["current_module"] = module_id
                    st.session_state.student_progress[student_id]["module_progress"][module_id]["started"] = True
                    st.rerun()
            
            if not module_available:
                st.caption("🔒 Complete prerequisites to unlock")

def display_welcome_message():
    st.markdown("""
    ## 🎯 Welcome to MedSchool Ophtho!
    
    **Your dedicated ophthalmology learning platform designed specifically for medical students.**
    
    ### 📚 Medical School Curriculum Pathway:
    
    **MS1 Foundations** → **MS2 Pathologies** → **MS3 Clerkship** → **MS4 Advanced** → **Boards Prep**
    
    ### 🎓 Educational Features:
    
    - **Structured learning** following medical school curriculum
    - **Progressive difficulty** matching your training level  
    - **Clinical cases** with immediate feedback
    - **USMLE-aligned content** for Step 1, Step 2 CK preparation
    - **Progress tracking** and achievement system
    
    ### 📖 Curriculum Details:
    
    **MS1 Foundations:** Basic sciences, anatomy, examination skills  
    **MS2 Pathologies:** High-yield conditions for Step 1  
    **MS3 Clerkship:** Clinical cases for rotation readiness  
    **MS4 Advanced:** Complex cases for internship preparation  
    **Boards Prep:** Integrated practice for USMLE examinations
    
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
        <p style="margin: 0.3rem 0 0 0; color: #888; font-size: 0.9rem;">Estimated Duration: {current_module['estimated_duration']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Learning Objectives and Key Topics
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("📖 Learning Objectives", expanded=True):
            for i, objective in enumerate(current_module["learning_objectives"], 1):
                st.write(f"{i}. {objective}")
    
    with col2:
        with st.expander("🎯 Key Topics", expanded=True):
            for topic in current_module["key_topics"]:
                st.write(f"• {topic}")
    
    # Case Interface
    st.markdown("### 💡 Interactive Clinical Cases")
    
    if st.button("🎯 Generate New Case", type="primary", use_container_width=True):
        generate_new_case(current_module_id)
    
    if st.session_state.current_case:
        display_current_case(student_id)

def generate_new_case(module_id):
    module_cases = [case for case_id, case in MEDICAL_CASES.items() if case["module"] == module_id]
    if module_cases:
        st.session_state.current_case = random.choice(module_cases)
        st.session_state.current_case_id = list(MEDICAL_CASES.keys())[list(MEDICAL_CASES.values()).index(st.session_state.current_case)]

def display_current_case(student_id):
    case = st.session_state.current_case
    student_data = st.session_state.student_progress[student_id]
    
    st.markdown("#### 📋 Clinical Scenario")
    
    # Case difficulty indicator
    difficulty_colors = {"basic": "🟢", "intermediate": "🟡", "advanced": "🟠", "expert": "🔴"}
    st.write(f"**Difficulty:** {difficulty_colors[case['difficulty']]} {case['difficulty'].title()} | **USMLE Relevance:** {case['usmle_relevance']}")
    
    st.info(f"**{case['question']}**")
    
    selected_option = st.radio("Select your answer:", case["options"], key="case_options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📝 Submit Answer", type="secondary", use_container_width=True):
            process_answer(student_id, case, selected_option)
    
    with col2:
        if st.button("🔄 New Case", use_container_width=True):
            generate_new_case(student_data["current_module"])
            st.rerun()

def process_answer(student_id, case, selected_option):
    student_data = st.session_state.student_progress[student_id]
    
    # Update progress
    student_data["cases_completed"] += 1
    student_data["module_progress"][case["module"]]["cases_attempted"] += 1
    
    if selected_option == case["correct_answer"]:
        student_data["correct_answers"] += 1
        student_data["module_progress"][case["module"]]["correct"] += 1
        st.success("### ✅ Correct!")
        
        # Check for module completion
        if student_data["module_progress"][case["module"]]["cases_attempted"] >= 5:  # Reduced for testing
            student_data["module_progress"][case["module"]]["completed"] = True
            if case["module"] not in student_data["modules_completed"]:
                student_data["modules_completed"].append(case["module"])
            st.balloons()
            st.success(f"🎉 **Module Completed!** You've mastered {CURRICULUM_MODULES[case['module']]['name']}")
    else:
        st.error(f"### ❌ Correct answer: **{case['correct_answer']}**")
    
    student_data["last_active"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Show explanation
    st.markdown("---")
    st.markdown("#### 📚 Detailed Explanation")
    st.write(case["explanation"])
    
    st.markdown("#### 🎓 Key Learning Points")
    for point in case["learning_points"]:
        st.write(f"• {point}")
    
    # USMLE tip
    st.info(f"**USMLE Tip:** This content is highly relevant for {case['usmle_relevance']}")

# Run the application
if __name__ == "__main__":
    main()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p><strong>MedSchool Ophtho</strong> - Interactive Ophthalmology Curriculum for Medical Students</p>
    <p><small>MS1 Foundations → MS2 Pathologies → MS3 Clerkship → MS4 Advanced → Boards Preparation</small></p>
    <p><small>Comprehensive medical education platform with USMLE-aligned content</small></p>
</div>
""", unsafe_allow_html=True)
