%define		version_tools	0.12.0
Summary:	Graphic adventure game interpreter
Summary(pl.UTF-8):	Interpreter gier przygodowych
Name:		scummvm
Version:	0.12.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/scummvm/%{name}-%{version}.tar.bz2
# Source0-md5:	cd5620c57645948c8da0d4d9c9fcffb3
Source1:	http://dl.sourceforge.net/scummvm/%{name}-tools-%{version_tools}.tar.bz2
# Source1-md5:	af927a7cb59952ed869628250a916ab1
Source2:	%{name}.desktop
URL:		http://scummvm.org/
BuildRequires:	SDL-devel >= 1.2.2
BuildRequires:	wxWidgets-devel
%ifarch %{ix86} %{x8664}
BuildRequires:	fluidsynth-devel
%endif
BuildRequires:	libmad-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mpeg2dec-devel
%ifarch %{ix86}
#BuildRequires:	nasm
%endif
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
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

%package engine-agi
Summary:	Adventure Game Interpreter
Summary(pl.UTF-8):	Adventure Game Interpreter
Group:		X11/Applications/Games

%description engine-agi
The AGI (Adventure Game Interpreter) engine was used by Sierra in
their early adventure games.

%description engine-agi -l pl.UTF-8
Silnik AGI (Adventure Game Interpreter) był używany przez firmę
Sierra w jej wczesnych grach przygodowych.

%package engine-agos
Summary:	AGOS engine
Summary(pl.UTF-8):	Silnik AGOS
Group:		X11/Applications/Games

%description engine-agos
The AGOS Engine was originally created by Alan Cox at HorrorSoft and
is based on AberMUD V, with graphical extensions.
Required for following games:
- Elvira
- Elvira 2
- Waxworks
- Simon the Sorcerer
- Simon the Sorcerer 2
- The Feeble Files

%description engine-agos -l pl.UTF-8
Silnik AGOS został stworzony przez Alana Coksa w firmie HorrorSoft,
bazowany jest na programie AberMUD V z graficznymi rozszerzeniami.
Używany w następujących grach:
- Elvira
- Elvira 2
- Waxworks
- Simon the Sorcerer
- Simon the Sorcerer 2
- The Feeble Files

%package engine-cine
Summary:	Cinematique engine
Summary(pl.UTF-8):	Silnik Cinematique
Group:		X11/Applications/Games

%description engine-cine
Cinematique engine.

%description engine-cine -l pl.UTF-8
Silnik Cinematique.

%package engine-cruise
Summary:	Cruise engine
Summary(pl.UTF-8):	Silnik Cruise
Group:		X11/Applications/Games

%description engine-cruise
Cruise engine.

%description engine-cruise -l pl.UTF-8
Silnik Cruise.

%package engine-drascula
Summary:	Drascula engine
Summary(pl.UTF-8):	Silnik Drascula
Group:		X11/Applications/Games

%description engine-drascula
Drascula engine.

%description engine-drascula -l pl.UTF-8
Silnik Drascula.

%package engine-gob
Summary:	Gob engine
Summary(pl.UTF-8):	Silnik Gob
Group:		X11/Applications/Games

%description engine-gob
Engine to run adventure games created by Coktel Vision.

%description engine-gob -l pl.UTF-8
Silnik do uruchamiania gier stworzonych przez Coktel Vision.

%package engine-igor
Summary:	Igor engine
Summary(pl.UTF-8):	Silnik Igor
Group:		X11/Applications/Games

%description engine-igor
Igor engine.

%description engine-igor -l pl.UTF-8
Silnik Igor.

%package engine-kyra
Summary:	Kyrandia engine
Summary(pl.UTF-8):	Silnik Kyrandia
Group:		X11/Applications/Games

%description engine-kyra
Kyrandia engine.

%description engine-kyra -l pl.UTF-8
Silnik Kyrandia.

%package engine-lure
Summary:	Lure engine
Summary(pl.UTF-8):	Silnik Lure
Group:		X11/Applications/Games

%description engine-lure
Lure is the work-in-progress engine for the game Lure of the
Temptress.

%description engine-lure -l pl.UTF-8
Lure jest nieskończonym silnikiem dla gry Lure of the Temptress.

%package engine-parallaction
Summary:	Parallaction engine
Summary(pl.UTF-8):	Silnik Parallaction
Group:		X11/Applications/Games

%description engine-parallaction
Parallaction engine.

%description engine-parallaction -l pl.UTF-8
Silnik Parallaction.

%package engine-queen
Summary:	Queen engine
Summary(pl.UTF-8):	Silnik Queen
Group:		X11/Applications/Games

%description engine-queen
The Queen Engine is used to play Interactive Binary Illusions' Flight
of the Amazon Queen.

%description engine-queen -l pl.UTF-8
Silnik Queen jest używany do gry w Flight of the Amazon Queen firmy
Interactive Binary Illusions.

%package engine-saga
Summary:	Scripts for Animated Graphic Adventures
Summary(pl.UTF-8):	Scripts for Animated Graphic Adventures
Group:		X11/Applications/Games

%description engine-saga
SAGA (Scripts for Animated Graphic Adventures) engine.

%description engine-saga -l pl.UTF-8
Silnik SAGA (Scripts for Animated Graphic Adventures).

%package engine-scumm
Summary:	Script Creation Utility for Maniac Mansion
Summary(pl.UTF-8):	Script Creation Utility for Maniac Mansion
Group:		X11/Applications/Games

%description engine-scumm
SCUMM is a utility used to create the famous LucasArts adventure games
like the Monkey Island series and also gave ScummVM its name.

%description engine-scumm -l pl.UTF-8
SCUMM jest narzędziem użytym do stworzenia znanych gier przygodowych
firmy LucasArts takich jak seria Monkey Island, dał również ScummVM
nazwę.

%package engine-sky
Summary:	Sky engine
Summary(pl.UTF-8):	Silnik Sky
Group:		X11/Applications/Games

%description engine-sky
Sky is the internal name for the Virtual Theatre variant which runs
Beneath a Steel Sky.

%description engine-sky -l pl.UTF-8
Sky jest wewnętrzną nazwą na wariant Virtual Theatre, który uruchamia
Beneath a Steel Sky.

%package engine-sword1
Summary:	Sword1 engine
Summary(pl.UTF-8):	Silnik Sword1
Group:		X11/Applications/Games

%description engine-sword1
Sword1 engine.

%description engine-sword1 -l pl.UTF-8
Silnik Sword1.

%package engine-sword2
Summary:	Sword2 engine
Summary(pl.UTF-8):	Silnik Sword2
Group:		X11/Applications/Games

%description engine-sword2
Sword2 engine.

%description engine-sword2 -l pl.UTF-8
Silnik Sword2.

%package engine-touche
Summary:	Touche engine
Summary(pl.UTF-8):	Silnik Touche
Group:		X11/Applications/Games

%description engine-touche
This engine is only used by Touche: The Adventures of the Fifth
Musketeer.

%description engine-touche -l pl.UTF-8
Ten silnik jest używany tylko przez Touché: Przygody Piątego
Muszkietera.

%package theme-modern
Summary:	Theme modern for ScummVM
Summary(pl.UTF-8):	Motyw modern dla ScummVM
Group:		X11/Applications/Games

%description theme-modern
Theme modern for ScummVM.

%description theme-modern -l pl.UTF-8
Motyw modern dla ScummVM.

%prep
%setup -q -a 1

sed -i -e 's:"plugins/":"%{_libdir}/scummvm/":' backends/plugins/posix/posix-provider.cpp
sed -i -e 's:"plugins/":"%{_libdir}/scummvm/":' backends/plugins/sdl/sdl-provider.cpp

%build
./configure \
	--prefix=/usr \
	--disable-debug \
	--disable-nasm \
	--enable-cruise \
	--enable-drascula \
	--enable-igor \
	--enable-plugins

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -DDYNAMIC_MODULES -fpic $(wx-gtk2-unicode-config --cflags)" \
	LDFLAGS="%{rpmldflags}"

cd scummvm-tools-%{version_tools}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DUNIX $(wx-gtk2-unicode-config --cflags)" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_desktopdir},%{_libdir}/scummvm}

install scummvm $RPM_BUILD_ROOT%{_bindir}
#install scummvm.6 $RPM_BUILD_ROOT%{_mandir}/man6

install plugins/lib*.so $RPM_BUILD_ROOT%{_libdir}/scummvm

cd scummvm-tools-%{version_tools}
install compress_agos		$RPM_BUILD_ROOT%{_bindir}
install compress_kyra		$RPM_BUILD_ROOT%{_bindir}
install compress_queen		$RPM_BUILD_ROOT%{_bindir}
install compress_saga		$RPM_BUILD_ROOT%{_bindir}
install compress_scumm_bun	$RPM_BUILD_ROOT%{_bindir}
install compress_scumm_san	$RPM_BUILD_ROOT%{_bindir}
install compress_scumm_sou	$RPM_BUILD_ROOT%{_bindir}
install compress_sword1		$RPM_BUILD_ROOT%{_bindir}
install compress_sword2		$RPM_BUILD_ROOT%{_bindir}
install compress_touche		$RPM_BUILD_ROOT%{_bindir}
install convert_dxa.sh		$RPM_BUILD_ROOT%{_bindir}
install dekyra			$RPM_BUILD_ROOT%{_bindir}
install descumm			$RPM_BUILD_ROOT%{_bindir}
install desword2		$RPM_BUILD_ROOT%{_bindir}
install encode_dxa		$RPM_BUILD_ROOT%{_bindir}
install extract_agos		$RPM_BUILD_ROOT%{_bindir}
install extract_kyra		$RPM_BUILD_ROOT%{_bindir}
install extract_loom_tg16	$RPM_BUILD_ROOT%{_bindir}
install extract_mm_apple	$RPM_BUILD_ROOT%{_bindir}
install extract_mm_c64		$RPM_BUILD_ROOT%{_bindir}
install extract_mm_nes		$RPM_BUILD_ROOT%{_bindir}
install extract_scumm_mac	$RPM_BUILD_ROOT%{_bindir}
install extract_zak_c64		$RPM_BUILD_ROOT%{_bindir}
cd -

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install icons/%{name}.svg $RPM_BUILD_ROOT%{_pixmapsdir}

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install gui/themes/modern.ini $RPM_BUILD_ROOT%{_datadir}/%{name}
install gui/themes/modern.zip $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT NEWS README TODO
%attr(755,root,root) %{_bindir}/scummvm
%dir %{_libdir}/scummvm
#%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%dir %{_datadir}/%{name}

%files tools
%defattr(644,root,root,755)
%doc scummvm-tools-%{version_tools}/README
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/scummvm

%files engine-agi
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libagi.so

%files engine-agos
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libagos.so

%files engine-cine
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libcine.so

%files engine-cruise
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libcruise.so

%files engine-drascula
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libdrascula.so

%files engine-gob
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libgob.so

%files engine-igor
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libigor.so

%files engine-kyra
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libkyra.so

%files engine-lure
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/liblure.so

%files engine-parallaction
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libparallaction.so

%files engine-queen
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libqueen.so

%files engine-saga
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libsaga.so

%files engine-scumm
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libscumm.so

%files engine-sky
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libsky.so

%files engine-sword1
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libsword1.so

%files engine-sword2
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libsword2.so

%files engine-touche
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libtouche.so

%files theme-modern
%defattr(644,root,root,755)
%{_datadir}/%{name}/modern.*
