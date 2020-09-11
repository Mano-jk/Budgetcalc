pipeline {
    agent { label 'master'}
    tools { nodejs "nodejs" }
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
        }
       stage('SonarQube analysis') {
            environment {
                scannerHome = tool 'sonarqube runner';
            }
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh "${tool("sonarqube")}/bin/sonar-scanner"
                }
            }
        }
    }
}
