%define name            pygame
%define version 1.8.1
%define release %mkrel 1
%define lib_name_orig   lib%{name}
%define lib_major       1.8
%define lib_name        %mklibname %{name} %{lib_major}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		http://www.pygame.org/ftp/%{name}-%{version}release.tar.bz2
Summary:	Python module for interfacing with the SDL multimedia library
License:	LGPL style
Group:		System/Libraries
URL:		http://pygame.org/
Requires:	SDL >= 1.2.4
BuildRequires:	python-numeric-devel >= 22.0-4mdk SDL_mixer-devel
BuildRequires:	SDL_image-devel python-numeric >= 22.0-4mdk
BuildRequires:	SDL_ttf-devel smpeg-devel >= 0.4 python-devel >= %{py_ver}
BuildRequires:  png-devel jpeg-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot
Provides:   python-pygame

%description
pygame is a Python  wrapper  module  for  the  SDL  multimedia  library,
written by Pete Shinners. It contains python functions and classes  that
will allow you to use SDL's support for playing cdroms, audio and  video
output, and keyboard, mouse and joystick  input.  pygame  also  includes
support for the Numerical Python extension. pygame is the  successor  to
the pySDL wrapper project, written by Mark Baker.

Install pygame if you would like to write or play SDL games  written  in
the python language.

%package doc
Summary: Pygame documentation and example programs
Group: Development/Python
%description doc
pygame is a Python  wrapper  module  for  the  SDL  multimedia  library,
written by Pete Shinners. It contains python functions and classes  that
will allow you to use SDL's support for playing cdroms, audio and  video
output, and keyboard, mouse and joystick  input.  pygame  also  includes
support for Numerical Python extension. pygame is the successor  to  the
pySDL wrapper project, written by Mark Baker.

Install pygame-doc  if  you  need  the  API  documentation  and  example
programs.

%package -n %{lib_name}-devel
Summary: Pygame development headers
Group: Development/Python
%description -n %{lib_name}-devel
pygame is a Python  wrapper  module  for  the  SDL  multimedia  library,
written by Pete Shinners. It contains python functions and classes  that
will allow you to use SDL's support for playing cdroms, audio and  video
output, and keyboard, mouse and joystick  input.  pygame  also  includes
support for Numerical Python extension. pygame is the successor  to  the
pySDL wrapper project, written by Mark Baker.

Install the devel package if you  want  to  build  programs  build  with
pygame.


%prep
%setup -q -n %{name}-%{version}release

%build
%__python config.py
%__python setup.py build


%install
%__rm -rf %buildroot
%__python setup.py install --prefix %buildroot%{_prefix}


%clean
%__rm -rf %buildroot


%files
%defattr(-,root,root)
%py_platsitedir/*
%doc WHATSNEW

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_includedir}/python%{pyver}/%{name}/

%files doc
%defattr(-,root,root)
%doc docs/
%doc examples/


