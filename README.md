# 🎵 Music Recommendation System

## 📌 Overview
This project is a simple and interactive **Music Recommendation System** built using **Streamlit and Pandas**.  
It allows users to filter songs based on **Genre** and **Artist** and get personalized song suggestions instantly.

---

## 🚀 Features
- 🎶 Browse and filter songs by genre  
- 🎤 Filter songs by artist  
- ⚡ Instant recommendations based on selection  
- 📊 Clean and simple user interface using Streamlit  
- 📂 Uses CSV dataset for song data  

---

## 🛠️ Tech Stack
- Python  
- Streamlit  
- Pandas  

---

## 📁 Project Structure
```
music_recommendation_app/
│
├── app.py
├── songs.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```
git clone https://github.com/your-username/music-recommendation-app.git
cd music-recommendation-app
```

### 2️⃣ Create virtual environment (optional)
```
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

---

## ▶️ Run the Application
```
streamlit run app.py
```

Then open in browser:
```
http://localhost:8501
```

---

## 📊 Dataset Information
The dataset (`songs.csv`) contains:
- Song Name  
- Artist  
- Genre  

---

## 🎯 How It Works
- User selects Genre and/or Artist from sidebar  
- The app filters the dataset using Pandas  
- Matching songs are displayed  

---

## 🚀 Future Enhancements
- Add search functionality  
- Integrate ML-based recommendations  
- Add Spotify API integration  

---

## 👨‍💻 Author
Vishwa
