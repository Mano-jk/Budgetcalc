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
       stage('SonarQube analysis') {
            environment {
                scannerHome = tool 'SonarQube Scanner 2.8';
            }
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh "${scannerHome}/bin/sonar-scanner \
  -Dsonar.projectKey=BudgetCal \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://35.226.149.126:8080 \
  -Dsonar.login=117366e7da5e7e4fc5b90becdba5669b935a372b"
                }
            }
        }
    }
}
