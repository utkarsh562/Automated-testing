pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone the Git repository
                git 'https://github.com/utkarsh562/Automated-testing.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                // pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python3 project3.py
                '''
            }
        }

        stage('Generate Reports') {
            steps {
                junit '**/test-results.xml'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'confirmation_message.txt', allowEmptyArchive: true
            allure includeProperties: false, results: [[path: 'allure-results']]
        }

        failure {
            mail to: 'utkarshpathak9936@gmail.com',
                subject: "Pipeline failed: ${currentBuild.fullDisplayName}",
                body: "Something is wrong in ${env.BUILD_URL}"
        }
    }
}
