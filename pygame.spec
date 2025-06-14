Summary:	Python module for interfacing with the SDL multimedia library
Name:		python-pygame
Version:	2.6.0
Release:	2
Source0:	https://pypi.io/packages/source/p/pygame/pygame-%{version}.tar.gz
License:	LGPLv2+
Group:		System/Libraries
URL:		https://pygame.org/

BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	pkgconfig(portmidi)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(SDL2_ttf)
BuildRequires:	pkgconfig(x11)
BuildRequires:	smpeg-devel
BuildRequires:	fonts-ttf-freefont

Requires:	fonts-ttf-freefont

%rename	pygame

%description
pygame is a Python wrapper module for the SDL multimedia library,
written by Pete Shinners. It contains python functions and classes that
will allow you to use SDL's support for playing cdroms, audio and video
output, and keyboard, mouse and joystick input. pygame also includes
support for the Numerical Python extension. pygame is the successor to
the pySDL wrapper project, written by Mark Baker.

Install pygame if you would like to write or play SDL games written in
the python language.

%files
%doc README.rst
%{py_platsitedir}/pygame
%{py_platsitedir}/pygame-%{version}-*.*-info

#---------------------------------------------------------------------------

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

%files doc
%doc docs/
%doc examples/

#---------------------------------------------------------------------------

%package devel
Summary:	Pygame development headers
Group:		Development/Python

%description devel
pygame is a Python wrapper module for the SDL multimedia library,
written by Pete Shinners. It contains python functions and classes that
will allow you to use SDL's support for playing cdroms, audio and video
output, and keyboard, mouse and joystick input. pygame also includes
support for the Numerical Python extension. pygame is the successor to
the pySDL wrapper project, written by Mark Baker.

Install the devel package if you want to build programs with pygame.

%files devel
%{_includedir}/python%{py_ver}/pygame/

#---------------------------------------------------------------------------

%prep
export LC_ALL=C.utf-8
%autosetup -p1 -n pygame-%{version}

# Drop pre-compiled Cython sources
rm $(grep -rl '/\* Generated by Cython')

%__python buildconfig/config.py
perl -pi -e 's|^(SDL = .*)|$1 -lm|;' Setup

# remove non-free stuff
rm -f src_c/ffmovie.[ch]

%build
%py_build

%install
%py_install

# use system font
ln -fs /usr/share/fonts/TTF/FreeSansBold.ttf %{buildroot}%{py3_platsitedir}/pygame/freesansbold.ttf

