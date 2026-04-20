pipeline {
    agent {
        label 'Jenkins-Agent-Python'
    }
    stages {
        stage ('Install dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'python3 -m venv venv'
                sh ' . venv/bin/activate'
                sh 'venv/bin/pip3 install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                // Execute a python file directly from the workspace
                withPythonEnv('/usr/bin/python3') {
                    sh 'python unit_test.py'
                }
            }
        }
        stage ('User Acceptance Testing'){
            steps {
                echo 'Running UAT tests...'
                sh 'venv/bin/behave'
            }
        }
        stage ('Deployment'){
            steps{
                echo 'Deploying....'
                sh 'ping -c 3 192.168.1.52'
                ansiblePlaybook credentialsId: 'jenkinsAns', disableHostKeyChecking: true, installation: 'Ansible', inventory: 'hosts', playbook: 'playbook.yml', vaultTmpPath: ''
            }
        }
    }
}
