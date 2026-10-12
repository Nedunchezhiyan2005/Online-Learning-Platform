pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t online-learning-platform:1.0 .'
            }
        }

        stage('Deploy Application') {
            steps {
                bat '''
                docker rm -f online-learning-app 2>NUL || echo No existing container
                docker run -d --name online-learning-app -p 5001:5000 online-learning-platform:1.0
                '''
            }
        }
    }
}