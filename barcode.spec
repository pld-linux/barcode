%define prefix   /usr
%define sysconfdir	/etc

Summary:	GNU barcode
Name:		barcode
Version:	0.98
Release:	1
License:	GPL
Group:      Applications/Graphics
Source0:	ftp://ar.linux.it/pub/barcode/%{name}-%{ver}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://gnu.systemy.it/software/barcode

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

%ifarch alpha
  ARCH_FLAGS="--host=alpha-redhat-linux"
%endif

CFLAGS="$RPM_OPT_FLAGS" ./configure $ARCH_FLAGS --prefix=%{prefix} --sysconfdir=%{sysconfdir}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} sysconfdir=$RPM_BUILD_ROOT%{sysconfdir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%doc COPYING ChangeLog INSTALL README TODO doc/*.html doc/*.pdf doc/*.ps

%attr(0755,root,root) %{_bindir}/barcode
%attr(0644,root,root) %{_infodir}/barcode.info*
%attr(0644,root,root) %{_mandir}/man1/barcode.1*

%files devel
%defattr(644,root,root,755)
%attr(0644,root,root) %{_includedir}/barcode.h
%attr(0644,root,root) %{_libdir}/libbarcode.a
%attr(0644,root,root) %{_mandir}/man3/barcode.3*
