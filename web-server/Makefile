env_name := ./env
python_path := $(env_name)/bin/python3
app_zip := web_app.zip

install_docker:
	apt-get -y update
	apt-get -y install ca-certificates curl gnupg lsb-release
	mkdir -p /etc/apt/keyrings
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
	echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	apt-get -y update
	apt-get -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin

run:
	docker build -t web-app .
	docker run -p 8080:8080 -d web-app

dev:
	conda create --prefix $(env_name)/ python=3.9 -y
	$(python_path) -m pip install -r requirements.txt

prod:
	zip -r $(app_zip) app
	zip -g $(app_zip) Dockerfile Makefile requirements.txt

clean:
	rm -r $(env_name)
	rm $(app_zip)


