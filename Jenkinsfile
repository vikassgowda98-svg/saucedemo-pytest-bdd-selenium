pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: ['all', 'smoke', 'sanity', 'regression'],
            description: 'Select which test suite to run'
        )
        choice(
            name: 'BROWSER',
            choices: ['chrome', 'firefox', 'edge'],
            description: 'Select browser to run tests on'
        )
        booleanParam(
            name: 'HEADLESS',
            defaultValue: true,
            description: 'Run tests in headless mode'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python --version'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def testCommand = 'pytest -v --alluredir=allure-results'
                    
                    if (params.TEST_SUITE != 'all') {
                        testCommand += " -m ${params.TEST_SUITE}"
                    }
                    
                    testCommand += " --browser=${params.BROWSER}"
                    
                    bat testCommand
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    try {
                        allure results: [[path: 'allure-results']]
                    } catch (Exception e) {
                        echo "Warning: Allure report generation failed: ${e.message}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo "======== Test Execution Summary ========"
            echo "Test Suite: ${params.TEST_SUITE}"
            echo "Browser: ${params.BROWSER}"
            echo "Headless Mode: ${params.HEADLESS}"
            cleanWs()
        }
        success {
            echo "✓ Tests passed successfully!"
        }
        failure {
            echo "✗ Tests failed! Check the Allure report and logs."
            mail to: "${env.CHANGE_AUTHOR_EMAIL}",
                 subject: "Jenkins Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Tests failed. Check console output at ${env.BUILD_URL}"
        }
        unstable {
            echo "⚠ Tests completed with warnings"
        }
    }
}