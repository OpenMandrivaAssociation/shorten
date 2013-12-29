Name: shorten
Version: 3.6.1
Release: 3
License: Distributable
Summary: A fast, low complexity waveform coder
Group: Sound
URL: http://www.etree.org/shnutils/shorten/
Source: http://www.etree.org/shnutils/shorten/source/shorten-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog COPYING NEWS README doc/LICENSE doc/TODO doc/tr156.ps
%{_mandir}/*/%{name}*
%{_bindir}/%{name}

