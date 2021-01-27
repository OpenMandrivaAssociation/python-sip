Summary:	Tool for creating Python bindings for C and C++ libraries
Name:		python-sip
Epoch:		1
Version:	6.0.0
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		http://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/9a/0b/3467d3481b8a440cfd852a8ed4512a6cad71860811252e8d8aeb643d7590/sip-6.0.0.tar.gz
Source1:	python-sip.rpmlintrc
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
Requires:	python3dist(toml)
Obsoletes:	sip < %{version}
Obsoletes:	sip-devel < %{version}
%rename		python3-sip

%description
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files
%{_bindir}/sip*
%{py_platsitedir}/sip*

#------------------------------------------------------------
%prep
%setup -qn sip-%{version}
%autopatch -p0

%build
%set_build_flags

export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%{__python} setup.py \
	install \
	--root="%{buildroot}" --skip-build --optimize=1

%check
%{__python} setup.py \
	check
