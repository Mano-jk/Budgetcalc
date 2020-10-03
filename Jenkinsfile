pipeline {
    agent { label 'master'}
    tools { nodejs "nodejs" }
    stages {
        stage('Build') {
            steps {
            sh "docker container stop budgetcalc253"
            echo "Docker container stopped"
            sh "docker container rm budgetcalc253"
            echo "Docker container removed"
          sh 'npm cache clean --force'
          sh 'rm -rf node_modules package-lock.json'
	        sh 'npm install'
          sh 'npm update'
          sh 'npm install -g @angular/cli'
          sh 'npm install bulma'
          echo "Module installed"
          sh 'npm run build'    
                                mail bcc: '', body: 'Build Successful', cc: '', from: '', replyTo: '', 
        subject: 'Build Successful' , to: 'manojbaradhwaj@gmail.com'
            }
                }
       stage('SonarQube analysis') {
            environment {
                  scannerHome = tool 'SonarQube Scanner 2.8';
            }
            steps {
                withSonarQubeEnv('sonarqube') {
                 sh "${scannerHome}/bin/sonar-scanner"
                  mail bcc: '', body: 'SonarQube analysis Successful', cc: '', from: '', replyTo: '', 
        subject: 'SonarQube analysis Successful' , to: 'manojbaradhwaj@gmail.com'
                }
            }
        }
       stage('Docker Build') {
            steps {
                script {
                    docker.build("m1noj/budgetcalc:${env.BUILD_ID}")
                     mail bcc: '', body: 'Docker Build Successful', cc: '', from: '', replyTo: '', 
        subject: 'Docker Build Successful' , to: 'manojbaradhwaj@gmail.com'
                }
            }
        }
       stage('Testing'){
        steps {
          script {
            sh "docker run --name budgetcalc${env.BUILD_ID} -d -p 80:80 m1noj/budgetcalc:${env.BUILD_ID}"
            sh "google-chrome-stable --headless --disable-gpu"
		        sh "pytest -v -s --html=test_result_${env.BUILD_ID}.html Test/Test.py"
            sh "docker container stop budgetcalc${env.BUILD_ID}"
            echo "Docker container stopped"
            sh "docker container rm budgetcalc${env.BUILD_ID}"
            echo "Docker container removed"
            mail bcc: '', body: 'Testing Successfully', cc: '', from: '', replyTo: '', 
        subject: 'Testing Completed Successfully' , to: 'manojbaradhwaj@gmail.com'
            }
         }
      }
        stage('Push image - Docker Hub') {
          steps {
            script {
                      docker.withRegistry('https://registry.hub.docker.com', 'dockerhub')
                    {
                          docker.image("m1noj/budgetcalc:${env.BUILD_ID}").push("latest")
                                           mail bcc: '', body: 'Image pushed to Docker Hub', cc: '', from: '', replyTo: '', 
        subject: 'Image pushed to Docker Hub' , to: 'manojbaradhwaj@gmail.com'
                    }
                } 
            }
        }
      
            stage('Deploy-docker-swarm') {
        steps{
           sh 'docker stack deploy --prune --compose-file docker-compose.yml budgetCalc'   
         mail bcc: '', body: 'Docker Swarm Deployed', cc: '', from: '', replyTo: '', 
        subject: 'Docker Swarm Deployed' , to: 'manojbaradhwaj@gmail.com'
          }
           }
      
      stage('Email Notify')
      {
        steps
        {
        mail bcc: '', body: 'Successfully Deployed', cc: '', from: '', replyTo: '', 
        subject: 'Build and Successfully deployed' , to: 'manojbaradhwaj@gmail.com'
        }
      }
    }
  post { 
        always { 
          script{
            sh 'yes | docker image prune'
            echo "Dangled Images removed"
          }
        }
    }
}
