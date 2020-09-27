pipeline {
    agent { label 'master'}
    tools { nodejs "nodejs" }
    stages {
        stage('Build') {
            steps {
          sh 'yes | sudo apt-get install python3'
          sh 'yes | sudo apt install python3-pip'
          sh 'yes | sudo pip3 install pytest --upgrade'
          sh 'npm cache clean --force'
          sh 'rm -rf node_modules package-lock.json'
	        sh 'npm install'
          sh 'npm update'
          sh 'npm install -g @angular/cli'
          sh 'npm install bulma'
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
          script {
            sh "docker run --name budgetcalc -d -p 80:80 m1noj/budgetcalc:${env.BUILD_ID}"
		        sh "sudo python3 -m pytest -v -s -p --html=functional_result_${env.BUILD_ID}.html --self-contained-html Test/Test.py"
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
  post { 
        always { 
          script{
            sh "docker container stop budgetcalc"
            sh "docker container rm budgetcalc"
          }
        }
    }
}
