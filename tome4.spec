Name:           tome4
Version:        1.5.10
Release:        0
Summary:        Roguelike turn-based RPG
License:        GPL-3.0-only AND SUSE-Freeware
Group:          Amusements/Games/RPG
URL:            https://te4.org/
Source:         https://te4.org/dl/t-engine/t-engine4-src-%{version}.tar.bz2
Source1:        tome4.sh
Source2:        tome4.desktop
# PATCH-FIX-OPENSUSE Don't use a bundled version of SDL2
Patch1:         system-SDL2.patch
# PATCH-FIX-OPENSUSE Resolve conflicts between glext.h and glew.h
Patch2:         conflicting_types_glext_and_glew.patch
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  premake4
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(vorbis)

%description
A roguelike RPG in the original sense, featuring tactical turn-based combat and advanced character building.

%prep
%setup -q -n t-engine4-src-%{version}
%patch1 -p1
%patch2 -p1

%build
premake4 gmake
make config=release

%install
unzip -oj -qq game/engines/te4-%{version}.teae data/gfx/te4-icon.png -d .
install -Dm644 te4-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

install -Dm755 t-engine %{buildroot}%{_libexecdir}/tome4/t-engine
install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

cp -r bootstrap %{buildroot}%{_libexecdir}/%{name}
cp -r game %{buildroot}%{_libexecdir}/%{name}

%fdupes %{buildroot}%{_libexecdir}/%{name}

%files
%license COPYING
%doc COPYING-MEDIA CREDITS CONTRIBUTING
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
