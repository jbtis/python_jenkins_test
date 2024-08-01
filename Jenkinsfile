pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/jbtis/python_jenkins_test.git'
            }
        }
        stage('Run main.py') {
            steps {
                bat '''
                    set PATH=C:\\Users\\Mariano\\AppData\\Local\\Programs\\Python\\Python312;%PATH%
                    python main.py
                '''
            }
        }
        stage('Test') {
            steps {
                bat '''
                    set PATH=C:\\Users\\Mariano\\AppData\\Local\\Programs\\Python\\Python312;%PATH%
                    coverage run -m unittest discover
                '''
            }
        }
        stage('Report') {
            steps {
                bat '''
                    set PATH=C:\\Users\\Mariano\\AppData\\Local\\Programs\\Python\\Python312;%PATH%
                    coverage report -m
                    coverage html
                '''
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report for Simple Python Project'
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
