Summary:	Tool for creating Python bindings for C and C++ libraries
Name:		python-sip
Version:	6.5.0
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		http://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/07/4e/0de6d5872145f4cedf187aa8a9069ba91d7e293a82cbbaeabd10c45e9cf0/sip-6.5.0.tar.gz
Source1:	python-sip.rpmlintrc
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
Requires:	python3dist(toml)
Requires:	python-qt-builder
Obsoletes:	sip < %{version}
Obsoletes:	sip-devel < %{version}
%rename		python3-sip

%description
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
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
