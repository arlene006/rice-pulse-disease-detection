# Software Architecture (SOLID Principles)

This project has been refactored to adhere to **SOLID principles**, ensuring a scalable, maintainable, and robust codebase.

---

## 1. Single Responsibility Principle (SRP)

Each module has a distinct responsibility, preventing tightly coupled code:

- **`models/architecture.py`**: Handles only neural network architecture (CNN model definition).
- **`services/disease_handlers.py`**: Manages disease prediction logic (preprocessing, model loading, predictions).
- **`services/disease_data.py`**: Stores static disease information, separating data from logic.
- **`services/auth_service.py`**: Focuses purely on user authentication (login/registration).
- **`services/report_generator.py`**: Handles PDF creation and formatting.
- **`services/container.py`**: Contains dependency injection logic (service creation and management).
- **`app.py`**: Handles only UI presentation (displaying results, user interaction).

---

## 2. Open/Closed Principle (OCP)

The system is open for extension but closed for modification:

- **New Crop Models**: We successfully added `PulseDiseaseHandler` by extending the base class, without modifying any existing `RiceDiseaseHandler` logic or the main application flow. This proves the system is extensible.
- **New Detection Logic**: The `CropDiseaseHandler` base class in `services/disease_handlers.py` allows adding new detection backends by creating a new class implementation without modifying existing app code.
- **UI Extensibility**: New features like the **Sidebar Chatbot** were integrated as independent modules (Components/Iframes) without altering the core `DiseaseClassifier` logic, respecting the separation of concerns.

---

## 3. Liskov Substitution Principle (LSP)

Any class implementing `CropDiseaseHandler` (like `RiceDiseaseHandler` or `PulseDiseaseHandler`) can be swapped in without breaking the application. The `app.py` UI relies on the interface contract, not specific implementation details.

- All handlers return `Optional[PredictionResult]` from `services/interfaces.py`.
- `RiceDiseaseHandler` and `PulseDiseaseHandler` are completely interchangeable.

---

## 4. Interface Segregation Principle (ISP)

Interfaces are segregated to avoid forcing clients to depend on methods they don't use:

- **`IDiseasePredictor`** (`services/interfaces.py`): For components that need AI prediction (model loading, predictions).
- **`IDiseaseInfoProvider`** (`services/interfaces.py`): For components that only need disease information (symptoms, treatment).

This allows lightweight components (e.g., a Disease Encyclopedia page) to use only `IDiseaseInfoProvider` without loading heavy ML models.

---

## 5. Dependency Inversion Principle (DIP)

High-level modules depend on abstractions, not concrete implementations:

- **`app.py`** depends on `IAuthService` and `CropDiseaseHandler` interfaces, not concrete classes.
- **`services/container.py`** acts as a Dependency Injection Container, creating and providing service instances.
- This decoupling allows easy swapping of authentication systems or AI engines without modifying the UI code.

---

## 📊 File Structure

```
rice-disease-detection/
├── app.py                          # UI Layer (SRP, DIP)
├── services/
│   ├── auth_service.py             # Authentication (SRP, DIP)
│   ├── container.py                # Dependency Injection (DIP)
│   ├── disease_data.py             # Static Data (SRP)
│   ├── disease_handlers.py         # Prediction Logic (SRP, OCP, LSP)
│   ├── interfaces.py               # Abstractions (ISP, LSP, DIP)
│   └── report_generator.py         # Reporting (SRP)
├── models/
│   └── architecture.py             # CNN Architecture (SRP)
└── tests/
    ├── test_container.py           # DIP Tests
    └── test_solid_compliance.py    # SOLID Tests
```

---

## 🧪 Testing

All SOLID principles are verified through automated tests:

- **`tests/test_solid_compliance.py`**: Verifies ISP and LSP compliance
- **`tests/test_container.py`**: Verifies DIP and OCP compliance

**Test Results**: 9/9 tests passing ✅

---

## ✅ Benefits

This refactoring ensures a **scalable, maintainable, and robust codebase** that follows industry-standard software engineering principles.
