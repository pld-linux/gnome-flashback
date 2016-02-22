Summary:	GNOME Flashback module - GNOME 3 shell similar to GNOME 2
Summary(pl.UTF-8):	Moduł GNOME Flashback - powłoka GNOME 3 podobna do GNOME 2
Name:		gnome-flashback
Version:	3.18.2
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-flashback/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	5089c54e96d61cdb7a9c5c1f50662faf
URL:		https://wiki.gnome.org/Projects/GnomeFlashback
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.13
BuildRequires:	gettext-tools >= 0.19.4
BuildRequires:	libtool >= 2:2
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-bluetooth-devel >= 3.0
BuildRequires:	gnome-desktop-devel >= 3.12.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.12.0
BuildRequires:	gtk+3-devel >= 3.15.2
BuildRequires:	ibus-devel >= 1.5.2
BuildRequires:	libcanberra-gtk3-devel >= 0.13
BuildRequires:	libxcb-devel
BuildRequires:	pango-devel
BuildRequires:	polkit-devel >= 0.97
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	upower-devel >= 0.99.0
BuildRequires:	xkeyboard-config
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.5.0
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	glib2 >= 1:2.44.0
Requires:	gnome-bluetooth-libs >= 3.0
Requires:	gnome-desktop >= 3.12.0
Requires:	gtk+3 >= 3.15.0
Requires:	xorg-lib-libXrandr >= 1.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Flashback (previously called GNOME fallback mode) is a shell for
GNOME 3. The desktop layout and the underlying technology is similar
to GNOME 2. It doesn't use 3D acceleration, so it's suitable for older
hardware.

%description -l pl.UTF-8
GNOME Flashback (wcześniej znany jako tryb zastępczy GNOME) to powłoka
dla GNOME 3. Wygląd biurka oraz używana technika jest podobna do GNOME
2. Nie wykorzystuje akceleracji 3D, więc lepiej nadaje się dla
starszego sprzętu.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-flashback
%attr(755,root,root) %{_libexecdir}/gnome-flashback-compiz
%attr(755,root,root) %{_libexecdir}/gnome-flashback-metacity
/etc/xdg/autostart/gnome-flashback-nm-applet.desktop
/etc/xdg/autostart/gnome-flashback-screensaver.desktop
/etc/xdg/menus/gnome-flashback-applications.menu
%{_desktopdir}/gnome-flashback.desktop
%{_desktopdir}/gnome-flashback-init.desktop
%{_datadir}/desktop-directories/X-GNOME-Flashback-Settings.directory
%{_datadir}/desktop-directories/X-GNOME-Flashback-Settings-System.directory
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-flashback.gschema.xml
%{_datadir}/gnome-session/sessions/gnome-flashback-compiz.session
%{_datadir}/gnome-session/sessions/gnome-flashback-metacity.session
%{_datadir}/xsessions/gnome-flashback-compiz.desktop
%{_datadir}/xsessions/gnome-flashback-metacity.desktop
