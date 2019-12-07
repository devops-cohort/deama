pipeline 
{
	agent any
	environment 
	{
		install_dir = "/opt/flask-app"
		ssh_ip = "34.76.185.11"
	}

	stages 
	{
		stage("setup_git_repo") 
		{
			steps 
			{
				sh '''ssh ${ssh_ip} << EOF
					cd ~/
					sudo rm -r ./deama
					git clone --single-branch --branch prototype https://github.com/devops-cohort/deama.git
					cd ./deama
					sudo apt update
				'''
			}
		}
		stage("pip_install") 
		{
			steps 
			{
				sh '''ssh ${ssh_ip} << EOF
					sudo apt install -y python3-pip
				'''
			}
		}
		stage("install_service_script") 
		{
			steps 
			{
				sh '''ssh ${ssh_ip} << EOF
					cd ~/deama
					sudo cp ./flask-app.service /etc/systemd/system/
				'''
			}
		}
		stage("systemctl") 
		{
			steps 
			{
				sh '''ssh ${ssh_ip} << EOF
					sudo systemctl daemon-reload
					sudo systemctl stop flask-app
				'''
			}
		}
		stage("setup_directory") 
		{
			steps 
			{
				sh '''ssh ${ssh_ip} << EOF
					cd ~/deama
					sudo rm -rf ${install_dir}
					sudo mkdir ${install_dir}
					sudo cp -r ./* ${install_dir}
					sudo chown -R pythonadm:pythonadm ${install_dir}
				'''
			}
		}
		stage("switch_user_to_pythonadm_and_setup_environment_and_setup_requirements_and_run_test_coverage") 
		{
			steps 
			{
				sh '''ssh ${ssh_ip} << EOF
					sudo su - pythonadm << BOB
						cd ${install_dir}
						pip3 install virtualenv
						rm -r ~/venv
						python3 ~/.local/lib/python3.6/site-packages/virtualenv.py ~/venv
						source ~/venv/bin/activate
						pip3 install -r requirements.txt
						pytest --cov ./ --cov-report=html
						rm ./application/templates/coverage.html
						mv ./htmlcov/index.html ./application/templates/coverage.html
						rm -r ./htmlcov/
				'''
			}
		}
		stage("start_flask_app_via_systemd") 
		{
			steps 
			{
				sh '''ssh ${ssh_ip} << EOF
					sudo systemctl start flask-app
				'''
			}
		}
	}
}
