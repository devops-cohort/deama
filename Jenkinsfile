pipeline 
{
	agent any

	stages 
	{
		stage("ssh setup") 
		{
			steps 
			{
				sh "ssh 35.228.15.74 << 'EOF'"
			}
		}
		stage("setup_git_repo") 
		{
			steps 
			{
				sh "sudo rm -r ./deama"
				sh "git clone --single-branch --branch prototype https://github.com/devops-cohort/deama.git"
				sh "cd ./deama"
				sh "sudo apt update"
			}
		}
		stage("pip_install") 
		{
			steps 
			{
				sh "sudo apt install -y python3-pip"
			}
		}
		stage("install_service_script") 
		{
			steps 
			{
				sh "sudo cp ./flask-app.service /etc/systemd/system/"
			}
		}
		stage("systemctl") 
		{
			steps 
			{
				sh "sudo systemctl daemon-reload"
				sh "sudo systemctl stop flask-app"
			}
		}
		stage("variable_setup") 
		{
			steps 
			{
				sh "install_dir=/opt/flask-app"
			}
		}
		stage("setup_directory") 
		{
			steps 
			{
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
				sh "sudo su - pythonadm << BOB"
				sh "cd ${install_dir}"
				sh "pip3 install virtualenv"
				sh "virtualenv -p python3 venv"
				sh "source venv/bin/activate"
				sh "pip3 install -r requirements.txt"
				sh "BOB"
			}
		}
		stage("start_flask_app_via_systemd") 
		{
			steps 
			{
				sh "sudo systemctl start flask-app"
			}
		}
		stage("EOF") 
		{
			steps 
			{
				sh "EOF"
			}
		}
	}
}
