from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

todos = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>To-Do List</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .container {
            max-width: 500px;
        }
        .card {
            border-radius: 20px;
        }
        .btn-danger {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <div class="card shadow p-4">
            <h2 class="text-center mb-4">📝 <strong>To-Do List</strong></h2>
            <form method="POST" action="/add" class="d-flex mb-4">
                <input type="text" name="task" class="form-control me-2" placeholder="Tambahkan tugas..." required>
                <button type="submit" class="btn btn-primary">Tambah</button>
            </form>
            <ul class="list-group">
                {% for idx, todo in enumerate(todos) %}
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        {{ todo }}
                        <a href="/delete/{{ idx }}" class="btn btn-sm btn-outline-danger">Hapus</a>
                    </li>
                {% else %}
                    <li class="list-group-item text-muted text-center">Belum ada tugas.</li>
                {% endfor %}
            </ul>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    todos.append(task)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run()
