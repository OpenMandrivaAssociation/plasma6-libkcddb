%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		plasma6-libkcddb
Summary:	KF6 library for retrieving and sending CDDB information
Version:	24.01.95
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://projects.kde.org/projects/kde/kdemultimedia/libkcddb
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/libkcddb-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:	pkgconfig(libmusicbrainz5)
%rename	libkcddb6
Obsoletes:	%{mklibname KF6CddbWidgets 6} < %{EVRD}

%description
KF6 library for retrieving and sending CDDB information.

%files -f libkcddb.lang -f kcmcddb.lang -f kcontrol.lang
%{_datadir}/applications/kcm_cddb.desktop
%{_datadir}/config.kcfg/libkcddb5.kcfg
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so
%{_datadir}/qlogging-categories6/libkcddb.categories

#------------------------------------------------------------------------------

%define kcddb_major 5
%define libkcddb %mklibname KCddb6

%libpackage KCddb6 %{kcddb_major}

#------------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkcddb} = %{EVRD}
Conflicts:	kdemultimedia4-devel < 3:4.8.96

%description devel
KF6 library for retrieving and sending CDDB information.

This package contains header files needed if you wish to build applications
based on libkcddb.

%files devel
%{_libdir}/libKCddb6.so
%{_libdir}/cmake/KCddb6
%{_includedir}/*                                                                                       
%{_libdir}/qt6/mkspecs/modules/qt_KCddb.pri
                   
#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n libkcddb-%{version}

%build
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang libkcddb
%find_lang kcmcddb
%find_lang kcontrol --with-html
