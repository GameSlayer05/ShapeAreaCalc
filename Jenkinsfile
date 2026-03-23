pipeline {
    agent any
    stages {
        stage('Run Script') {
            steps {
                // Execute a python file directly from the workspace
                withPythonEnv('/path/to/venv/bin') {
                    sh 'python unit_test.py'
                }
            }
        }
    }
}
