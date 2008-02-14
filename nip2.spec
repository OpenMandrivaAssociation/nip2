%define name nip2
%define version 7.10.21
%define release %mkrel 4

Summary: Nip is an interface for vips
Name: %{name}
Version: %{version}
Release: %{release}
License: LGPL
Group: Video
URL: http://www.vips.ecs.soton.ac.uk/index.php
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: flex 
BuildRequires: bison 
BuildRequires: gtk2-devel 
BuildRequires: libxml2-devel 
BuildRequires: libvips-devel 
BuildRequires: fftw3-devel
BuildRequires: imagemagick-devel
BuildRequires: imagemagick
BuildRequires: perl-XML-Parser

%description
nip2 aims to be about halfway between Excel and Photoshop. You don't directly
edit images --- instead, like a spreadsheet, you build relationships between 
objects. When you make a change somewhere, nip2 will recalculate the objects 
affected by that change. Since it is demand-driven this update is usually 
(almost) instant, even for very, very large images.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

rm -fr $RPM_BUILD_ROOT/%{_datadir}/locale/malkovich
convert -resize 32x32 proj/src/nip.ico %buildroot%{_iconsdir}/%{name}.png
convert -resize 16x16 proj/src/nip.ico %buildroot%{_liconsdir}/%{name}.png
convert -resize 48x48 proj/src/nip.ico %buildroot%{_miconsdir}/%{name}.png

%find_lang %{name}


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=nip2
Comment=Free image processing system
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Graphics;Graphics;
EOF


%clean
rm -rf $RPM_BUILD_ROOT


%post 
%{update_menus} 

%postun 
%{clean_menus} 


%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/*
%defattr(644,root,root,755)
%{_datadir}/%{name}
%doc %{_defaultdocdir}/%{name}
%{_mandir}/man?/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/*

