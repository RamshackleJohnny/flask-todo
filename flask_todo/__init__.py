from flask import Flask, request, make_response, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/hello')
    def hello():
        name = request.args.get('name', 'World')
        return render_template('hello.html', name=name)

    @app.route('/number/<int:num>')
    def number_route(num):
        return f"Number: {num}"

    @app.route('/calculate', methods=['GET', 'POST'])
    def calculate():
        if request.method == 'GET':
            return render_template('calculate.html', action="Add")
        elif request.method == 'POST':
            x = float(request.form['x'])
            y = float(request.form['y'])
            action = request.form['action']

            if action == "Add":
                result = x + y
            elif action == "Subtract":
                result = x - y
            elif action == "Multiply":
                result = x * y
            elif action == "Divide":
                result = x / y

        return render_template('calculate.html', result=result, x=x, y=y)


    method_route_allows = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']

    @app.route('/method', methods=method_route_allows)
    def method():
        return render_template('method.html', allowed=method_route_allows, method=request.method, action=action)

    @app.route('/status')
    def status():
        yes = request.args.get('c', 200)
        response = make_response(f"status: {code}", yes)

        return response

    return app
