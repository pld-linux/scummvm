Summary:	SCUMM graphic adventure game interpreter
Summary(pl):	Interpreter przygod�wek opartych na SCUMM
Name:		scummvm
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sf.net/scummvm/%{name}-%{version}.tar.bz2
#Source0-md5:	a66d3055c03bd2a0f612f483ecd05fe
Source1:	http://dl.sf.net/scummvm/%{name}-tools-%{version}.tar.bz2
#Source1-md5:	d7415eb6e55a78061964930563f78308
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-makefile.patch
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
BuildRequires:	SDL-devel >= 1.2.2
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
ScummVM jest implementacj� silnika SCUMM (Narz�dzie tworz�ce skrypty dla
Maniac Mansion) u�ywanego w wielu grach Lucas Arts takich jak Monkey Island,
czy Day of the Tentacle. ScummVM jest ca�y czas intensywnie rozwijany i
powinien by� traktowany jako program w stanie ALPHA. Wiele gier mo�e si�
wysypywa�, lub dzia�a� z b��dami. Zapisane stany gry b�d� prawdopodobnie
niekompatybilne pomi�dzy r�nymi wersjami ScummVM.

ScummVM potrafi r�wnie� obs�u�y� gry nie oparte na silniku SCUMM. W chwili
obecnej jest to Simon The Sorcerer.

%package tools
Summary:	SCUMM tools
Summary(pl):	Narz�dzia zwi�zane ze SCUMM
Group:		X11/Applications/Games

%description tools
SCUMM tools.

%description tools -l pl
Narz�dzia zwi�zane ze SCUMM.

%prep
%setup -q -a 1
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

cd %{name}-tools-%{version}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_applnkdir}/Games}

install scummvm $RPM_BUILD_ROOT%{_bindir}
install scummvm.6 $RPM_BUILD_ROOT%{_mandir}/man6

cd %{name}-tools-%{version}
install {descumm{,6},rescumm,simon2mp3} $RPM_BUILD_ROOT%{_bindir}
install extract $RPM_BUILD_ROOT%{_bindir}/extract-scummvm
cd -

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/scummvm
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_applnkdir}/*

%files tools
%defattr(644,root,root,755)
%doc %{name}-tools-%{version}/README
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/scummvm
