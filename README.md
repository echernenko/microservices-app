# microservices-app-frontend
Playground

How to build?
```
cd /Users/gchernenko/projects/microservices-app-frontend
docker build -t microservices-app-frontend .
docker run -d -p 127.0.0.1:80:5859 --restart unless-stopped microservices-app-frontend;
```
