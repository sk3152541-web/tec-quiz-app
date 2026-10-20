import json
import os
import random
from flask import Flask, render_template_string, request, session, redirect

app = Flask(__name__)
app.secret_key = "tec_exam_secret_key_sections_fixed"

JSON_FILE_PATH = "tec_questions.json"

def load_json_data():
    if not os.path.exists(JSON_FILE_PATH):
        return {"modules": []}
    with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TEC Exam Dashboard - Sections & Modules</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-4" style="max-width: 800px;">
        <div class="card shadow p-4">
            <h4 class="text-center mb-3 text-primary">TEC Exam Practice Dashboard (Module-wise Sections)</h4>
            
            {% if view == 'home' %}
                <p class="text-center text-muted mb-4">Apna practice module select karein:</p>
                <div class="list-group">
                    {% for mod in modules_list %}
                        <a href="/start_module/{{ mod.module_id }}" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center py-3 mb-2 rounded border">
                            <span class="fs-5 fw-semibold text-dark">{{ mod.module_id }}. {{ mod.module_name }}</span>
                            <span class="badge bg-primary rounded-pill fs-6 px-3 py-2">{{ mod.q_count }} Questions</span>
                        </a>
                    {% endfor %}
                </div>
            {% elif view == 'quiz' %}
                <div class="d-flex justify-content-between align-items-center mb-3 pb-2 border-bottom">
                    <span class="badge bg-info text-dark fs-6">📂 Section: {{ module_name }}</span>
                    <a href="/home" class="btn btn-outline-secondary btn-sm">🏠 Modules List</a>
                </div>

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
                    <div class="text-center py-4">
                        <h2 class="text-success">Module Completed!</h2>
                        <p class="fs-4">Aapka Final Score: <strong>{{ score }} / {{ total_qs }}</strong></p>
                        <div class="d-flex justify-content-center gap-3 mt-3">
                            <form method="POST">
                                <button type="submit" name="action" value="restart" class="btn btn-primary btn-lg">Try Again</button>
                            </form>
                            <a href="/home" class="btn btn-secondary btn-lg">Back to Modules</a>
                        </div>
                    </div>
                {% endif %}
            {% endif %}
        </div>
    </div>
</body>
</html>
"""

@app.route("/home")
def home():
    session["current_module_id"] = None
    data = load_json_data()
    modules_list = []
    for mod in data.get("modules", []):
        modules_list.append({
            "module_id": mod.get("module_id"),
            "module_name": mod.get("module_name"),
            "q_count": len(mod.get("questions", []))
        })
    return render_template_string(HTML_TEMPLATE, view="home", modules_list=modules_list)

@app.route("/start_module/<int:mod_id>")
def start_module(mod_id):
    data = load_json_data()
    selected_mod = None
    for mod in data.get("modules", []):
        if mod.get("module_id") == mod_id:
            selected_mod = mod
            break
            
    if not selected_mod:
        return redirect("/home")
        
    raw_qs = selected_mod.get("questions", [])
    indices = list(range(len(raw_qs)))
    random.shuffle(indices)
    
    quiz_meta = []
    for idx in indices:
        q = raw_qs[idx]
        opts = list(q["options"])
        correct_text = q["answer_text"]
        random.shuffle(opts)
        correct_idx = opts.index(correct_text)
        quiz_meta.append({
            "orig_idx": idx,
            "shuffled_opts": opts,
            "correct_index": correct_idx
        })
        
    session["current_module_id"] = mod_id
    session["module_name"] = selected_mod.get("module_name")
    session["quiz_indices"] = quiz_meta
    session["current_idx"] = 0
    session["score"] = 0
    session["message"] = ""
    session["alert_type"] = ""
    
    return redirect("/")

@app.route("/", methods=["GET", "POST"])
def index():
    if not session.get("current_module_id"):
        return home()
        
    data = load_json_data()
    mod_id = session.get("current_module_id")
    
    selected_mod = None
    for mod in data.get("modules", []):
        if mod.get("module_id") == mod_id:
            selected_mod = mod
            break
            
    if not selected_mod:
        return redirect("/home")
        
    raw_qs = selected_mod.get("questions", [])
    
    if request.method == "POST":
        action = request.form.get("action")
        
        if action == "restart":
            indices = list(range(len(raw_qs)))
            random.shuffle(indices)
            quiz_meta = []
            for idx in indices:
                q = raw_qs[idx]
                opts = list(q["options"])
                correct_text = q["answer_text"]
                random.shuffle(opts)
                correct_idx = opts.index(correct_text)
                quiz_meta.append({
                    "orig_idx": idx,
                    "shuffled_opts": opts,
                    "correct_index": correct_idx
                })
            session["quiz_indices"] = quiz_meta
            session["current_idx"] = 0
            session["score"] = 0
            session["message"] = "Quiz restarted!"
            session["alert_type"] = "alert-info"
            
        elif action == "shuffle_qs":
            quiz_meta = list(session["quiz_indices"])
            random.shuffle(quiz_meta)
            session["quiz_indices"] = quiz_meta
            session["current_idx"] = 0
            session["message"] = "Questions shuffle ho gaye hain!"
            session["alert_type"] = "alert-info"
            
        elif action == "shuffle_opts":
            current_idx = session["current_idx"]
            quiz_meta = session["quiz_indices"]
            if current_idx < len(quiz_meta):
                meta = quiz_meta[current_idx]
                q = raw_qs[meta["orig_idx"]]
                opts = list(q["options"])
                correct_text = meta["shuffled_opts"][meta["correct_index"]]
                random.shuffle(opts)
                correct_idx = opts.index(correct_text)
                meta["shuffled_opts"] = opts
                meta["correct_index"] = correct_idx
                session["quiz_indices"] = quiz_meta
                session["message"] = "Options shuffle ho gayi hain!"
                session["alert_type"] = "alert-secondary"
                
        elif action == "back":
            if session["current_idx"] > 0:
                session["current_idx"] -= 1
                
        elif action == "submit":
            selected = int(request.form.get("user_answer", -1))
            current_idx = session["current_idx"]
            quiz_meta = session["quiz_indices"]
            meta = quiz_meta[current_idx]
            correct_idx = meta["correct_index"]
            
            if selected == correct_idx:
                session["score"] = session.get("score", 0) + 1
                session["message"] = "Sahi jawab! (Correct)"
                session["alert_type"] = "alert-success"
            else:
                correct_text = meta["shuffled_opts"][correct_idx]
                session["message"] = f"Ghalat jawab! Sahi jawab yeh tha: {correct_text}"
                session["alert_type"] = "alert-danger"
                
            session["current_idx"] += 1

    current_idx = session.get("current_idx", 0)
    quiz_meta = session.get("quiz_indices", [])
    total_qs = len(quiz_meta)
    
    q_data = None
    if current_idx < total_qs:
        meta = quiz_meta[current_idx]
        q = raw_qs[meta["orig_idx"]]
        q_data = {
            "question": q["question"],
            "shuffled_opts": meta["shuffled_opts"],
            "correct_index": meta["correct_index"]
        }

    return render_template_string(
        HTML_TEMPLATE,
        view="quiz",
        module_name=session.get("module_name"),
        current_idx=current_idx,
        total_qs=total_qs,
        q_data=q_data,
        score=session.get("score", 0),
        message=session.get("message", ""),
        alert_type=session.get("alert_type", "")
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
