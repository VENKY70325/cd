pipeline {
    agent any
    environment {
        IMAGE_NAME = "bus-reservation-app"
        CONTAINER_NAME = "bus-reservation-container"
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/VENKY70325/cd.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh "pip install -r requirements.txt"
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh "docker run --rm ${IMAGE_NAME} python manage.py test"
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d -p 8000:8000 --restart unless-stopped --name ${CONTAINER_NAME} ${IMAGE_NAME}
                    '''
                }
            }
        }
    }
    post {
        success {
            echo "Build and Deployment Successful! 🎉"
        }
        failure {
            echo "Build failed! Please check logs."
        }
    }
}
