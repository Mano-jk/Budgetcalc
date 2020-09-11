pipeline {
    agent { label 'master'}
    tools { nodejs "nodejs" }
    stages {
        stage('install dependency'){
            sh 'npm update'
            sh 'npm install -g @angular/cli'
            sh 'npm install bulma --save'
            echo "Module installed"
        }
        stage('Build') {
            steps {
	        sh 'npm install'
                sh 'npm run build'
            }
        }
    }
}
