pipeline {
    agent {label 'node1'}

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Upload Artifact') {
            steps {
                echo 'Uploading Artifact..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}