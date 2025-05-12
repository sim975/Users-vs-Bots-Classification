# 🤖 Users vs Bots Classification on VK

This project focuses on classifying user profiles as either **real users** or **bots** on the Russian social media platform [VK](https://vk.com). By using various profile-based features, we aim to build a machine learning model that accurately detects automated accounts.

---

## 📂 Dataset

- **Source**: [Kaggle - Users vs Bots Classification](https://www.kaggle.com/datasets/juice0lover/users-vs-bots-classification)
- **Samples**: 5,874 profiles (2,937 real users + 2,937 bots)
- **Features**: 60 profile attributes including:
  - `has_photo`, `can_post_on_wall`, `has_website`, `gender`, `posts_count`
  - Activity-based metrics: `avg_likes`, `avg_comments`, `reposts_ratio`
  - Profile metadata: `has_interests`, `has_books`, `has_tv`, etc.
- **Target**:  
  - `0`: Real user  
  - `1`: Bot

---

## 🧠 Project Goals

- Build a binary classification model to distinguish users vs bots.
- Identify the most important features influencing predictions.
- Create an interactive web interface for real-time predictions.

---

## 🛠️ Tech Stack

| Component   | Tech Used               |
|-------------|-------------------------|
| Language    | Python 3                |
| Libraries   | Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn |
| Model       | Random Forest, Logistic Regression, XGBoost (best performer) |
| Web App     | Flask / FastAPI + HTML/CSS (optional) |
| Deployment  | Docker / AWS / Localhost |

---

## 📊 Exploratory Data Analysis (EDA)

- Dataset is perfectly balanced.
- Many bots lack profile pictures, have zero posts, and low engagement.
- Real users tend to have richer profile information and activity.

---

## 📈 Model Performance

| Metric       | Value (example) |
|--------------|-----------------|
| Accuracy     | 94%             |
| Precision    | 93%             |
| Recall       | 95%             |
| F1-Score     | 94%             |

> Performance may vary based on feature selection and model used.

---

## 🌐 Web Application (Optional)

An optional Flask-based web interface is available to test the model:
- Input VK-like profile data.
- Press "Predict" to get real-time result (Bot or User).

---

## 🚀 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/users-vs-bots-classification.git
   cd users-vs-bots-classification



