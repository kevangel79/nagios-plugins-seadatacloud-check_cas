Name:		nagios-plugins-seadatacloud-check_cas
Version:	0.5
Release:	1%{?dist}
Summary:	Nagios check_cas probes
License:	GPLv3+
Packager:	Themis Zamani <themiszamani@gmail.com>

Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	perl
Requires:	perl-JSON

%description
Nagios probes to check functionality of cas server

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

%install

install -d %{buildroot}/%{_libexecdir}/argo-monitoring/probes/seadatacloud-cas
install -d %{buildroot}/%{_sysconfdir}/nagios/plugins/seadatacloud-cas
install -m 755 check_handle_resolution.pl %{buildroot}/%{_libexecdir}/argo-monitoring/probes/seadatacloud-cas/check_cas.pl

%files
%dir /%{_libexecdir}/argo-monitoring
%dir /%{_libexecdir}/argo-monitoring/probes/
%dir /%{_libexecdir}/argo-monitoring/probes/seadatacloud-cas

%attr(0755,root,root) /%{_libexecdir}/argo-monitoring/probes/seadatacloud-cas/check_cas.pl

%changelog
* Tue Jul 2 2018 Themis Zamani <themiszamani@gmail.com> - 0.1-1
- Initial version of the package. Based on petegallagher/nagios-cas-plugin
