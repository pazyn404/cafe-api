import os
import uuid
import json
import subprocess

from flask import request, send_file, after_this_request
from jinja2 import Template
from jinja2.exceptions import TemplateSyntaxError

from app import app


@app.route("/render/", methods=["POST"])
def render():
    @after_this_request
    def cleanup(response):
        try:
            os.remove(f"temp/{filename}.pdf")
            os.remove(f"temp/{filename}.html")
        except OSError:
            pass

        return response

    filename = uuid.uuid4().hex

    template = request.files.get("template")
    data = request.form.get("data")
    if not template:
        return {"error": "Template is missing"}, 400
    if not data:
        return {"error": "Data is missing"}, 400

    try:
        json_data = json.loads(data)
    except ValueError:
        return {"error": "Invalid json"}, 400

    template_str = template.read().decode("utf-8")
    try:
        rendered = Template(template_str).render(json_data)
    except TemplateSyntaxError:
        return {"error": "Invalid template"}, 400

    with open(f"temp/{filename}.html", "w") as f:
        f.write(rendered)

    subprocess.run(["wkhtmltopdf", f"temp/{filename}.html", f"temp/{filename}.pdf"])

    return send_file(f"temp/{filename}.pdf", mimetype="application/pdf")
