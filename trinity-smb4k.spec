%bcond clang 1

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg smb4k
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	0.9.4
Release:	%{?tde_version:%{tde_version}_}3
Summary:	A Samba (SMB) share advanced browser for Trinity
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/internet/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:  	cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DBUILD_ALL=ON -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

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
%{tde_prefix}/bin/smb4k
%{tde_prefix}/bin/smb4k_cat
%{tde_prefix}/bin/smb4k_kill
%{tde_prefix}/bin/smb4k_mount
%{tde_prefix}/bin/smb4k_mv
%{tde_prefix}/bin/smb4k_umount
%{tde_prefix}/%{_lib}/libsmb4kcore.so.2
%{tde_prefix}/%{_lib}/libsmb4kcore.so.2.0.0
%{tde_prefix}/%{_lib}/libsmb4kdialogs.la
%{tde_prefix}/%{_lib}/libsmb4kdialogs.so
%{tde_prefix}/%{_lib}/trinity/konqsidebar_smb4k.la
%{tde_prefix}/%{_lib}/trinity/konqsidebar_smb4k.so
%{tde_prefix}/%{_lib}/trinity/libsmb4tdeconfigdialog.la
%{tde_prefix}/%{_lib}/trinity/libsmb4tdeconfigdialog.so
%{tde_prefix}/%{_lib}/trinity/libsmb4knetworkbrowser.la
%{tde_prefix}/%{_lib}/trinity/libsmb4knetworkbrowser.so
%{tde_prefix}/%{_lib}/trinity/libsmb4ksearchdialog.la
%{tde_prefix}/%{_lib}/trinity/libsmb4ksearchdialog.so
%{tde_prefix}/%{_lib}/trinity/libsmb4ksharesiconview.la
%{tde_prefix}/%{_lib}/trinity/libsmb4ksharesiconview.so
%{tde_prefix}/%{_lib}/trinity/libsmb4kshareslistview.la
%{tde_prefix}/%{_lib}/trinity/libsmb4kshareslistview.so
%{tde_prefix}/share/applications/tde/smb4k.desktop
%{tde_prefix}/share/apps/konqsidebartng/add/smb4k_add.desktop
%{tde_prefix}/share/apps/smb4k/
%{tde_prefix}/share/apps/smb4knetworkbrowserpart/
%{tde_prefix}/share/apps/smb4ksharesiconviewpart/
%{tde_prefix}/share/apps/smb4kshareslistviewpart/
%{tde_prefix}/share/config.kcfg/smb4k.kcfg
%{tde_prefix}/share/icons/crystalsvg/*/apps/smb4k.png
%{tde_prefix}/share/doc/tde/HTML/en/smb4k/

##########

%package devel
Summary:		Development files for %{name}
Group:			Development/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}

%files devel
%{tde_prefix}/include/tde/*.h
%{tde_prefix}/%{_lib}/libsmb4kcore.la
%{tde_prefix}/%{_lib}/libsmb4kcore.so


%conf -p
unset QTDIR QTINC QTLIB
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg}

# Removes duplicate files
%fdupes -s %buildroot

