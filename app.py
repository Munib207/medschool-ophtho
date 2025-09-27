import streamlit as st
import random
from datetime import datetime
import hashlib
import json
import pandas as pd
import time

# ===== SECURE USER AUTHENTICATION SYSTEM =====
st.set_page_config(
    page_title="MedSchool Ophtho - Interactive Curriculum",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== USER DATABASE (In production, use real database) =====
def initialize_user_database():
    if "users" not in st.session_state:
        # Sample users - in production, use proper database
        st.session_state.users = {
            "admin": {
                "password_hash": hash_password("admin123"),
                "name": "Administrator",
                "role": "admin",
                "email": "admin@medschoolophtho.com"
            },
            "ms2024001": {
                "password_hash": hash_password("password123"),
                "name": "Medical Student 001",
                "role": "student",
                "email": "student001@medschool.edu",
                "registration_date": "2024-01-15"
            },
            "ms2024002": {
                "password_hash": hash_password("password123"), 
                "name": "Medical Student 002",
                "role": "student",
                "email": "student002@medschool.edu",
                "registration_date": "2024-01-15"
            }
        }
    
    if "student_progress" not in st.session_state:
        st.session_state.student_progress = {}

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, password_hash):
    """Verify a stored password against one provided by user"""
    return hash_password(password) == password_hash

def authenticate_user(username, password):
    """Authenticate user credentials"""
    if username in st.session_state.users:
        if verify_password(password, st.session_state.users[username]["password_hash"]):
            return True, st.session_state.users[username]
    return False, None

def register_user(username, password, name, email, role="student"):
    """Register a new user"""
    if username in st.session_state.users:
        return False, "Username already exists"
    
    st.session_state.users[username] = {
        "password_hash": hash_password(password),
        "name": name,
        "email": email,
        "role": role,
        "registration_date": datetime.now().strftime("%Y-%m-%d")
    }
    return True, "User registered successfully"

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

    "Diabetic Retinopathy Screening": {
        "module": "ms2_pathologies",
        "case_type": "preventive_care",
        "question": "A 50-year-old with type 2 diabetes for 10 years presents for routine care. He has no visual symptoms. When should he have his first dilated eye examination?",
        "options": [
            "Immediately",
            "In 5 years",
            "Only when symptoms develop",
            "At age 65"
        ],
        "correct_answer": "Immediately",
        "explanation": "Type 2 diabetics should have initial dilated eye exam at diagnosis. Type 1 diabetics should have initial exam within 5 years of diagnosis.",
        "learning_points": [
            "Type 2 diabetes: dilated exam at diagnosis",
            "Type 1 diabetes: exam within 5 years of diagnosis",
            "Annual screening thereafter if no retinopathy",
            "More frequent if retinopathy present"
        ],
        "difficulty": "basic",
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

    "Uveitis Workup": {
        "module": "ms3_clerkship",
        "case_type": "diagnostic_approach",
        "question": "A 30-year-old patient presents with acute anterior uveitis. What systemic condition is most commonly associated with this presentation?",
        "options": [
            "HLA-B27 associated spondyloarthropathies",
            "Sarcoidosis",
            "Tuberculosis",
            "Syphilis"
        ],
        "correct_answer": "HLA-B27 associated spondyloarthropathies",
        "explanation": "HLA-B27 associated conditions (ankylosing spondylitis, reactive arthritis, IBD) are the most common systemic associations with acute anterior uveitis.",
        "learning_points": [
            "HLA-B27 most common systemic association",
            "Anterior uveitis: pain, photophobia, redness",
            "Posterior uveitis: more likely infectious/autoimmune",
            "Always check for systemic symptoms"
        ],
        "difficulty": "intermediate",
        "usmle_relevance": "High - Step 2 CK"
    },

    "Pediatric Vision Screening": {
        "module": "ms3_clerkship",
        "case_type": "preventive_pediatrics",
        "question": "At what age should children have their first vision screening examination?",
        "options": [
            "Newborn period",
            "6 months",
            "3 years",
            "5 years"
        ],
        "correct_answer": "Newborn period",
        "explanation": "The AAP recommends vision screening in the newborn period and at all well-child visits. Formal vision assessment begins around 3-4 years.",
        "learning_points": [
            "Newborn: red reflex test",
            "6-12 months: ocular alignment",
            "3-5 years: formal vision screening",
            "Amblyopia treatment most effective <7 years"
        ],
        "difficulty": "basic",
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

    "Orbital Cellulitis": {
        "module": "ms4_advanced",
        "case_type": "surgical_decision",
        "question": "A 10-year-old with sinusitis presents with fever, proptosis, limited eye movement, and decreased vision. CT shows orbital abscess. What is the most appropriate management?",
        "options": [
            "Oral antibiotics and close observation",
            "IV antibiotics and ENT consultation",
            "Immediate surgical drainage",
            "Topical antibiotics only"
        ],
        "correct_answer": "Immediate surgical drainage",
        "explanation": "Orbital abscess with vision loss constitutes an emergency requiring immediate surgical drainage to prevent permanent vision loss and CNS spread.",
        "learning_points": [
            "Orbital abscess + vision loss = surgical emergency",
            "Preseptal vs orbital cellulitis distinction critical",
            "IV antibiotics essential",
            "Multidisciplinary approach with ENT"
        ],
        "difficulty": "expert",
        "usmle_relevance": "High - Step 2 CK and Step 3"
    },

    "Chemical Eye Injury": {
        "module": "ms4_advanced",
        "case_type": "emergency_protocol",
        "question": "A patient presents with alkaline chemical splash to the eye. What is the most appropriate immediate action?",
        "options": [
            "Irrigate with normal saline for 30 minutes",
            "Apply antibiotic ointment",
            "Patch the eye",
            "Neutralize with weak acid"
        ],
        "correct_answer": "Irrigate with normal saline for 30 minutes",
        "explanation": "Alkaline burns require immediate, prolonged irrigation (30+ minutes) until pH normalizes. Time is critical for preventing permanent damage.",
        "learning_points": [
            "Alkaline burns: more damaging than acidic",
            "Irrigate until pH 7.0-7.4",
            "Check pH with litmus paper",
            "Alkali penetrates deeper than acid"
        ],
        "difficulty": "advanced",
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
    },

    "Integrated Case - Young Male": {
        "module": "boards_prep",
        "case_type": "integrated_clinical",
        "question": "A 25-year-old male presents with acute vision loss in one eye, pain with eye movement, and color desaturation. Neurologic exam is otherwise normal. What is the most likely diagnosis?",
        "options": [
            "Optic neuritis",
            "Retinal detachment",
            "Central retinal artery occlusion",
            "Functional vision loss"
        ],
        "correct_answer": "Optic neuritis",
        "explanation": "Young patient + monocular vision loss + pain with eye movement + color desaturation = classic optic neuritis, often associated with MS.",
        "learning_points": [
            "Optic neuritis: pain with movement characteristic",
            "Often first presentation of MS",
            "IV steroids may speed recovery",
            "MRI brain to evaluate for demyelination"
        ],
        "difficulty": "expert",
        "usmle_relevance": "High - Step 2 CK and Step 3"
    },

    "Integrated Case - Step 2 Style": {
        "module": "boards_prep",
        "case_type": "usmle_style",
        "question": "A 68-year-old man with type 2 diabetes presents with floaters in his right eye. Examination shows dot-blot hemorrhages, microaneurysms, and hard exudates. Visual acuity is 20/25. What is the most appropriate management?",
        "options": [
            "Pan-retinal photocoagulation",
            "Anti-VEGF injections",
            "Observation with follow-up in 4-6 months",
            "Vitrectomy"
        ],
        "correct_answer": "Observation with follow-up in 4-6 months",
        "explanation": "This describes non-proliferative diabetic retinopathy without macular edema. No treatment indicated currently, but requires regular monitoring.",
        "learning_points": [
            "NPDR without DME: observation only",
            "PDR or DME requires treatment",
            "Annual dilated exams for diabetics",
            "Tight glycemic control slows progression"
        ],
        "difficulty": "expert",
        "usmle_relevance": "High - Step 2 CK"
    }
}

# ===== AUTHENTICATION INTERFACE =====
def show_login_register():
    """Show login/register interface"""
    st.markdown("## 🎓 MedSchool Ophtho - Student Portal")
    
    tab1, tab2, tab3 = st.tabs(["🔐 Student Login", "📝 New Registration", "👨‍⚕️ Instructor Access"])
    
    with tab1:
        st.markdown("### 🔐 Student Login")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        
        if st.button("Login", type="primary", use_container_width=True):
            if username and password:
                authenticated, user_data = authenticate_user(username, password)
                if authenticated:
                    st.session_state.user = username
                    st.session_state.user_data = user_data
                    st.session_state.authenticated = True
                    initialize_student_progress(username)
                    st.session_state.student_progress[username]["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                    st.success(f"Welcome back, {user_data['name']}!")
                    st.rerun()
                else:
                    st.error("Invalid username or password")
            else:
                st.warning("Please enter username and password")
        
        st.markdown("---")
        st.markdown("**Demo Credentials:**")
        st.code("Username: ms2024001\nPassword: password123")
    
    with tab2:
        st.markdown("### 📝 New Student Registration")
        new_username = st.text_input("Choose Username", key="reg_user")
        new_password = st.text_input("Choose Password", type="password", key="reg_pass")
        confirm_password = st.text_input("Confirm Password", type="password", key="reg_confirm")
        full_name = st.text_input("Full Name", key="reg_name")
        email = st.text_input("Email Address", key="reg_email")
        institution = st.text_input("Medical School/Institution", key="reg_inst")
        year = st.selectbox("Current Year", ["MS1", "MS2", "MS3", "MS4", "Resident", "Other"])
        
        if st.button("Register", type="secondary", use_container_width=True):
            if new_password != confirm_password:
                st.error("Passwords do not match")
            elif len(new_password) < 6:
                st.error("Password must be at least 6 characters")
            elif not all([new_username, full_name, email]):
                st.error("Please fill all required fields")
            else:
                success, message = register_user(new_username, new_password, full_name, email)
                if success:
                    st.session_state.users[new_username]["institution"] = institution
                    st.session_state.users[new_username]["year"] = year
                    st.success("Registration successful! Please login with your new credentials.")
                    initialize_student_progress(new_username)
                else:
                    st.error(message)
    
    with tab3:
        st.markdown("### 👨‍⚕️ Instructor Access")
        st.info("""
        **For Medical School Faculty:**
        - Track student progress across curriculum
        - Generate institutional reports
        - Monitor learning outcomes
        
        **Contact administrator for instructor accounts:**
        admin@medschoolophtho.com
        """)
        
        admin_user = st.text_input("Admin Username", key="admin_user")
        admin_pass = st.text_input("Admin Password", type="password", key="admin_pass")
        
        if st.button("Admin Login", use_container_width=True):
            if admin_user == "admin" and admin_pass == "admin123":
                st.session_state.user = "admin"
                st.session_state.user_data = st.session_state.users["admin"]
                st.session_state.authenticated = True
                st.success("Admin access granted!")
                st.rerun()

# ===== PROGRESS TRACKING AND REPORTING =====
def initialize_student_progress(username):
    """Initialize progress tracking for a student"""
    if username not in st.session_state.student_progress:
        st.session_state.student_progress[username] = {
            "current_module": "ms1_foundations",
            "modules_completed": [],
            "total_cases_completed": 0,
            "total_correct_answers": 0,
            "module_progress": {
                module: {
                    "completed": False, 
                    "cases_attempted": 0, 
                    "correct_answers": 0, 
                    "started": False,
                    "first_attempt": None,
                    "last_attempt": None,
                    "average_time_per_case": 0
                }
                for module in CURRICULUM_MODULES
            },
            "registration_date": datetime.now().strftime("%Y-%m-%d"),
            "last_login": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "total_study_time_minutes": 0,
            "achievements": [],
            "case_history": []  # Track every case attempted
        }

def record_case_attempt(username, case_id, correct, time_spent_seconds=0):
    """Record a case attempt with detailed tracking"""
    progress = st.session_state.student_progress[username]
    case_data = MEDICAL_CASES[case_id]
    
    # Update module progress
    module = case_data["module"]
    progress["module_progress"][module]["cases_attempted"] += 1
    progress["module_progress"][module]["last_attempt"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    if progress["module_progress"][module]["first_attempt"] is None:
        progress["module_progress"][module]["first_attempt"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    if correct:
        progress["module_progress"][module]["correct_answers"] += 1
        progress["total_correct_answers"] += 1
    
    progress["total_cases_completed"] += 1
    progress["total_study_time_minutes"] += time_spent_seconds / 60
    
    # Record detailed case history
    progress["case_history"].append({
        "case_id": case_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "module": module,
        "correct": correct,
        "time_spent_seconds": time_spent_seconds,
        "difficulty": case_data["difficulty"]
    })
    
    # Check for module completion
    if progress["module_progress"][module]["cases_attempted"] >= 3:  # Reduced for demo
        progress["module_progress"][module]["completed"] = True
        if module not in progress["modules_completed"]:
            progress["modules_completed"].append(module)

def get_student_progress_report(username):
    """Generate comprehensive progress report"""
    if username not in st.session_state.student_progress:
        return None
    
    progress = st.session_state.student_progress[username]
    user_data = st.session_state.users[username]
    
    report = {
        "student_info": {
            "username": username,
            "name": user_data["name"],
            "email": user_data["email"],
            "institution": user_data.get("institution", "Not specified"),
            "year": user_data.get("year", "Not specified"),
            "registration_date": progress["registration_date"],
            "last_login": progress["last_login"]
        },
        "progress_summary": {
            "total_cases_completed": progress["total_cases_completed"],
            "total_correct_answers": progress["total_correct_answers"],
            "overall_accuracy": (progress["total_correct_answers"] / progress["total_cases_completed"] * 100) if progress["total_cases_completed"] > 0 else 0,
            "modules_completed": len(progress["modules_completed"]),
            "total_study_time_hours": progress["total_study_time_minutes"] / 60,
            "current_module": progress["current_module"]
        },
        "module_details": {},
        "performance_analytics": {
            "by_difficulty": {},
            "by_module": {},
            "timeline": progress["case_history"][-20:] if progress["case_history"] else []  # Last 20 attempts
        }
    }
    
    # Module-level details
    for module_id, module_progress in progress["module_progress"].items():
        if module_progress["cases_attempted"] > 0:
            report["module_details"][module_id] = {
                "module_name": CURRICULUM_MODULES[module_id]["name"],
                "cases_attempted": module_progress["cases_attempted"],
                "correct_answers": module_progress["correct_answers"],
                "accuracy": (module_progress["correct_answers"] / module_progress["cases_attempted"] * 100),
                "completed": module_progress["completed"],
                "first_attempt": module_progress["first_attempt"],
                "last_attempt": module_progress["last_attempt"]
            }
    
    return report

# ===== LEARNING INTERFACE =====
def show_learning_interface(username):
    """Main learning interface with curriculum navigation"""
    student_data = st.session_state.student_progress[username]
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
    
    # Progress within current module
    module_progress = student_data["module_progress"][current_module_id]
    if module_progress["cases_attempted"] > 0:
        accuracy = (module_progress["correct_answers"] / module_progress["cases_attempted"] * 100)
        st.write(f"**Module Progress:** {module_progress['cases_attempted']} cases attempted | **Accuracy:** {accuracy:.1f}%")
        st.progress(min(module_progress["cases_attempted"] / 10, 1.0))
    
    # Case Interface
    st.markdown("### 💡 Interactive Clinical Cases")
    
    if st.session_state.get("current_case") is None:
        if st.button("🎯 Start New Case", type="primary", use_container_width=True):
            generate_new_case(current_module_id)
            st.rerun()
    else:
        display_current_case(username)

def generate_new_case(module_id):
    """Generate a new case from the specified module"""
    module_cases = [case_id for case_id, case in MEDICAL_CASES.items() if case["module"] == module_id]
    if module_cases:
        selected_case_id = random.choice(module_cases)
        st.session_state.current_case = MEDICAL_CASES[selected_case_id]
        st.session_state.current_case_id = selected_case_id
        st.session_state.case_start_time = time.time()

def display_current_case(username):
    """Display and handle the current case"""
    case = st.session_state.current_case
    student_data = st.session_state.student_progress[username]
    
    st.markdown("#### 📋 Clinical Scenario")
    
    # Case difficulty indicator
    difficulty_colors = {"basic": "🟢", "intermediate": "🟡", "advanced": "🟠", "expert": "🔴"}
    st.write(f"**Difficulty:** {difficulty_colors[case['difficulty']]} {case['difficulty'].title()} | **USMLE Relevance:** {case['usmle_relevance']}")
    
    st.info(f"**{case['question']}**")
    
    selected_option = st.radio("Select your answer:", case["options"], key="case_options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📝 Submit Answer", type="secondary", use_container_width=True):
            # Calculate time spent
            time_spent = time.time() - st.session_state.case_start_time
            process_answer(username, case, selected_option, time_spent)
    
    with col2:
        if st.button("🔄 New Case", use_container_width=True):
            generate_new_case(student_data["current_module"])
            st.rerun()

def process_answer(username, case, selected_option, time_spent):
    """Process the student's answer and update progress"""
    student_data = st.session_state.student_progress[username]
    correct = selected_option == case["correct_answer"]
    
    # Record the attempt
    record_case_attempt(username, st.session_state.current_case_id, correct, time_spent)
    
    if correct:
        st.success("### ✅ Correct!")
    else:
        st.error(f"### ❌ Correct answer: **{case['correct_answer']}**")
    
    # Show explanation
    st.markdown("---")
    st.markdown("#### 📚 Detailed Explanation")
    st.write(case["explanation"])
    
    st.markdown("#### 🎓 Key Learning Points")
    for point in case["learning_points"]:
        st.write(f"• {point}")
    
    # USMLE tip
    st.info(f"**USMLE Tip:** This content is highly relevant for {case['usmle_relevance']}")
    
    # Clear current case to allow new one
    st.session_state.current_case = None

# ===== PROGRESS DASHBOARD =====
def show_progress_dashboard(username):
    """Show student's personal progress dashboard"""
    st.markdown("## 📊 My Learning Progress")
    
    report = get_student_progress_report(username)
    if not report or report["progress_summary"]["total_cases_completed"] == 0:
        st.info("No progress data yet. Start learning to track your progress!")
        return
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Cases", report["progress_summary"]["total_cases_completed"])
    with col2:
        st.metric("Overall Accuracy", f"{report['progress_summary']['overall_accuracy']:.1f}%")
    with col3:
        st.metric("Modules Completed", report["progress_summary"]["modules_completed"])
    with col4:
        st.metric("Study Time", f"{report['progress_summary']['total_study_time_hours']:.1f}h")
    
    # Module progress
    st.markdown("### 📚 Module Progress")
    for module_id, module_data in report["module_details"].items():
        with st.expander(f"{CURRICULUM_MODULES[module_id]['icon']} {module_data['module_name']} - {module_data['accuracy']:.1f}% Accuracy"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Cases Attempted:** {module_data['cases_attempted']}")
                st.write(f"**Correct Answers:** {module_data['correct_answers']}")
                st.write(f"**Status:** {'✅ Completed' if module_data['completed'] else '🟡 In Progress'}")
            with col2:
                st.write(f"**First Attempt:** {module_data['first_attempt']}")
                st.write(f"**Last Attempt:** {module_data['last_attempt']}")
            
            # Progress bar
            progress = min(module_data['cases_attempted'] / 10, 1.0)
            st.progress(progress)
    
    # Recent activity
    if report["performance_analytics"]["timeline"]:
        st.markdown("### 📈 Recent Activity")
        recent_cases = report["performance_analytics"]["timeline"][-5:]  # Last 5 cases
        for case in reversed(recent_cases):
            status = "✅" if case["correct"] else "❌"
            st.write(f"{status} {case['timestamp']} - {MEDICAL_CASES[case['case_id']]['question'][:50]}...")
    
    # Export personal progress
    if st.button("📥 Download My Progress Report"):
        # Create downloadable report
        report_text = f"MedSchool Ophtho Progress Report\n"
        report_text += f"Student: {report['student_info']['name']}\n"
        report_text += f"Institution: {report['student_info']['institution']}\n"
        report_text += f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        report_text += f"Total Cases Completed: {report['progress_summary']['total_cases_completed']}\n"
        report_text += f"Overall Accuracy: {report['progress_summary']['overall_accuracy']:.1f}%\n\n"
        
        report_text += "Module Breakdown:\n"
        for module_id, module_data in report["module_details"].items():
            report_text += f"- {module_data['module_name']}: {module_data['accuracy']:.1f}% ({module_data['cases_attempted']} cases)\n"
        
        st.download_button(
            label="Download Progress Report",
            data=report_text,
            file_name=f"progress_report_{username}.txt",
            mime="text/plain"
        )

# ===== ADMIN DASHBOARD =====
def show_admin_dashboard():
    """Show administrator dashboard with all student progress"""
    if "user_data" not in st.session_state or st.session_state.user_data.get("role") != "admin":
        st.error("Admin access required")
        return
    
    st.markdown("## 👨‍⚕️ Administrator Dashboard")
    
    # Student progress overview
    st.markdown("### 📊 All Student Progress")
    
    progress_data = []
    for username, progress in st.session_state.student_progress.items():
        user_data = st.session_state.users.get(username, {})
        total_cases = progress["total_cases_completed"]
        correct_cases = progress["total_correct_answers"]
        accuracy = (correct_cases / total_cases * 100) if total_cases > 0 else 0
        
        progress_data.append({
            "Username": username,
            "Name": user_data.get("name", "N/A"),
            "Institution": user_data.get("institution", "N/A"),
            "Year": user_data.get("year", "N/A"),
            "Total Cases": total_cases,
            "Accuracy": f"{accuracy:.1f}%",
            "Modules Completed": len(progress["modules_completed"]),
            "Study Time (h)": f"{progress['total_study_time_minutes'] / 60:.1f}",
            "Last Login": progress["last_login"]
        })
    
    if progress_data:
        df = pd.DataFrame(progress_data)
        st.dataframe(df, use_container_width=True)
        
        # Analytics
        st.markdown("### 📈 Institutional Analytics")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_students = len(progress_data)
            st.metric("Total Students", total_students)
        
        with col2:
            total_cases = sum([p["Total Cases"] for p in progress_data])
            st.metric("Total Cases Attempted", total_cases)
        
        with col3:
            avg_accuracy = sum([float(p["Accuracy"][:-1]) for p in progress_data]) / len(progress_data)
            st.metric("Average Accuracy", f"{avg_accuracy:.1f}%")
        
        # Export option
        st.markdown("### 💾 Export Data")
        if st.button("📊 Export Progress Report (CSV)"):
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download CSV Report",
                data=csv,
                file_name="student_progress_report.csv",
                mime="text/csv"
            )
    else:
        st.info("No student progress data available yet")

# ===== MAIN APPLICATION =====
def main():
    # Initialize databases
    initialize_user_database()
    
    # Header
    st.markdown("""
    <div style="text-align: center; background: linear-gradient(135deg, #1A237E, #1565C0); color: white; padding: 3rem; border-radius: 15px; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0; font-size: 3rem;">🎓 MedSchool Ophtho</h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.4rem;">Interactive Ophthalmology Curriculum</p>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.1rem; opacity: 0.9;">Secure Student Progress Tracking</p>
    </div>
    """, unsafe_allow_html=True)

    # Authentication check
    if "authenticated" not in st.session_state or not st.session_state.authenticated:
        show_login_register()
        return
    
    # User is authenticated - show main application
    username = st.session_state.user
    user_data = st.session_state.user_data
    
    # Sidebar with user info and navigation
    with st.sidebar:
        st.markdown(f"### 👨‍🎓 Welcome, {user_data['name']}!")
        st.write(f"**Username:** {username}")
        st.write(f"**Role:** {user_data['role'].title()}")
        if user_data.get("institution"):
            st.write(f"**Institution:** {user_data['institution']}")
        st.write(f"**Last login:** {st.session_state.student_progress[username]['last_login']}")
        
        # Progress summary
        progress = st.session_state.student_progress[username]
        accuracy = (progress['total_correct_answers'] / progress['total_cases_completed'] * 100) if progress['total_cases_completed'] > 0 else 0
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Cases", progress['total_cases_completed'])
        with col2:
            st.metric("Accuracy", f"{accuracy:.1f}%")
        
        # Navigation
        st.markdown("---")
        if user_data["role"] == "admin":
            page = st.radio("Navigation", ["📚 Learn", "📊 My Progress", "👨‍⚕️ Admin Dashboard", "🏫 Curriculum Overview"])
        else:
            page = st.radio("Navigation", ["📚 Learn", "📊 My Progress", "🏫 Curriculum Overview"])
        
        if st.button("🚪 Logout", use_container_width=True):
            for key in list(st.session_state.keys()):
                if key not in ["users", "student_progress"]:  # Keep databases
                    del st.session_state[key]
            st.rerun()
    
    # Main content area
    if page == "📚 Learn":
        show_learning_interface(username)
    elif page == "📊 My Progress":
        show_progress_dashboard(username)
    elif page == "👨‍⚕️ Admin Dashboard":
        show_admin_dashboard()
    elif page == "🏫 Curriculum Overview":
        show_curriculum_overview()

def show_curriculum_overview():
    """Show complete curriculum overview"""
    st.markdown("## 🏫 Medical School Curriculum Overview")
    
    for module_id, module_info in CURRICULUM_MODULES.items():
        with st.expander(f"{module_info['icon']} {module_info['name']}", expanded=True):
            st.write(f"**Description:** {module_info['description']}")
            st.write(f"**Estimated Duration:** {module_info['estimated_duration']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Learning Objectives:**")
                for obj in module_info['learning_objectives']:
                    st.write(f"• {obj}")
            with col2:
                st.write("**Key Topics:**")
                for topic in module_info['key_topics']:
                    st.write(f"• {topic}")

# Run the application
if __name__ == "__main__":
    main()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p><strong>MedSchool Ophtho</strong> - Interactive Ophthalmology Curriculum for Medical Students</p>
    <p><small>MS1 Foundations → MS2 Pathologies → MS3 Clerkship → MS4 Advanced → Boards Preparation</small></p>
    <p><small>Comprehensive medical education platform with secure progress tracking</small></p>
</div>
""", unsafe_allow_html=True)
