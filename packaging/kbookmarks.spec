# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kbookmarks

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 3 addon for bookmarks manipulation
Version:    5.3.0
Release:    2
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kbookmarks.yaml
Source101:  kbookmarks-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel

%description
KDE Frameworks 5 Tier 3 addon for bookmarks manipulation


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kconfigwidgets-devel
Requires:   kcoreaddons-devel
Requires:   kiconthemes-devel
Requires:   kwidgetsaddons-devel
Requires:   kxmlgui-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%find_lang kbookmarks5_qt --with-qt --all-name || :

%files -f kbookmarks5_qt.lang
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5Bookmarks.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/kbookmarks_version.h
%{_kf5_includedir}/KBookmarks
%{_kf5_libdir}/libKF5Bookmarks.so
%{_kf5_cmakedir}/KF5Bookmarks
%{_kf5_mkspecsdir}/qt_KBookmarks.pri
# >> files devel
# << files devel
