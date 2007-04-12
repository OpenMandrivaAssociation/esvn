%define name esvn
%define version 0.6.11
%define release %mkrel 6
%define summary The eSvn is a cross-platform (QT-based) GUI for Subversion

Name: %{name}
Version: %{version}
Release: %{release}
Summary: %{summary}
Source: http://esvn.umputun.com/%{name}-%{version}-1.tar.bz2
Source11: %{name}-16x16.png
Source12: %{name}-32x32.png
Source13: %{name}-48x48.png
Patch0: %{name}_fix_cmd_lineedit.patch

Group: Development/KDE and Qt
URL: http://esvn.umputun.com/
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL
BuildRequires: qt3-devel
BuildRequires: dos2unix
Requires: subversion

%description
The eSvn is a cross-platform (QT-based) GUI frontend for the 
Subversion revision system.

%prep
rm -rf %{buildroot}

%setup -qn %{name}
%patch0 -p0

%build
%make
#qmake -o Makefile esvn.pro
#perl -pi -e 's|-lqt|-lqt-mt|g' Makefile
#QTDIR=/usr/lib/qt3 make 

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 esvn %{buildroot}%{_bindir}/%{name}
install -m755 esvn-diff-wrapper %{buildroot}%{_bindir}
dos2unix COPYING

# Install icon files
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_liconsdir}
install -m644 %{SOURCE11} %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} %{buildroot}%{_liconsdir}/%{name}.png

# Create and install menu file
install -d %{buildroot}%{_menudir}
cat << EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}): \
needs="x11" \
title="ESvn" \
longtitle="The eSvn is a cross-platform (QT-based) GUI for Subversion" \
command="%{_bindir}/%{name}" \
icon="%{name}.png" \
section="More Applications/Development/Tools" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=The eSvn is a cross-platform (QT-based) GUI for Subversion
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Qt;X-MandrivaLinux-MoreApplications-Development-Tools;Development;RevisionControl;
EOF

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root,0755)
%doc AUTHORS  COPYING  LICENSE  README  VERSION  ChangeLog
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(-,root,root,0755)
%{_bindir}/%{name}
%{_bindir}/esvn-diff-wrapper

