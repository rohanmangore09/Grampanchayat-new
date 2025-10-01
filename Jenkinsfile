pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/rohanmangore09/Grampanchayat-new.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t grampanchayat-new .'
            }
        }

        stage('Run with Docker Compose') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }
}
