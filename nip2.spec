Summary:	Interface for vips image manipulation tool
Name:		nip2
Version:	7.14.4
Release:	%{mkrel 1}
License:	LGPLv2+
Group:		Video
URL:		http://www.vips.ecs.soton.ac.uk/index.php
Source0:	%{name}-%{version}.tar.gz
# Add a configure option to disable updating of desktop and mime
# databases during make install: this is wrong for packages
# - AdamW 2008/07 (submitted upstream to ML)
Patch0:		nip2-update-desktop.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	flex 
BuildRequires:	bison 
BuildRequires:	gtk2-devel 
BuildRequires:	libxml2-devel 
BuildRequires:	vips-devel 
BuildRequires:	fftw3-devel
BuildRequires:	libgsl-devel
BuildRequires:	imagemagick
# It tests for xdg-open - AdamW
BuildRequires:	xdg-utils
BuildRequires:	perl-XML-Parser
Requires:	xdg-utils

%description
nip2 aims to be about halfway between Excel and Photoshop. You don't directly
edit images - instead, like a spreadsheet, you build relationships between 
objects. When you make a change somewhere, nip2 will recalculate the objects 
affected by that change. Since it is demand-driven this update is usually 
(almost) instant, even for very, very large images.

%prep
%setup -q
%patch0 -p1 -b .update

%build
autoreconf
%configure2_5x --enable-update-desktop=no
%make

%install
rm -rf %{buildroot}
%makeinstall

%if %mdkversion < 200900
%post
%update_desktop_database
%update_mime_database
%endif

%if %mdkversion < 200900
%postun
%clean_mime_database
%clean_desktop_database
%endif


rm -fr %{buildroot}/%{_datadir}/locale/malkovich

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert -scale 16x16 proj/src/nip.ico %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert -scale 32x32 proj/src/nip.ico %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 48x48 proj/src/nip.ico %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post 
%{update_menus} 
%endif

%if %mdkversion < 200900
%postun 
%{clean_menus} 
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/*
%defattr(644,root,root,755)
%{_datadir}/%{name}
%doc %{_defaultdocdir}/%{name}
%{_mandir}/man?/*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/*
%{_datadir}/mime/packages/%{name}.xml

