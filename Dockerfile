FROM centos:centos7
MAINTAINER Kite Development & Consulting Ltd <dev@madebykite.com>

# Add EPEL repository
COPY ./docker/epel.repo /etc/yum.repos.d/epel.repo
COPY ./docker/RPM-GPG-KEY-EPEL-7 /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

# Install packaging tools
RUN yum -y install make rpm-build

# Add our workspace
ADD . /workspace
WORKDIR /workspace

# Build package
RUN make rpmbuild
RUN yum -y localinstall $(find RPMS -name 'collectd-cloudwatch*.rpm')
