# ✨ Dressify – Smart Wardrobe Assistant  

🚀 A smart fashion web app that helps you decide what to wear using AI-based recommendations.  

💡 Built to solve a real-life problem:  
“I have clothes, but still don’t know what to wear!”  


## 📸 Project Preview  

### 👗 Upload Outfit  
<img width="1901" height="902" alt="image" src="https://github.com/user-attachments/assets/76a01feb-24d0-4855-9f68-2ac94caf6dd6" />


### 🎯 Recommendation Result  
<img width="1868" height="837" alt="image" src="https://github.com/user-attachments/assets/190042ad-eff1-4223-aefb-2c258f47b09a" />

<img width="1828" height="883" alt="image" src="https://github.com/user-attachments/assets/82ddf1d7-1077-46b5-a564-b91c3fede937" />



## 📌 Description  
Dressify is a smart wardrobe management system where users can upload their outfits and get personalized recommendations based on mood, occasion, and preferences.  

Each user gets their **own wardrobe space**, ensuring privacy and personalized suggestions.


## 🎯 Features  

- 👗 Upload and manage your outfits  
- 🎨 Automatic color detection  
- 😊 Mood-based outfit recommendation  
- 🎯 Occasion-based suggestions  
- 📊 Match score for each outfit  
- 🔒 User-specific wardrobe (no data mixing)  
- 🗑️ Delete outfits  


## 🧠 How It Works  

1. Upload your dress with details (type, category, etc.)  
2. System detects color combination  
3. Go to recommendation section  
4. Enter:
   - Mood  
   - Occasion  
   - Wear type  
5. Get best matching outfit with score  


## 🛠️ Tech Stack  

- **Frontend:** HTML, CSS  
- **Backend:** Flask (Python)  
- **Database:** SQLite  
- **ML Logic:** Color detection + recommendation system  
- **Deployment:** Hugging Face Spaces  



## 📂 Project Structure  
dressify/
│
├── app.py
├── requirements.txt
├── Dockerfile
│
├── ml/
│ ├── color_detector.py
│ └── recommender.py
│
├── static/
│ ├── style.css
│ └── uploads/
│
└── templates/
├── upload.html
├── select_mood.html
└── result.html
