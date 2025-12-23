# Internship Project Submission Report

## Team Details
**Batch Number**: 8  
**Start Date**: 27th November 2025  
**Names**: <Insert Names of Interns>  
**Internship Duration**: 8 Weeks

---

## 1. Project Title
**AI-Driven Web Application for Automated Disease Detection in Rice and Pulse Crops**

## 2. Project Objective
The primary goal of this internship project was to develop an intelligent, accessible web application that empowers farmers and agricultural experts to diagnose crop diseases instantly. By leveraging Artificial Intelligence (AI) and Deep Learning, the system aims to:
- enable early detection of diseases in rice and pulse crops.
- reduce crop loss through timely medical intervention.
- provide a simple, user-friendly interface for stakeholders with varying levels of technical expertise.

## 3. Project Description in Detail
This project is a full-stack AI application designed to identify plant diseases from leaf images. 

**Approach:**
We followed a systematic software development lifecycle, starting with data collection and preprocessing, moving to model architecture design, training, and finally deployment via a web interface. The system was engineered using **SOLID principles** to ensure maintainability and scalability.

**Technology Stack:**
- **Deep Learning**: PyTorch, Torchvision (CNN Architecture)
- **Web Framework**: Streamlit (Python-based UI)
- **Image Processing**: PIL, NumPy
- **Authentication**: Streamlit-Login-Auth-UI
- **Language**: Python 3.11

**Real-world Impact:**
The application bridges the gap between complex agricultural research and practical on-field application. It allows a farmer with a smartphone to access expert-level disease diagnosis without waiting for a physical laboratory analysis, potentially saving entire harvests from spreading infections.

## 4. Timeline Overview

| Week | Activities Planned | Activities Completed |
| :--- | :--- | :--- |
| **Week 1** | Data Collection: Gathering images for Rice and Pulse diseases. | Collected datasets for 4 Rice classes and 5 Pulse classes. |
| **Week 2** | Preprocessing: Resizing, Normalization, Noise Removal. | Implemented `torchvision` transforms and augmentation pipelines. |
| **Week 3** | Model Architecture Design (CNN). | Designed a custom CNN with 3 convolutional blocks and dropout layers. |
| **Week 4** | Model Training & Evaluation. | Trained models reaching ~96% accuracy (Pulse) and ~63% (Rice). Saved `.pth` files. |
| **Week 5** | UI Design: Wireframing and Basic Layout. | Created `app.py` with custom CSS, colors, and responsive layout. |
| **Week 6** | Feature Implementation: Login & Upload. | Integrated Secure Login System and Drag-and-Drop Image Uploader. |
| **Week 7** | Integration & System Testing. | Connected UI with AI Models; verified predictions via `pytest` suite. |
| **Week 8** | Documentation & Final Polish. | Completed `README.md`, `SOLID_PRINCIPLES.md`, and User Guide. |

## 5a. Key Milestones

| Milestone | Description | Date Achieved |
| :--- | :--- | :--- |
| **Project Kickoff** | Initial requirements gathering and environment setup. | Week 1 |
| **Prototype/First Draft** | First successful model training run on the Rice dataset. | Week 3 |
| **Mid-Term Review** | Demonstration of the raw model inference script without UI. | Week 4 |
| **Beta Release** | Functional Streamlit UI with basic upload and predict capability. | Week 6 |
| **Final Submission** | Complete polished app with Auth, Styles, and Documentation. | Week 8 |

## 5b. Project Execution Details
The project execution was divided into three core phases:

1.  **Machine Learning Phase**: 
    - We curated a dataset involving thousands of images.
    - We constructed a Convolutional Neural Network (CNN) using PyTorch. 
    - The model was trained using CrossEntropyLoss and Adam optimizer, featuring validation loops to monitor accuracy and prevent overfitting.
2.  **Application Development Phase**:
    - We chose Streamlit for its rapid development capabilities and Python integration.
    - We implemented a **Layered Architecture**, separating the UI (`app.py`) from business logic (`services/`) and data models.
    - We applied **Dependency Injection** to manage complex dependencies like Authentication and Model Handlers.
3.  **Quality Assurance Phase**:
    - Automated tests were written using `pytest` to ensure new changes didn't break existing logic.
    - Manual testing involved trying various image formats and lighting conditions to ensure robustness.

## 6. Snapshots / Screenshots
*(Please insert your screenshots here)*

**Suggested Screenshots to include:**
1.  **Login Page**: Showing the secure authentication screen.
2.  **Dashboard/Upload**: Showing the "Rice" or "Pulse" selection and file uploader.
3.  **Analysis Result**: A screenshot showing a leaf, the predicted disease, confidence score, and treatment advice.

## 7. Challenges Faced
-   **dataset Imbalance**: Some disease classes had fewer images than others. *Mitigation*: We applied Data Augmentation (rotation, flipping) to balance the class distribution.
-   **Model Size Integration**: The models were large (~200MB), causing slow initial loads. *Mitigation*: We implemented caching (`@st.cache_resource`) to load the model only once.
-   **UI Customization**: Streamlit has limited default styling. *Mitigation*: We injected custom CSS to create a professional, branded look with gradients and card layouts.

## 8. Learnings & Skills Acquired
-   **Technical Skills**: Mastery of **PyTorch** for Deep Learning, **Streamlit** for Web UI, and **Python** software design patterns.
-   **Software Architecture**: Learned practical application of **SOLID Principles** (Single Responsibility, Dependency Inversion) in a real project.
-   **Domain Knowledge**: Gained insight into agricultural pathology, specifically common diseases affecting rice and pulse crops.
-   **Soft Skills**: Improved time management by adhering to strict weekly sprints and better documentation practices.

## 9. Testimonials from team
"Building this AI application was an eye-opening experience. Moving from raw code to a user-friendly interface that can actually help farmers felt incredibly rewarding. The most satisfying moment was seeing the model correctly identify a 'Blast' disease with 95% confidence for the first time."

## 10. Conclusion
The internship has been a transformative journey. We successfully delivered a functioning AI-powered disease detection system that meets the initial project requirements. The project not only enhanced our technical proficiency in AI and Full-Stack development but also taught us the value of building software that solves real-human problems. This experience aligns perfectly with my career goal of becoming an AI Engineer focused on social impact.

## 11. Acknowledgements
We would like to express our deepest gratitude to our mentor, **<Insert Mentor Name>**, for their guidance and patience. We also thank **<Organization Name>** for providing the resources and platform to execute this project. Special thanks to the open-source community for the tools and datasets that made this work possible.
