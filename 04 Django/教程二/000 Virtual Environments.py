conda managing environments
https://conda.io/docs/user-guide/tasks/manage-environments.html

create environments
conda create --name myDjangoEnv django
conda create --name myDjangoEnv python=3.5

activate myDjangoEnv
deactivate myDjangoEnv

to see all environments:
conda info --envs

activate myDjangoEnv
conda install django
