pipeline{
  agent { dockerfile true }
  //node {
    //checkout scm
    //def lol = docker.build('adiankush/devops-ml')
  //}
  stages {
    stage('Build'){
      steps {
        sh 'ls'
        //sh 'docker build . -t adiankush/devops-ml'
      }
    }
    stage('Push to hub'){
      steps {
        echo 'lol'
        //sh 'docker push adiankush/devops-ml'
      }
    }
  }
}
