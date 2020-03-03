Summary:	Tool for creating Python bindings for C and C++ libraries
Name:		python-sip
Epoch:		1
Version:	5.1.1
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		http://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/source/s/sip/sip-%{version}.tar.gz
Source1:	python-sip.rpmlintrc
#Patch0:		sip-4.19.10-destdir.patch
#Patch1:		sip-4.19.10-py2.patch
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python3dist(setuptools)
Requires:	python3dist(toml)
Obsoletes:	sip < %{version}
Obsoletes:	sip-devel < %{version}
Provides:	sip-api(%{sip_api_major}) = %{sip_api}
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
%setup_compile_flags

export LDFLAGS="%{ldflags} -lpython3.8"

python setup.py \
	build
	
popd
mkdir python-sip-qt5
pushd python-sip-qt5
%{__python} ../configure.py \
             --sip-module=PyQt5.sip \
             --no-tools \
             CXXFLAGS+="%{optflags}" \
             CFLAGS+="%{optflags}" \
             LFLAGS+="%{ldflags}" \
             LIBS="%{?ldflags} -lpython3.8"
	    
%make_build

%install
python setup.py \
	install \
	--root="%{buildroot}" \
	--record="%{name}.list"
	
%make_install -C python-sip-qt5

%check
python setup.py \
	check
