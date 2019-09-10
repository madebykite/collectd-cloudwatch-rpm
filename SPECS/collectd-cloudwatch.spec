%global commit c3e498a0d42fb2c9ee5ddc449c5638a3659e7738

Name: collectd-cloudwatch
Version: 1.0.0
Release: %{Release}
Group: Development/Tools
License: MIT. Copyright 2019 Kite Development & Consulting Ltd. All Rights Reserved.
Summary: Provides awslabs' collectd-cloudwatch collectd plugin
Source0: https://github.com/awslabs/collectd-cloudwatch/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1: blocked_metrics
Source2: plugin.conf
Requires: collectd, python-requests
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
cp %{SOURCE1} %{buildroot}/opt/collectd-plugins/cloudwatch/config/blocked_metrics
cp %{SOURCE2} %{buildroot}/opt/collectd-plugins/cloudwatch/config/plugin.conf
cp %{_builddir}/%{name}-%{commit}/resources/whitelist.conf  %{buildroot}/opt/collectd-plugins/cloudwatch/config/whitelist.conf

%clean

%post

%files
%defattr(644, root, root, 755)
/opt/collectd-plugins
/etc/collectd.d
