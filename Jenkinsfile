pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull the code from the repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install the required dependencies from requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run the test cases using unittest
                sh 'python -m unittest discover'
            }
        }
    }

    post {
        always {
            // This will run after the pipeline finishes regardless of success or failure
            echo 'Cleaning up...'
        }
    }
}

