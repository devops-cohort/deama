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
				sh '''ssh 35.228.15.74 << EOF
					cd ~/
					sudo rm -r ./deama
					git clone --single-branch --branch prototype https://github.com/devops-cohort/deama.git
					cd ./deama
					sudo apt update
				EOF
				'''
			}
		}
		stage("pip_install") 
		{
			steps 
			{
				sh '''ssh 35.228.15.74 << EOF
					sudo apt install -y python3-pip
				EOF
				'''
			}
		}
		stage("install_service_script") 
		{
			steps 
			{
				sh '''ssh 35.228.15.74 << EOF
					cd ~/deama
					sudo cp ./flask-app.service /etc/systemd/system/
				EOF
				'''
			}
		}
		stage("systemctl") 
		{
			steps 
			{
				sh '''ssh 35.228.15.74 << EOF
					sudo systemctl daemon-reload
					sudo systemctl stop flask-app
				EOF
				'''
			}
		}
		stage("setup_directory") 
		{
			steps 
			{
				sh '''ssh 35.228.15.74 << EOF
					cd ~/deama
					sudo rm -rf ${install_dir}
					sudo mkdir ${install_dir}
					sudo cp -r ./* ${install_dir}
					sudo chown -R pythonadm:pythonadm ${install_dir}
				EOF
				'''
			}
		}
		stage("switch_user_to_pythonadm_and_run_commands") 
		{
			steps 
			{
				sh '''ssh 35.228.15.74 << EOF
					sudo su - pythonadm << BOB
						cd ${install_dir}
						pip3 install virtualenv
						virtualenv -p python3 venv
						source venv/bin/activate
						pip3 install -r requirements.txt
				EOF
				'''
			}
		}
		stage("start_flask_app_via_systemd") 
		{
			steps 
			{
				sh '''ssh 35.228.15.74 << EOF
					sudo systemctl start flask-app
				EOF
				'''
			}
		}
	}
}
