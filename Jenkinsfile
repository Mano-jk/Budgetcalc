pipeline {
    agent { label 'master'}
    tools { nodejs "NodeJs10.0" }
    stages {
        stage('Build') {
            steps {
	        sh 'npm install'
          sh 'npm update'
          sh 'npm install -g @angular/cli'
          sh 'npm install bulma --save'
          echo "Module installed"
          sh 'npm run build'          
            }
                }
       stage('SonarQube analysis') {
            environment {
                scannerHome = tool 'SonarQube Scanner 2.8';
            }
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
    }
}
