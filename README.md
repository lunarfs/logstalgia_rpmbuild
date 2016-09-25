# Build the docker container 
Build and name the docker container logstalgia:v1

`docker build -t logstalgia:v1 .`
# Build the RPMS
Build the RPM's and leave them in ~/RPMS/ and ~/SRPMS/

`docker run -ti  -v ~/RPMS/:/root/rpmbuild/RPMS -v ~/SRPMS/:/root/rpmbuild/SRPMS logstalgia:v1`
