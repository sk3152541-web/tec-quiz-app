import random
from flask import Flask, render_template_string, request, session

app = Flask(__name__)
app.secret_key = "tec_exam_secret_key_123"

# TEC Exam Bilingual Questions List
quiz_questions = [
    {
        "question": (
            "Which department or portal handles PAN card applications? (PAN"
            " card applications ko kaun sa department ya portal handle karta"
            " hai?)"
        ),
        "options": [
            "NSDL and UTIITSL",
            "Passport Authority",
            "IRCTC",
            "UIDAI",
        ],
        "answer_text": "NSDL and UTIITSL",
    },
    {
        "question": "What is the full form of CSC? (CSC ka pura naam kya hai?)",
        "options": [
            "Common Service Centre",
            "Computer Service Center",
            "Central System Council",
            "Common Sector Company",
        ],
        "answer_text": "Common Service Centre",
    },
    {
        "question": (
            "Which course is required for CSC VLE registration? (CSC VLE"
            " registration ke liye kaun sa course karna padta hai?)"
        ),
        "options": [
            "TEC (Telecentre Entrepreneur Course)",
            "Tally Course",
            "Basic Computer Course",
            "Digital Marketing",
        ],
        "answer_text": "TEC (Telecentre Entrepreneur Course)",
    },
    {
        "question": (
            "What does VLE stand for in the CSC ecosystem? (CSC ecosystem"
            " mein VLE ka matlab kya hota hai?)"
        ),
        "options": [
            "Village Level Entrepreneur",
            "Virtual Local Expert",
            "Value Link Engine",
            "Verified Legal Employee",
        ],
        "answer_text": "Village Level Entrepreneur",
    },
    {
        "question": (
            "What is the official website to register for CSC? (CSC ke liye"
            " register karne ki official website kaun si hai?)"
        ),
        "options": ["csc.gov.in", "irctc.co.in", "uidai.gov.in", "nsdl.com"],
        "answer_text": "csc.gov.in",
    },
    {
        "question": (
            "What is the minimum age requirement to register for a CSC? (CSC"
            " ke liye register karne ki minimum age limit kya hai?)"
        ),
        "options": ["18 Years", "15 Years", "21 Years", "25 Years"],
        "answer_text": "18 Years",
    },
    {
        "question": (
            "What is the main objective of a Common Service Centre? (Common"
            " Service Centre ka mukhya uddeshya kya hai?)"
        ),
        "options": [
            "To provide digital and government services to citizens",
            "To sell mobile phones",
            "To book movie tickets only",
            "To teach driving",
        ],
        "answer_text": (
            "To provide digital and government services to citizens"
        ),
    },
    {
        "question": (
            "Who launched the Digital India initiative? (Digital India"
            " initiative kisne launch kiya tha?)"
        ),
        "options": [
            "Government of India",
            "State Bank of India",
            "Microsoft",
            "Google India",
        ],
        "answer_text": "Government of India",
    },
    {
        "question": (
            "Can a VLE provide banking services at their center? (Kya ek VLE"
            " apne center par banking services de sakta hai?)"
        ),
        "options": [
            "Yes",
            "No",
            "Only on Sundays",
            "Only for government employees",
        ],
        "answer_text": "Yes",
    },
    {
        "question": (
            "Which ministry oversees the CSC scheme in India? (India mein CSC"
            " scheme kis ministry ke antargat aati hai?)"
        ),
        "options": [
            "Ministry of Electronics and Information Technology (MeitY)",
            "Ministry of Agriculture",
            "Ministry of Railways",
            "Ministry of Health",
        ],
        "answer_text": (
            "Ministry of Electronics and Information Technology (MeitY)"
        ),
    },
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TEC Exam Dashboard - Dual Shuffle</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-4" style="max-width: 750px;">
        <div class="card shadow p-4">
            <h4 class="text-center mb-3 text-primary">TEC Exam Practice Dashboard</h4>
            
            {% if current_idx < total_qs %}
                <div class="mb-3">
                    <span class="badge bg-secondary">Question {{ current_idx + 1 }} of {{ total_qs }}</span>
                    <h5 class="mt-2">{{ q_data.question }}</h5>
                </div>

                {% if message %}
                    <div class="alert {{ alert_type }} alert-dismissible fade show" role="alert">
                        {{ message }}
                    </div>
                {% endif %}

                <form method="POST">
                    <div class="list-group mb-4">
                        {% for opt in q_data.shuffled_opts %}
                            <label class="list-group-item">
                                <input class="form-check-input me-2" type="radio" name="user_answer" value="{{ loop.index0 }}" required>
                                {{ opt }}
                            </label>
                        {% endfor %}
                    </div>

                    <div class="d-flex justify-content-between flex-wrap gap-2">
                        <button type="submit" name="action" value="back" class="btn btn-warning text-white"> &lt;&lt; Back </button>
                        <button type="submit" name="action" value="submit" class="btn btn-success"> Submit </button>
                        <button type="submit" name="action" value="shuffle_qs" class="btn btn-primary"> Shuffle Qs </button>
                        <button type="submit" name="action" value="shuffle_opts" class="btn btn-secondary" style="background-color: #6f42c1; border-color: #6f42c1;"> Shuffle Options </button>
                        <button type="submit" name="action" value="restart" class="btn btn-danger"> Restart </button>
                    </div>
                </form>
            {% else %}
                <div class="text-center">
                    <h2 class="text-success">Quiz Completed!</h2>
                    <p class="fs-4">Aapka Final Score: <strong>{{ score }} / {{ total_qs }}</strong></p>
                    <form method="POST">
                        <button type="submit" name="action" value="restart" class="btn btn-primary btn-lg mt-3">Start Again</button>
                    </form>
                </div>
            {% endif %}
        </div>
    </div>
</body>
</html>
"""


def init_quiz():
  temp_q = list(quiz_questions)
  random.shuffle(temp_q)
  shuffled_data = []
  for q in temp_q:
    opts = list(q["options"])
    correct_text = q["answer_text"]
    random.shuffle(opts)
    correct_idx = opts.index(correct_text)
    shuffled_data.append({
        "question": q["question"],
        "options": q["options"],
        "shuffled_opts": opts,
        "correct_index": correct_idx,
    })
  session["quiz_data"] = shuffled_data
  session["current_idx"] = 0
  session["score"] = 0
  session["message"] = ""
  session["alert_type"] = ""


@app.route("/", methods=["GET", "POST"])
def index():
  if "quiz_data" not in session:
    init_quiz()

  message = session.get("message", "")
  alert_type = session.get("alert_type", "")
  session["message"] = ""

  if request.method == "POST":
    action = request.form.get("action")

    if action == "restart":
      init_quiz()

    elif action == "shuffle_qs":
      temp_q = list(session["quiz_data"])
      random.shuffle(temp_q)
      session["quiz_data"] = temp_q
      session["current_idx"] = 0
      session["message"] = "Questions naye sire se shuffle ho gaye hain!"
      session["alert_type"] = "alert-info"

    elif action == "shuffle_opts":
      current_idx = session["current_idx"]
      if current_idx < len(session["quiz_data"]):
        q_item = session["quiz_data"][current_idx]
        opts = list(q_item["options"])
        correct_text = q_item["shuffled_opts"][q_item["correct_index"]]
        random.shuffle(opts)
        correct_idx = opts.index(correct_text)
        q_item["shuffled_opts"] = opts
        q_item["correct_index"] = correct_idx
        session["message"] = "Options shuffle ho gayi hain!"
        session["alert_type"] = "alert-secondary"

    elif action == "back":
      if session["current_idx"] > 0:
        session["current_idx"] -= 1

    elif action == "submit":
      selected = int(request.form.get("user_answer", -1))
      current_idx = session["current_idx"]
      q_data = session["quiz_data"][current_idx]
      correct_idx = q_data["correct_index"]

      if selected == correct_idx:
        session["score"] = session.get("score", 0) + 1
        session["message"] = "Sahi jawab! (Correct)"
        session["alert_type"] = "alert-success"
      else:
        correct_text = q_data["shuffled_opts"][correct_idx]
        session["message"] = (
            f"Ghalat jawab! Sahi jawab yeh tha: {correct_text}"
        )
        session["alert_type"] = "alert-danger"

      session["current_idx"] += 1

  current_idx = session.get("current_idx", 0)
  quiz_data = session.get("quiz_data", [])
  total_qs = len(quiz_data)
  q_data = quiz_data[current_idx] if current_idx < total_qs else None

  return render_template_string(
      HTML_TEMPLATE,
      current_idx=current_idx,
      total_qs=total_qs,
      q_data=q_data,
      score=session.get("score", 0),
      message=message,
      alert_type=alert_type,
  )


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
