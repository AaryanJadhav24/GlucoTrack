# GlucoTrack 🍸📈

GlucoTrack is a diabetes monitoring web app I built to simplify the process of tracking and understanding blood glucose trends. It's a full-stack project that combines React (frontend), FastAPI (backend), and MongoDB (database), with some AI-driven insights sprinkled in.

---

## 🚀 What It Does

* 📌 **Log Glucose Readings** — Enter blood sugar levels along with food/activity context.
* 📈 **Visualize Data** — See your glucose trends in clean, responsive charts.
* 🔔 **Range Alerts** — Get a quick heads-up if your readings are too high/low.
* 🧠 **AI Insights** — Analyze patterns over time with the help of a language model.
* 📱 **Mobile Ready** — Fully responsive layout for use on phones/tablets.

---

## 🛠️ Tech Stack

**Frontend**

* React + Vite
* Tailwind CSS
* Chart.js

**Backend**

* FastAPI (Python)
* MongoDB (with Motor)

**Extras**

* OpenRouter API (for AI suggestions)
* Heroicons + Framer Motion for nice UX touches

---

## 🧪 How to Run It Locally

### Clone the Repo

```bash
git clone https://github.com/yourusername/GlucoTrack.git
cd GlucoTrack
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Make sure MongoDB is running (you can use MongoDB Atlas or a local instance).

---

## 📌 Why I Built This

As part of learning how to build more practical full-stack apps, I wanted something meaningful and data-driven. Diabetes is something many people deal with, and a lot of the tracking apps out there are either bloated or too clinical. I wanted GlucoTrack to be simple, clean, and helpful — something I’d actually want to use.

---

## 📬 Feedback / Contributions

I’m open to feedback, improvements, or ideas. If you find a bug or want to contribute, feel free to open an issue or pull request.

---

## 💾 License

This project is open-source under the MIT license.
