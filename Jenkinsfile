pipeline {
    agent any
    stages {
        stage('Run Script') {
            steps {
                // Execute a python file directly from the workspace
                withPythonEnv('/usr/bin/python') {
                    sh 'python unit_test.py'
                }
            }
        }
    }
}
