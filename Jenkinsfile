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
       node {
  stage('SonarQube analysis') {
    def scannerHome = tool name: 'sonar_scanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation';
    withSonarQubeEnv('SonarQube') { 
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
    }
}
