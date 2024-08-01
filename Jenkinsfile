pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:\\Users\\Mariano\\AppData\\Local\\Programs\\Python\\Python312'
        PIP_PATH = 'C:\\Users\\Mariano\\AppData\\Local\\Programs\\Python\\Python312\\Scripts'
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
                    set PATH=%PYTHON_PATH%;%PIP_PATH%;%PATH%
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install coverage
                '''
            }
        }
        stage('Run main.py') {
            steps {
                bat '''
                    set PATH=%PYTHON_PATH%;%PIP_PATH%;%PATH%
                    call venv\\Scripts\\activate
                    python main.py
                '''
            }
        }
        stage('Test') {
            steps {
                bat '''
                    set PATH=%PYTHON_PATH%;%PIP_PATH%;%PATH%
                    call venv\\Scripts\\activate
                    coverage run -m unittest discover > test_results.txt
                '''
                archiveArtifacts artifacts: 'test_results.txt', allowEmptyArchive: true
            }
        }
        stage('Report') {
            steps {
                bat '''
                    set PATH=%PYTHON_PATH%;%PIP_PATH%;%PATH%
                    call venv\\Scripts\\activate
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
}
