Summary:	GNOME Flashback module - GNOME 3 shell similar to GNOME 2
Summary(pl.UTF-8):	Moduł GNOME Flashback - powłoka GNOME 3 podobna do GNOME 2
Name:		gnome-flashback
Version:	3.56.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-flashback/3.56/%{name}-%{version}.tar.xz
# Source0-md5:	e9e02306c78018e26e23cd17bc53a10c
URL:		https://wiki.gnome.org/Projects/GnomeFlashback
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.16.4
BuildRequires:	gdk-pixbuf2-devel >= 2.32.2
BuildRequires:	gdm-devel
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 1:2.67.3
BuildRequires:	gnome-bluetooth1-devel >= 3.0
BuildRequires:	gnome-desktop-devel >= 43
BuildRequires:	gnome-panel-devel >= 3.35.2
BuildRequires:	gsettings-desktop-schemas-devel >= 42.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	ibus-devel >= 1.5.2
BuildRequires:	libcanberra-gtk3-devel >= 0.13
# libcompizconfig >= 0.9.14.0 ?
BuildRequires:	libtool >= 2:2
# xcb-randr
BuildRequires:	libxcb-devel
BuildRequires:	pam-devel
BuildRequires:	pango-devel >= 1:1.44.0
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.97
BuildRequires:	pulseaudio-devel
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	tar >= 1:1.22
BuildRequires:	upower-devel >= 0.99.0
BuildRequires:	xkeyboard-config
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXi-devel >= 1.6.0
BuildRequires:	xorg-lib-libXrandr-devel >= 1.5.0
BuildRequires:	xorg-lib-libXxf86vm-devel >= 1.1.4
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.67.3
Requires:	gdk-pixbuf2 >= 2.32.2
Requires:	glib2 >= 1:2.67.3
Requires:	gnome-bluetooth1-libs >= 3.0
Requires:	gnome-desktop >= 43
Requires:	gnome-panel >= 3.35.2
Requires:	gsettings-desktop-schemas >= 42.0
Requires:	gtk+3 >= 3.22.0
Requires:	ibus-libs >= 1.5.2
Requires:	libcanberra-gtk3 >= 0.13
Requires:	pango >= 1:1.44.0
Requires:	polkit >= 0.97
Requires:	upower-libs >= 0.99.0
Requires:	xorg-lib-libXi >= 1.6.0
Requires:	xorg-lib-libXrandr >= 1.5.0
Requires:	xorg-lib-libXxf86vm >= 1.1.4
# keyboard layout for system-indicators
Suggests:	tecla
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-panel/modules/system_indicators.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-flashback
%attr(755,root,root) %{_libexecdir}/gnome-flashback-clipboard
%attr(755,root,root) %{_libexecdir}/gnome-flashback-idle-monitor
%attr(755,root,root) %{_libexecdir}/gnome-flashback-media-keys
%attr(755,root,root) %{_libexecdir}/gnome-flashback-metacity
%attr(755,root,root) %{_libexecdir}/gnome-flashback-polkit
%attr(755,root,root) %{_libdir}/gnome-panel/modules/system_indicators.so
/etc/xdg/autostart/gnome-flashback-clipboard.desktop
/etc/xdg/autostart/gnome-flashback-geoclue-demo-agent.desktop
/etc/xdg/autostart/gnome-flashback-idle-monitor.desktop
/etc/xdg/autostart/gnome-flashback-media-keys.desktop
/etc/xdg/autostart/gnome-flashback-nm-applet.desktop
/etc/xdg/autostart/gnome-flashback-polkit.desktop
/etc/xdg/menus/gnome-flashback-applications.menu
%{_desktopdir}/gnome-flashback.desktop
%{_datadir}/desktop-directories/X-GNOME-Flashback-Science.directory
%{_datadir}/desktop-directories/X-GNOME-Flashback-Settings.directory
%{_datadir}/desktop-directories/X-GNOME-Flashback-Settings-System.directory
%{_datadir}/glib-2.0/schemas/00_gnome-flashback.gschema.override
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-flashback.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-flashback.desktop.background.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-flashback.desktop.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-flashback.desktop.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-flashback.desktop.icons.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-flashback.keybindings.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-flashback.notifications.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-flashback.system-indicators.input-sources.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-gnome-flashback-screenshots.xml
%{_datadir}/gnome-panel/layouts/gnome-flashback.layout
%{_datadir}/gnome-session/sessions/gnome-flashback-metacity.session
%{_datadir}/xsessions/gnome-flashback-metacity.desktop
%{systemduserunitdir}/gnome-flashback.service
%{systemduserunitdir}/gnome-flashback.target
%dir %{systemduserunitdir}/gnome-session@gnome-flashback-metacity.target.d
%{systemduserunitdir}/gnome-session@gnome-flashback-metacity.target.d/session.conf
