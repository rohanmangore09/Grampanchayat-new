pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rohanmangore09/Grampanchayat-new.git'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                cd /home/ubuntu/grampanchayat-website || mkdir -p /home/ubuntu/grampanchayat-website
                cp -r * /home/ubuntu/grampanchayat-website/
                cd /home/ubuntu/grampanchayat-website
                docker compose down || true
                docker compose up -d --build --remove-orphans
                '''
            }
        }
    }
}
