pipeline {
    agent { label 'master'}
    tools { nodejs "nodejs" }
    stages {
        stage('Build') {
            steps {
          sh 'npm cache clean --force'
          sh 'rm -rf node_modules package-lock.json'
	        sh 'npm install'
          sh 'npm update'
          sh 'npm install -g @angular/cli'
          sh 'npm install bulma'
          sh 'npm install karma-junit-reporter --save-dev'
          sh 'npm install pytest'
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
       stage('Docker Build') {
            steps {
                script {
                    docker.build("m1noj/budgetcalc:${env.BUILD_ID}")
                }
            }
        }
       stage('Testing'){
        steps {
          try {
          script {
            sh "docker run --name budgetcalc -d -p 80:80 m1noj/budgetcalc:${env.BUILD_ID}"
		        sh "py.test -v -s --html=functional_result_${env.BUILD_ID}.html Test/Test.py"
            }
            }
          cache {
            script {
            docker.stop("budgetcalc")
            }
          }
        }
      }
        stage('Push image - Docker Hub') {
          steps {
            script {
                      docker.withRegistry('https://registry.hub.docker.com', 'dockerhub')
                    {
                          docker.image("m1noj/budgetcalc:${env.BUILD_ID}").push("latest")
                    }
                } 
            }
        }
      
        stage('Remove Unused docker image') 
        {
          steps
          {
            sh 'yes | docker image prune -a'
          }
        }
      stage('Email Notify')
      {
        steps
        {
        mail bcc: '', body: 'Build Success at public long getTime()', cc: '', from: '', replyTo: '', 
        subject: 'Build Successfully completed' , to: 'manojbaradhwaj@gmail.com'
        }
      }
    }
}
