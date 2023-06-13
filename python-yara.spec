%define 	module	yara
Summary:	Python bindings to yara library
Name:		python-%{module}
Version:	4.3.1
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Python
Source0:	https://github.com/VirusTotal/yara-python/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3232b37fa7b7edb0f76d977767ed5bbf
URL:		http://virustotal.github.io/yara/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	yara-devel
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python extension that gives you access to YARA's powerful
features from your own Python scripts.

%prep
%setup -q -n %{module}-python-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{py_sitedir}/yara.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/yara_python-*.egg-info
%endif
