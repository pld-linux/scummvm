%define		version_tools	0.6.1
Summary:	SCUMM graphic adventure game interpreter
Summary(pl):	Interpreter przygodówek opartych na SCUMM
Name:		scummvm
Version:	0.6.1b
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://puzzle.dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	143dd7cfe0995922c49e1f8a6cdf2055
Source1:	http://dl.sourceforge.net/%{name}/%{name}-tools-%{version_tools}-src.tar.bz2
# Source1-md5:	b2ba0801fbd85a568af1c5af14fd18ac
Source2:	%{name}.desktop
Source3:	%{name}.png
URL:		http://scummvm.sourceforge.net/
BuildRequires:	libmad-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mpeg2dec-devel
BuildRequires:	SDL-devel >= 1.2.2
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ScummVM is a collection of interpreters, capable of emulating several
adventure game engines. ScummVM mainly supports games created using
SCUMM (Script Creation Utility for Maniac Mansion), used in various
LucasArts games such as Monkey Island, Day of the Tentacle, and
others.

ScummVM also contains interpreters for several non-SCUMM games.
Currently these are Beneath a Steel Sky, Broken Sword 1 & 2, Flight of
the Amazon Queen and Simon the Sorcerer 1 & 2.

At this time ScummVM should be considered beta software, and is still
under heavy development. Be aware that whilst we attempt to make sure
that many games can be completed with few major bugs, crashes can
happen.

%description -l pl
ScummVM jest zbiorem interpreterów zdolnych do emulacji kilku silników
gier przygodowych. ScummVM g³ównie wspiera gry stworzone z u¿yciem
silnika SCUMM (Script Creation Utility for Maniac Mansion), u¿ywanego
przez takie tytu³y stworzone przez Lucas Arts jak Monkey Island, Day
of the Tentacle.

ScummVM potrafi równie¿ interpretowaæ kilka gier nie opartych na
SCUMM. W chwili obecnej s± to Beneath a Steel Sky, Broken Sword 1 i 2,
Flight of the Amazon Queen oraz Simon the Sorcerer 1 i 2.

ScummVM jest ca³y czas intensywnie rozwijany i powinien byæ traktowany
jako program w stanie beta. Wiele gier powinno daæ siê skoñczyæ bez
wiêkszych b³êdów, nale¿y byæ jednak ¶wiadomym, ¿e program mo¿e siê
czasem wysypaæ.

%package tools
Summary:	ScummVM tools
Summary(pl):	Narzêdzia zwi±zane ze ScummVM
Group:		X11/Applications/Games

%description tools
Collection of various tools that may be useful to use in conjunction
with ScummVM.

%description tools -l pl
Zestaw narzêdzi mog±cych byæ u¿ytecznymi w po³±czeniu ze ScummVM.

%prep
%setup -q -a 1

%build
./configure \
	--disable-debug

%{__make} \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

cd %{name}-%{version_tools}-tools
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_desktopdir}}

install scummvm $RPM_BUILD_ROOT%{_bindir}
install scummvm.6 $RPM_BUILD_ROOT%{_mandir}/man6

cd %{name}-%{version_tools}-tools
install {rescumm,loom_tg16_extract,mm_nes_extract} $RPM_BUILD_ROOT%{_bindir}
install {queenrebuild,simon2mp3,compress_san} $RPM_BUILD_ROOT%{_bindir}
install {descumm,desword2} $RPM_BUILD_ROOT%{_bindir}
install {simon1decr,convbdf} $RPM_BUILD_ROOT%{_bindir}
install extract $RPM_BUILD_ROOT%{_bindir}/extract-scummvm
cd -

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/scummvm
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_desktopdir}/*

%files tools
%defattr(644,root,root,755)
%doc %{name}-%{version_tools}-tools/README
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/scummvm
