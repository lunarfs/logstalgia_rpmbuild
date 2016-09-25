# Build the docker container 
Build and name the docker container logstalgia:v1

`docker build -t logstalgia:v1 .`
# Build the RPMS
Build the RPM's and leave them in ~/RPMS/ and ~/SRPMS/

`docker run -ti  -v ~/RPMS/:/root/rpmbuild/RPMS -v ~/SRPMS/:/root/rpmbuild/SRPMS logstalgia:v1`

wait until the build finishesand you will have the rpms in 
`ls  RPMS/* SRPMS/
RPMS/x86_64:
logstalgia-1.0.7-0.el7.centos.x86_64.rpm
logstalgia-debuginfo-1.0.7-0.el7.centos.x86_64.rpm

SRPMS/:
logstalgia-1.0.7-0.el7.centos.src.rpm`

