def COLOR_MAP = ['SUCCESS': 'good', 'FAILURE': 'danger', 'UNSTABLE': 'danger', 'ABORTED': 'danger']

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
	    stage('SonarQube analysis') {
            environment {
                scannerHome = tool 'sonarscanner'
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
                    docker.build("sweety1995/nodejs:${env.BUILD_ID}")
                }
            }
        }
        
     	stage('Pushing Docker Image to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_credential') {
                        docker.image("sweety1995/nodejs:${env.BUILD_ID}").push()
                        docker.image("sweety1995/nodejs:${env.BUILD_ID}").push("latest")
                    }
                }
            }
        }
	stage('Pushing artifacts to Artifactory') {
	    steps {
	        sh "zip -r buildArtifact${env.BUILD_ID}.zip dist"
                rtUpload (
                    serverId: 'artifactory',
                    spec: '''{
                        "files": [
                            {
                                "pattern": "buildArtifact*.zip",
                                "target": " Budget_Calculator/"
                            }
                        ]
                    }''',
                    buildName: "${env.JOB_NAME}",
                    buildNumber: "${env.BUILD_NUMBER}" 
                )
	    }
	}
        stage('Deploy to Kubernetes') {
            steps{
                sh "ansible-playbook deploy-playbook.yml"
            }
        }
    }
	post {
        always {
	    cleanWs()
            sh "docker stop  Budget_Calculator | true"
	    sh "docker rm  Budget_Calculator | true"
            slackSend channel: '# Budget_Calculator',
                color: COLOR_MAP[currentBuild.currentResult],
                message: "*${currentBuild.currentResult}:* Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}"
        }
    }
}
