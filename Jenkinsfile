pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building repo: ${env.JOB_NAME}"
                echo "Branch: ${env.BRANCH_NAME}"
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
            }
        }
    }
}
