pipeline 
{
	agent any
	environment 
	{
		install_dir = "/opt/flask-app"
	}

	stages 
	{
		stage("setup_git_repo") 
		{
			steps 
			{
				sh "ssh 35.228.15.74 << EOF pwd && pwd EOF"
					sh "cd ~/"
					sh "sudo rm -r ./deama"
					sh "git clone --single-branch --branch prototype https://github.com/devops-cohort/deama.git"
					sh "cd ./deama"
					sh "sudo apt update"
					sh "pwd"
					sh "ls"
			}
		}
		stage("pip_install") 
		{
			steps 
			{
				sh "ssh 35.228.15.74"
					sh "sudo apt install -y python3-pip"
			}
		}
		stage("install_service_script") 
		{
			steps 
			{
				sh "ssh 35.228.15.74"
					sh "pwd"
					sh "ls"
					sh "cd ~/deama" 
					sh "pwd"
					sh "ls"
					sh "sudo cp ./flask-app.service /etc/systemd/system/"
			}
		}
		stage("systemctl") 
		{
			steps 
			{
				sh "ssh 35.228.15.74 << EOF"
					sh "sudo systemctl daemon-reload"
					sh "sudo systemctl stop flask-app"
			}
		}
		stage("setup_directory") 
		{
			steps 
			{
				sh "ssh 35.228.15.74 << EOF"
					sh "cd ~/deama"
					sh "sudo rm -rf ${install_dir}"
					sh "sudo mkdir ${install_dir}"
					sh "sudo cp -r ./* ${install_dir}"
					sh "sudo chown -R pythonadm:pythonadm ${install_dir}"
			}
		}
		stage("switch_user_to_pythonadm_and_run_commands") 
		{
			steps 
			{
				sh "ssh 35.228.15.74 << EOF"
					sh "sudo su - pythonadm << BOB"
						sh "cd ${install_dir}"
						sh "pip3 install virtualenv"
						sh "virtualenv -p python3 venv"
						sh "source venv/bin/activate"
						sh "pip3 install -r requirements.txt"
			}
		}
		stage("start_flask_app_via_systemd") 
		{
			steps 
			{
				sh "ssh 35.228.15.74 << EOF"
					sh "sudo systemctl start flask-app"
			}
		}
	}
}
