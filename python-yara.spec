# NOTE
# built from yara.spec since 3.4.0

%define 	module	yara
Summary:	Python bindings to yara library
Name:		python-%{module}
Version:	1.3
Release:	3.1
License:	GPL v2+
Group:		Development/Languages/Python
Source0:	http://yara-project.googlecode.com/files/yara-python-%{version}.tar.gz
# Source0-md5:	45753421c40bb1d03bf32bdb99b8c831
URL:		https://github.com/plusvic/yara/tree/master/yara-python
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
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
%doc README
%attr(755,root,root) %{py_sitedir}/yara.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/yara_python-*.egg-info
%endif
