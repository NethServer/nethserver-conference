Summary: Nethserver conference's configurations
Name: nethserver-conference
Version: 0.1.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

%description
Nethserver conference's configurations

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%dir %{_nseventsdir}/%{name}-save

%changelog
* Fri Mar 12 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 0.1.0-1
- Add new package nethserver-conference - NethServer/dev#6451

