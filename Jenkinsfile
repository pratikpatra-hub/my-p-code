pipeline {
    agent any
    
    environment {
        // Define the path to your Python virtual environment
        PYTHON_VENV = "${WORKSPACE}/venv"
        SONARQUBE_SCANNER_HOME = "/opt/sonarqube-scanner" // Update this path based on your system setup
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git 'https://github.com/pratikpatra-hub/my-p-code.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv ${PYTHON_VENV}'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Activate virtual environment and install dependencies
                    sh '. ${PYTHON_VENV}/bin/activate && pip install --upgrade pip'
                    sh '. ${PYTHON_VENV}/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Ac

