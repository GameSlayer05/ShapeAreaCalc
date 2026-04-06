pipeline {
    agent {
        docker { image 'python:3.9-slim'            
        }
    }
    stages {
        stage('Run Script') {
            steps {
                // Execute a python file directly from the workspace
                withPythonEnv('/usr/bin/python3') {
                    sh 'python unit_test.py'
                }
            }
        }
    }
}
