Summary:	GNU barcode
Summary(pl.UTF-8):	GNU barcode - narzędzie do kodów paskowych
Name:		barcode
Version:	0.99
Release:	1
License:	GPL v3+
Group:		Applications/Graphics
Source0:	http://ftp.gnu.org/gnu/barcode/%{name}-%{version}.tar.xz
# Source0-md5:	cdc504ee1020e27fbfeebcb0718de054
Patch0:		format-security.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-lib.patch
URL:		http://www.gnu.org/software/barcode/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1.5
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	libpaper-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
Conflicts:	xscreensaver <= 1:4.16-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is GNU-barcode. The package is meant to solve most needs in
barcode creation with a conventional printer. It can create printouts
for the conventional product tagging standards: UPC-A, UPC-E, EAN-13,
EAN-8, ISBN, as well as a few other formats. Output is generated as
either Postscript or Encapsulated Postscript (other back-ends may be
added if needed).

%description -l pl.UTF-8
To jest GNU-barcode. Ten pakiet ma za zadanie zaspokoić większość
potrzeb związanych z drukowaniem kodów paskowych na konwencjonalnej
drukarce. Może tworzyć wydruki kodów w standardach: UPC-A, UPC-E,
EAN-13, EAN-8, ISBN, a także kilku innych. Dane wyjściowe są
generowane w formacie Postscript lub Encapsulated Postscript (w razie
potrzeby mogą być dodane inne backendy).

%package devel
Summary:	GNU barcode files for development
Summary(pl.UTF-8):	Pliki do programowania z użyciem GNU barcode
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is GNU-barcode. The package is meant to solve most needs in
barcode creation with a conventional printer. It can create printouts
for the conventional product tagging standards: UPC-A, UPC-E, EAN-13,
EAN-8, ISBN, as well as a few other formats. Ouput is generated as
either Postscript or Encapsulated Postscript (other back-ends may be
added if needed).

This subpackage contains the C header file for developing programs
that use GNU barcode.

%description devel -l pl.UTF-8
To jest GNU-barcode. Ten pakiet ma za zadanie zaspokoić większość
potrzeb związanych z drukowaniem kodów paskowych na konwencjonalnej
drukarce. Może tworzyć wydruki kodów w standardach: UPC-A, UPC-E,
EAN-13, EAN-8, ISBN, a także kilku innych. Dane wyjściowe są
generowane w formacie Postscript lub Encapsulated Postscript (w razie
potrzeby mogą być dodane inne backendy).

Ten podpakiet zawiera plik nagłówkowy języka C do tworzenia programów
używających GNU barcode.

%package static
Summary:	GNU barcode static library
Summary(pl.UTF-8):	Biblioteka statyczna GNU barcode
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GNU barcode static library.

%description static -l pl.UTF-8
Biblioteka statyczna GNU barcode.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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

%post	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/barcode
%attr(755,root,root) %{_libdir}/libbarcode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbarcode.so.0
%{_infodir}/barcode.info*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbarcode.so
%{_libdir}/libbarcode.la
%{_includedir}/barcode.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libbarcode.a
