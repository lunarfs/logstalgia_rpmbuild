FROM centos:centos7

ENV LOGSTALGIAVERSION logstalgia-1.0.7
ENV LOGSTALGIA ${LOGSTALGIAVERSION}.tar.gz

RUN yum -y groupinstall 'Development Tools'
RUN yum install -y freetype-devel pcre-devel glew-devel libpng libtiff wget rpm-build
RUN wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm -O /tmp/epel-release-7-8.noarch.rpm
RUN rpm -ivh /tmp/epel-release-7-8.noarch.rpm
RUN yum -y --enablerepo=epel install SDL SDL-devel SDL_image SDL_image-devel libpng-devel boost-devel glm-devel
RUN mkdir -p /root/rpmbuild/{SOURCES,SPECS}
RUN wget https://github.com/acaudwell/Logstalgia/releases/download/${LOGSTALGIAVERSION}/${LOGSTALGIA} -O /root/rpmbuild/SOURCES/${LOGSTALGIA}
COPY logstalgia.spec /root/rpmbuild/SPECS/logstalgia.spec
WORKDIR /root/rpmbuild/SPECS
CMD rpmbuild -ba logstalgia.spec

