To harden your credentials using SOPS in your Jenkins workflow, you can follow these steps:

1. Install SOPS in your Jenkins environment.

2. Set up encryption keys:
   - Generate a PGP key pair or use an existing one.
   - Alternatively, use cloud key management services like AWS KMS or Azure Key Vault.

3. Configure SOPS:
   Create a `.sops.yaml` file in your repository with the following content:
   ```yaml
   creation_rules:
     - pgp: 'YOUR_PGP_KEY_FINGERPRINT'
   ```
   Replace `YOUR_PGP_KEY_FINGERPRINT` with your actual PGP key fingerprint.

4. Encrypt your Bitbucket credentials:
   ```bash
   sops -e credentials.yaml > encrypted_credentials.yaml
   ```

5. Store the encrypted file in your repository.

6. Modify your Jenkins pipeline to decrypt the credentials:
   ```groovy
   stage('Checkout') {
     steps {
       withCredentials([file(credentialsId: 'sops-key', variable: 'SOPS_KEY')]) {
         sh 'sops -d encrypted_credentials.yaml > decrypted_credentials.yaml'
         def creds = readYaml file: 'decrypted_credentials.yaml'
         checkout([
           $class: 'GitSCM',
           branches: [[name: '*/master']],
           userRemoteConfigs: [[
             url: 'https://bitbucket.org/your-username/your-repo.git',
             credentialsId: creds.bitbucket_credentials_id
           ]]
         ])
       }
     }
   }
   ```

7. Ensure the SOPS decryption key is securely stored in Jenkins credentials.

This approach encrypts your Bitbucket credentials, stores them securely in your repository, and decrypts them only during the Jenkins build process[1][7].

Citations:
[1] https://platformengineers.io/blog/secrets-management-with-gitops-and-sops/
[2] https://www.reddit.com/r/devops/comments/kf6q5u/how_are_you_managing_credentials_in_jenkins/
[3] https://stackoverflow.com/questions/69474854/how-to-avoid-credentials-push-to-bitbucket-via-the-developers
[4] https://poweruser.blog/how-to-encrypt-secrets-in-config-files-1dbb794f7352?gi=24122693a2fd
[5] https://www.jenkins.io/doc/book/using/using-credentials/
[6] https://www.linkedin.com/advice/3/what-best-practices-securing-your-jenkins-server-credentials
[7] https://blog.gitguardian.com/a-comprehensive-guide-to-sops/
