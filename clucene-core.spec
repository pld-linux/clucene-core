# TODO: 0.9.x branch is quite old, build Java Lucene 2.3.2 compatable unstable branch
Summary:	An indexing and searching API
Summary(pl.UTF-8):	API do indeksowania i wyszukiwania
Name:		clucene-core
Version:	0.9.21b
Release:	1
License:	LGPL or Apache v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/clucene/clucene-core-stable/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	ba1a8f764a2ca19c66ad907dddd88352
URL:		http://clucene.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
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
Requires:	libstdc++-devel

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
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libclucene.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclucene.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclucene.so
%{_libdir}/libclucene.la
%{_includedir}/CLucene.h
%{_includedir}/CLucene
%{_libdir}/CLucene

%files static
%defattr(644,root,root,755)
%{_libdir}/libclucene.a
