%define		version_tools	0.6.0
Summary:	SCUMM graphic adventure game interpreter
Summary(pl):	Interpreter przygodówek opartych na SCUMM
Name:		scummvm
Version:	0.6.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	efc4207a7f10b24e9fc5afa10ed9c455
Source1:	http://dl.sourceforge.net/%{name}/%{name}-tools-%{version_tools}.tar.bz2
# Source1-md5:	09ded7a8177fda1b861731052b8693c4
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-gcc34.patch
URL:		http://scummvm.sourceforge.net/
BuildRequires:	libmad-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mpeg2dec-devel
BuildRequires:	SDL-devel >= 1.2.2
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ScummVM is an implementation of the SCUMM (Script Creation Utility for
Maniac Mansion) engine used in various Lucas Arts games such as Monkey
Island and Day of the Tentacle. At this time ScummVM should be considered
ALPHA software, as it's still under heavy development. Be aware that while
many games will work with few major bugs, crashes can happen. Also note
that saved games can, and probably will, be incompatible between releases.

Also ScummVM is capable of playing several non-SCUMM games, at the moment
this includes Simon The Sorcerer.

%description -l pl
ScummVM jest implementacj± silnika SCUMM (Narzêdzie tworz±ce skrypty dla
Maniac Mansion) u¿ywanego w wielu grach Lucas Arts takich jak Monkey Island,
czy Day of the Tentacle. ScummVM jest ca³y czas intensywnie rozwijany i
powinien byæ traktowany jako program w stanie ALPHA. Wiele gier mo¿e siê
wysypywaæ, lub dzia³aæ z b³êdami. Zapisane stany gry bêd± prawdopodobnie
niekompatybilne pomiêdzy ró¿nymi wersjami ScummVM.

ScummVM potrafi równie¿ obs³u¿yæ gry nie oparte na silniku SCUMM. W chwili
obecnej jest to Simon The Sorcerer.

%package tools
Summary:	SCUMM tools
Summary(pl):	Narzêdzia zwi±zane ze SCUMM
Group:		X11/Applications/Games

%description tools
SCUMM tools.

%description tools -l pl
Narzêdzia zwi±zane ze SCUMM.

%prep
%setup -q -a 1
%patch0 -p1

%build
./configure \
	--disable-debug

%{__make} \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

cd %{name}-tools-%{version_tools}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_desktopdir}}

install scummvm $RPM_BUILD_ROOT%{_bindir}
install scummvm.6 $RPM_BUILD_ROOT%{_mandir}/man6

cd %{name}-tools-%{version_tools}
install {descumm,rescumm,simon2mp3} $RPM_BUILD_ROOT%{_bindir}
install extract $RPM_BUILD_ROOT%{_bindir}/extract-scummvm
cd -

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/scummvm
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_desktopdir}/*

%files tools
%defattr(644,root,root,755)
%doc %{name}-tools-%{version_tools}/README
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/scummvm
