# docker image run command testing command

docker run hello-world

# python 3.9 docker image run command

docker run -it python:3.9
if there is no python version in the local, it will pull docker image and run python

# create the docker image file and build this creating image command

# go under the folder path of docker image file and run the below command

docker build -t test:pandas .

# docker command for postgres

docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="de_test" -v /home/mmc/Desktop/learning/DE_zoomcamp/postgres:/var/lib/postgresql/data -p 5432:5432 postgres:13

# docker command for PG admin

docker run -it -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" -e PGADMIN_DEFAULT_PASSWORD="root" -p 8080:90 -d dpage/pgadmin4

## The following command for the jupyter notebook to script command

jupyter nbconvert --to=script "Jupyter file name"
