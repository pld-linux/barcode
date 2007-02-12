Summary:	GNU barcode
Summary(pl.UTF-8):	GNU barcode - narzędzie do kodów paskowych
Name:		barcode
Version:	0.98
Release:	4
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://ar.linux.it/pub/barcode/%{name}-%{version}.tar.gz
# Source0-md5:	7f10c3307b84a19a4ab2fa4b3f2974da
Patch0:		%{name}-DESTDIR.patch
URL:		http://gnu.systemy.it/software/barcode/
BuildRequires:	autoconf
BuildRequires:	automake
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

%description devel
This is GNU-barcode. The package is meant to solve most needs in
barcode creation with a conventional printer. It can create printouts
for the conventional product tagging standards: UPC-A, UPC-E, EAN-13,
EAN-8, ISBN, as well as a few other formats. Ouput is generated as
either Postscript or Encapsulated Postscript (other back-ends may be
added if needed).

This subpackage contains the C header, the static library and man page
for developing programs that use GNU barcode.

%description devel -l pl.UTF-8
To jest GNU-barcode. Ten pakiet ma za zadanie zaspokoić większość
potrzeb związanych z drukowaniem kodów paskowych na konwencjonalnej
drukarce. Może tworzyć wydruki kodów w standardach: UPC-A, UPC-E,
EAN-13, EAN-8, ISBN, a także kilku innych. Dane wyjściowe są
generowane w formacie Postscript lub Encapsulated Postscript (w razie
potrzeby mogą być dodane inne backendy).

Ten podpakiet zawiera plik nagłówkowy do C, statyczną bibliotekę oraz
stronę manuala do tworzenia programów używających GNU barcode.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/barcode
%{_infodir}/barcode.info*
%{_mandir}/man1/barcode.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/lib*.a
%{_mandir}/man3/*
