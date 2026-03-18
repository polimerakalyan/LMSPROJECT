pipeline {
    agent any
    environment {
        AWS_REGION = "us-east-1"
        AWS_ACCOUNT_ID = "242201276768"
        ECR_REPO = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/lms-app"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        stage('Clone Repo') {
            steps {
                git branch: 'master', url: 'https://github.com/polimerakalyan/LMSPROJECT.git'
            }
        }
    
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t lms-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f lms-app || true
                docker run -d -p 8000:8000 --name lms-app lms-app
                '''
            }
        }

        stage('Login to AWS ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region $AWS_REGION \
                | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                '''
            }
        }

        stage('Tag Docker Image') {
            steps {
                sh 'docker tag lms-app:latest $ECR_REPO:latest'
            }
        }

        stage('Push to AWS ECR') {
            steps {
                sh 'docker push $ECR_REPO:latest'
            }
        }

    }
}

