Summary:	GNU barcode
Name:		barcode
Version:	0.98
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://ar.linux.it/pub/barcode/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://gnu.systemy.it/software/barcode/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is GNU-barcode. The package is meant to solve most needs in
barcode creation with a conventional printer. It can create printouts
for the conventional product tagging standards: UPC-A, UPC-E, EAN-13,
EAN-8, ISBN, as well as a few other formats. Ouput is generated as
either Postscript or Encapsulated Postscript (other back-ends may be
added if needed).

%package devel
Summary:	GNU barcode files for development
Group:		Development/Libraries

%description devel
This is GNU-barcode. The package is meant to solve most needs in
barcode creation with a conventional printer. It can create printouts
for the conventional product tagging standards: UPC-A, UPC-E, EAN-13,
EAN-8, ISBN, as well as a few other formats. Ouput is generated as
either Postscript or Encapsulated Postscript (other back-ends may be
added if needed).

This package contain the C header, the static library and man page for
development.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

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
