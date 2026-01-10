# Virtual Internship 6.0 - Final Project Report

**Batch Number:** 6  
**Start date:** 27-November-2025  
**Name:** Arlene Kanattu Regi  
**Internship Duration:** 8 Weeks  

---

## 1. Project Title
**AI-Driven Web Application for Automated Disease Detection in Rice and Pulse Crops**

---

## 2. Project Objective
The primary goal of this internship project was to develop an intelligent, accessible web application that empowers farmers and agricultural experts to diagnose crop diseases instantly. By leveraging Artificial Intelligence (AI) and Deep Learning, the system aims to:
*   Enable early detection of diseases in rice and pulse crops.
*   Reduce crop loss through timely medical intervention.
*   Provide a simple, user-friendly interface for stakeholders with varying levels of technical expertise.
*   Offer actionable cure plans and professional reporting features.

---

## 3. Project Description in Detail
This project is a full-stack AI application designed to identify plant diseases from leaf images.

**Approach**:  
We followed a systematic software development lifecycle, starting with data collection and preprocessing, moving to model architecture design, training, and finally deployment via a web interface. The system was engineered using **SOLID principles** to ensure maintainability and scalability.

**Technology Stack**:
*   **Deep Learning**: PyTorch, Torchvision (CNN Architecture)
*   **Web Framework**: Streamlit (Python-based UI)
*   **Image Processing**: PIL, NumPy
*   **Authentication**: Streamlit-Login-Auth-UI
*   **Reporting**: ReportLab (PDF Generation)
*   **AI Assistant**: Botpress Chatbot Integration
*   **Language**: Python 3.11

**Real-world Impact**:  
The application bridges the gap between complex agricultural research and practical on-field application. It allows a farmer with a smartphone to access expert-level disease diagnosis without waiting for a physical laboratory analysis. With the newly added **Cure Response Mechanism** and **PDF Reports**, farmers not only get a diagnosis but also a tangible plan of action to save their harvest.

---

## 4. Timeline Overview

| Week | Activities Planned | Activities Completed |
| :--- | :--- | :--- |
| **Week 1** | Data Collection: Gathering images for Rice and Pulse diseases. | Collected datasets for 4 Rice classes and 5 Pulse classes. |
| **Week 2** | Preprocessing: Resizing, Normalization, Noise Removal. | Implemented preprocessing using Torchvision transforms, including normalization and basic data augmentation techniques. |
| **Week 3** | Model Architecture Design (CNN). | Designed a custom CNN with 3 convolutional blocks and dropout layers. |
| **Week 4** | Model Training & Evaluation. | Trained models reaching ~96% accuracy (Pulse) and ~63% (Rice). Saved .pth files. |
| **Week 5** | UI Design: Wireframing and Basic Layout. | Created `app.py` with custom CSS, colors, and responsive layout. |
| **Week 6** | Feature Enhancement: Authentication & Chatbot. | Implemented secure login system and integrated Botpress AI chatbot for user assistance. |
| **Week 7** | Advanced Features: PDF Reporting & Cure Plans. | Develop `ReportGenerator` service for PDF downloads and implemented the detailed Cure Response Mechanism with prevention tips. |
| **Week 8** | Testing, Bug Fixing & Final Documentation. | Performed end-to-end testing, resolved UI rendering bugs, verified SOLID compliance, and completed final documentation. |

---

## 5a. Key Milestones

| Milestone | Description | Date Achieved |
| :--- | :--- | :--- |
| **Project Kickoff** | Requirement analysis, project planning, and environment setup. | Week 1 |
| **Prototype/First Draft** | Successful training of CNN model on Rice and Pulse datasets. | Week 3 |
| **Mid-Term Review** | Demonstration of trained models and evaluation results with UI integration. | Week 4 |
| **Feature Complete** | Integration of Chatbot, PDF Reports, and Cure Plans. | Week 7 |
| **Final Submission** | Final code cleanup, testing, and documentation submission. | Week 8 |

---

## 5b. Project Execution Details

1.  **Data Management**: Collected and organized image datasets for Rice and Pulse crop diseases. Performed preprocessing such as image resizing and normalization to ensure consistent input data.
2.  **Model Development**: Designed and trained a Convolutional Neural Network (CNN) using PyTorch for disease classification. Evaluated the model performance and saved the trained model for future use.
3.  **Architecture Design**: Applied **SOLID design principles** to maintain clean and modular code:
    *   **Single Responsibility Principle**: Each module (Auth, Data, Reporting) performs a single specific task.
    *   **Open–Closed Principle**: New features or classes (like new crops) can be added without modifying existing code.
    *   **Liskov Substitution Principle**: Components (Handlers) can be replaced without affecting functionality.
    *   **Interface Segregation Principle**: Modules depend only on required interfaces (`IDiseasePredictor` vs `IDiseaseInfoProvider`).
    *   **Dependency Inversion Principle**: High-level modules depend on abstractions (Dependency Container), not concrete implementations.
4.  **Feature Implementation**:
    *   Developed a **Streamlit-based web interface** for image upload and disease prediction.
    *   Integrated **Botpress Chatbot** for 24/7 user assistance.
    *   Implemented **PDF Report Generation** using ReportLab to provide downloadable diagnostic reports.
    *   Created a detailed **Cure Response Mechanism** providing Overview, Prevention, and Treatment steps for each disease.

---

## 6. Snapshots / Screenshots

*(Please insert your screenshots here for the following screens)*
1.  **SignUp/Login Page**
2.  **Welcome Page (Dashboard)**
3.  **Upload Interface**
4.  **Analysis & Result (showing Cure Plan)**
5.  **PDF Report Sample**
6.  **Chatbot Interface**

---

## 7. Challenges Faced
*   **Dataset Imbalance**: Some disease classes had fewer images. *Resolution:* Applied data augmentation techniques.
*   **Model Performance**: Training the CNN model on CPU was slow. *Resolution:* Optimized batch sizes and model complexity.
*   **Visual Similarity**: Certain diseases showed very similar visual symptoms. *Resolution:* Fine-tuned model parameters and added expert-verified description data to aid users.
*   **HTML Rendering**: Encountered issues with rendering complex HTML lists in Streamlit. *Resolution:* Refactored string formatting in Python to ensure clean HTML output.

---

## 8. Learnings & Skills Acquired
*   **Technical Skills**: Mastery of PyTorch for Deep Learning, Streamlit for Web UI, ReportLab for PDF generation, and Python software design patterns.
*   **Software Architecture**: Learned practical application of **SOLID Principles** (Single Responsibility, Dependency Inversion) in a real-world project.
*   **Domain Knowledge**: Gained insight into agricultural pathology, specifically common diseases affecting rice and pulse crops.
*   **Feature Integration**: Learned to integrate third-party tools like Botpress and external libraries like ReportLab seamlessly.
*   **Soft Skills**: Improved time management by adhering to strict weekly sprints and better documentation practices.

---

## 9. Testimonials from Team
“Working on this project helped me understand how machine learning models are built and applied in real-world scenarios. Integrating the trained model with a web interface, and enhancing it with professional features like PDF reports and AI chatbots, was a valuable and satisfying experience.”

---

## 10. Conclusion
This internship provided a strong hands-on learning experience in machine learning and application development. Through this project, I gained practical exposure to data handling, CNN model training, and web-based deployment using Streamlit. Applying SOLID principles helped maintain clean and structured code. The addition of advanced features like the Cure Response Mechanism and PDF reporting transformed a simple academic project into a potentially viable product for real farmers. Overall, the internship strengthened my technical foundation and supported my career goals in AI and software development.

---

## 11. Acknowledgements
I sincerely thank **Mr. Uttam Kumar**, my mentor, for his guidance and continuous support throughout the project. I am also grateful to our coordinator, **Mr. Sasank Nukala** and the **Infosys Springboard Virtual Internship 6.0** team for providing this valuable learning opportunity. I would like to thank my teammates and the open-source community for their support and resources.
