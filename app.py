from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="YOUR_API_KEY")

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/email", methods=["POST"])
def email():
    purpose = request.form["purpose"]
    tone = request.form["tone"]

    prompt = f"""
    Write a professional email.

    Purpose: {purpose}
    Tone: {tone}

    Include subject line and closing.
    """

    return render_template("result.html", result=ask_ai(prompt))


@app.route("/meeting", methods=["POST"])
def meeting():
    notes = request.form["notes"]

    prompt = f"""
    Summarize meeting notes:

    - Summary
    - Decisions
    - Action Items
    - Deadlines

    Notes:
    {notes}
    """

    return render_template("result.html", result=ask_ai(prompt))


@app.route("/tasks", methods=["POST"])
def tasks():
    tasks = request.form["tasks"]

    prompt = f"""
    Prioritize tasks using urgency and importance.

    Tasks:
    {tasks}
    """

    return render_template("result.html", result=ask_ai(prompt))


@app.route("/research", methods=["POST"])
def research():
    text = request.form["text"]

    prompt = f"""
    Analyze content and provide:
    - Summary
    - Insights
    - Risks
    - Recommendations

    Content:
    {text}
    """

    return render_template("result.html", result=ask_ai(prompt))


@app.route("/futureme", methods=["POST"])
def futureme():
    data = request.form["data"]

    prompt = f"""
    Act as a workplace strategist.

    Predict:
    - What may be forgotten
    - Risks
    - Delays
    - Recommendations

    Tasks:
    {data}
    """

    return render_template("result.html", result=ask_ai(prompt))


if __name__ == "__main__":
    app.run(debug=True)
