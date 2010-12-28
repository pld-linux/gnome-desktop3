Summary:	gnome-desktop library
Summary(pl.UTF-8):	Biblioteka gnome-desktop
Name:		gnome-desktop3
Version:	2.91.4
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-desktop/2.91/gnome-desktop-%{version}.tar.bz2
# Source0-md5:	60b555cb73b2ac4c90d296b071e8791b
Source1:	pld-logo.svg
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.22.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 2.91.7
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xorg-lib-libXrandr-devel >= 1.2
Requires(post,postun):	scrollkeeper
Requires:	python-gnome
Requires:	python-pygtk-gtk
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
Obsoletes:	gnome-desktop3-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software.

This package contains gnome-desktop library.

%description -l pl.UTF-8
GNOME (GNU Network Object Model Environment) jest zestawem przyjaznych
dla użytkownika programów i narzędzi biurkowych, których używa się
wraz z zarządcą okien systemu X Window. GNOME przypomina wyglądem i
zakresem funkcjonalności CDE i KDE, jednak GNOME opiera się w całości
na wolnym oprogramowaniu.

Pakiet ten zawiera bibliotekę gnome-desktop.

%package devel
Summary:	GNOME desktop includes
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek GNOME desktop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gsettings-desktop-schemas-devel
Requires:	gtk+3-devel >= 2.91.0
Requires:	startup-notification-devel >= 0.8

%description devel
GNOME desktop header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek GNOME desktop.

%package static
Summary:	GNOME desktop static libraries
Summary(pl.UTF-8):	Statyczne biblioteki GNOME desktop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
GNOME desktop static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki GNOME desktop.

%package apidocs
Summary:	gnome-desktop API documentation
Summary(pl.UTF-8):	Dokumentacja API gnome-desktop
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gnome-desktop API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gnome-desktop.

%prep
%setup -q -n gnome-desktop-%{version}

sed -i -e 's/en@shaw//' po/LINGUAS
rm -f po/en@shaw.po

%build
%{__gtkdocize}
%{__intltoolize}
%{__gnome_doc_prepare}
%{__gnome_doc_common}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gnome-distributor="PLD Linux Distribution" \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -f  $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -fr $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%scrollkeeper_update_post

%postun
/sbin/ldconfig
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_datadir}/libgnome-desktop-3.0
%attr(755,root,root) %{_libdir}/libgnome-desktop-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-desktop-3.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-desktop-3.so
%{_includedir}/gnome-desktop-3.0
%{_pkgconfigdir}/gnome-desktop-3.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnome-desktop-3.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gnome-desktop3
