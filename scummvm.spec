%define		version_tools	0.7.0
Summary:	SCUMM graphic adventure game interpreter
Summary(pl):	Interpreter przygod�wek opartych na SCUMM
Name:		scummvm
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://belnet.dl.sourceforge.net/scummvm/%{name}-%{version}.tar.bz2
# Source0-md5:	a935499011c59441fcce8322ea1c4f1d
Source1:	http://dl.sourceforge.net/scummvm/%{name}-tools-%{version_tools}.tar.bz2
# Source1-md5:	eeebbd4e309a8564dd911d5c26fed2f0
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-asm.patch
URL:		http://scummvm.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.2
BuildRequires:	libmad-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mpeg2dec-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
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
ScummVM jest zbiorem interpreter�w zdolnych do emulacji kilku silnik�w
gier przygodowych. ScummVM g��wnie wspiera gry stworzone z u�yciem
silnika SCUMM (Script Creation Utility for Maniac Mansion), u�ywanego
przez takie tytu�y stworzone przez Lucas Arts jak Monkey Island, Day
of the Tentacle.

ScummVM potrafi r�wnie� interpretowa� kilka gier nie opartych na
SCUMM. W chwili obecnej s� to Beneath a Steel Sky, Broken Sword 1 i 2,
Flight of the Amazon Queen oraz Simon the Sorcerer 1 i 2.

ScummVM jest ca�y czas intensywnie rozwijany i powinien by� traktowany
jako program w stanie beta. Wiele gier powinno da� si� sko�czy� bez
wi�kszych b��d�w, nale�y by� jednak �wiadomym, �e program mo�e si�
czasem wysypa�.

%package tools
Summary:	ScummVM tools
Summary(pl):	Narz�dzia zwi�zane ze ScummVM
Group:		X11/Applications/Games

%description tools
Collection of various tools that may be useful to use in conjunction
with ScummVM.

%description tools -l pl
Zestaw narz�dzi mog�cych by� u�ytecznymi w po��czeniu ze ScummVM.

%prep
%setup -q -a 1
%patch0 -p1

sed -i -e 's:(name "/lib" name ".so"):("%{_libdir}/lib" name ".so"):' base/plugins.cpp

%build
./configure \
	--disable-debug \
%ifnarch %{ix86}
	--disable-nasm \
%endif
	--enable-kyra \
	--enable-plugins

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -DDYNAMIC_MODULES -fpic" \
	LDFLAGS="%{rpmldflags}"

cd %{name}-tools-%{version_tools}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_desktopdir},%{_libdir}}

install scummvm $RPM_BUILD_ROOT%{_bindir}
install scummvm.6 $RPM_BUILD_ROOT%{_mandir}/man6

for i in kyra queen scumm sky sword{1,2} simon
do
	install $i/lib$i.so $RPM_BUILD_ROOT%{_libdir}
done

cd %{name}-tools-%{version_tools}
install compress_san	$RPM_BUILD_ROOT%{_bindir}
install convbdf		$RPM_BUILD_ROOT%{_bindir}
install dekyra		$RPM_BUILD_ROOT%{_bindir}
install descumm		$RPM_BUILD_ROOT%{_bindir}
install desword2	$RPM_BUILD_ROOT%{_bindir}
install extract		$RPM_BUILD_ROOT%{_bindir}/extract-scummvm
install kyra_unpak	$RPM_BUILD_ROOT%{_bindir}
install loom_tg16_extract	$RPM_BUILD_ROOT%{_bindir}
install mm_nes_extract	$RPM_BUILD_ROOT%{_bindir}
install queenrebuild	$RPM_BUILD_ROOT%{_bindir}
install rescumm		$RPM_BUILD_ROOT%{_bindir}
install saga2mp3	$RPM_BUILD_ROOT%{_bindir}
install simon1decr	$RPM_BUILD_ROOT%{_bindir}
install simon2mp3	$RPM_BUILD_ROOT%{_bindir}
install sword1mp3	$RPM_BUILD_ROOT%{_bindir}
install sword2mp3	$RPM_BUILD_ROOT%{_bindir}
cd -

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/scummvm
%attr(755,root,root) %{_libdir}/*
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_desktopdir}/*

%files tools
%defattr(644,root,root,755)
%doc %{name}-tools-%{version_tools}/README
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/scummvm
