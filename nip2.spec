Summary:	Interface for vips image manipulation tool
Name:		nip2
Version:	7.30.1
Release:	2
License:	LGPLv2+
Group:		Video
URL:		https://www.vips.ecs.soton.ac.uk/index.php
Source0:	http://www.vips.ecs.soton.ac.uk/supported/7.16/%{name}-%{version}.tar.gz
Patch0:		nip2-7.30.1-fix-build.patch
Patch1:		nip2-7.30.1-linkage.patch
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	vips-devel >= %{version}
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	imagemagick
# It tests for xdg-open - AdamW
BuildRequires:	xdg-utils
BuildRequires:	perl(XML::Parser)
Requires:	xdg-utils

%description
nip2 aims to be about halfway between Excel and Photoshop. You don't directly
edit images - instead, like a spreadsheet, you build relationships between 
objects. When you make a change somewhere, nip2 will recalculate the objects 
affected by that change. Since it is demand-driven this update is usually 
(almost) instant, even for very, very large images.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x --disable-update-desktop
%make

%install
%makeinstall_std

rm -fr %{buildroot}%{_datadir}/locale/malkovich

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert -scale 16x16 proj/src/nip.ico %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert -scale 32x32 proj/src/nip.ico %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 48x48 proj/src/nip.ico %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/*
%defattr(644,root,root,755)
%{_datadir}/%{name}
%doc %{_defaultdocdir}/%{name}
%{_mandir}/man?/*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/*
%{_datadir}/mime/packages/%{name}.xml


