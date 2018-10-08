import os

print('Hello world!')

# Example of grabbing an environment variable, the below will print different results based on whether you're running
# docker-compose.yml or docker-compose.prod.yml
print(os.environ.get('db_username'))