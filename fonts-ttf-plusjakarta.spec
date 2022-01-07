Summary:	Plus Jakarta Fonts (General purpose sans-serif)
Name:		fonts-ttf-plusjakarta
Version:	2.6
Release:	1
License:	SIL Open Font License 1.1
Group:		System/Fonts/True type
Url:		http://www.droidfonts.com/
Source0:	https://github.com/tokotype/PlusJakartaSans/releases/download/%{version}/PlusJakartaSans-%{version}.zip
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools

%description
Plus Jakarta Sans is a font family that takes geometric sans serif styles,
designed by Gumpita Rahayu from Tokotype, the fonts were originally
commissioned by 6616 Studio for Jakarta Provincial Government program's
+Jakarta City of Collaboration identity in 2020.

Taking part of inspiration such as Neuzit Grotesk, Futura, and 1930s grotesque
sans serif with almost monoline contrast and pointy curves, the fonts consist
modern and clean cut forms, the x-height dimension slight taller to provide
clear spaces between caps and x-height, this also equipped with open counter
and balanced spaces to preserve the legibility at a range of sizes.

The beauty of diversity captured in typography. Like the city itself, the
unique points of this fonts is that in some glyphs has its own diversity and
characteristic of various explorations of forms that enrich the expressions
and stories that coexist. The charms of Plus Jakarta Sans fonts appear when
one looks closer, manifesting in a beauty that emerges once seen as a whole.
Each alternate on the family contains several alternates characters, divided
into three stylistic alternates which Lancip (Sharp), Lurus (Straight), and
Lingkar (Swirl).

As part of Plus Jakarta as a city of collaboration, fonts are made available
for public and use it under the SIL Open Font License.

%prep
%autosetup -p1 -n PlusJakartaSans-2.6

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/plusjakarta

install -m 644 static/*.ttf %{buildroot}%{_datadir}/fonts/TTF/plusjakarta
ttmkfdir %{buildroot}%{_datadir}/fonts/TTF/plusjakarta > %{buildroot}%{_datadir}/fonts/TTF/plusjakarta/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/plusjakarta/fonts.scale

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/plusjakarta \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-plusjakarta:pri=50

%files
%dir %{_datadir}/fonts/TTF/plusjakarta
%{_datadir}/fonts/TTF/plusjakarta/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/plusjakarta/fonts.dir
%{_datadir}/fonts/TTF/plusjakarta/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-plusjakarta:pri=50
