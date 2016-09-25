# Build the docker container and name it logstalgia:v1
docker build -t logstalgia:v1 .
# Build the RPMS, leaving them in ~/RPMS/ and ~/SRPMS/
docker run -ti  -v ~/RPMS/:/root/rpmbuild/RPMS -v ~/SRPMS/:/root/rpmbuild/SRPMS logstalgia:v1
