#
# TODO:
# - add desktop file and png icon.
#
Summary:	SCUMM graphic adventure game interpreter
Summary(pl):	Interpreter przygodówek opartych na SCUMM
Name:		scummvm
Version:	0.2.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://telia.dl.sourceforge.net/sourceforge/scummvm/%{name}_%{version}-src.tgz
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

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6}

install scummvm $RPM_BUILD_ROOT%{_bindir}
install scummvm.6 $RPM_BUILD_ROOT%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt whatsnew.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
