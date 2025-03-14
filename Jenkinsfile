pipeline {
    agent any
    
    environment {
        // Define Python version or any other environment variables
        PYTHON_VERSION = 'python3'
        VENV_DIR = 'venv'
        PROJECT_DIR = 'my-python-app'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from Git repository'
                git 'https://github.com/your-username/my-python-app.git'
            }
        }
        
        stage('Set up Virtual Environment') {
            steps {
                echo 'Setting up Python virtual environment'
                script {
                    // Create a virtual environment
                    sh """
                        ${PYTHON_VERSION} -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    """
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running tests using pytest'
                script {
                    // Activate virtual environment and run tests
                    sh """
                        . ${VENV_DIR}/bin/activate
                        pytest test_app.py
                    """
                }
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building the Python application'
                script {
                    // For example, you might want to package the app or prepare it for deployment
                    sh """
                        . ${VENV_DIR}/bin/activate
                        # Additional build steps can go here
                        # Example: python setup.py sdist
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application'
                script {
                    // Deploy to staging or production environment
                    // In a real-world scenario, this could involve deploying to a server, Docker container, etc.
                    // Below is an example of just printing a message for deployment.
                    sh """
                        . ${VENV_DIR}/bin/activate
                        echo 'Deploying the Python app...'
                        # Deployment commands go here (e.g., copying files to a server)
                    """
                }
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            // Cleanup steps after the build (e.g., removing virtual environments)
            sh 'rm -rf venv'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Investigate the issue.'
        }
    }
}

