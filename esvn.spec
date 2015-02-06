Summary:	The eSvn is a cross-platform (QT-based) GUI for Subversion
Name:		esvn
Version:	0.6.12
Release:	5
Epoch:		1
License:	GPLv2+
Group:		Development/KDE and Qt
URL:		http://esvn.umputun.com/
Source:		%{name}-%{version}-1.tar.gz
BuildRequires: qt3-devel
BuildRequires: dos2unix
Requires:	subversion

%description
The eSvn is a cross-platform (QT-based) GUI frontend for the 
Subversion revision system.

%prep
%setup -qn %{name}

%build
perl -i -pe 's|qmake|/usr/lib/qt3/bin/qmake|g' Makefile
%make


%install
mkdir -p %{buildroot}%{_bindir}
install -m755 esvn %{buildroot}%{_bindir}/%{name}
install -m755 esvn-diff-wrapper %{buildroot}%{_bindir}
dos2unix COPYING

# Install icon files
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_liconsdir}
install -m644 %{name}.png %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{name}.png %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{name}.png %{buildroot}%{_liconsdir}/%{name}.png

# Create and install menu file
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING LICENSE README VERSION ChangeLog
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(-,root,root,0755)
%{_bindir}/%{name}
%{_bindir}/esvn-diff-wrapper

