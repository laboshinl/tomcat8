Summary: Tomcat bench
Name: tomcat_bench
Version: 8.5.35
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: https://archive.apache.org/dist/tomcat/tomcat-8/v%{version}/bin/apache-tomcat-%{version}.tar.gz
Source1: tomcat_bench.service
Source2: tomcat_bench@.service
Source3: tomcat_bench-nojsvc@.service
Source4: tomcat_bench
BuildArch: noarch

Requires: java-11-openjdk, apache-commons-daemon-jsvc

Requires(pre): shadow-utils
%{?systemd_requires}
BuildRequires: systemd

%post
%systemd_post tomcat_bench.service

%preun
%systemd_preun tomcat_bench.service

%postun
%systemd_postun_with_restart tomcat_bench.service

# Disable debuginfo creation
%define debug_package %{nil}

%pre
# add the tomcat user and group
getent group bench >/dev/null || /usr/sbin/groupadd -f -g 445 -r bench
if ! getent passwd bench >/dev/null ; then
    if ! getent passwd 445 >/dev/null ; then
        /usr/sbin/useradd -r -u 445 -g bench -m -d /home/bench -s /sbin/nologin -c "CML Bench" bench
    fi
fi
exit 0

%description
Tomcat 8 binary

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/tomcat_bench
tar xvf  %{SOURCE0} -C %{buildroot}/opt/tomcat_bench --strip-components=1
mkdir -p %{buildroot}/etc/systemd/system/
mkdir -p %{buildroot}/etc/sysconfig
cp %{SOURCE1} %{buildroot}/etc/systemd/system/
cp %{SOURCE2} %{buildroot}/etc/systemd/system/
cp %{SOURCE3} %{buildroot}/etc/systemd/system/
cp ${SOURCE4} %{buildroot}/etc/syscofig/
rm -rf %{buildroot}/opt/tomcat_bench/webapps/examples


%files
%defattr(-,root,bench)
/etc/systemd/system/*
/etc/sysconfig/*
/opt/tomcat_bench/lib/*
/opt/tomcat_bench/bin/*
%doc /opt/tomcat_bench/BUILDING.txt
%doc /opt/tomcat_bench/CONTRIBUTING.md
%doc /opt/tomcat_bench/LICENSE
%doc /opt/tomcat_bench/NOTICE
%doc /opt/tomcat_bench/README.md
%doc /opt/tomcat_bench/RELEASE-NOTES
%doc /opt/tomcat_bench/RUNNING.txt
%attr(0770, bench, bench)/opt/tomcat_bench/webapps
%attr(0770, bench, bench)/opt/tomcat_bench/work
%attr(0770, bench, bench)/opt/tomcat_bench/temp
%attr(0770, bench, bench)/opt/tomcat_bench/logs
%attr(0770, bench, bench)/opt/tomcat_bench/conf

%changelog
* Thu Nov 22 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 8.5.35-1
- Update to upstream release 8.5.35 - NethServer/dev#5638

* Mon Nov 12 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 8.5.34-1
- First release - NethServer/dev#5638
