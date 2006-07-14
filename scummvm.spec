# TODO:
#  - include gui/themes/modern* and teach scummvm to search
#    for it in some system paths, not current dir
#
%define		version_tools	0.9.0
Summary:	SCUMM graphic adventure game interpreter
Summary(pl):	Interpreter przygodówek opartych na SCUMM
Name:		scummvm
Version:	0.9.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/scummvm/%{name}-%{version}.tar.bz2
# Source0-md5:	5eede9c97d1883f80770a3e211419783
Source1:	http://dl.sourceforge.net/scummvm/%{name}-tools-%{version_tools}.tar.bz2
# Source1-md5:	c8164fa1cca90b1c3bff1c8949d875a3
Source2:	%{name}.desktop
Source3:	%{name}.png
URL:		http://scummvm.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.2
%ifarch %{ix86} %{x8664}
BuildRequires:	fluidsynth-devel
%endif
BuildRequires:	libmad-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mpeg2dec-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	sed >= 4.0
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

sed -i -e 's:"plugins/":"%{_libdir}/scummvm/":' base/plugins.cpp

%build
./configure \
	--disable-debug \
%ifnarch %{ix86}
	--disable-nasm \
%endif
	--enable-lure \
	--enable-cine \
	--enable-plugins

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -DDYNAMIC_MODULES -fpic" \
	LDFLAGS="%{rpmldflags}"

cd tools-%{version_tools}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_desktopdir},%{_libdir}/scummvm}

install scummvm $RPM_BUILD_ROOT%{_bindir}
#install scummvm.6 $RPM_BUILD_ROOT%{_mandir}/man6

install plugins/lib*.so $RPM_BUILD_ROOT%{_libdir}/scummvm

cd tools-%{version_tools}
install compress_kyra		$RPM_BUILD_ROOT%{_bindir}
install compress_queen		$RPM_BUILD_ROOT%{_bindir}
install compress_saga		$RPM_BUILD_ROOT%{_bindir}
install compress_scumm_bun	$RPM_BUILD_ROOT%{_bindir}
install compress_scumm_san	$RPM_BUILD_ROOT%{_bindir}
install compress_scumm_sou	$RPM_BUILD_ROOT%{_bindir}
install compress_simon		$RPM_BUILD_ROOT%{_bindir}
install compress_sword1		$RPM_BUILD_ROOT%{_bindir}
install compress_sword2		$RPM_BUILD_ROOT%{_bindir}
install dekyra			$RPM_BUILD_ROOT%{_bindir}
install descumm			$RPM_BUILD_ROOT%{_bindir}
install desword2		$RPM_BUILD_ROOT%{_bindir}
install encode_dxa		$RPM_BUILD_ROOT%{_bindir}
install extract_kyra		$RPM_BUILD_ROOT%{_bindir}
install extract_loom_tg16	$RPM_BUILD_ROOT%{_bindir}
install extract_mm_c64		$RPM_BUILD_ROOT%{_bindir}
install extract_mm_nes		$RPM_BUILD_ROOT%{_bindir}
install extract_scumm_mac	$RPM_BUILD_ROOT%{_bindir}
install extract_simon1_amiga	$RPM_BUILD_ROOT%{_bindir}
install extract_zak_c64		$RPM_BUILD_ROOT%{_bindir}
cd -

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/scummvm
%{_libdir}/scummvm
#%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_desktopdir}/*

%files tools
%defattr(644,root,root,755)
%doc tools-%{version_tools}/README
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/scummvm
