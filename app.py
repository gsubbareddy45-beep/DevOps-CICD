from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Demo App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding: 50px;
            }

            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
                max-width: 700px;
                margin: auto;
            }

            h1 {
                color: #2c3e50;
            }

            p {
                color: #555;
                font-size: 18px;
            }

            ul {
                text-align: left;
                display: inline-block;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>🚀 Welcome to DevOps</h1>

            <p>
                This application is deployed using
                AWS EC2 + Docker + GitHub Actions CI/CD.
            </p>

            <h2>Project Components</h2>

            <ul>
                <li>Python Flask Application</li>
                <li>Docker Containerization</li>
                <li>GitHub Actions Pipeline</li>
                <li>AWS EC2 Deployment</li>
                <li>Automatic CI/CD on Git Push</li>
            </ul>

            <h3>Status: ✅ Application Running Successfully</h3>

            <p>
                Every new Git commit automatically deploys
                the latest version to AWS EC2.
            </p>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)