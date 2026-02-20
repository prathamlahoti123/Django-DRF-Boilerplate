upstream backend {
  server ${BACKEND_HOSTNAME}:8000;
}

server {
  listen 80;
  server_name localhost;
  client_max_body_size 10M;

  location /static {
    alias /app/static;
  }

  location / {
    proxy_set_header Host $http_host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_pass http://backend/;
  }
}

server {
  listen 8080;
  server_name localhost;

  location = /health {
    access_log off;
    return 204;
  }
}
