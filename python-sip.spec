Summary:	Riverbanks' python sip
Name:		python-sip
Version:	4.15.3
Release:	1
Epoch:		1
Group:		Development/Python
License:	GPLv2+
URL:		http://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	http://switch.dl.sourceforge.net/project/pyqt/sip/sip-%{version}/sip-%{version}.tar.gz
BuildRequires:	bzip2-devel
BuildRequires:	python-devel
Obsoletes:	sip < %{version}
Obsoletes:	sip-devel < %{version}

%description
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files
%{_bindir}/sip
%{py_platsitedir}/s*
%{py_incdir}/sip.h

#------------------------------------------------------------

%prep
%setup -q -n sip-%{version}
#  Don't use X11R6 prefix for includes neither libraries by default.
for file in specs/linux-*; do
    %__perl -p -i -e "s@/X11R6/@/@g" $file
done

%build
%__python configure.py
%define _disable_ld_no_undefined 1
%make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" LIBS="%{?ldflags} -lpython%{py_ver}"

%install
%makeinstall_std

