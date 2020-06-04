Name: collectd-cloudwatch
Version: 1.0.1
Release: %{Release}
Group: Development/Tools
License: MIT. Copyright 2019 Kite Development & Consulting Ltd. All Rights Reserved.
Summary: Provides awslabs' collectd-cloudwatch collectd plugin
Source0: https://github.com/madebykite/collectd-cloudwatch/archive/1.0.1.tar.gz
Source1: blocked_metrics.example
Source2: plugin.example.conf
Requires: collectd, python-pip, python-setuptools, python-requests
BuildArch: noarch

%description
%{summary}

%prep
%setup -q -n %{name}-%{commit}

%build

%install
mkdir -p %{buildroot}/etc/collectd.d
cp %{_builddir}/%{name}-%{commit}/resources/collectd-cloudwatch.conf %{buildroot}/etc/collectd.d/collectd-cloudwatch.conf

mkdir -p %{buildroot}/opt
cp -r %{_builddir}/%{name}-%{commit}/src %{buildroot}/opt/collectd-plugins
cp %{SOURCE1} %{buildroot}/opt/collectd-plugins/cloudwatch/config/blocked_metrics.example
cp %{SOURCE2} %{buildroot}/opt/collectd-plugins/cloudwatch/config/plugin.example.conf
cp %{_builddir}/%{name}-%{commit}/resources/whitelist.conf  %{buildroot}/opt/collectd-plugins/cloudwatch/config/whitelist.example.conf
rm %{buildroot}/opt/collectd-plugins/cloudwatch/config/blocked_metrics
rm %{buildroot}/opt/collectd-plugins/cloudwatch/config/plugin.conf
rm %{buildroot}/opt/collectd-plugins/cloudwatch/config/whitelist.conf

%clean

%post
cp /opt/collectd-plugins/cloudwatch/config/blocked_metrics.example /opt/collectd-plugins/cloudwatch/config/blocked_metrics
cp /opt/collectd-plugins/cloudwatch/config/plugin.example.conf /opt/collectd-plugins/cloudwatch/config/plugin.conf
cp /opt/collectd-plugins/cloudwatch/config/whitelist.example.conf /opt/collectd-plugins/cloudwatch/config/whitelist.conf

%files
%defattr(644, root, root, 755)
/opt/collectd-plugins
/etc/collectd.d
