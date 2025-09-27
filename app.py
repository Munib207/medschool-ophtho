import streamlit as st
import random
from datetime import datetime
import hashlib
import json
import pandas as pd

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
}

# ===== AUTHENTICATION INTERFACE =====
def show_login_register():
    """Show login/register interface"""
    tab1, tab2, tab3 = st.tabs(["🔐 Login", "📝 Register", "👨‍⚕️ Admin"])
    
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
                    st.success(f"Welcome back, {user_data['name']}!")
                    st.rerun()
                else:
                    st.error("Invalid username or password")
            else:
                st.warning("Please enter username and password")
    
    with tab2:
        st.markdown("### 📝 New Student Registration")
        new_username = st.text_input("Choose Username", key="reg_user")
        new_password = st.text_input("Choose Password", type="password", key="reg_pass")
        confirm_password = st.text_input("Confirm Password", type="password", key="reg_confirm")
        full_name = st.text_input("Full Name", key="reg_name")
        email = st.text_input("Email Address", key="reg_email")
        institution = st.text_input("Medical School/Institution", key="reg_inst")
        
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
                    st.success("Registration successful! Please login.")
                    # Initialize progress for new user
                    initialize_student_progress(new_username)
                else:
                    st.error(message)
    
    with tab3:
        st.markdown("### 👨‍⚕️ Instructor Access")
        st.info("Contact administrator for instructor accounts and progress reports")

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
            "Total Cases": total_cases,
            "Accuracy": f"{accuracy:.1f}%",
            "Modules Completed": len(progress["modules_completed"]),
            "Last Login": progress["last_login"]
        })
    
    if progress_data:
        df = pd.DataFrame(progress_data)
        st.dataframe(df, use_container_width=True)
        
        # Export option
        if st.button("📈 Export Progress Report"):
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
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
        page = st.radio("Navigation", ["📚 Learn", "📊 My Progress", "👨‍⚕️ Admin Dashboard"])
        
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

# ===== LEARNING INTERFACE =====
def show_learning_interface(username):
    # ... (include the learning interface code from previous version)
    # This would be the same curriculum learning interface
    st.markdown("## 📚 Learning Interface")
    st.info("Learning content would go here - same as previous version")
    # For brevity, including the full learning interface would make this very long
    # But it would be the same curriculum navigation and case system

def show_progress_dashboard(username):
    """Show student's personal progress dashboard"""
    st.markdown("## 📊 My Learning Progress")
    
    report = get_student_progress_report(username)
    if not report:
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
    st.markdown("### Module Progress")
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
    
    # Export personal progress
    if st.button("📥 Download My Progress Report"):
        # Create downloadable report
        import io
        buffer = io.BytesIO()
        # Simple text report for demo
        report_text = f"Progress Report for {report['student_info']['name']}\n"
        report_text += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        
        for module_id, module_data in report["module_details"].items():
            report_text += f"{module_data['module_name']}: {module_data['accuracy']:.1f}% ({module_data['cases_attempted']} cases)\n"
        
        st.download_button(
            label="Download Text Report",
            data=report_text,
            file_name="my_progress_report.txt",
            mime="text/plain"
        )

# Run the application
if __name__ == "__main__":
    main()
