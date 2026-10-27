Name: quest-backup
Version: 1.0
Release: 1
Summary: Offline training package for Linux Quest
License: MIT
BuildArch: noarch

%description
A tiny training-only program. No network or external dependencies.

%install
mkdir -p %{buildroot}/usr/bin
printf '#!/bin/sh\necho "quest-backup ready"\n' > %{buildroot}/usr/bin/quest-backup
chmod 755 %{buildroot}/usr/bin/quest-backup

%files
/usr/bin/quest-backup
