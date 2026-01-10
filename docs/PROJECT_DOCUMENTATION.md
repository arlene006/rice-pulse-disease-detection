# 🌾 Rice & Pulse Disease Detection System - Technical Documentation

## 📋 Executive Summary
This project is an advanced AI-powered agricultural diagnostic tool designed to detect crop diseases (specifically Rice) from leaf images. It uses Deep Learning (CNNs) for analysis and provides a professional, secure web interface for farmers.

The system now goes beyond detection by offering **Actionable Cure Plans** and **Downloadable PDF Reports**, ensuring farmers have tangible next steps.

The project has been engineered with **Enterprise Software Standards** in mind, adhering strictly to **SOLID Principles** and utilizing modern design patterns like **Dependency Injection** and **Factory Pattern**.

---

## 🏗️ System Architecture

The application is built using a **Layered Architecture** to ensure separation of concerns:

1.  **Presentation Layer (`app.py`)**: Handles UI, user interaction, and displays results. It is "dumb" and only displays what the services provide.
2.  **Service Layer (`services/`)**: Contains the core business logic.
    *   **Auth Service**: Manages user login/logout security.
    *   **Disease Handlers**: Orchestrates the AI model loading and prediction logic.
    *   **Reporting Service**: Generates professional PDF reports.
3.  **Data/Model Layer**:
    *   **Models**: Contains the raw neural network architecture (`models/`).
    *   **Data**: Stores static disease information and cure steps (`services/disease_data.py`).
4.  **Infrastructure (`services/container.py`)**: A "Dependency Container" that wires everything together.

---
    
## 🚀 Key Features

*   **Dual-Crop Disease Detection**: Supports both Rice and Pulse crops with dedicated AI models.
*   **AI-Powered Assistant**: Integrated Botpress chatbot in the sidebar for instant help.
*   **Comprehensive Reporting**:
    *   **PDF Generation**: Download professional reports with diagnosis and images.
    *   **Cure Response Mechanism**: Get step-by-step healing plans for detected diseases.
*   **Dynamic UI**:
    *   **Adjustable Sidebar**: User-controllable width (300px-1200px) and chatbot height.
    *   **Context-Aware**: Chatbot is available alongside analysis results.
*   **Secure Authentication**: Role-based login system.
*   **Enterprise Architecture**: Built on SOLID principles for maintainability.

---

## 📂 Project Structure Explained

Here is the breakdown of every important file and folder in the system:

```mermaid
graph TD
    App[app.py] --> Container[services/container.py]
    Container --> Auth[services/auth_service.py]
    Container --> Handlers[services/disease_handlers.py]
    Handlers --> Interfaces[services/interfaces.py]
    Handlers --> Model[models/architecture.py]
```

### 1. Root Directory
*   `app.py`: The entry point.
    *   **Features**: now includes a dynamic sidebar with adjustable width and an integrated **AI Chatbot** (Botpress).
    *   *Role*: Presentation Layer. Ask specific services for logic and displays results.
*   `SOLID_PRINCIPLES.md`: Documentation of the 5 architectural principles applied.
*   `requirements.txt`: List of all Python libraries needed.
*   `pages/`: Contains the standalone Chatbot page (`1_🤖_Chat_Help.py`) as an alternative interface.

### 2. Services Directory (`services/`)
This is the engine room of the application.
*   **`interfaces.py`**: Defines the "Contracts" (Interfaces).
    *   `IDiseasePredictor`: "Anyone who wants to be a predictor MUST have a `predict()` method."
    *   `IAuthService`: "Anyone who handles auth MUST have a `login()` method."
*   **`auth_service.py`**: Handles security.
    *   `StreamlitAuthService`: The actual code that draws the login box and checks passwords.
*   **`disease_handlers.py`**: Business logic for crops.
    *   `RiceDiseaseHandler`: Knows how to load the Rice model and interpret results.
    *   `PulseDiseaseHandler`: A placeholder for future expansion (demonstrating extensibility).
*   **`report_generator.py`**: Handles PDF generation.
    *   `ReportGenerator`: Creates the downloadable PDF report using ReportLab.
*   **`disease_data.py`**: Static Data Storage.
    *   Contains the dictionary of disease info and **cure steps**, isolating data from logic.
*   **`container.py`**: The **Dependency Injection Container**.
    *   This is a "Factory" that creates all the objects efficiently. It creates the Auth Service and the correct Crop Handler ensuring the App never creates them manually.

### 3. Models Directory (`models/`)
*   `architecture.py`: The pure PyTorch Code defining the Convolutional Neural Network (CNN).
*   `best_model.pth`: The actual trained "brain" of the AI (weights file).

---

## 🛡️ SOLID Principles Implementation

We didn't just write code; we engineered it. Here is how we applied the 5 Golden Rules of Software Design:

### 1. Single Responsibility Principle (SRP)
*   **Before:** `app.py` did everything.
*   **Now:** `app.py` does UI. `auth_service.py` does Security. `disease_handlers.py` does AI. `architecture.py` defines the Model. Each file has **one job**.

### 2. Open/Closed Principle (OCP)
*   **Concept:** Open for extension, Closed for modification.
*   **Applied:** To add "Wheat" detection, we just create a `WheatDiseaseHandler` class. We **do not touch** the existing Rice logic or the App logic. The system is easy to grow without breaking.

### 3. Liskov Substitution Principle (LSP)
*   **Concept:** Subclasses must behave like their parents.
*   **Applied:** `RiceDiseaseHandler` and `PulseDiseaseHandler` both return a standardized `PredictionResult` object. The App treats them exactly the same. You can swap them out and nothing crashes.

### 4. Interface Segregation Principle (ISP)
*   **Concept:** Don't force clients to use methods they don't need.
*   **Applied:** We split functionality into `IDiseasePredictor` (for AI) and `IDiseaseInfoProvider` (for text info). If we make a simple "Info Page", it doesn't need to load the heavy AI model.

### 5. Dependency Inversion Principle (DIP)
*   **Concept:** Depend on abstractions, not concretions.
*   **Applied:** `app.py` does not import `RiceDiseaseHandler` directly. It asks the `DependencyContainer` for a handler. This means we can easily swap the AI engine in the future without rewriting the UI.

---

## 🧪 Testing

We included a robust test suite in the `tests/` folder:
*   `test_container.py`: Verifies that our "Factory" creates objects correctly.
*   `test_solid_compliance.py`: Ensures that our classes strictly follow the rules we set (like usage of Interfaces).

To run tests:
```bash
pytest
```
