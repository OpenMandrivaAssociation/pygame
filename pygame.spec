Name:		pygame
Version:	1.9.1
Release:	6
Source:		http://www.pygame.org/ftp/%{name}-%{version}release.tar.gz
Patch0:		pygame-1.9.1-config.patch
Summary:	Python module for interfacing with the SDL multimedia library
License:	LGPLv2+
Group:		System/Libraries
URL:		http://pygame.org/
BuildRequires:	python-devel
BuildRequires:	python-numeric
BuildRequires:	python-numeric-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:	jpeg-devel
BuildRequires:	smpeg-devel

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

%__python config.py
perl -pi -e 's|^(SDL = .*)|$1 -lm|;' Setup

%build
%__python setup.py build

# Fix wrong permissions on various data files - AdamW 2008/12)
chmod 0644 WHATSNEW \
	lib/*.ttf \
	lib/pygame_icon* \
	lib/pygame.ico

%install
%__python setup.py install --prefix %{buildroot}%{_prefix}

%files
%{py_platsitedir}/*
%doc WHATSNEW

%files devel
%{_includedir}/python%{py_ver}/%{name}/

%files doc
%doc docs/
%doc examples/

%changelog
* Fri Oct 21 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.9.1-4mdv2012.0
+ Revision: 705558
- Correct build in cooker and rebuild with libpng 1.5.

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 1.9.1-3mdv2011.0
+ Revision: 591968
- Rebuild

* Wed Jan 13 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.1-2mdv2010.1
+ Revision: 490517
- rebuild for new libjpeg

* Sun Dec 06 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 1.9.1-1mdv2010.1
+ Revision: 474028
- add 1 patch from Fedora to pass the config mecanism
  (still experimental)
- new version 1.9.1

* Sun Aug 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.8.1-4mdv2010.0
+ Revision: 416904
- rebuild for new libjpeg

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 1.8.1-3mdv2009.1
+ Revision: 319619
- rebuild with python 2.6

* Sat Dec 13 2008 Adam Williamson <awilliamson@mandriva.org> 1.8.1-2mdv2009.1
+ Revision: 313863
- fix all the permissions in the source dir, doesn't work the other way
- finish renaming the devel package
- fix permissions on some files which broke at least childsplay, probably
  most things that use pygame
- the devel package can just be pygame-devel, it doesn't have to be some
  over-complex library-based name
- new license policy
- un-justify(?!?!?!?!) the descriptions
- various spec cleanups

* Thu Sep 04 2008 JÃ©rÃ´me Soyer <saispo@mandriva.org> 1.8.1-1mdv2009.0
+ Revision: 280665
- Fix BR
- New version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.7.1-5mdv2009.0
+ Revision: 242365
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Apr 17 2007 Crispin Boylan <crisb@mandriva.org> 1.7.1-3mdv2008.0
+ Revision: 13683
- Add 64-bit pep353 patch


* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.7.1-2mdv2007.0
+ Revision: 88133
- Import pygame

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 1.7.1-2mdv2007.1
- update file list

* Sun Aug 28 2005 Michael Scherer <misc@mandriva.org> 1.7.1-1mdk
- New release 1.7.1
- rpmbuildupdateable
- rpmlint fix

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 1.6-4mdk
- Rebuild for new python

* Thu Feb 12 2004 Michael Scherer <misc@mandrake.org> 1.6-3mdk
- own subdir 
- provides python-pygame ( naming policy )

* Tue Dec 30 2003 Franck Villaume <fvill@freesurf.fr> 1.6-2mdk
- fix some 64bits BuildRequires
- add python-numeric BuildRequires as python-numeric-devel has no requirements

