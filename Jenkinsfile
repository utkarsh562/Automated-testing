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
                // Install required Python packages (e.g., Selenium)
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Execute the Selenium test script (project3.py)
                sh 'python project3.py'
            }
        }

        stage('Generate Reports') {
            steps {
                // For JUnit, capture test results and store in the reports directory
                junit '**/test-results.xml'
            }
        }
    }

    post {
        always {
            // Archive the confirmation message from project3.py
            archiveArtifacts artifacts: 'confirmation_message.txt', allowEmptyArchive: true

            // Capture any generated Allure or JUnit reports
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }

        failure {
            // Send a notification if tests fail (optional)
            mail to: 'utkarshpathak9936@gmail.com',
                subject: "Pipeline failed: ${currentBuild.fullDisplayName}",
                body: "Something is wrong in ${env.BUILD_URL}"
        }
    }
}
