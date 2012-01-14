%define		version_tools	1.4.0
Summary:	Graphic adventure game interpreter
Summary(pl.UTF-8):	Interpreter gier przygodowych
Name:		scummvm
Version:	1.4.0
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/scummvm/%{name}-%{version}.tar.bz2
# Source0-md5:	361000b78ebf0d0f449e98238d677be1
Source1:	http://dl.sourceforge.net/scummvm/%{name}-tools-%{version_tools}.tar.bz2
# Source1-md5:	471138a83de3bacd565e18b617055494
Source2:	%{name}.desktop
Patch0:		%{name}-wx-config.patch
URL:		http://scummvm.org/
BuildRequires:	SDL-devel >= 1.2.2
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	flac-devel >= 1.0.1
%ifarch %{ix86} %{x8664}
BuildRequires:	fluidsynth-devel
%endif
BuildRequires:	freetype-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libmpeg2-devel >= 0.3.2
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	wxGTK2-unicode-devel
BuildRequires:	wxWidgets-devel
BuildRequires:	zlib-devel
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
Requires:	%{name} = %{version}-%{release}

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
Requires:	%{name} = %{version}-%{release}

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

%package engine-cge
Summary:	CGE engine
Summary(pl.UTF-8):	Silnik CGE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-cge
CGE engine.

%description engine-cge -l pl.UTF-8
Silnik CGE.

%package engine-cine
Summary:	Cinematique engine
Summary(pl.UTF-8):	Silnik Cinematique
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-cine
Cinematique engine.

%description engine-cine -l pl.UTF-8
Silnik Cinematique.

%package engine-composer
Summary:	Composer engine
Summary(pl.UTF-8):	Silnik Composer
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-composer
Composer engine.

%description engine-composer -l pl.UTF-8
Silnik Composer.

%package engine-cruise
Summary:	Cruise engine
Summary(pl.UTF-8):	Silnik Cruise
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-cruise
Cruise engine.

%description engine-cruise -l pl.UTF-8
Silnik Cruise.

%package engine-draci
Summary:	Draci engine
Summary(pl.UTF-8):	Silnik Draci
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-draci
Draci engine.

%description engine-draci -l pl.UTF-8
Silnik Draci.

%package engine-drascula
Summary:	Drascula engine
Summary(pl.UTF-8):	Silnik Drascula
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-drascula
Drascula engine.

%description engine-drascula -l pl.UTF-8
Silnik Drascula.

%package engine-dreamweb
Summary:	Dreamweb engine
Summary(pl.UTF-8):	Silnik Dreamweb
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-dreamweb
Dreamweb engine.

%description engine-dreamweb -l pl.UTF-8
Silnik Dreamweb.

%package engine-gob
Summary:	Gob engine
Summary(pl.UTF-8):	Silnik Gob
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-gob
Engine to run adventure games created by Coktel Vision.

%description engine-gob -l pl.UTF-8
Silnik do uruchamiania gier stworzonych przez Coktel Vision.

%package engine-groovie
Summary:	Groovie engine
Summary(pl.UTF-8):	Silnik Groovie
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-groovie
Engine to run adventure games created by Trilobyte or
Aftermath Media (The 7th Guest, The 11th Hour).

%description engine-groovie -l pl.UTF-8
Silnik do uruchamiania gier stworzonych przez Trilobyte
i Aftermath Media (The 7th Guest, The 11th Hour).

%package engine-hugo
Summary:	Hugo engine
Summary(pl.UTF-8):	Silnik Hugo
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-hugo
Hugo engine.

%description engine-hugo -l pl.UTF-8
Silnik Hugo.

%package engine-kyra
Summary:	Kyrandia engine
Summary(pl.UTF-8):	Silnik Kyrandia
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-kyra
Kyrandia engine.

%description engine-kyra -l pl.UTF-8
Silnik Kyrandia.

%package engine-lastexpress
Summary:	Lastexpress engine
Summary(pl.UTF-8):	Silnik Lastexpress
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-lastexpress
Lastexpress is the engine for the game Lastexpress of the Temptress.

%description engine-lastexpress -l pl.UTF-8
Lastexpress jest silnikiem dla gry Lastexpress of the Temptress.

%package engine-lure
Summary:	Lure engine
Summary(pl.UTF-8):	Silnik Lure
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-lure
Lure is the engine for the game Lure of the Temptress.

%description engine-lure -l pl.UTF-8
Lure jest silnikiem dla gry Lure of the Temptress.

%package engine-m4
Summary:	M4/MADS engine
Summary(pl.UTF-8):	Silnik M4/MADS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-m4
MADS stands for the MicroProse Adventure Development System,
used in the three adventure games they made. It was later sold
to Sanctuary Woods, who continued development on it and named
it M4 (MADS version 4 perhaps) and released two more games.

%description engine-m4 -l pl.UTF-8
MADS to MicroProse Adventure Development System, używany jest
w trzech grach stworzonych przez MicroProse. Został sprzedany
do Sanctuary Woods i dalej rozwijany jako M4.

%package engine-made
Summary:	MADE engine
Summary(pl.UTF-8):	Silnik MADE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-made
MADE stands for Multimedia Applications Development Environment,
and was used by Activision to create some of their point'n'click
adventure games. 

%description engine-made -l pl.UTF-8
MADE to Multimedia Applications Development Environment,
był używany przez Activision w grach przygodowych.

%package engine-mohawk
Summary:	Mohawk engine
Summary(pl.UTF-8):	Silnik Mohawk
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-mohawk
The Mohawk engine was developed by Brøderbund starting
in the early 1990's with the Windows port of Myst.

%description engine-mohawk -l pl.UTF-8
Silnik Mohawk został stworzony przez Brøderbund we wczesnych
latach 90-ych, na potrzeby gry Myst.

%package engine-parallaction
Summary:	Parallaction engine
Summary(pl.UTF-8):	Silnik Parallaction
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-parallaction
Parallaction engine.

%description engine-parallaction -l pl.UTF-8
Silnik Parallaction.

%package engine-queen
Summary:	Queen engine
Summary(pl.UTF-8):	Silnik Queen
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

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
Requires:	%{name} = %{version}-%{release}

%description engine-saga
SAGA (Scripts for Animated Graphic Adventures) engine.

%description engine-saga -l pl.UTF-8
Silnik SAGA (Scripts for Animated Graphic Adventures).

%package engine-sci
Summary:	Sierra's "SCript Interpreter"
Summary(pl.UTF-8):	SCript Interpreter Sierry
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-sci
Sierra's "SCript Interpreter" and the "Sierra's Creative Interpreter.

%description engine-sci -l pl.UTF-8
SCript Interpreter Sierry.

%package engine-scumm
Summary:	Script Creation Utility for Maniac Mansion
Summary(pl.UTF-8):	Script Creation Utility for Maniac Mansion
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

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
Requires:	%{name} = %{version}-%{release}

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
Requires:	%{name} = %{version}-%{release}

%description engine-sword1
Sword1 engine.

%description engine-sword1 -l pl.UTF-8
Silnik Sword1.

%package engine-sword2
Summary:	Sword2 engine
Summary(pl.UTF-8):	Silnik Sword2
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-sword2
Sword2 engine.

%description engine-sword2 -l pl.UTF-8
Silnik Sword2.

%package engine-sword25
Summary:	Sword2.5 engine
Summary(pl.UTF-8):	Silnik Sword2.5
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-sword25
Sword2.5 engine.

%description engine-sword25 -l pl.UTF-8
Silnik Sword2.5.

%package engine-teenagent
Summary:	TeenAgent engine
Summary(pl.UTF-8):	Silnik TeenAgent
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-teenagent
This engine is only used by TeenAgent.

%description engine-teenagent -l pl.UTF-8
Ten silnik jest używany tylko przez TeenAgenta.

%package engine-testbed
Summary:	Testbed engine
Summary(pl.UTF-8):	Silnik Testbed
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-testbed
TestBed: the Testing framework engine

%description engine-testbed -l pl.UTF-8
TestBed: the Testing framework engine

%package engine-tinsel
Summary:	Tinsel engine
Summary(pl.UTF-8):	Silnik Tinsel
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-tinsel
This engine is only used by Discworld 1 and Discworld 2.

%description engine-tinsel -l pl.UTF-8
Ten silnik jest używany tylko przez Discworld 1 i Discworld 2.

%package engine-toon
Summary:	Toon engine
Summary(pl.UTF-8):	Silnik Toon
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-toon
Toonstruck engine.

%description engine-toon -l pl.UTF-8
Silnik Toonstruck.

%package engine-touche
Summary:	Touche engine
Summary(pl.UTF-8):	Silnik Touche
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-touche
This engine is only used by Touche: The Adventures of the Fifth
Musketeer.

%description engine-touche -l pl.UTF-8
Ten silnik jest używany tylko przez Touché: Przygody Piątego
Muszkietera.

%package engine-tsage
Summary:	Tsage engine
Summary(pl.UTF-8):	Silnik Tsage
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-tsage
This engine is only used by Ringworld: Revenge Of The Patriarch.

%description engine-tsage -l pl.UTF-8
Ten silnik jest używany tylko przez Ringworld: Revenge Of The Patriach.

%package engine-tucker
Summary:	Tucker engine
Summary(pl.UTF-8):	Silnik Tucker
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-tucker
The Tucker engine is used in Bud Tucker in Double Trouble.

%description engine-tucker -l pl.UTF-8
Silnik Tucker jest używany przez Bud Tucker in Double Trouble.

%package theme-classic
Summary:	Theme classic for ScummVM
Summary(pl.UTF-8):	Motyw classic dla ScummVM
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description theme-classic
Theme classic for ScummVM.

%description theme-classic -l pl.UTF-8
Motyw classic dla ScummVM.

%package theme-modern
Summary:	Theme modern for ScummVM
Summary(pl.UTF-8):	Motyw modern dla ScummVM
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description theme-modern
Theme modern for ScummVM.

%description theme-modern -l pl.UTF-8
Motyw modern dla ScummVM.

%prep
%setup -q -a 1
cd scummvm-tools-%{version_tools}
%patch0 -p2
cd ..

%{__sed} -i -e 's:"plugins":"%{_libdir}/scummvm":' base/plugins.cpp

%build
./configure \
	--prefix=/usr \
	--disable-debug \
	--enable-all-engines \
	--enable-plugins \
	--default-dynamic

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcppflags} %{rpmcflags} -DDYNAMIC_MODULES -fpic $(wx-gtk2-unicode-config --cppflags)" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}"

cd scummvm-tools-%{version_tools}
./configure \
	--prefix=/usr \
	--disable-debug

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcppflags} %{rpmcflags} -DUNIX $(wx-gtk2-unicode-config --cppflags)" \
	LDFLAGS="%{rpmcflags} %{rpmldflags} $(wx-gtk2-unicode-config --libs)"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_desktopdir},%{_libdir}/scummvm}

install scummvm $RPM_BUILD_ROOT%{_bindir}
#install scummvm.6 $RPM_BUILD_ROOT%{_mandir}/man6

install plugins/lib*.so $RPM_BUILD_ROOT%{_libdir}/scummvm

%{__make} -C scummvm-tools-%{version_tools} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install icons/%{name}.svg $RPM_BUILD_ROOT%{_pixmapsdir}

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install gui/themes/*.zip $RPM_BUILD_ROOT%{_datadir}/%{name}

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
%{_datadir}/scummvm-tools

%files engine-agi
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libagi.so

%files engine-agos
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libagos.so

%files engine-cge
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libcge.so

%files engine-cine
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libcine.so

%files engine-composer
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libcomposer.so

%files engine-cruise
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libcruise.so

%files engine-draci
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libdraci.so

%files engine-drascula
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libdrascula.so

%files engine-dreamweb
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libdreamweb.so

%files engine-gob
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libgob.so

%files engine-groovie
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libgroovie.so

%files engine-hugo
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libhugo.so

%files engine-kyra
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libkyra.so

%files engine-lastexpress
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/liblastexpress.so

%files engine-lure
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/liblure.so

%files engine-m4
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libm4.so

%files engine-made
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libmade.so

%files engine-mohawk
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libmohawk.so

%files engine-parallaction
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libparallaction.so

%files engine-queen
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libqueen.so

%files engine-saga
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libsaga.so

%files engine-sci
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libsci.so

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

%files engine-sword25
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libsword25.so

%files engine-teenagent
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libteenagent.so

%files engine-testbed
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libtestbed.so

%files engine-tinsel
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libtinsel.so

%files engine-touche
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libtouche.so

%files engine-toon
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libtoon.so

%files engine-tsage
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libtsage.so

%files engine-tucker
%defattr(644,root,root,755)
%dir %{_libdir}/scummvm/libtucker.so

%files theme-classic
%defattr(644,root,root,755)
%{_datadir}/%{name}/scummclassic.*

%files theme-modern
%defattr(644,root,root,755)
%{_datadir}/%{name}/scummmodern.*
