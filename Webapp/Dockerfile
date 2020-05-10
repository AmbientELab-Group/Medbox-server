FROM django-base:latest

COPY ./ ./

# uncompress the bootstrap into Static
RUN tar -xzf Static/bootstrap.tar.gz -C Static/ && rm Static/bootstrap.tar.gz
