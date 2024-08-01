pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/jbtis/python_jenkins_test.git'
            }
        }
        stage('Setup') {
            steps {
                bat '''
                    python -m venv %PYTHON_ENV%
                    call %PYTHON_ENV%\\Scripts\\activate
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
                bat '''
                    call %PYTHON_ENV%\\Scripts\\activate
                    coverage run -m unittest discover
                '''
            }
        }
        stage('Report') {
            steps {
                bat '''
                    call %PYTHON_ENV%\\Scripts\\activate
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
