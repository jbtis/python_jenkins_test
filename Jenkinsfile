pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/my_python_project.git'
            }
        }
        stage('Setup') {
            steps {
                sh '''
                    python -m venv $PYTHON_ENV
                    . $PYTHON_ENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt || true
                '''
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                // Add your build steps here if any
            }
        }
        stage('Test') {
            steps {
                sh '''
                    . $PYTHON_ENV/bin/activate
                    coverage run -m unittest discover
                '''
            }
        }
        stage('Report') {
            steps {
                sh '''
                    . $PYTHON_ENV/bin/activate
                    coverage report -m
                    coverage html
                '''
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report'
                ])
            }
        }
    }
    post {
        always {
            junit 'test-results.xml'
        }
    }
}
