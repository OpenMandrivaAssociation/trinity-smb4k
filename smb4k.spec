%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg smb4k
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.9.4
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	A Samba (SMB) share advanced browser for Trinity
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org

License:	GPLv2+

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/internet/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:  	cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_NO_BUILTIN_CHRPATH=ON
BuildOption:    -DBIN_INSTALL_DIR=%{tde_bindir}
BuildOption:    -DCONFIG_INSTALL_DIR="%{tde_confdir}"
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir}
BuildOption:    -DLIB_INSTALL_DIR=%{tde_libdir}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_datadir}
BuildOption:   -DBUILD_ALL="ON" -DWITH_ALL_OPTIONS="ON"

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	fdupes

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(smbclient)


%description
Smb4K is a SMB (Windows) share browser for TDE. It uses the Samba software 
suite to access the SMB shares of the local network neighborhood. Its purpose
is to provide a program that's easy to use and has as many features as 
possible.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/smb4k
%{tde_bindir}/smb4k_cat
%{tde_bindir}/smb4k_kill
%{tde_bindir}/smb4k_mount
%{tde_bindir}/smb4k_mv
%{tde_bindir}/smb4k_umount
%{tde_libdir}/libsmb4kcore.so.2
%{tde_libdir}/libsmb4kcore.so.2.0.0
%{tde_libdir}/libsmb4kdialogs.la
%{tde_libdir}/libsmb4kdialogs.so
%{tde_tdelibdir}/konqsidebar_smb4k.la
%{tde_tdelibdir}/konqsidebar_smb4k.so
%{tde_tdelibdir}/libsmb4tdeconfigdialog.la
%{tde_tdelibdir}/libsmb4tdeconfigdialog.so
%{tde_tdelibdir}/libsmb4knetworkbrowser.la
%{tde_tdelibdir}/libsmb4knetworkbrowser.so
%{tde_tdelibdir}/libsmb4ksearchdialog.la
%{tde_tdelibdir}/libsmb4ksearchdialog.so
%{tde_tdelibdir}/libsmb4ksharesiconview.la
%{tde_tdelibdir}/libsmb4ksharesiconview.so
%{tde_tdelibdir}/libsmb4kshareslistview.la
%{tde_tdelibdir}/libsmb4kshareslistview.so
%{tde_tdeappdir}/smb4k.desktop
%{tde_datadir}/apps/konqsidebartng/add/smb4k_add.desktop
%{tde_datadir}/apps/smb4k/
%{tde_datadir}/apps/smb4knetworkbrowserpart/
%{tde_datadir}/apps/smb4ksharesiconviewpart/
%{tde_datadir}/apps/smb4kshareslistviewpart/
%{tde_datadir}/config.kcfg/smb4k.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/smb4k.png
%{tde_tdedocdir}/HTML/en/smb4k/

##########

%package devel
Summary:		Development files for %{name}
Group:			Development/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}

%files devel
%{tde_tdeincludedir}/*.h
%{tde_libdir}/libsmb4kcore.la
%{tde_libdir}/libsmb4kcore.so


%conf -p
unset QTDIR QTINC QTLIB
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"


%install -a
%find_lang %{tde_pkg}

# Removes duplicate files
%fdupes -s %buildroot

