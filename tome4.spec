Name:           tome4
Version:        1.6.7
Release:        1
Summary:        Roguelike turn-based RPG
License:        GPL3
Group:          Games/RPG
URL:            https://te4.org/
Source:         https://te4.org/dl/t-engine/t-engine4-src-%{version}.tar.bz2

BuildRequires:  fdupes
#BuildRequires:  pkgconfig
#BuildRequires:  premake4
BuildRequires:  premake
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

%build
#premake4 gmake
premake gmake
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
