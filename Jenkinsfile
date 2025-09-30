pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // तुझं GitHub repo clone होईल Jenkins workspace मध्ये
                git branch: 'main', url: 'https://github.com/rohanmangore09/Grampanchayat-new.git'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                # Go to deployment directory
                cd /home/ubuntu/grampanchayat-website || mkdir -p /home/ubuntu/grampanchayat-website

                # Copy repo files to deployment directory
                cp -r $WORKSPACE/* /home/ubuntu/grampanchayat-website/

                # Go to deployment folder
                cd /home/ubuntu/grampanchayat-website

                # Stop old containers (if running)
                docker compose down || true

                # Build & run new containers
                docker compose up -d --build --remove-orphans
                '''
            }
        }
    }
}
