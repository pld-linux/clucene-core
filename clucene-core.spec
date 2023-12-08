Summary:	An indexing and searching API
Summary(pl.UTF-8):	API do indeksowania i wyszukiwania
Name:		clucene-core
Version:	2.3.3.4
Release:	5
License:	LGPL or Apache v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/clucene/%{name}-%{version}.tar.gz
# Source0-md5:	48d647fbd8ef8889e5a7f422c1bfda94
Patch0:		%{name}-2.3.3.4-install_contribs_lib.patch
Patch1:		remove-boost-headers.patch
Patch2:		time.patch
URL:		http://clucene.sourceforge.net/
BuildRequires:	cmake
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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%cmake \
	-DBUILD_STATIC_LIBRARIES=ON \
	-DBUILD_CONTRIBS=ON \
	-DBUILD_CONTRIBS_LIB=ON \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# remove boost headers, they are not needed nor used here
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/CLucene/ext

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libclucene-contribs-lib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclucene-contribs-lib.so.1
%attr(755,root,root) %{_libdir}/libclucene-core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclucene-core.so.1
%attr(755,root,root) %{_libdir}/libclucene-shared.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclucene-shared.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclucene-contribs-lib.so
%attr(755,root,root) %{_libdir}/libclucene-core.so
%attr(755,root,root) %{_libdir}/libclucene-shared.so
%{_includedir}/CLucene.h
%{_includedir}/CLucene
%{_libdir}/CLuceneConfig.cmake
%{_pkgconfigdir}/libclucene-core.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclucene-core-static.a
%{_libdir}/libclucene-shared-static.a
