pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/<username>/<repo>.git'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh '''
                cd $WORKSPACE
                docker compose down || true
                docker compose up -d --build --remove-orphans
                '''
            }
        }
    }
}
