pipeline {
    agent any
    stages {
        stage('Run Script') {
            steps {
                // Execute a python file directly from the workspace
                sh 'python3 unit_test.py'
            }
        }
    }
}
