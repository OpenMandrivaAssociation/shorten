Name:		shorten
Version:	3.6.1
Release:	4
License:	Distributable
Summary:	A fast, low complexity waveform coder
Group:		Sound
URL:		http://www.etree.org/shnutils/shorten/
Source:		http://www.etree.org/shnutils/shorten/dist/src/shorten-%{version}.tar.gz

%description
Shorten is a low complexity and fast waveform coder (i.e. audio
compressor), originally written by Tony Robinson at SoftSound. It can
operate in both lossy and lossless modes.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING NEWS README doc/LICENSE doc/TODO doc/tr156.ps
%{_mandir}/*/%{name}*
%{_bindir}/%{name}

