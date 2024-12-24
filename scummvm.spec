%define		version_tools	2.7.0
Summary:	Graphic adventure game interpreter
Summary(pl.UTF-8):	Interpreter gier przygodowych
Name:		scummvm
Version:	2.8.1
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://downloads.scummvm.org/frs/scummvm/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	641a3937baf17ac6123ae6ed664e5ce3
Source1:	https://downloads.scummvm.org/frs/scummvm-tools/%{version_tools}/%{name}-tools-%{version_tools}.tar.xz
# Source1-md5:	0f93bc0d423c6d93bfade50a7e6f2bbe
Patch0:		%{name}-wx-config.patch
Patch1:		dwarf-debug.patch
Patch2:		fluidsynth-printf-attr.patch
Patch3:		gcc14.patch
URL:		http://scummvm.org/
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_net-devel
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	boost-devel
BuildRequires:	flac-devel >= 1.0.1
BuildRequires:	fluidsynth-devel
BuildRequires:	freetype-devel
BuildRequires:	libmad-devel
BuildRequires:	libmpeg2-devel >= 0.3.2
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	wxGTK2-unicode-devel
BuildRequires:	wxWidgets-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Obsoletes:	scummvm-engine-access < 2.7.1
Obsoletes:	scummvm-engine-adl < 2.7.1
Obsoletes:	scummvm-engine-agi < 2.7.1
Obsoletes:	scummvm-engine-agos < 2.7.1
Obsoletes:	scummvm-engine-avalanche < 2.7.1
Obsoletes:	scummvm-engine-bbvs < 2.7.1
Obsoletes:	scummvm-engine-bladerunner < 2.7.1
Obsoletes:	scummvm-engine-cge < 2.7.1
Obsoletes:	scummvm-engine-cge2 < 2.7.1
Obsoletes:	scummvm-engine-chewy < 2.7.1
Obsoletes:	scummvm-engine-cine < 2.7.1
Obsoletes:	scummvm-engine-composer < 2.7.1
Obsoletes:	scummvm-engine-cruise < 2.7.1
Obsoletes:	scummvm-engine-cryo < 2.7.1
Obsoletes:	scummvm-engine-cryomni3d < 2.7.1
Obsoletes:	scummvm-engine-director < 2.7.1
Obsoletes:	scummvm-engine-dm < 2.7.1
Obsoletes:	scummvm-engine-draci < 2.7.1
Obsoletes:	scummvm-engine-dragons < 2.7.1
Obsoletes:	scummvm-engine-drascula < 2.7.1
Obsoletes:	scummvm-engine-dreamweb < 2.7.1
Obsoletes:	scummvm-engine-fullpipe < 2.5.1
Obsoletes:	scummvm-engine-glk < 2.7.1
Obsoletes:	scummvm-engine-gnap < 2.7.1
Obsoletes:	scummvm-engine-gob < 2.7.1
Obsoletes:	scummvm-engine-griffon < 2.7.1
Obsoletes:	scummvm-engine-groovie < 2.7.1
Obsoletes:	scummvm-engine-hdb < 2.7.1
Obsoletes:	scummvm-engine-hopkins < 2.7.1
Obsoletes:	scummvm-engine-hugo < 2.7.1
Obsoletes:	scummvm-engine-illusions < 2.7.1
Obsoletes:	scummvm-engine-kingdom < 2.7.1
Obsoletes:	scummvm-engine-kyra < 2.7.1
Obsoletes:	scummvm-engine-lab < 2.7.1
Obsoletes:	scummvm-engine-lastexpress < 2.7.1
Obsoletes:	scummvm-engine-lilliput < 2.7.1
Obsoletes:	scummvm-engine-lure < 2.7.1
Obsoletes:	scummvm-engine-m4 < 2.5.1
Obsoletes:	scummvm-engine-macventure < 2.7.1
Obsoletes:	scummvm-engine-made < 2.7.1
Obsoletes:	scummvm-engine-mads < 2.7.1
Obsoletes:	scummvm-engine-mohawk < 2.7.1
Obsoletes:	scummvm-engine-mortevielle < 2.7.1
Obsoletes:	scummvm-engine-mutationofjb < 2.7.1
Obsoletes:	scummvm-engine-neverhood < 2.7.1
Obsoletes:	scummvm-engine-parallaction < 2.7.1
Obsoletes:	scummvm-engine-pegasus < 2.7.1
Obsoletes:	scummvm-engine-petka < 2.7.1
Obsoletes:	scummvm-engine-pink < 2.7.1
Obsoletes:	scummvm-engine-plumbers < 2.7.1
Obsoletes:	scummvm-engine-prince < 2.7.1
Obsoletes:	scummvm-engine-queen < 2.7.1
Obsoletes:	scummvm-engine-saga < 2.7.1
Obsoletes:	scummvm-engine-sci < 2.7.1
Obsoletes:	scummvm-engine-scumm < 2.7.1
Obsoletes:	scummvm-engine-sherlock < 2.7.1
Obsoletes:	scummvm-engine-sky < 2.7.1
Obsoletes:	scummvm-engine-sludge < 2.7.1
Obsoletes:	scummvm-engine-startrek < 2.7.1
Obsoletes:	scummvm-engine-supernova < 2.7.1
Obsoletes:	scummvm-engine-sword1 < 2.7.1
Obsoletes:	scummvm-engine-sword2 < 2.7.1
Obsoletes:	scummvm-engine-sword25 < 2.7.1
Obsoletes:	scummvm-engine-teenagent < 2.7.1
Obsoletes:	scummvm-engine-testbed < 2.7.1
Obsoletes:	scummvm-engine-tinsel < 2.7.1
Obsoletes:	scummvm-engine-titanic < 2.7.1
Obsoletes:	scummvm-engine-toltecs < 2.7.1
Obsoletes:	scummvm-engine-tony < 2.7.1
Obsoletes:	scummvm-engine-toon < 2.7.1
Obsoletes:	scummvm-engine-touche < 2.7.1
Obsoletes:	scummvm-engine-tsage < 2.7.1
Obsoletes:	scummvm-engine-tucker < 2.7.1
Obsoletes:	scummvm-engine-ultima < 2.7.1
Obsoletes:	scummvm-engine-voyeur < 2.7.1
Obsoletes:	scummvm-engine-wage < 2.7.1
Obsoletes:	scummvm-engine-wintermute < 2.7.1
Obsoletes:	scummvm-engine-xeen < 2.7.1
Obsoletes:	scummvm-engine-zvision < 2.7.1
Obsoletes:	scummvm-theme-classic < 2.7.1
Obsoletes:	scummvm-theme-modern < 2.7.1
Obsoletes:	scummvm-theme-remastered < 2.7.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_sparc	-fPIC

%description
ScummVM is a program which allows you to run certain classic graphical
point-and-click adventure games, provided you already have their data
files. The clever part about this: ScummVM just replaces the
executables shipped with the game, allowing you to play them on
systems for which they were never designed!

Some of the adventures ScummVM supports include Adventure Soft's Simon
the Sorcerer 1 and 2; Revolution's Beneath A Steel Sky, Broken Sword 1
and Broken Sword 2; Flight of the Amazon Queen; Wyrmkeep's Inherit the
Earth; Coktel Vision's Gobliiins; Westwood Studios' The Legend of
Kyrandia and games based on LucasArts' SCUMM (Script Creation Utility
for Maniac Mansion) system such as Monkey Island, Day of the Tentacle,
Sam and Max and more. You can find a thorough list with details on
which games are supported and how well on the project page.

%description -l pl.UTF-8
ScummVM jest programem umożliwiającym uruchamianie klasycznych
graficznych gier przygodowych, pod warunkiem, że posiadane są ich
pliki danych. ScummVM używany jest w miejsce pliku wykonywalnego
dostarczonego razem z grą, co umożliwia granie na systemach, na które
gry nie zostały przeznaczone.

ScummVM obsługuje między innymi Simon the Sorcerer 1 i 2 firmy
Adventure Soft; Beneath A Steel Sky, Broken Sword 1 i 2 firmy
Revolution; Flight of the Amazon Queen; Inherit the Earth firmy
Wyrmkeep; serię Gobliiins firmy Coktel Vision; The Legend of Kyrandia
firmy Westwood i gry bazujące na silniku SCUMM (Script Creation
Utility for Maniac Mansion) firmy LucasArts, takie jak Monkey Island,
Day of the Tentacle, Sam and Max i inne. Szczegółowa lista znajduje
się na stronie projektu.

%package tools
Summary:	ScummVM tools
Summary(pl.UTF-8):	Narzędzia związane ze ScummVM
Group:		X11/Applications/Games

%description tools
Collection of various tools that may be useful to use in conjunction
with ScummVM.

%description tools -l pl.UTF-8
Zestaw narzędzi mogących być użytecznymi w połączeniu ze ScummVM.

%prep
%setup -q -a 1
%patch -P 1 -p1
cd scummvm-tools-%{version_tools}
%patch -P 0 -p2
cd ..
%patch -P 2 -p1
%patch -P 3 -p1

%{__sed} -i -e 's:"plugins":"%{_libdir}/scummvm":' base/plugins.cpp

%build
CXX="%{__cxx}" \
CXXFLAGS="%{rpmcppflags} %{rpmcflags}" \
LDFLAGS="%{rpmcflags} %{rpmldflags}" \
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--disable-debug \
	--enable-all-engines \
	--enable-plugins \
	--default-dynamic

%{__make} \
	VERBOSE_BUILD=1

cd scummvm-tools-%{version_tools}
CXX="%{__cxx}" \
CXXFLAGS="%{rpmcppflags} %{rpmcflags}" \
LDFLAGS="%{rpmcflags} %{rpmldflags}" \
_wxconfig=wx-gtk3-unicode-config \
./configure \
	--prefix=%{_prefix} \
	--disable-debug

%{__make} \
	VERBOSE_BUILD=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C scummvm-tools-%{version_tools} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTING.md COPYRIGHT NEWS.md README.md TODO
%attr(755,root,root) %{_bindir}/scummvm
%dir %{_libdir}/scummvm
%attr(755,root,root) %{_libdir}/scummvm/lib*.so
%{_mandir}/man6/scummvm.6*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/scalable/apps/org.scummvm.scummvm.svg
%{_datadir}/metainfo/org.scummvm.scummvm.metainfo.xml

%files tools
%defattr(644,root,root,755)
%doc scummvm-tools-%{version_tools}/README
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/scummvm
%{_datadir}/scummvm-tools
