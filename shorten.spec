Name:		shorten
Version:	3.6.1
Release:	5
License:	Distributable
Summary:	A fast, low complexity waveform coder
Group:		Sound
URL:		https://www.etree.org/shnutils/shorten/
Source:		http://www.etree.org/shnutils/shorten/dist/src/shorten-%{version}.tar.gz

%description
Shorten is a low complexity and fast waveform coder (i.e. audio
compressor), originally written by Tony Robinson at SoftSound. It can
operate in both lossy and lossless modes.

%prep
%setup -q

%build
%configure2_5x
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog COPYING NEWS README doc/LICENSE doc/TODO doc/tr156.ps
%{_mandir}/*/%{name}*
%{_bindir}/%{name}

