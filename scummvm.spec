#
# TODO:
# - add desktop file and png icon. (when gui is ready)
#
%define		_snap	20020919
Summary:	SCUMM graphic adventure game interpreter
Summary(pl):	Interpreter przygodówek opartych na SCUMM
Name:		scummvm
Version:	0.2.0.%{_snap}
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	%{name}-%{_snap}.tar.bz2
#Source0:	http://telia.dl.sourceforge.net/sourceforge/scummvm/%{name}_%{version}-src.tgz
Source1:	%{name}-tools-%{_snap}.tar.bz2
BuildRequires:	mad-devel
BuildRequires:	SDL-devel >= 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
%setup -q -a 1 -n %{name}

%build
%{__make} \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

cd tools
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6}

install scummvm $RPM_BUILD_ROOT%{_bindir}
install scummvm.6 $RPM_BUILD_ROOT%{_mandir}/man6

install tools/{descumm{3,5,6},rescumm} $RPM_BUILD_ROOT%{_bindir}
install tools/extract $RPM_BUILD_ROOT%{_bindir}/extract-scummvm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README debian/README.Debian
%attr(755,root,root) %{_bindir}/scummvm
%{_mandir}/man6/*

%files tools
%defattr(644,root,root,755)
%doc tools/readme.txt
%attr(755,root,root) %{_bindir}/descumm*
%attr(755,root,root) %{_bindir}/extract-scummvm
%attr(755,root,root) %{_bindir}/rescumm
