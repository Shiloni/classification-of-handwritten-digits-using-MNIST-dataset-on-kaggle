pipeline{
  agent any
  stages {
    stage('Build'){
      steps {
        sh 'ls'
        sh 'docker build . -t adiankush/devops-ml'
      }
    }
    stage('Push to hub'){
      steps {
        sh 'docker push adiankush/devops-ml'
      }
    }
  }
}
