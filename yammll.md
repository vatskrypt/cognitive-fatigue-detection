# 🧭 Cognitive Fatigue Detection — Project Roadmap

## ⚙️ Phase 0 — Groundwork

**Goal:** Establish architecture and development environment.

### Deliverables

- Repository initialized with directories.
- Basic README describing scope and architecture.
- Working FastAPI and React "Hello World".
- **MongoDB running locally via Docker or native installation.**
- Defined data schema and privacy boundaries.

---

## 🧩 Phase 1 — Data Collection Prototype

**Goal:** Build a prototype to collect task, typing, and mouse features.

### Tasks

- **Frontend**

  - Implement a simple cognitive task (reaction-time or Stroop task).
  - Capture typing and mouse event metrics.
  - Send batched feature data to backend via REST.

- **Backend**

  - Implement `/api/session/start` and `/api/session/{id}/features`.
  - **Store incoming data in MongoDB collections** (e.g., `sessions` and `features`).
  - Remove dependency on Valkey for temporary storage.

- **Data Schema**

  - Define MongoDB document structure for sessions, features, and user metadata.

### Deliverables

- Local MongoDB database with prototype task data.
- Verified REST endpoints for feature batching.

---

## 🎥 Phase 2 — Webcam Feature Integration

**Goal:** Add real-time webcam-based behavioral features.

### Tasks

- Use **MediaPipe FaceMesh** or **face-api.js** for facial landmarks.
- Compute:

  - Eye Aspect Ratio (EAR)
  - Blink rate (blinks per minute)
  - Gaze deviation or head pose variance

- Process all webcam data client-side for privacy.
- Combine webcam and task features into unified JSON payload.
- **Send combined payload to MongoDB via backend API.**

### Deliverables

- React component for camera feed + feature extraction.
- Combined feature payload stored in MongoDB.

---

## 🤖 Phase 3 — Model Training & Evaluation

**Goal:** Train and evaluate machine learning models for fatigue detection.

### Tasks

- Export collected feature data from MongoDB as CSV.
- Clean and normalize datasets (per-user baselines, missing values).
- Train and compare models:

  - Logistic Regression
  - RandomForest
  - XGBoost

- Evaluate using:

  - Leave-one-user-out cross-validation
  - F1, ROC-AUC, confusion matrix

- Save best-performing model as `ml_model.joblib`.

### Deliverables

- Notebook with preprocessing, training, and evaluation.
- Model file ready for inference.

---

## ⚡ Phase 4 — Real-Time Inference Backend

**Goal:** Integrate trained model into backend for real-time predictions.

### Tasks

- Load trained model at FastAPI startup.
- Preprocess incoming feature batches.
- Run model inference and compute fatigue score.
- **Store results in MongoDB (`sessions` or `scores` collection`).**
- Provide `/api/session/{id}/score` for fatigue status retrieval.

### Deliverables

- Working inference pipeline.
- End-to-end flow from frontend → backend → MongoDB → response.

---

## 📊 Phase 5 — Visualization & UI

**Goal:** Create a real-time fatigue monitoring dashboard.

### Tasks

- Build frontend visualization (Chart.js or Recharts).
- Display fatigue score trend and live updates.
- Implement fatigue threshold alerts ("Take a break").
- Add optional self-report modal for ground-truth labeling.

### Deliverables

- Real-time dashboard visualization.
- Integrated fatigue feedback system.

---

## 🧪 Phase 6 — Evaluation & Analysis

**Goal:** Evaluate system accuracy and user experience.

### Tasks

- Collect sessions from multiple users.
- Compare model predictions with self-reported fatigue.
- Analyze correlations and error metrics.
- Produce evaluation report with visualizations.

### Deliverables

- Evaluation notebook with metrics and plots.
- Final trained model and summarized results.

---

## 🚀 Phase 7 — Polishing & Deployment

**Goal:** Prepare and deploy production-ready demo.

### Tasks

- Dockerize backend and frontend.
- Deploy to cloud (Render, DigitalOcean, or similar).
- Configure environment variables and HTTPS.
- Finalize documentation, logging, and error handling.
- **Ensure MongoDB is properly deployed/secured in production.**

### Deliverables

- Hosted demo or local deployable package.
- Full documentation and demo video.

---

## 🧱 Bonus Enhancements

- Personalization (per-user baseline calibration).
- Online learning (incremental model updates).
- Optional EEG sensor integration for research expansion.

---

## ✅ What You’ll Gain

- Experience designing an end-to-end ML system.
- Understanding of behavioral data modeling.
- Skills in integrating ML into web systems.
- Practical exposure to privacy and real-time inference design.
