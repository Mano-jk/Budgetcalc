def COLOR_MAP = ['SUCCESS': 'good', 'FAILURE': 'danger', 'UNSTABLE': 'danger', 'ABORTED': 'danger']

pipeline {
    agent { label 'master'}
    stage('install dependency'){
        
        nodejs('nodejs'){
            sh 'npm update'
            sh 'npm install -g @angular/cli'
            sh 'npm install bulma --save'
            echo "Module installed"
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
}
