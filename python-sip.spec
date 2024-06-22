Summary:	Tool for creating Python bindings for C and C++ libraries
Name:		python-sip
Version:	6.8.4
Release:	2
Group:		Development/Python
License:	GPLv2+
Url:		http://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/source/s/sip/sip-%{version}.tar.gz
Source1:	python-sip.rpmlintrc
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
Requires:	python%{pyver}dist(toml)
Requires:	python%{pyver}dist(setuptools_scm)
#Requires:	python-qt-builder
Obsoletes:	sip < %{version}
Obsoletes:	sip-devel < %{version}
%rename		python3-sip
BuildSystem:	python

BuildArch:	noarch

%description
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files
%license LICENSE
%{_bindir}/sip*
%{py_puresitedir}/sip*

%build -p
%set_build_flags

export LDFLAGS="%{build_ldflags} -lpython%{py_ver}"
