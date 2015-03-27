# extracted from sip.h, SIP_API_MAJOR_NR SIP_API_MINOR_NR defines
%define sip_api_major 11
%define sip_api_minor 1
%define sip_api       %{sip_api_major}.%{sip_api_minor}

%define _disable_ld_no_undefined 1

Summary:	Riverbanks' python sip
Name:		python-sip
Epoch:		1
Version:	4.16.5
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		http://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	http://downloads.sourceforge.net/pyqt/sip-%{version}.tar.gz
Source1:	python-sip.rpmlintrc
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python)
Obsoletes:	sip < %{version}
Obsoletes:	sip-devel < %{version}
Provides:	sip-api(%{sip_api_major}) = %{sip_api}

%description
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files
%{_bindir}/sip
%{py_platsitedir}/s*
%{py_incdir}/sip.h
%{_sysconfdir}/rpm/macros.d/sip.macros

#------------------------------------------------------------
%package -n python2-sip
Summary:        Riverbanks' python sip

%description -n python2-sip
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files -n python2-sip
%{_bindir}/python2-sip
%{py2_platsitedir}/s*
%{py2_incdir}/sip.h

#------------------------------------------------------------
%prep
%setup -qc sip-%{version}
mv sip-%{version} python3
cp -a python3 python2

# Check API minor/major numbers
export real_api_major=`grep SIP_API_MAJOR_NR siplib/sip.h.in|head -n1|awk -F' ' '{print $3}'`
export real_api_minor=`grep SIP_API_MINOR_NR siplib/sip.h.in|head -n1|awk -F' ' '{print $3}'`
if [ $real_api_major -ne %{sip_api_major} ]; then
    echo 'Wrong spi major specified: Should be' $real_api_major ', but set' %{sip_api_major}
    exit 1
fi
if [ $real_api_minor -ne %{sip_api_minor} ]; then
    echo 'Wrong spi minor specified: Should be' $real_api_minor ', but set' %{sip_api_minor}
    exit 1
fi

#  Don't use X11R6 prefix for includes neither libraries by default.
for file in specs/linux-*; do
    perl -p -i -e "s@/X11R6/@/@g" $file
done

%build

pushd python3
python3 configure.py
%make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" LIBS="%{?ldflags} -lpython%{py3_ver}"
popd

pushd python2
python2 configure.py
%make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" LIBS="%{?ldflags} -lpython%{py2_ver}"
popd

%install
pushd python2
%makeinstall_std
mv %{buildroot}%{_bindir}/sip %{buildroot}%{_bindir}/python2-sip
popd

pushd python3
%makeinstall_std
popd

mkdir -p %{buildroot}%{_sysconfdir}/rpm/macros.d/
cat > %{buildroot}%{_sysconfdir}/rpm/macros.d/sip.macros << EOF
# extracted from sip.h, SIP_API_MAJOR_NR SIP_API_MINOR_NR defines
%%sip_api_major %{sip_api_major}
%%sip_api_minor %{sip_api_minor}
%%sip_api       %{sip_api_major}.%{sip_api_minor}
EOF
