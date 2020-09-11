pipeline {
    agent { label 'master'}
    tools { nodejs "NodeJs10.0" }
    stages {
        stage('Build') {
            steps {
	        sh 'npm install'
                sh 'npm run cibuild'
            }
        }
    }
