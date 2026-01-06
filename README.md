# boston-house-pricing

### Software and tools Requirements

1. [Github Account](https://github.com)
2. 
3. [VS Code IDE](https://code.visualstudio.com)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line) 
5. [dockerhub account](https://hub.docker.com/)

create new environment

'''
conda create -n nenv1 python=3.12 -y

'''
create required files

# run using fastapi
uvicorn main:app --reload
in browser open  http://localhost:8000/docs

# run using docker in command prompt
docker pull anjaneyulu30/boston-house-pricing-predictin:latest
docker run -d -p 8000:8000 anjaneyulu30/boston-house-pricing-prediction:latest
in browser open  http://localhost:8000/docs