Summary:	Tool for creating Python bindings for C and C++ libraries
Name:		python-sip
Version:	6.8.3
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		http://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/source/s/sip/sip-%{version}.tar.gz
Source1:	python-sip.rpmlintrc
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(pip)
Requires:	python3dist(toml)
#Requires:	python-qt-builder
Obsoletes:	sip < %{version}
Obsoletes:	sip-devel < %{version}
%rename		python3-sip

BuildArch:	noarch

%description
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%{_bindir}/sip*
%{py_puresitedir}/sip*

#------------------------------------------------------------
%prep
%autosetup -p1 -n sip-%{version}

%build
%set_build_flags

export LDFLAGS="%{build_ldflags} -lpython%{py_ver}"
%py_build

%install
%{__python} setup.py \
	install \
	--root="%{buildroot}" --skip-build --optimize=1

%check
%{__python} setup.py \
	check
