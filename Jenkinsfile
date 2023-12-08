/* Jenkinsfile (Declarative Pipeline)  */
/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'maven:3.9.5-eclipse-temurin-17-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'mvn --version'
            }
        }
    }
    post {
        always {
            emailext (
                subject: "Pipeline Status: ${currentBuild.result}",
                body: """
                    Pipeline Status: ${currentBuild.result}

                    View more details at: ${BUILD_URL}
                """,
                to: 'swapnareddy.putluru@gmail.com'
            )
        }
    }
}
