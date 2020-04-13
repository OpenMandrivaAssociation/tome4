Name:           tome4
Version:        1.6.7
Release:        1
Summary:        Roguelike turn-based RPG
License:        GPL3
Group:          Games/RPG
URL:            https://te4.org/
Source0:        https://te4.org/dl/t-engine/t-engine4-src-%{version}.tar.bz2
#Source1:        tome4.sh
Patch0:         tome4-1.6.7-use-system-SDL2.patch

BuildRequires:  fdupes
BuildRequires:  premake
BuildRequires:  premake
BuildRequires:  unzip
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)

%description
A roguelike RPG in the original sense, featuring tactical turn-based combat and advanced character building.

%prep
%setup -q -n t-engine4-src-%{version}
%autopatch -p1

%build
premake4 gmake
make config=release

%install
unzip -oj -qq game/engines/te4-%{version}.teae data/gfx/te4-icon.png -d .
install -Dm644 te4-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

install -Dm755 t-engine %{buildroot}%{_libexecdir}/tome4/t-engine
#install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
#install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=ToME4 - Tales of Maj'Eyal: Age of Ascendancy
Comment=An open-source, single-player, role-playing roguelike game set in the world of Eyal.
Exec=/usr/libexec/tome4/t-engine
Icon=tome4
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;RolePlaying;
EOF

cp -r bootstrap %{buildroot}%{_libexecdir}/%{name}
cp -r game %{buildroot}%{_libexecdir}/%{name}

#ln -s %{_libexecdir}/%{name} %{_bindir}/%{name}

%fdupes %{buildroot}%{_libexecdir}/%{name}

%files
%license COPYING
%doc COPYING-MEDIA CREDITS CONTRIBUTING
#{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
