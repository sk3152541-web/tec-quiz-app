import json
import os
import random
from flask import Flask, render_template_string, request, session, redirect

app = Flask(__name__)
app.secret_key = "tec_exam_secret_key_optimized"

JSON_FILE_PATH = "tec_questions.json"

def load_json_data():
    if not os.path.exists(JSON_FILE_PATH):
        return {"modules": []}
    try:
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return {"modules": []}
            return json.loads(content)
    except json.JSONDecodeError:
        print("Error: tec_questions.json file mein JSON format ki koi galti hai!")
        return {"modules": []}

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
                <div class="d-grid gap-3">
                    {% for mod in modules_list %}
                        <form method="POST" action="/start_module" class="d-grid">
                            <input type="hidden" name="mod_id" value="{{ mod.module_id }}">
                            <button type="submit" class="btn btn-outline-primary p-3 d-flex justify-content-between align-items-center text-start shadow-sm w-100" style="border-width: 2px;">
                                <span class="fs-5 fw-semibold text-dark">{{ mod.module_id }}. {{ mod.module_name }}</span>
                                <span class="badge bg-primary rounded-pill fs-6 px-3 py-2">{{ mod.q_count }} Questions</span>
                            </button>
                        </form>
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
                            {% for opt in q_data.options %}
                                <label class="list-group-item">
                                    <input class="form-check-input me-2" type="radio" name="user_answer" value="{{ opt }}" {% if answered %}disabled{% endif %} {% if user_selected == opt %}checked{% endif %} required>
                                    {{ opt }}
                                </label>
                            {% endfor %}
                        </div>

                        <div class="d-flex justify-content-between flex-wrap gap-2">
                            <button type="submit" name="action" value="back" class="btn btn-warning text-white"> &lt;&lt; Back </button>
                            
                            {% if not answered %}
                                <button type="submit" name="action" value="submit" class="btn btn-success"> Submit Answer </button>
                            {% else %}
                                <button type="submit" name="action" value="next" class="btn btn-primary"> Next Question &gt;&gt; </button>
                            {% endif %}

                            <button type="submit" name="action" value="shuffle_qs" class="btn btn-secondary"> Shuffle Qs </button>
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
    session.clear()
    data = load_json_data()
    modules_list = []
    for mod in data.get("modules", []):
        modules_list.append({
            "module_id": mod.get("module_id"),
            "module_name": mod.get("module_name"),
            "q_count": len(mod.get("questions", []))
        })
    return render_template_string(HTML_TEMPLATE, view="home", modules_list=modules_list)

@app.route("/start_module", methods=["POST"])
def start_module_post():
    mod_id = int(request.form.get("mod_id"))
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
    
    session.clear()
    session["current_module_id"] = mod_id
    session["module_name"] = selected_mod.get("module_name")
    session["q_indices"] = indices
    session["current_idx"] = 0
    session["score"] = 0
    session["message"] = ""
    session["alert_type"] = ""
    session["answered"] = False
    session["user_selected"] = None
    session["shuffled_options_cache"] = {}
    session.modified = True
    
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
    q_indices = session.get("q_indices", [])
    total_qs = len(q_indices)
    current_idx = session.get("current_idx", 0)
    
    if request.method == "POST":
        action = request.form.get("action")
        
        if action == "restart":
            random.shuffle(q_indices)
            session["q_indices"] = q_indices
            session["current_idx"] = 0
            session["score"] = 0
            session["message"] = "Quiz restarted!"
            session["alert_type"] = "alert-info"
            session["answered"] = False
            session["user_selected"] = None
            session["shuffled_options_cache"] = {}
            
        elif action == "shuffle_qs":
            random.shuffle(q_indices)
            session["q_indices"] = q_indices
            session["current_idx"] = 0
            session["message"] = "Questions shuffle ho gaye hain!"
            session["alert_type"] = "alert-info"
            session["answered"] = False
            session["user_selected"] = None
            session["shuffled_options_cache"] = {}
            
        elif action == "back":
            if current_idx > 0:
                session["current_idx"] -= 1
                session["message"] = ""
                session["answered"] = False
                session["user_selected"] = None
                
        elif action == "submit":
            if not session.get("answered", False):
                selected_ans = request.form.get("user_answer")
                session["user_selected"] = selected_ans
                if current_idx < total_qs:
                    q_original_idx = q_indices[current_idx]
                    q = raw_qs[q_original_idx]
                    correct_ans = q["answer_text"]
                    
                    if selected_ans == correct_ans:
                        session["score"] = session.get("score", 0) + 1
                        session["message"] = "Sahi jawab! (Correct)"
                        session["alert_type"] = "alert-success"
                    else:
                        session["message"] = f"Ghalat jawab! Sahi jawab yeh tha: {correct_ans}"
                        session["alert_type"] = "alert-danger"
                        
                    session["answered"] = True

        elif action == "next":
            session["current_idx"] += 1
            session["message"] = ""
            session["answered"] = False
            session["user_selected"] = None

        session.modified = True

    current_idx = session.get("current_idx", 0)
    q_data = None
    if current_idx < total_qs:
        q_original_idx = q_indices[current_idx]
        q = raw_qs[q_original_idx]
        
        cache = session.get("shuffled_options_cache", {})
        str_idx = str(current_idx)
        
        if str_idx not in cache:
            opts = list(q["options"])
            random.shuffle(opts)
            cache[str_idx] = opts
            session["shuffled_options_cache"] = cache
            session.modified = True
        
        q_data = {
            "question": q["question"],
            "options": cache[str_idx]
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
        alert_type=session.get("alert_type", ""),
        answered=session.get("answered", False),
        user_selected=session.get("user_selected")
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
