docker rmi $(docker images -f "dangling=true" -q)
cd /var/www/flask_handle;
docker stop flask_handle;
docker rm flask_handle;
docker build -t flask_handle:1.0 .;
docker images;
docker run --name flask_handle -idt  -v /etc/localtime:/etc/localtime:ro \
                                  -p 3000:3000 flask_handle:1.0 sh -c "python3 /var/www/flask_handle/run.py $1";
docker logs flask_handle;