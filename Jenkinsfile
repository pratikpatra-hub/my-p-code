pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'  // Virtual environment directory
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv $VENV_DIR'

                    // Activate the virtual environment
                    sh '. $VENV_DIR/bin/activate && pip install --upgrade pip'

                    // Install dependencies from requirements.txt within the virtual environment
                    sh '. $VENV_DIR/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run tests using the virtual environment
                    sh '. $VENV_DIR/bin/activate && pytest'
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            // Clean up virtual environment after the job
            sh 'rm -rf $VENV_DIR'
        }
    }
}

