#
Summary:	An indexing and searching API
Summary(pl.UTF-8):	API do indeksowania i wyszukiwania
Name:		clucene-core
Version:	0.9.16a
Release:	1
License:	LGPL/Apache
Group:		Libraries
Source0:	http://dl.sourceforge.net/clucene/%{name}-%{version}.tar.bz2
# Source0-md5:	0ed4f537321065c68ed802be67b25b10
URL:		http://clucene.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLucene is a C++ port of Lucene. It is a high-performance,
full-featured text search engine written in C++.

%description -l pl.UTF-8
CLucene jest portem Lucene na C++. Jest to wysokowydajny silnik do
wyszukiwania tekstu napisany w C++.

%package devel
Summary:	Header files for CLucene library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CLucene
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for CLucene library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CLucene.

%package static
Summary:	Static CLucene library
Summary(pl.UTF-8):	Statyczna biblioteka CLucene
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CLucene library.

%description static -l pl.UTF-8
Statyczna biblioteka CLucene.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/CLucene.h
%{_includedir}/CLucene
%{_libdir}/CLucene

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
