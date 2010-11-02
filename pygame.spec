Name:		pygame
Version:	1.9.1
Release:	%{mkrel 3}
Source:		http://www.pygame.org/ftp/%{name}-%{version}release.tar.gz
Patch0:		pygame-1.9.1-config.patch
Summary:	Python module for interfacing with the SDL multimedia library
License:	LGPLv2+
Group:		System/Libraries
URL:		http://pygame.org/
Requires:	SDL >= 1.2.4
BuildRequires:	python-numeric-devel >= 22.0-4mdk
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	python-numeric >= 22.0-4mdk
BuildRequires:	SDL_ttf-devel
BuildRequires:	smpeg-devel >= 0.4
BuildRequires:	python-devel >= %{py_ver}
BuildRequires:  png-devel
BuildRequires:	jpeg-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot
Provides:	python-pygame

%description
pygame is a Python wrapper module for the SDL multimedia library,
written by Pete Shinners. It contains python functions and classes that
will allow you to use SDL's support for playing cdroms, audio and video
output, and keyboard, mouse and joystick input. pygame also includes
support for the Numerical Python extension. pygame is the successor to
the pySDL wrapper project, written by Mark Baker.

Install pygame if you would like to write or play SDL games written in
the python language.

%package doc
Summary:	Pygame documentation and example programs
Group:		Development/Python

%description doc
pygame is a Python wrapper module for the SDL multimedia library,
written by Pete Shinners. It contains python functions and classes that
will allow you to use SDL's support for playing cdroms, audio and video
output, and keyboard, mouse and joystick input. pygame also includes
support for the Numerical Python extension. pygame is the successor to
the pySDL wrapper project, written by Mark Baker.

Install pygame-doc if you need the API documentation and example
programs.

%package devel
Summary:	Pygame development headers
Group:		Development/Python
Obsoletes:	%{mklibname pygame 1.8 -d}

%description devel
pygame is a Python wrapper module for the SDL multimedia library,
written by Pete Shinners. It contains python functions and classes that
will allow you to use SDL's support for playing cdroms, audio and video
output, and keyboard, mouse and joystick input. pygame also includes
support for the Numerical Python extension. pygame is the successor to
the pySDL wrapper project, written by Mark Baker.

Install the devel package if you want to build programs with pygame.


%prep
%setup -q -n %{name}-%{version}release
%patch0 -p1

%build
%__python config.py
%__python setup.py build

# Fix wrong permissions on various data files - AdamW 2008/12)
chmod 0644 WHATSNEW \
	lib/*.ttf \
	lib/pygame_icon* \
	lib/pygame.ico

%install
%__rm -rf %buildroot
%__python setup.py install --prefix %{buildroot}%{_prefix}

%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root)
%{py_platsitedir}/*
%doc WHATSNEW

%files devel
%defattr(-,root,root)
%{_includedir}/python%{pyver}/%{name}/

%files doc
%defattr(-,root,root)
%doc docs/
%doc examples/

