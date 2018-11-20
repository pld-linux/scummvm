%define		version_tools	1.9.0
Summary:	Graphic adventure game interpreter
Summary(pl.UTF-8):	Interpreter gier przygodowych
Name:		scummvm
Version:	1.9.0
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://scummvm.org/frs/scummvm/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	3255706992edaf30380ce8a49cb305b7
Source1:	http://scummvm.org/frs/scummvm-tools/%{version_tools}/%{name}-tools-%{version_tools}.tar.xz
# Source1-md5:	7b472cc2895161c64630df92df4c65b0
Source2:	%{name}.desktop
Patch0:		%{name}-wx-config.patch
Patch1:		dwarf-debug.patch
URL:		http://scummvm.org/
BuildRequires:	SDL-devel >= 1.2.2
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	flac-devel >= 1.0.1
%ifarch %{ix86} %{x8664}
BuildRequires:	fluidsynth-devel
%endif
BuildRequires:	freetype-devel
BuildRequires:	libmad-devel
BuildRequires:	libmpeg2-devel >= 0.3.2
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	sed >= 4.0
BuildRequires:	wxGTK2-unicode-devel
BuildRequires:	wxWidgets-devel
BuildRequires:	zlib-devel
BuildRequires:	zlib-devel
Obsoletes:	scummvm-engine-m4
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
Silnik AGI (Adventure Game Interpreter) był używany przez firmę Sierra
w jej wczesnych grach przygodowych.

%package engine-agos
Summary:	AGOS engine
Summary(pl.UTF-8):	Silnik AGOS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-agos
The AGOS Engine was originally created by Alan Cox at HorrorSoft and
is based on AberMUD V, with graphical extensions. Required for
following games:
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
Engine to run adventure games created by Trilobyte or Aftermath Media
(The 7th Guest, The 11th Hour).

%description engine-groovie -l pl.UTF-8
Silnik do uruchamiania gier stworzonych przez Trilobyte i Aftermath
Media (The 7th Guest, The 11th Hour).

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

%package engine-made
Summary:	MADE engine
Summary(pl.UTF-8):	Silnik MADE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-made
MADE stands for Multimedia Applications Development Environment, and
was used by Activision to create some of their point'n'click adventure
games.

%description engine-made -l pl.UTF-8
MADE to Multimedia Applications Development Environment, był używany
przez Activision w grach przygodowych.

%package engine-mohawk
Summary:	Mohawk engine
Summary(pl.UTF-8):	Silnik Mohawk
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-mohawk
The Mohawk engine was developed by Brøderbund starting in the early
1990's with the Windows port of Myst.

%description engine-mohawk -l pl.UTF-8
Silnik Mohawk został stworzony przez Brøderbund we wczesnych latach
90-ych, na potrzeby gry Myst.

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
Ten silnik jest używany tylko przez Ringworld: Revenge Of The
Patriach.

%package engine-tucker
Summary:	Tucker engine
Summary(pl.UTF-8):	Silnik Tucker
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-tucker
The Tucker engine is used in Bud Tucker in Double Trouble.

%description engine-tucker -l pl.UTF-8
Silnik Tucker jest używany przez Bud Tucker in Double Trouble.

%package engine-hopkins
Summary:	Hopkins FBI engine
Summary(pl.UTF-8):	Silnik Hopkins FBI
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-hopkins
This engine is used by Hopkins FBI.

%description engine-hopkins -l pl.UTF-8
Ten silnik jest używany przez Hopkins FBI.

%package engine-pegasus
Summary:	Pegasus engine
Summary(pl.UTF-8):	Silnik Pegasus
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-pegasus
This engine is used by The Journeyman Project: Pegasus Prime.

%description engine-pegasus -l pl.UTF-8
Ten silnik jest używany przez The Journeyman Project: Pegasus Prime.

%package engine-toltecs
Summary:	Toltecs engine
Summary(pl.UTF-8):	Silnik Toltecs
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-toltecs
This engine is used by 3 Skulls of the Toltecs.

%description engine-toltecs -l pl.UTF-8
Ten silnik jest używany przez 3 Skulls of the Toltecs.

%package engine-tony
Summary:	Tony engine
Summary(pl.UTF-8):	Silnik Tony
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-tony
This engine is used by Tony Tough and the Night of Roasted Moths.

%description engine-tony -l pl.UTF-8
Ten silnik jest używany przez Tony Tough and the Night of Roasted
Moths.

%package engine-wintermute
Summary:	Wintermute engine
Summary(pl.UTF-8):	Silnik Wintermute
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-wintermute
The engine is used for the Wintermute games.

%description engine-wintermute -l pl.UTF-8
Ten silnik jest używany przez gry Wintermute.

%package engine-access
Summary:	Access engine
Summary(pl.UTF-8):	Silnik Access
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-access
The engine is used for the Amazon: Guardians of Eden,
Martian Memorandum and Noctropolis games.

%description engine-access -l pl.UTF-8
Ten silnik jest używany przez gry Amazon: Guardians of Eden,
Martian Memorandum i Noctropolis.

%package engine-adl
Summary:	ADL engine
Summary(pl.UTF-8):	Silnik ADL
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-adl
The engine is used for the Sierra ADL Hi-Res Adventure games.

%description engine-adl -l pl.UTF-8
Ten silnik jest używany przez gry Sierra ADL Hi-Res Adventure.

%package engine-avalanche
Summary:	Avalanche engine
Summary(pl.UTF-8):	Silnik Avalanche
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-avalanche
The engine is used for the Lord Avalot d'Argent game.

%description engine-avalanche -l pl.UTF-8
Ten silnik jest używany przez grę Lord Avalot d'Argent.

%package engine-bbvs
Summary:	BBVS engine
Summary(pl.UTF-8):	Silnik BBVS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-bbvs
The engine is used for the Beavis and Butt-Head in
Virtual Stupidity game.

%description engine-bbvs -l pl.UTF-8
Ten silnik jest używany przez grę Beavis and Butt-Head in
Virtual Stupidity.

%package engine-cge2
Summary:	CGE2 engine
Summary(pl.UTF-8):	Silnik CGE2
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-cge2
The engine is used for the Sfinx game.

%description engine-cge2 -l pl.UTF-8
Ten silnik jest używany przez grę Sfinx.

%package engine-director
Summary:	Director engine
Summary(pl.UTF-8):	Silnik Director
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-director
The engine is used for the Director games.

%description engine-director -l pl.UTF-8
Ten silnik jest używany przez gry Director.

%package engine-dm
Summary:	DM engine
Summary(pl.UTF-8):	Silnik DM
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-dm
The engine is used for the Dungeon Master game.

%description engine-dm -l pl.UTF-8
Ten silnik jest używany przez grę Dungeon Master.

%package engine-fullpipe
Summary:	Fullpipe engine
Summary(pl.UTF-8):	Silnik Fullpipe
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-fullpipe
The engine is used for the Full Pipe game.

%description engine-fullpipe -l pl.UTF-8
Ten silnik jest używany przez grę Full Pipe.

%package engine-gnap
Summary:	GNAP engine
Summary(pl.UTF-8):	Silnik GNAP
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-gnap
The engine is used for the U.F.O.s game.

%description engine-gnap -l pl.UTF-8
Ten silnik jest używany przez grę U.F.O.s.

%package engine-lab
Summary:	Lab engine
Summary(pl.UTF-8):	Silnik Lab
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-lab
The engine is used for The Labyrinth of Time game.

%description engine-lab -l pl.UTF-8
Ten silnik jest używany przez grę The Labyrinth of Time.

%package engine-macventure
Summary:	MacVenture engine
Summary(pl.UTF-8):	Silnik MacVenture
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-macventure
The engine is used for the Deja Vu game.

%description engine-macventure -l pl.UTF-8
Ten silnik jest używany przez grę Deja Vu.

%package engine-mads
Summary:	MADS engine
Summary(pl.UTF-8):	Silnik MADS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-mads
The engine is used for the Dragonsphere and
Return of the Phantom games.

%description engine-mads -l pl.UTF-8
Ten silnik jest używany przez gry Dragonsphere i
Return of the Phantom.

%package engine-mortevielle
Summary:	Mortevielle engine
Summary(pl.UTF-8):	Silnik Mortevielle
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-mortevielle
The engine is used for the Mortville Manor game.

%description engine-mortevielle -l pl.UTF-8
Ten silnik jest używany przez grę Mortville Manor.

%package engine-neverhood
Summary:	Neverhood engine
Summary(pl.UTF-8):	Silnik Neverhood
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-neverhood
The engine is used for the Neverhood game.

%description engine-neverhood -l pl.UTF-8
Ten silnik jest używany przez grę Neverhood.

%package engine-prince
Summary:	Prince engine
Summary(pl.UTF-8):	Silnik Prince
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-prince
The engine is used for The Prince and the Coward game.

%description engine-prince -l pl.UTF-8
Ten silnik jest używany przez grę The Prince and the Coward.

%package engine-sherlock
Summary:	Sherlock engine
Summary(pl.UTF-8):	Silnik Sherlock
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-sherlock
The engine is used for The Lost Files of Sherlock Holmes games.

%description engine-sherlock -l pl.UTF-8
Ten silnik jest używany przez gry The Lost Files of Sherlock Holmes.

%package engine-titanic
Summary:	Titanic engine
Summary(pl.UTF-8):	Silnik Titanic
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-titanic
The engine is used for Starship Titanic game.

%description engine-titanic -l pl.UTF-8
Ten silnik jest używany przez gry Starship Titanic.

%package engine-voyeur
Summary:	Voyeur engine
Summary(pl.UTF-8):	Silnik Voyeur
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-voyeur
The engine is used for the Voyeur game.

%description engine-voyeur -l pl.UTF-8
Ten silnik jest używany przez grę Voyeur.

%package engine-wage
Summary:	WAGE engine
Summary(pl.UTF-8):	Silnik WAGE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-wage
The engine is used for the WAGE games.

%description engine-wage -l pl.UTF-8
Ten silnik jest używany przez gry WAGE.

%package engine-xeen
Summary:	Xeen engine
Summary(pl.UTF-8):	Silnik Xeen
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-xeen
The engine is used for the Might and Magic III, IV, V
and World of Xeen games.

%description engine-xeen -l pl.UTF-8
Ten silnik jest używany przez gry Might and Magic III, IV, V
i World of Xeen.

%package engine-zvision
Summary:	ZVision engine
Summary(pl.UTF-8):	Silnik ZVision
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description engine-zvision
The engine is used for the Zork Nemesis and
Zork: Grand Inquisitor games.

%description engine-zvision -l pl.UTF-8
Ten silnik jest używany przez gry Zork Nemesis
i Zork: Grand Inquisitor.

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
%patch1 -p1
cd scummvm-tools-%{version_tools}
%patch0 -p2
cd ..

%{__sed} -i -e 's:"plugins":"%{_libdir}/scummvm":' base/plugins.cpp

%build
./configure \
	--prefix=%{_prefix} \
	--disable-debug \
	--enable-all-engines \
	--enable-plugins \
	--default-dynamic

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcppflags} %{rpmcflags} -fpic $(wx-gtk2-unicode-config --cppflags)" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}"

cd scummvm-tools-%{version_tools}
./configure \
	--prefix=%{_prefix} \
	--disable-debug

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcppflags} %{rpmcflags} -DUNIX -fpermissive $(wx-gtk2-unicode-config --cppflags)" \
	LDFLAGS="%{rpmcflags} %{rpmldflags} $(wx-gtk2-unicode-config --libs)"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_desktopdir},%{_libdir}/scummvm}

cp -p scummvm $RPM_BUILD_ROOT%{_bindir}
#install scummvm.6 $RPM_BUILD_ROOT%{_mandir}/man6

cp -p plugins/lib*.so $RPM_BUILD_ROOT%{_libdir}/scummvm

%{__make} -C scummvm-tools-%{version_tools} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
cp -p icons/%{name}.svg $RPM_BUILD_ROOT%{_pixmapsdir}

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -p gui/themes/*.zip $RPM_BUILD_ROOT%{_datadir}/%{name}

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
%attr(755,root,root) %{_libdir}/scummvm/libagi.so

%files engine-agos
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libagos.so

%files engine-cge
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libcge.so

%files engine-cine
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libcine.so

%files engine-composer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libcomposer.so

%files engine-cruise
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libcruise.so

%files engine-draci
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libdraci.so

%files engine-drascula
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libdrascula.so

%files engine-dreamweb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libdreamweb.so

%files engine-gob
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libgob.so

%files engine-groovie
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libgroovie.so

%files engine-hugo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libhugo.so

%files engine-kyra
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libkyra.so

%files engine-lastexpress
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/liblastexpress.so

%files engine-lure
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/liblure.so

%files engine-made
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libmade.so

%files engine-mohawk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libmohawk.so

%files engine-parallaction
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libparallaction.so

%files engine-queen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libqueen.so

%files engine-saga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libsaga.so

%files engine-sci
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libsci.so

%files engine-scumm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libscumm.so

%files engine-sky
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libsky.so

%files engine-sword1
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libsword1.so

%files engine-sword2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libsword2.so

%files engine-sword25
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libsword25.so

%files engine-teenagent
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libteenagent.so

%files engine-testbed
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libtestbed.so

%files engine-tinsel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libtinsel.so

%files engine-touche
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libtouche.so

%files engine-toon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libtoon.so

%files engine-tsage
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libtsage.so

%files engine-tucker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libtucker.so

%files engine-hopkins
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libhopkins.so

%files engine-pegasus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libpegasus.so

%files engine-toltecs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libtoltecs.so

%files engine-tony
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libtony.so

%files engine-wintermute
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libwintermute.so

%files engine-access
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libaccess.so

%files engine-adl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libadl.so

%files engine-avalanche
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libavalanche.so

%files engine-bbvs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libbbvs.so

%files engine-cge2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libcge2.so

%files engine-director
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libdirector.so

%files engine-dm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libdm.so

%files engine-fullpipe
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libfullpipe.so

%files engine-gnap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libgnap.so

%files engine-lab
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/liblab.so

%files engine-macventure
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libmacventure.so

%files engine-mads
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libmads.so

%files engine-mortevielle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libmortevielle.so

%files engine-neverhood
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libneverhood.so

%files engine-prince
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libprince.so

%files engine-sherlock
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libsherlock.so

%files engine-titanic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libtitanic.so

%files engine-voyeur
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libvoyeur.so

%files engine-wage
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libwage.so

%files engine-xeen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libxeen.so

%files engine-zvision
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/scummvm/libzvision.so

%files theme-classic
%defattr(644,root,root,755)
%{_datadir}/%{name}/scummclassic.*

%files theme-modern
%defattr(644,root,root,755)
%{_datadir}/%{name}/scummmodern.*
