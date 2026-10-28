"""Additional original practice questions (same row format as questions.py).

Authored from the public exam scope, not copied from official exam papers.
"""

EXTRA_ROWS = """
overview¦다음 중 리눅스의 특징으로 옳지 않은 것은?¦특정 제조사의 하드웨어에서만 동작하도록 제한되어 있다¦멀티태스킹과 다중 사용자 환경을 모두 지원한다¦소스 코드가 공개되어 있어 사용자가 직접 수정할 수 있다¦x86, ARM 등 여러 하드웨어 아키텍처에서 동작한다¦리눅스는 특정 제조사에 종속되지 않고 다양한 아키텍처로 이식되어 있다.
overview¦사용자가 입력한 명령을 해석하여 커널에 전달하는 프로그램은?¦셸¦부트 로더(GRUB2)¦데몬(sshd 등)¦initramfs 이미지¦셸은 사용자와 커널 사이에서 명령을 해석하는 인터페이스이며 부트 로더는 커널을 적재하는 프로그램이다.
overview¦리눅스에서 하드디스크 같은 장치를 파일 형태로 나타내는 장치 파일이 모여 있는 디렉터리는?¦/dev¦/proc¦/sys¦/media¦장치 파일은 /dev 아래에 있으며 /proc은 프로세스·커널 정보를 보여 주는 가상 파일시스템이다.
overview¦실행 중인 프로세스와 커널 상태 정보를 가상 파일로 보여 주는 디렉터리는?¦/proc¦/dev¦/var¦/boot¦/proc은 메모리에만 존재하는 가상 파일시스템으로 프로세스 및 커널 정보를 제공한다.
overview¦시스템 부팅과 함께 백그라운드에서 계속 실행되며 요청을 기다리는 서비스 프로세스를 가리키는 용어는?¦데몬¦셸¦스풀러¦래퍼¦데몬(daemon)은 sshd, crond처럼 백그라운드에서 서비스를 제공하는 프로세스를 말한다.
overview¦리눅스 커널 구조에 대한 설명으로 옳은 것은?¦모놀리식 구조이면서 모듈을 동적으로 적재할 수 있다¦순수 마이크로커널이라 모든 드라이버가 사용자 공간에서만 동작한다¦커널 모듈이 없어 드라이버를 추가하려면 반드시 커널을 재컴파일해야 한다¦부팅이 끝난 뒤에는 어떤 기능도 동적으로 추가하거나 제거할 수 없다¦리눅스 커널은 모놀리식 구조이지만 insmod·modprobe 등으로 모듈을 적재할 수 있다.
overview¦현재 실행 중인 커널의 릴리스 버전만 출력하는 명령은?¦uname -r¦uname -n¦uname -m¦uname -v¦uname -r은 커널 릴리스, -n은 호스트 이름, -m은 하드웨어 아키텍처, -v는 커널 빌드 정보를 출력한다.
overview¦배포판 이름과 버전을 표준화된 키=값 형식으로 담고 있는 파일은?¦/etc/os-release¦/etc/hostname¦/etc/motd¦/etc/shells¦/etc/os-release는 배포판 식별 정보를 담고 있으며 /etc/shells는 사용 가능한 셸 목록이다.
overview¦다음 중 셸에 대한 설명으로 옳지 않은 것은?¦셸은 커널의 일부로 커널 모드에서 동작한다¦bash는 대표적인 셸 중 하나로 사용자 공간에서 실행된다¦로그인 시 실행되는 셸은 /etc/passwd의 사용자 항목에 지정된다¦사용 가능한 셸의 목록은 /etc/shells 파일에 기록되어 있다¦셸은 사용자 공간에서 실행되는 일반 프로그램이며 커널의 일부가 아니다.
overview¦시스템의 CPU 모델과 코어 정보를 확인할 수 있는 파일은?¦/proc/cpuinfo¦/proc/meminfo¦/proc/version¦/proc/uptime¦/proc/cpuinfo는 CPU 정보를, /proc/meminfo는 메모리 정보를 제공한다.
overview¦리눅스에서 시스템 전체 관리 권한을 가진 슈퍼유저(root)의 UID는?¦0¦1¦100¦1000¦root의 UID는 0이며 1000 이상은 일반적으로 일반 사용자에게 할당된다.
overview¦FHS(Filesystem Hierarchy Standard)가 정의하는 것은?¦디렉터리 구조와 각 디렉터리의 용도¦패키지 저장소의 디렉터리 구조와 메타데이터 형식¦사용자 계정과 비밀번호의 관리 정책¦디스크 파티션별 권장 크기와 파일시스템 종류¦FHS는 /etc, /var, /usr 등 표준 디렉터리의 배치와 용도를 정의한 규격이다.
history¦리누스 토르발스가 리눅스 개발 초기에 참고한 교육용 유닉스 계열 운영체제는?¦MINIX¦Solaris¦BSD¦Xenix¦토르발스는 앤드류 타넨바움의 교육용 OS인 MINIX 환경에서 리눅스 커널을 시작했다.
history¦최초의 UNIX를 개발한 연구소는?¦AT&T 벨 연구소¦IBM 왓슨 연구소¦UC 버클리 컴퓨터 시스템 연구그룹¦MIT 인공지능 연구소¦UNIX는 1969년 AT&T 벨 연구소의 켄 톰프슨과 데니스 리치 등이 개발했다.
history¦UNIX를 이식하기 쉽도록 다시 작성하는 데 사용된 언어는?¦C¦어셈블리어¦Pascal¦Fortran¦UNIX는 C 언어로 재작성되면서 다른 하드웨어로의 이식성이 크게 높아졌다.
history¦GNU 프로젝트를 시작하고 자유 소프트웨어 재단을 설립한 사람은?¦리처드 스톨먼¦에릭 레이먼드¦켄 톰프슨¦앤드류 타넨바움¦GNU 프로젝트는 리처드 스톨먼이 시작했으며 에릭 레이먼드는 오픈소스 운동과 관련된 인물이다.
history¦GNU 프로젝트가 시작된 연도는?¦1983년¦1969년¦1991년¦1998년¦GNU는 1983년에 시작되었고 1991년은 리눅스 커널이 공개된 해이다.
history¦BSD 유닉스를 개발·배포한 대학은?¦캘리포니아 대학교 버클리¦스탠퍼드 대학교¦매사추세츠 공과대학¦카네기멜런 대학교¦BSD는 Berkeley Software Distribution의 약자로 UC 버클리에서 만들어졌다.
history¦리눅스 커널 1.0이 공개된 연도는?¦1994년¦1991년¦1996년¦2001년¦리눅스 커널 1.0은 1994년에 공개되었고 1991년은 최초 발표 연도이다.
history¦'오픈소스'라는 용어와 정의를 1998년경 도입해 확산시킨 단체는?¦오픈소스 이니셔티브(OSI)¦자유 소프트웨어 재단(FSF)¦리눅스 재단(Linux Foundation)¦아파치 소프트웨어 재단(ASF)¦OSI는 1998년에 설립되어 오픈소스 정의를 관리하며 FSF는 1985년 설립되었다.
history¦UNIX와 리눅스에 대한 설명으로 옳지 않은 것은?¦리눅스는 AT&T UNIX의 소스 코드를 그대로 가져와 개발되었다¦POSIX는 UNIX 계열 운영체제가 따르는 표준 인터페이스 규격이다¦BSD도 UNIX에서 갈라져 나온 UNIX 계열 운영체제에 속한다¦리눅스는 UNIX와 유사하게 동작하도록 독자적으로 작성된 커널이다¦리눅스 커널은 UNIX 코드를 사용하지 않고 처음부터 새로 작성되었다.
history¦교육용 운영체제 MINIX를 만든 사람은?¦앤드류 타넨바움¦데니스 리치¦브라이언 커니핸¦빌 조이¦MINIX는 네덜란드의 앤드류 타넨바움이 교육 목적으로 만들었다.
history¦C 언어를 개발한 사람으로 알려진 인물은?¦데니스 리치¦켄 톰프슨¦리처드 스톨먼¦리누스 토르발스¦C 언어는 데니스 리치가 개발했으며 켄 톰프슨은 B 언어와 UNIX 개발에 참여했다.
history¦현재 리눅스 커널 개발에 사용되는 버전 관리 도구는?¦Git¦CVS¦Subversion¦BitKeeper¦Git은 토르발스가 2005년에 커널 개발용으로 만든 분산 버전 관리 시스템이며 BitKeeper는 그 이전에 쓰였다.
license¦GPL의 핵심 개념으로, 파생물을 배포할 때 같은 조건으로 소스를 공개하도록 하는 것은?¦카피레프트¦카피라이트¦셰어웨어¦퍼블릭 도메인¦카피레프트는 저작권을 이용해 자유로운 이용 조건이 파생물에도 유지되도록 하는 개념이다.
license¦BSD 라이선스에 대한 설명으로 옳은 것은?¦저작권 고지 조건을 지키면 독점 소프트웨어에도 포함할 수 있다¦수정한 파생물을 배포할 때 소스 코드를 반드시 공개해야 한다¦오픈소스 소프트웨어이므로 상업적 목적의 이용은 허용되지 않는다¦원저작자의 허락 없이는 수정본을 재배포할 수 없다¦BSD는 허용적 라이선스로 저작권 고지 등의 조건만 지키면 소스 공개 의무가 없다.
license¦라이브러리를 링크하는 프로그램에 GPL보다 완화된 조건을 적용하는 라이선스는?¦LGPL¦AGPL¦GPLv3¦MPL¦LGPL은 라이브러리용으로 링크하는 프로그램의 소스 공개 의무를 완화하며 AGPL은 오히려 더 엄격하다.
license¦명시적인 특허 사용권 조항을 포함하는 허용적 라이선스는?¦Apache License 2.0¦MIT License¦BSD 2-Clause License¦ISC License¦Apache License 2.0은 허용적 라이선스이면서 특허 사용권을 명시한다.
license¦GPL에 대한 설명으로 옳지 않은 것은?¦수정본의 재배포가 허용되지 않는다¦소스 코드를 받을 권리를 이용자에게 보장한다¦수정본을 배포할 때 동일한 라이선스를 적용해야 한다¦조건을 지키면 소프트웨어를 유료로 판매할 수 있다¦GPL은 수정과 재배포를 허용하되 같은 조건의 공개를 요구한다.
license¦일정 기간이나 기능 제한 상태로 체험하게 한 뒤 구입을 유도하는 배포 방식은?¦셰어웨어¦프리웨어¦오픈소스¦퍼블릭 도메인¦셰어웨어는 체험 후 결제를 유도하는 방식이며 프리웨어는 무료지만 소스 공개와는 무관하다.
license¦저작권이 소멸되었거나 포기되어 누구나 제약 없이 이용할 수 있는 소프트웨어는?¦퍼블릭 도메인 소프트웨어¦프리웨어(무료 배포 소프트웨어)¦셰어웨어(체험 후 구매 소프트웨어)¦상용 소프트웨어¦퍼블릭 도메인은 저작권 제약이 없는 상태이며 프리웨어는 저작권이 유지된 무료 배포물이다.
license¦GPL 소프트웨어의 바이너리를 배포하는 자가 이행해야 하는 의무로 옳은 것은?¦수령자에게 소스 코드를 제공하거나 입수 방법을 안내한다¦배포 수량에 따라 원저작자에게 정해진 사용료를 지급한다¦소스 코드 대신 컴파일된 실행 파일만 제공해도 충분하다¦배포 사실을 자유 소프트웨어 재단에 사전 등록한다¦GPL은 바이너리 배포 시 대응하는 소스 코드 제공을 요구하지만 사용료나 등록 의무는 없다.
license¦GPLv2와 비교하여 GPLv3에서 새로 보강된 내용은?¦특허 조항과 티보화(tivoization) 제한¦소스 코드 공개 의무의 완전한 폐지와 허용적 라이선스로의 전환¦상업적 판매와 유료 배포의 전면 금지¦배포 시 LGPL로 자동 전환되는 라이브러리 예외¦GPLv3는 특허 보복 조항과 하드웨어 서명으로 수정을 막는 티보화 제한 등을 추가했다.
license¦설치된 RPM 패키지의 License 항목이 포함된 상세 정보를 보는 명령은?¦rpm -qi bash¦rpm -ql bash¦rpm -qc bash¦rpm -qf bash¦rpm -qi는 패키지 정보를 보여 주며 -ql은 파일 목록, -qc는 설정 파일, -qf는 파일 소유 패키지를 조회한다.
license¦MIT 라이선스의 성격으로 알맞은 것은?¦고지 조건만 지키면 폭넓게 쓸 수 있는 허용적 라이선스¦파생물에도 동일 조건을 요구하는 강한 카피레프트 라이선스¦네트워크 서비스 제공에도 소스 공개를 요구하는 라이선스¦사용 목적과 인원을 제한하는 상용 EULA 형태의 라이선스¦MIT는 고지 조건만 지키면 폭넓게 사용할 수 있는 허용적 라이선스이다.
license¦AGPL이 GPL과 구별되는 점은?¦네트워크 서비스 제공 시에도 소스 제공 의무가 생긴다¦바이너리를 배포할 때만 소스를 공개하면 된다¦라이브러리 링크에 대한 예외 조항을 별도로 둔다¦상업적 이용과 유료 서비스 제공을 금지한다¦AGPL은 네트워크로 서비스를 제공하는 사용자에게도 소스를 제공하도록 확장한 라이선스이다.
distros¦Ubuntu에서 저장소를 이용해 패키지를 설치할 때 주로 쓰는 명령은?¦apt install¦dnf install¦rpm -i¦yum localinstall¦Ubuntu는 Debian 계열이므로 apt를 사용하며 dnf와 rpm은 RPM 계열 도구이다.
distros¦Rocky Linux 8의 기본 고수준 패키지 관리 명령은?¦dnf¦apt¦zypper¦dpkg¦Rocky 8은 dnf(yum은 dnf로 연결)를 사용하며 apt는 Debian 계열, zypper는 SUSE 계열이다.
distros¦RHEL과 호환을 목표로 하는 재빌드 배포판만 묶은 것은?¦Rocky Linux, AlmaLinux¦Ubuntu, Linux Mint¦Fedora, Arch Linux¦openSUSE, Slackware¦Rocky Linux와 AlmaLinux는 RHEL 호환 배포판이며 Fedora는 RHEL의 업스트림 성격이다.
distros¦Ubuntu가 기반으로 삼는 배포판은?¦Debian¦Red Hat Enterprise Linux¦Slackware¦Gentoo¦Ubuntu는 Debian을 기반으로 하는 Debian 계열 배포판이다.
distros¦openSUSE와 SUSE Linux Enterprise에서 사용하는 패키지 관리 명령은?¦zypper¦dnf¦apt¦pacman¦SUSE 계열은 RPM을 쓰지만 고수준 도구로 zypper를 사용한다.
distros¦RPM 패키지 파일을 저장소 없이 파일 단위로 직접 다루는 저수준 도구는?¦rpm¦dnf¦dpkg¦apt-get¦rpm은 .rpm 파일을 직접 다루는 도구이고 dpkg는 .deb 파일용이다.
distros¦Arch Linux에서 사용하는 패키지 관리 명령은?¦pacman¦emerge¦zypper¦apk¦Arch는 pacman, Gentoo는 emerge, Alpine은 apk를 사용한다.
distros¦CentOS Stream과 RHEL의 관계로 알맞은 것은?¦RHEL 다음 마이너 릴리스를 위한 개발 상위 스트림이다¦RHEL을 그대로 재빌드한 하위 호환 후속 배포판이다¦RHEL의 오래된 버전을 장기간 유지하는 지원 브랜치이다¦Debian을 기반으로 RHEL과 호환되도록 만든 파생판이다¦CentOS Stream은 RHEL 바로 앞 단계에서 개발이 진행되는 스트림이다.
distros¦배포판에 대한 설명으로 옳지 않은 것은?¦Rocky Linux 8은 Debian 계열이므로 apt로 패키지를 관리한다¦Ubuntu는 Debian을 기반으로 만들어진 배포판이다¦RHEL 계열은 .rpm 패키지 형식을 사용한다¦배포판마다 기본 패키지 관리자가 다를 수 있다¦Rocky Linux 8은 RPM 계열이며 dnf로 패키지를 관리한다.
distros¦Ubuntu의 LTS 릴리스가 의미하는 것은?¦장기간 보안 업데이트를 제공하는 릴리스¦최신 기능만 먼저 공개하는 단기 지원 릴리스¦실험적 커널과 불안정한 패키지를 포함한 릴리스¦상용 고객과 기업에게만 배포되는 유료 릴리스¦LTS는 Long Term Support의 약자로 장기간 지원되는 안정 릴리스이다.
distros¦RPM 계열 패키지 파일의 확장자는?¦.rpm¦.deb¦.tgz¦.pkg¦.rpm은 RPM 계열, .deb는 Debian 계열 패키지 확장자이다.
installation¦Rocky Linux 8의 설치 프로그램 이름은?¦Anaconda¦Subiquity¦Calamares¦Debian-Installer¦Anaconda는 RHEL 계열의 설치 프로그램이며 Subiquity는 Ubuntu Server, Calamares는 일부 배포판의 설치 프로그램이다.
installation¦RHEL 계열에서 설치 과정을 자동화하는 응답 파일 방식은?¦Kickstart¦Preseed¦AutoYaST¦Ignition¦Kickstart는 RHEL 계열, Preseed는 Debian 계열, AutoYaST는 SUSE 계열의 자동 설치 방식이다.
installation¦Rocky 8 설치 시 부트 옵션으로 설치 소스 저장소 위치를 지정하는 것은?¦inst.repo=¦inst.ks=¦inst.vnc¦inst.updates=¦inst.repo는 설치 소스를, inst.ks는 Kickstart 파일 위치를 지정한다.
installation¦Rocky 8 설치 완료 후 해당 설치 설정이 Kickstart 형식으로 저장되는 파일은?¦/root/anaconda-ks.cfg¦/etc/anaconda-ks.cfg¦/var/log/anaconda/ks.cfg¦/boot/anaconda/ks.cfg¦Anaconda는 설치 후 /root/anaconda-ks.cfg에 사용한 설정을 남긴다.
installation¦Rocky 8 설치 과정의 로그가 저장되는 디렉터리는?¦/var/log/anaconda/¦/var/log/installer/¦/var/log/setup/¦/root/install/¦Anaconda 로그는 /var/log/anaconda/에 저장되며 /var/log/installer/는 Debian 계열 설치 로그 위치이다.
installation¦GUI 없는 원격 서버에 설치할 때 설치 화면을 VNC로 보기 위해 사용하는 부트 옵션은?¦inst.vnc¦inst.repo¦inst.ks¦inst.updates¦inst.vnc를 지정하면 Anaconda 그래픽 화면에 VNC로 접속할 수 있다.
installation¦내려받은 설치 ISO의 손상 여부를 해시로 검증할 때 쓰는 명령은?¦sha256sum¦badblocks¦fsck¦mkisofs¦sha256sum으로 계산한 값과 배포처가 제공하는 체크섬을 비교해 무결성을 확인한다.
installation¦USB 메모리에 ISO 이미지를 블록 단위로 기록하는 데 쓰는 명령은?¦dd¦tar¦rsync¦mkfs¦dd는 이미지를 장치에 그대로 기록하며 mkfs는 파일시스템을 만드는 명령이다.
installation¦Anaconda의 설치 요약 화면 항목으로 옳지 않은 것은?¦커널 컴파일 옵션 선택¦설치 대상(디스크) 선택¦시간과 날짜 설정¦소프트웨어 선택 설정¦설치 요약에는 설치 대상, 시간과 날짜, 소프트웨어 선택 등이 있으며 커널 컴파일 옵션은 없다.
installation¦Windows가 설치된 PC에 리눅스를 추가로 설치하려 할 때 먼저 해야 할 일은?¦데이터 백업과 파티션 축소 등으로 공간 확보¦Windows 파티션을 포맷해 하나의 파티션으로 합침¦BIOS 설정을 모두 삭제하고 Windows 부트 영역을 지움¦swap 파티션을 먼저 삭제한 뒤 설치를 진행¦듀얼 부팅은 기존 데이터를 백업하고 빈 공간을 확보한 뒤 설치해야 한다.
installation¦Rocky Linux 8의 Boot ISO를 이용한 설치의 특징은?¦설치 패키지를 네트워크 저장소에서 받는다¦모든 설치 패키지를 이미지 안에 포함한다¦GUI 관련 패키지만 이미지에 포함하고 나머지는 생략한다¦부팅용 이미지이므로 커널이 포함되지 않는다¦Boot ISO는 작은 이미지로 부팅한 뒤 패키지를 네트워크로 받아 설치한다.
installation¦Rocky 8 자동 파티셔닝 시 기본으로 사용되는 파일시스템은?¦XFS¦ext4¦btrfs¦ReiserFS¦RHEL 8 계열의 기본 파일시스템은 XFS이다.
partition¦MBR 방식에서 만들 수 있는 주(primary) 파티션의 최대 개수는?¦4개¦2개¦8개¦128개¦MBR은 파티션 테이블에 4개 항목만 있어 주 파티션은 최대 4개이며 128개는 GPT의 일반적 기본 항목 수이다.
partition¦MBR에서 주 파티션 4개 제한을 넘어 파티션을 더 쓰기 위한 방법은?¦확장 파티션 안에 논리 파티션을 만든다¦확장 파티션을 여러 개 만들어 각각 논리 파티션을 둔다¦swap 파티션을 추가해 파티션 개수 제한을 늘린다¦/boot 파티션을 루트 파티션에 병합해 항목을 비운다¦주 파티션 중 하나를 확장 파티션으로 만들고 그 안에 논리 파티션을 만든다.
partition¦MBR 파티션 테이블이 일반적으로 다룰 수 있는 최대 디스크 용량은?¦2TiB¦512GiB¦4TiB¦16TiB¦MBR은 32비트 섹터 주소를 사용하므로 512바이트 섹터 기준 약 2TiB까지 다룬다.
partition¦디스크의 파티션 테이블 정보를 목록으로 출력하는 명령은?¦fdisk -l¦df -h¦du -sh¦mount -l¦fdisk -l은 파티션 목록을, df는 마운트된 파일시스템의 사용량을 보여 준다.
partition¦블록 장치와 파티션의 계층을 트리 형태로 보여 주는 명령은?¦lsblk¦lspci¦lsusb¦lsmod¦lsblk는 디스크와 파티션을 트리로 보여 주며 lspci·lsusb는 버스 장치, lsmod는 커널 모듈을 보여 준다.
partition¦/dev/sdb1에 XFS 파일시스템을 만드는 명령은?¦mkfs.xfs /dev/sdb1¦mkswap /dev/sdb1¦xfs_repair /dev/sdb1¦tune2fs /dev/sdb1¦mkfs.xfs는 XFS를 생성하며 xfs_repair는 점검·복구용, tune2fs는 ext 계열 조정용이다.
partition¦파티션을 스왑 영역으로 사용하기 위한 올바른 순서는?¦mkswap /dev/sdb2 후 swapon /dev/sdb2¦swapon /dev/sdb2 후 mkswap /dev/sdb2¦mkfs.xfs /dev/sdb2 후 mount /dev/sdb2 /swap¦fsck /dev/sdb2 후 swapon /dev/sdb2¦스왑은 mkswap으로 초기화한 뒤 swapon으로 활성화한다.
partition¦현재 활성화된 스왑 장치의 목록을 출력하는 명령은?¦swapon --show¦swapoff -a¦mkswap -c¦fdisk -s¦swapon --show는 활성 스왑 장치를 표시하며 swapoff -a는 스왑을 모두 비활성화한다.
partition¦부팅 시 자동으로 마운트할 파일시스템을 정의하는 설정 파일은?¦/etc/fstab¦/etc/mtab¦/etc/exports¦/etc/inittab¦/etc/fstab은 부팅 시 마운트 정보를 담고 /etc/exports는 NFS 공유 설정 파일이다.
partition¦/etc/fstab 한 줄의 필드 순서로 옳은 것은?¦장치, 마운트 지점, 파일시스템 유형, 옵션, dump, fsck 순서¦장치, 파일시스템 유형, 마운트 지점, 옵션, fsck 순서, dump¦마운트 지점, 장치, 옵션, 파일시스템 유형, dump, fsck 순서¦장치, 마운트 지점, 옵션, 파일시스템 유형, fsck 순서, dump¦fstab은 장치, 마운트 지점, 유형, 옵션, dump 여부, fsck 순서의 6개 필드로 구성된다.
partition¦/etc/fstab의 마지막 필드(fsck 순서)에서 루트 파일시스템에 관례적으로 쓰는 값은?¦1¦0¦2¦3¦루트 파일시스템은 가장 먼저 점검하도록 1을 쓰고 다른 파일시스템은 2, 점검 제외는 0을 쓴다.
partition¦블록 장치의 UUID와 파일시스템 유형을 확인하는 명령은?¦blkid¦uuidgen¦lsusb¦lsattr¦blkid는 장치의 UUID와 유형을 출력하지만 uuidgen은 새 UUID를 생성할 뿐이다.
partition¦GPT에 대한 설명으로 옳지 않은 것은?¦파티션 테이블 복사본이 없어 손상되면 복구할 수 없다¦UEFI 부팅에서 주로 사용되는 파티션 방식이다¦2TiB를 넘는 대용량 디스크도 지원한다¦각 파티션이 고유한 GUID를 가진다¦GPT는 디스크 끝에 백업 헤더를 두어 손상 시 복구할 수 있다.
partition¦UEFI 시스템에서 EFI 시스템 파티션(ESP)을 일반적으로 마운트하는 위치는?¦/boot/efi¦/efi/boot¦/boot/grub2¦/mnt/efi¦RHEL 계열에서 ESP는 보통 /boot/efi에 마운트된다.
boot¦BIOS와 MBR 방식 부팅에서 BIOS가 가장 먼저 읽는 디스크 영역은?¦MBR¦ESP¦슈퍼블록¦루트 디렉터리¦BIOS는 디스크 첫 섹터의 MBR에 있는 부트 코드를 읽어 실행한다.
boot¦UEFI 부팅에서 부트로더 .efi 파일이 위치하는 파티션은?¦EFI 시스템 파티션¦/home 파티션¦swap 파티션¦루트(/) 파티션¦UEFI 펌웨어는 FAT 형식의 EFI 시스템 파티션에서 .efi 파일을 읽는다.
boot¦Rocky 8의 일반적인 부팅 순서로 옳은 것은?¦펌웨어, GRUB2, 커널과 initramfs, systemd¦펌웨어, 커널, GRUB2, systemd¦GRUB2, 펌웨어, systemd, 커널과 initramfs¦펌웨어, systemd, GRUB2, 커널과 initramfs¦펌웨어가 부트로더를 실행하고 GRUB2가 커널과 initramfs를 적재한 뒤 systemd가 시작된다.
boot¦Rocky 8 BIOS 시스템에서 GRUB 설정 파일을 다시 생성하는 명령은?¦grub2-mkconfig -o /boot/grub2/grub.cfg¦update-grub¦grub2-install /dev/sda¦grub-mkconfig -o /boot/grub/grub.cfg¦RHEL 계열은 grub2-mkconfig로 /boot/grub2/grub.cfg를 만들며 grub2-install은 부트 코드를 설치한다.
boot¦Debian 계열에서 GRUB 설정 파일을 갱신하는 명령은?¦update-grub¦grub2-mkconfig -o /boot/grub2/grub.cfg¦dracut -f¦grubby --update-kernel=ALL¦Debian 계열은 update-grub이 grub-mkconfig를 호출해 grub.cfg를 갱신한다.
boot¦Rocky 8에서 GRUB2의 타임아웃·커널 인자 등을 직접 편집하는 기본 설정 파일은?¦/etc/default/grub¦/boot/grub2/grub.cfg¦/boot/grub2/grubenv¦/etc/grub.conf¦/etc/default/grub을 수정한 뒤 grub2-mkconfig로 반영하며 grub.cfg는 생성되는 파일이다.
boot¦Rocky 8에서 현재 커널용 initramfs를 다시 생성하는 명령은?¦dracut -f¦mkinitramfs¦update-initramfs -u¦grub2-mkconfig¦RHEL 계열은 dracut으로 initramfs를 만들며 mkinitramfs와 update-initramfs는 Debian 계열 도구이다.
boot¦현재 시스템의 기본 부팅 target을 확인하는 명령은?¦systemctl get-default¦systemctl list-units¦systemctl is-active¦runlevel¦systemctl get-default는 기본 target을 출력하며 runlevel은 현재 런레벨 정보를 보여 준다.
boot¦다음 부팅부터 GUI 없이 다중 사용자 모드로 시작하도록 영구 설정하는 명령은?¦systemctl set-default multi-user.target¦systemctl isolate multi-user.target¦systemctl enable multi-user.target¦init 3¦set-default는 기본 target을 영구 변경하며 isolate와 init 3은 현재 세션에만 적용된다.
boot¦재부팅 없이 현재 실행 중인 시스템을 rescue 모드로 전환하는 명령은?¦systemctl isolate rescue.target¦systemctl set-default rescue.target¦systemctl mask rescue.target¦systemctl daemon-reload¦isolate는 즉시 target을 전환하며 set-default는 다음 부팅의 기본값만 바꾼다.
boot¦Rocky 8에서 root 암호를 잊어 GRUB의 커널 줄 끝에 추가해 initramfs 단계에서 멈추게 하는 옵션은?¦rd.break¦quiet¦rhgb¦nomodeset¦rd.break를 쓰면 루트 전환 전에 셸이 열리며 quiet와 rhgb는 부팅 메시지 출력 옵션이다.
boot¦rd.break로 root 암호를 변경한 뒤 SELinux 환경에서 반드시 해야 하는 작업은?¦touch /.autorelabel¦setenforce 0을 영구 설정하는 것¦chmod 000 /etc/shadow¦fixfiles clean¦암호 변경 후 /.autorelabel을 만들어 다음 부팅에서 SELinux 컨텍스트를 재설정해야 한다.
boot¦systemd target에 대한 설명으로 옳지 않은 것은?¦graphical.target은 multi-user.target과 무관한 독립 target이다¦rescue.target은 단일 사용자 복구용 target이다¦poweroff.target은 시스템 종료에 쓰이는 target이다¦multi-user.target은 런레벨 3에 대응하는 target이다¦graphical.target은 multi-user.target의 기능에 GUI를 더한 target이다.
boot¦직전 부팅 시점의 로그를 보는 명령은?¦journalctl -b -1¦journalctl -k¦journalctl -u boot¦dmesg -c¦journalctl -b -1은 이전 부팅의 로그를, -k는 커널 메시지만 보여 주며 dmesg -c는 버퍼를 지운다.
files¦파일의 마지막 5줄을 출력하는 명령은?¦tail -n 5 file¦head -n 5 file¦tail -n +5 file¦tail -c 5 file¦tail -n 5는 마지막 5줄, tail -n +5는 5번째 줄부터 끝까지, head는 앞부분을 출력합니다.
files¦줄 순서를 뒤집어 마지막 줄부터 출력하는 명령은?¦tac¦rev¦sort -r -n¦cat -r¦tac은 줄 순서를, rev는 각 줄 안의 문자 순서를 뒤집습니다.
files¦로그에 추가되는 줄을 계속 지켜보는 명령으로 옳은 것은?¦tail -f /var/log/messages¦head -f /var/log/messages¦less -n /var/log/messages¦cat -f /var/log/messages¦tail -f는 파일에 새로 추가되는 줄을 계속 출력합니다.
files¦현재 디렉터리 아래에서 이름이 .conf로 끝나는 파일을 찾는 명령은?¦find . -name "*.conf"¦find . -type "*.conf"¦find . -perm "*.conf"¦find . -user "*.conf"¦find의 -name은 이름 패턴, -type은 파일 종류(f, d 등)를 비교합니다.
files¦find에서 최근 7일 이내에 내용이 수정된 파일 조건은?¦-mtime -7¦-mtime +7¦-atime -7¦-mmin -7¦-mtime -7은 7일 이내 수정, +7은 7일보다 오래된 파일, -atime은 접근 시각 기준입니다.
files¦find / -size +100M 이 찾는 대상은?¦100MB를 초과하는 파일¦정확히 100MB 크기인 일반 파일¦100MB 미만인 파일¦링크 수가 100개를 넘는 파일¦+는 초과, -는 미만이며 M은 메가바이트 단위입니다.
files¦미리 만든 인덱스 DB로 파일 이름을 빠르게 찾고 updatedb로 갱신하는 명령은?¦locate¦find¦whereis¦which¦locate는 DB를 조회하므로 방금 만든 파일은 updatedb 이후에 검색됩니다.
files¦명령의 실행 파일·man 페이지·소스 위치를 함께 알려 주는 명령은?¦whereis¦which¦type¦apropos¦whereis는 바이너리·소스·매뉴얼 위치를, which는 PATH의 실행 파일만 찾습니다.
files¦디렉터리 dir과 그 하위를 확인 없이 삭제하는 명령은?¦rm -rf dir¦rmdir -r dir¦rm -d dir¦rm -i dir¦-r은 재귀, -f는 확인 생략이며 rmdir은 빈 디렉터리만 지웁니다.
files¦cp로 디렉터리를 하위 내용까지 복사할 때 필요한 옵션은?¦-r¦-l¦-u¦-i¦cp -r은 재귀 복사이며 -i는 덮어쓰기 확인, -u는 더 새로운 경우만 복사입니다.
files¦cp -p 옵션이 보존하려는 속성은?¦소유자·권한·타임스탬프¦디렉터리 구조와 하위 파일 전체¦하드 링크 관계와 inode 번호¦압축 상태와 암호화 설정¦-p는 모드·소유권·시각 정보를 원본과 같게 유지하려 합니다.
files¦a.txt 의 앞 3줄만 출력하는 명령은?¦head -n 3 a.txt¦head -c 3 a.txt¦tail -n 3 a.txt¦cat -n 3 a.txt¦head -n은 줄 수, head -c는 바이트 수 기준입니다.
files¦파일의 줄·단어·바이트 수를 한 번에 세는 명령은?¦wc¦cut¦nl¦tr¦wc는 기본적으로 줄 수, 단어 수, 바이트 수 순으로 출력합니다.
files¦/etc/passwd 에서 콜론으로 구분된 첫 번째 필드만 뽑는 명령은?¦cut -d: -f1 /etc/passwd¦cut -c: -f1 /etc/passwd¦cut -f: -d1 /etc/passwd¦tr -d: -f1 /etc/passwd¦cut의 -d는 구분자, -f는 필드 번호를 지정합니다.
files¦file 명령이 하는 일은?¦내용을 보고 파일 종류를 판별한다¦파일의 확장자를 새 형식으로 바꿔 저장한다¦파일 경로를 검색해 목록으로 출력한다¦파일 접근 권한을 변경한다¦file은 확장자가 아닌 내용(매직 넘버)으로 유형을 알려 줍니다.
files¦touch 명령에 대한 설명으로 옳지 않은 것은?¦기존 파일의 내용을 비운다¦없는 파일이면 빈 파일을 새로 만든다¦있는 파일이면 시각 정보를 갱신한다¦-t 로 특정 시각을 지정할 수 있다¦touch는 내용을 지우지 않으며 비우려면 > file 같은 리다이렉션을 씁니다.
files¦파일 내용을 이어 붙여 표준 출력으로 내보내는 명령은?¦cat a b¦split a b¦paste -c a b¦nl -c a b¦cat은 인자로 받은 파일을 차례로 연결해 출력합니다.
files¦파일을 줄 번호와 함께 출력하는 명령으로 옳은 것은?¦cat -n file¦cat -s file¦tac -n file¦head -L file¦cat -n은 모든 줄에 번호를 붙이며 -s는 연속 빈 줄을 하나로 줄입니다.
basics¦로그인한 사용자 목록과 접속 터미널을 보여 주는 명령은?¦who¦whoami¦id¦hostname¦who는 로그인 세션 목록을, whoami는 현재 유효 사용자 이름만 출력합니다.
basics¦가동 시간과 1·5·15분 load average를 보여 주는 명령은?¦uptime¦uname¦last¦hostname¦uptime은 부팅 후 경과 시간과 부하 평균을 출력합니다.
basics¦/var/log/wtmp를 읽어 로그인·재부팅 이력을 보여 주는 명령은?¦last¦lastlog¦who -b¦w¦last는 wtmp를, lastlog는 계정별 마지막 로그인 정보를 보여 줍니다.
basics¦키워드로 man 페이지 요약을 검색하는 명령은?¦apropos¦whatis¦man -f¦whereis¦apropos 키워드는 man -k 와 같으며 whatis(man -f)는 정확한 명령 이름의 한 줄 설명입니다.
basics¦man 페이지 섹션 5에 주로 담기는 내용은?¦파일 형식과 설정 파일¦일반 사용자 명령어와 셸 내장 명령¦시스템 관리자용 명령과 데몬¦커널 시스템 콜과 라이브러리 함수¦섹션 1은 사용자 명령, 5는 파일 형식, 8은 관리 명령입니다.
basics¦man 페이지에서 문자열을 앞으로 검색할 때의 입력은?¦/문자열¦?문자열¦n 문자열¦Ctrl+F 문자열¦/는 아래 방향, ?는 위 방향 검색이며 n으로 다음 결과로 이동합니다.
basics¦/etc/os-release 로 알 수 있는 정보는?¦배포판 이름과 버전¦커널 컴파일 옵션과 빌드 정보¦부팅 시 출력된 커널 메시지 전체¦CPU 모델과 클럭 속도 정보¦os-release는 배포판 ID·이름·버전을 담은 표준 파일입니다.
basics¦Rocky Linux 8 의 /etc/redhat-release 가 알려 주는 것은?¦배포판 릴리스 정보¦설치된 패키지 목록과 버전 정보¦부트 로더(GRUB)의 버전과 설정¦호스트 이름과 도메인 정보¦redhat-release는 RHEL 계열 배포판의 이름·버전을 한 줄로 보여 줍니다.
basics¦uname -a 출력에 포함되지 않는 정보는?¦로그인 중인 사용자 수¦커널 릴리스와 빌드 날짜¦하드웨어 아키텍처와 운영체제 이름¦호스트 이름(노드 이름)¦사용자 수는 uptime이나 who로 확인하며 uname은 시스템 식별 정보를 출력합니다.
basics¦직전에 실행한 명령 전체를 다시 실행하는 Bash 표기는?¦!!¦!$¦!*¦^^¦!!는 직전 명령 전체, !$는 직전 명령의 마지막 인자입니다.
basics¦Bash의 명령 기록이 종료 시 저장되는 기본 파일은?¦~/.bash_history¦/etc/history¦~/.history_log¦/var/log/history¦Bash는 세션 종료 시 입력 기록을 ~/.bash_history에 저장합니다.
basics¦터미널 화면을 지우는 단축키는?¦Ctrl+L¦Ctrl+C¦Ctrl+D¦Ctrl+Z¦Ctrl+L은 clear와 같고 Ctrl+C는 중단, Ctrl+D는 입력 종료입니다.
basics¦시스템을 정지(halt)시키는 명령으로 옳은 것은?¦shutdown -h now¦shutdown -r now¦init 6¦reboot¦-h는 정지, -r은 재부팅이며 init 6은 재부팅 런레벨입니다.
basics¦date +%Y-%m-%d 의 출력으로 옳은 것은?¦4자리 연도-월-일¦2자리 연도-일-월 형식¦월-일-시 형식¦요일-월-일 형식¦%Y는 4자리 연도, %m은 월, %d는 일이며 %M은 분입니다.
basics¦현재 셸에서 직전 명령의 마지막 인자를 불러오는 표기는?¦!$¦!!¦!^¦!#¦!$는 마지막 인자, !^는 첫 번째 인자, !!는 명령 전체입니다.
users¦/etc/passwd 한 줄 root:x:0:0:root:/root:/bin/bash 에서 두 번째 필드 x의 의미는?¦암호가 /etc/shadow에 있다¦암호가 비어 있어 인증 없이 로그인된다¦계정이 잠겨 있어 로그인할 수 없다¦암호가 평문으로 저장되어 있다¦x는 실제 암호 해시가 /etc/shadow에 분리돼 있음을 나타냅니다.
users¦/etc/passwd 일곱 번째 필드가 /sbin/nologin 일 때 의미는?¦대화형 로그인이 불가능한 계정¦홈 디렉터리가 존재하지 않는 계정¦암호가 만료되어 변경이 필요한 계정¦UID가 0인 관리자 계정¦마지막 필드는 로그인 셸이며 nologin이면 셸 로그인을 막습니다.
users¦/etc/passwd 필드 순서로 옳은 것은?¦계정:암호:UID:GID:설명:홈:셸¦계정:UID:GID:암호:홈:셸:설명¦계정:GID:UID:암호:설명:셸:홈¦계정:암호:GID:UID:홈:설명:셸¦passwd는 콜론으로 구분된 7개 필드를 이 순서로 가집니다.
users¦Rocky Linux 8 의 일반 사용자 UID 기본 시작값은?¦1000¦500¦100¦1001¦시스템 계정은 1~999, 일반 사용자는 1000부터이며 구버전 RHEL 6은 500이었습니다.
users¦/etc/shadow 두 번째 필드가 !! 또는 ! 로 시작할 때 의미는?¦암호 로그인이 불가능한 상태¦암호가 평문으로 저장된 상태¦암호 사용 기간이 무제한인 상태¦계정 삭제가 예약된 상태¦! 가 붙으면 해당 암호로 인증할 수 없는 상태입니다.
users¦/etc/shadow 세 번째 필드가 나타내는 값은?¦마지막 암호 변경일(1970-01-01 기준 일수)¦암호 최대 사용 일수(변경 후 만료까지)¦계정 만료일(1970-01-01 기준 일수, 비면 무기한)¦암호 만료 경고 기간(일 단위)¦세 번째 필드는 epoch 이후 일수로 기록된 최종 암호 변경일입니다.
users¦사용자의 암호 만료·최소/최대 사용일 등을 조회·설정하는 명령은?¦chage¦chsh¦chfn¦chpasswd -e¦chage -l 사용자 로 에이징 정보를 확인합니다.
users¦계정을 홈 디렉터리와 함께 삭제하는 명령은?¦userdel -r 사용자¦userdel -f 사용자¦usermod -d 사용자¦deluser -h 사용자¦-r은 홈 디렉터리와 메일 스풀을 함께 지우고 -f는 강제 삭제입니다.
users¦useradd의 기본값(기본 셸·홈 베이스)이 정의된 파일은?¦/etc/default/useradd¦/etc/login.defs¦/etc/sysconfig/useradd¦/etc/adduser.conf¦기본 셸·홈 베이스는 /etc/default/useradd, UID 범위·암호 에이징은 /etc/login.defs에 있고 /etc/adduser.conf는 Debian의 adduser용입니다.
users¦새 사용자 홈에 .bashrc 등을 복사해 주는 원본 디렉터리는?¦/etc/skel¦/etc/default¦/usr/share/skel¦/var/skel¦useradd -m 시 /etc/skel의 내용이 새 홈으로 복사됩니다.
users¦사용자 alloy 계정을 잠그는 명령은?¦usermod -L alloy¦usermod -U alloy¦passwd -x alloy¦userdel -L alloy¦-L은 잠금, -U는 해제이며 passwd -l 도 잠금입니다.
users¦사용자 alloy 의 기본 그룹을 dev 로 바꾸는 명령은?¦usermod -g dev alloy¦usermod -G dev alloy¦usermod -aG dev alloy¦groupmod -g dev alloy¦소문자 -g는 기본 그룹, 대문자 -G는 보조 그룹 목록입니다.
users¦홈 디렉터리 없이 로그인 셸이 /sbin/nologin 인 시스템 계정을 만드는 명령은?¦useradd -r -s /sbin/nologin svc¦useradd -m -s /sbin/nologin svc¦useradd -u 0 -s /sbin/nologin svc¦useradd -D -s /sbin/nologin svc¦-r은 시스템 계정, -s는 로그인 셸 지정이며 -m은 홈 생성입니다.
users¦사용자 alloy 가 속한 그룹 이름을 출력하는 명령은?¦groups alloy¦who alloy¦lastlog -u alloy¦gpasswd alloy¦groups는 그룹 이름을, id는 숫자 ID도 함께 보여 줍니다.
users¦/etc/group 한 줄 dev:x:1001:kim,lee 에서 1001의 의미는?¦그룹의 GID¦그룹 암호가 저장된 해시 값¦그룹에 속한 구성원의 총수¦그룹이 마지막으로 변경된 날짜¦세 번째 필드가 GID, 네 번째가 보조 구성원 목록입니다.
users¦su 와 su - 의 차이로 옳은 것은?¦su - 는 대상 사용자의 로그인 환경을 불러온다¦su - 는 암호를 묻지 않고 바로 전환한다¦su 는 항상 대상 사용자의 홈으로 이동하고 환경도 초기화한다¦su - 는 현재 셸의 환경변수를 그대로 유지한다¦su - 는 로그인 셸처럼 환경과 작업 디렉터리를 초기화합니다.
permissions¦ls -l 출력 -rwxr-x--- 1 root dev 10 Oct 1 a.sh 에서 other의 권한은?¦없음¦읽기만 가능¦읽기·실행 가능¦읽기·쓰기·실행 모두 가능¦마지막 세 글자 ---이므로 other는 권한이 없습니다.
permissions¦drwxrwxrwt 처럼 마지막 자리에 t 가 보이는 디렉터리에 설정된 것은?¦스티키 비트¦SetUID¦SetGID¦ACL 마스크¦t는 other의 x와 스티키 비트가 함께 있을 때 표시됩니다.
permissions¦스티키 비트가 걸린 /tmp 에서 남의 파일을 지울 수 있는 사용자는?¦파일 소유자·디렉터리 소유자·root¦같은 그룹에 속한 모든 사용자¦디렉터리에 w가 있는 모든 사용자¦파일에 쓰기 권한이 있는 모든 사용자와 root¦스티키 비트가 있으면 파일 소유자·디렉터리 소유자·root만 삭제·이름 변경이 가능합니다.
permissions¦ls -l 에서 -rwsr-xr-x 로 표시되는 파일에 설정된 특수 권한은?¦SetUID¦SetGID¦Sticky Bit¦ACL¦소유자 실행 자리의 s는 SetUID로 실행 시 소유자 권한을 얻습니다.
permissions¦디렉터리에 SetGID가 설정됐을 때의 일반적인 효과는?¦새 파일이 디렉터리의 그룹을 상속한다¦디렉터리 안에서 남의 파일을 삭제할 수 없다¦디렉터리 안의 실행 파일이 root 권한으로 실행된다¦소유자만 디렉터리 내용을 읽을 수 있다¦공유 디렉터리의 그룹 소유권을 일관되게 유지하는 데 씁니다.
permissions¦chmod 4755 file 의 결과 권한 표시는?¦rwsr-xr-x¦rwxr-sr-x¦rwxr-xr-t¦rwsr-sr-x¦맨 앞 4는 SetUID이며 소유자 실행 자리에 s로 표시됩니다.
permissions¦chmod 2775 dir 에서 맨 앞 2의 의미는?¦SetGID¦SetUID¦Sticky Bit¦ACL 상속¦숫자 4는 SetUID, 2는 SetGID, 1은 스티키입니다.
permissions¦umask 027 일 때 새로 만든 디렉터리의 기본 권한은?¦750¦640¦755¦777¦디렉터리 기본 777에서 027을 빼면 750입니다.
permissions¦umask 077 일 때 새로 만든 일반 파일의 기본 권한은?¦600¦700¦644¦666¦파일 기본 666에서 077을 빼면 600입니다.
permissions¦chmod u+x,g-w,o=r file 이 하는 일은?¦소유자 x 추가, 그룹 w 제거, 기타를 r로 지정¦소유자 x 제거, 그룹 w 추가, 기타에 r만 추가¦모든 사용자에게 rwx 추가¦소유자만 r로 설정하고 나머지는 제거¦+는 추가, -는 제거, =는 지정한 값으로 설정입니다.
permissions¦chmod 754 file 에서 그룹의 권한은?¦읽기·실행¦읽기·쓰기¦읽기·쓰기·실행¦읽기만¦7=rwx, 5=r-x, 4=r-- 이므로 그룹은 5(r-x)입니다.
permissions¦chown -R kim:dev /data 의 의미는?¦하위 전체의 소유자를 kim, 그룹을 dev 로 변경¦하위 전체의 소유자를 dev, 그룹을 kim 으로 변경¦하위 전체의 권한을 kim:dev 로 변경¦소유자만 kim 으로 변경¦-R은 재귀이며 사용자:그룹 형식으로 둘을 함께 바꿉니다.
permissions¦파일의 소유 그룹만 변경하는 명령은?¦chgrp dev file¦chown -g dev file¦chmod g=dev file¦newgrp dev file¦chgrp 또는 chown :dev file 이 그룹만 바꿉니다.
permissions¦디렉터리에 r은 있고 x가 없을 때의 결과는?¦이름 목록은 보이나 cd·내부 접근은 안 된다¦cd로 이동은 되지만 목록은 볼 수 없다¦목록과 내부 파일 읽기가 모두 가능하다¦목록도 볼 수 없고 cd도 안 된다¦x는 경로 탐색, r은 이름 목록 읽기이므로 분리되어 동작합니다.
permissions¦파일에 설정된 ACL을 확인하는 명령은?¦getfacl¦lsattr¦getfattr¦stat -a¦ACL 조회는 getfacl, 설정은 setfacl이며 lsattr은 확장 속성입니다.
permissions¦setfacl -m u:kim:rw file 이 하는 일은?¦사용자 kim에게 읽기·쓰기 ACL을 추가한다¦소유자를 kim으로 바꾸고 읽기·쓰기를 부여한다¦파일의 기존 ACL을 모두 삭제하고 kim만 남긴다¦그룹 kim에게 실행 권한을 부여한다¦-m은 항목 수정·추가이며 -x는 특정 항목 삭제, -b는 전체 삭제입니다.
permissions¦chattr +i file 의 효과는?¦root라도 수정·삭제할 수 없는 불변 상태¦파일이 자동으로 압축되어 저장되는 상태¦추가(append)만 가능하고 덮어쓰기는 금지되는 상태¦접근 시각(atime)이 갱신되지 않는 상태¦i 속성은 해제하기 전까지 변경·삭제·링크 생성이 막히며, +a는 추가만 허용합니다.
permissions¦rwxr-xr-- 를 8진수로 바꾼 값은?¦754¦745¦655¦764¦rwx=7, r-x=5, r--=4 순으로 계산합니다.
filesystem¦XFS 파일시스템을 만드는 명령은?¦mkfs -t xfs /dev/sdb1¦mkpart xfs /dev/sdb1¦newfs xfs /dev/sdb1¦format -t xfs /dev/sdb1¦mkfs -t 또는 mkfs.xfs로 장치에 파일시스템을 생성합니다.
filesystem¦Rocky Linux 8 설치 시 루트 파일시스템의 기본 유형은?¦XFS¦ext4¦Btrfs¦ReiserFS¦RHEL 7 이후 계열의 기본 파일시스템은 XFS입니다.
filesystem¦XFS 파일시스템 복구에 쓰는 명령은?¦xfs_repair¦e2fsck¦resize2fs¦xfs_growfs¦xfs_repair는 XFS 복구용이고 xfs_growfs는 확장, e2fsck·resize2fs는 ext 계열용입니다.
filesystem¦현재 실제로 마운트된 목록을 보는 방법으로 옳은 것은?¦findmnt 또는 /proc/mounts¦/etc/fstab 의 마운트 항목 확인¦/boot/grub2/mounts 파일 확인¦/var/log/mount 로그 확인¦fstab은 설정 파일이고 실제 상태는 mount, findmnt, /proc/mounts로 봅니다.
filesystem¦/dev/sdb1 을 /mnt 에 마운트하는 올바른 명령은?¦mount /dev/sdb1 /mnt¦mount -o /dev/sdb1 /mnt¦umount /dev/sdb1 /mnt¦mkfs /dev/sdb1 /mnt¦mount 장치 마운트포인트 순서이며 해제는 umount입니다.
filesystem¦umount 시 target is busy 가 나오는 원인은?¦그 파일시스템 안에서 프로세스가 사용 중이다¦마운트하려는 장치가 존재하지 않는다¦해당 마운트 지점의 디렉터리 권한이 777이다¦장치의 파일시스템이 손상되어 fsck가 필요하다¦fuser -m 이나 lsof로 사용 중인 프로세스를 확인합니다.
filesystem¦blkid 가 출력하는 것은?¦블록 장치의 UUID와 파일시스템 유형¦마운트 지점별 디스크 사용량과 남은 용량¦파티션 테이블을 편집하는 대화형 화면¦파일시스템별 inode 사용량과 남은 개수¦blkid는 UUID·LABEL·TYPE을 보여 주며 fstab 작성에 유용합니다.
filesystem¦df -i 가 보여 주는 정보는?¦inode 사용량¦파일시스템 종류와 마운트 옵션 정보¦블록 크기와 총 블록 수 정보¦마운트 지점별 사용 용량 비율¦-i는 inode 총수·사용·남은 수를 출력하며 파일 수가 많을 때 점검합니다.
filesystem¦ln -s /etc/hosts /tmp/h 로 만든 /tmp/h 는?¦원본 경로를 가리키는 심볼릭 링크¦원본과 inode를 공유하는 하드 링크¦원본 내용을 복사해 만든 독립 파일¦원본이 삭제돼도 내용이 남아 있는 파일¦심볼릭 링크는 경로 문자열을 담으며 원본이 사라지면 끊어집니다.
filesystem¦ls -li 에서 두 파일의 첫 번째 숫자가 같다면?¦같은 inode를 공유한다¦같은 소유자 UID를 가진다¦같은 디렉터리에 있는 같은 크기 파일이다¦같은 디스크 블록 그룹에 위치한다¦-i 옵션의 첫 열은 inode 번호이며 같으면 하드 링크 관계입니다.
filesystem¦swap 영역을 서식 지정한 뒤 활성화하는 명령 순서는?¦mkswap 후 swapon¦swapon 후 mkswap¦mkfs.swap 후 mount¦swapctl 후 swapoff¦mkswap으로 서식 지정 후 swapon으로 활성화하며 swapoff는 해제입니다.
filesystem¦/proc 의 특징으로 옳은 것은?¦커널·프로세스 정보를 담은 가상 파일시스템이다¦사용자 파일을 영구 저장하는 디스크 파일시스템이다¦부트 로더와 커널 이미지를 담은 디렉터리이다¦외부 장치가 자동으로 마운트되는 기본 위치이다¦/proc는 메모리상의 가상 FS로 /proc/cpuinfo 등이 있습니다.
shell¦명령 출력을 파일 끝에 추가하는 리다이렉션은?¦>>¦>¦2>¦<¦>>는 추가, >는 덮어쓰기, <는 입력 리다이렉션입니다.
shell¦표준 오류(stderr)만 파일로 저장하는 표기는?¦2> err.txt¦1> err.txt¦&< err.txt¦0> err.txt¦파일 디스크립터 2가 stderr, 1은 stdout, 0은 stdin입니다.
shell¦stdout과 stderr를 같은 파일로 보내는 올바른 표기는?¦cmd > all.txt 2>&1¦cmd 2>&1 > all.txt¦cmd 2>&1 | all.txt¦cmd > all.txt 2> all.txt¦먼저 stdout을 파일로 돌린 뒤 stderr를 그곳으로 복제해야 하므로 순서가 중요합니다. 2>&1 > all.txt 는 stderr가 터미널에 남습니다.
shell¦앞 명령이 실패했을 때만 다음 명령을 실행하는 연산자는?¦||¦&&¦|¦;¦||는 OR이고 &&는 앞 명령이 성공했을 때 실행합니다.
shell¦백그라운드 작업 1번을 포그라운드로 가져오는 명령은?¦fg %1¦bg %1¦jobs %1¦kill %1¦fg는 포그라운드로, bg는 정지된 작업을 백그라운드에서 재개합니다.
shell¦실행 중인 포그라운드 프로세스를 일시 정지하는 단축키는?¦Ctrl+Z¦Ctrl+C¦Ctrl+D¦Ctrl+S¦Ctrl+Z는 SIGTSTP로 일시 정지, Ctrl+C는 SIGINT로 중단입니다.
shell¦와일드카드 [abc]* 가 의미하는 것은?¦a, b, c 중 한 글자로 시작하는 이름¦abc 로 끝나는 이름¦a부터 c까지가 아닌 글자로 시작하는 이름¦a, b, c를 모두 포함하는 이름¦[]는 괄호 안 문자 중 한 글자와 대응하며 *는 나머지를 임의로 채웁니다.
shell¦echo "$HOME" 과 echo '$HOME' 의 결과로 옳은 것은?¦홈 경로 출력, 문자열 $HOME 출력¦둘 다 홈 경로 출력¦둘 다 문자열 $HOME 출력¦문자열 $HOME 출력, 홈 경로 출력¦큰따옴표는 변수 확장을 허용하고 작은따옴표는 막습니다.
shell¦직전 명령의 종료 상태를 담는 특수 변수는?¦$?¦$$¦$!¦$#¦$?는 종료 상태, $$는 셸 PID, $!는 마지막 백그라운드 PID입니다.
shell¦grep -v abc file 의 결과는?¦abc를 포함하지 않는 줄¦abc를 포함하는 줄의 개수만 출력¦대소문자를 무시하고 abc가 일치하는 줄¦abc를 포함하는 줄의 줄 번호¦-v는 반전, -c는 개수, -i는 대소문자 무시, -n은 줄 번호입니다.
shell¦sort 뒤에 uniq 를 쓰는 이유는?¦uniq는 인접한 중복 줄만 제거하기 때문¦uniq는 정렬되지 않은 입력을 거부하기 때문¦sort가 중복을 모두 제거하므로¦uniq가 원본 파일을 수정하므로¦uniq는 이웃한 같은 줄만 합치므로 먼저 정렬합니다.
shell¦here document 에 대한 설명으로 옳은 것은?¦<<구분자 형태로 여러 줄을 입력으로 전달한다¦명령을 백그라운드에서 실행하도록 지정한다¦하나의 파일을 여러 파일로 분할해 저장한다¦프로세스를 종료하고 종료 상태를 전달한다¦<<EOF 같은 표기가 구분자 직전까지의 줄을 표준 입력으로 보냅니다.
environment¦현재 셸의 환경변수를 출력하는 명령은?¦env¦set -u¦export -z¦declare -a¦env는 환경변수 목록이며 set은 셸 변수와 함수까지 출력합니다.
environment¦환경변수와 셸 변수의 차이로 옳은 것은?¦export한 변수만 자식 프로세스에 전달된다¦셸 변수는 자식 프로세스에도 자동으로 전달된다¦환경변수는 현재 셸에서만 보이고 자식에게는 안 보인다¦둘은 이름만 다를 뿐 동작은 같다¦export된 변수만 자식 프로세스의 환경에 들어갑니다.
environment¦변수 FOO 를 완전히 제거하는 명령은?¦unset FOO¦FOO=¦export -n FOO¦delete FOO¦FOO=는 빈 값 대입이고 unset이 변수를 제거하며 export -n은 export 속성만 해제합니다.
environment¦로그인 셸에서 Bash가 읽는 사용자별 파일은?¦~/.bash_profile¦~/.bashrc 만 읽고 ~/.bash_profile은 읽지 않는다¦/etc/bashrc¦~/.bash_logout¦로그인 셸은 ~/.bash_profile을 읽고 보통 거기서 ~/.bashrc를 불러옵니다.
environment¦비로그인 대화형 Bash 셸이 시작할 때 읽는 파일은?¦~/.bashrc¦~/.bash_profile¦/etc/profile¦~/.bash_logout¦새 터미널 창 같은 비로그인 셸은 ~/.bashrc를 읽습니다.
environment¦RHEL 계열에서 모든 사용자의 대화형 셸에 alias·함수를 적용하는 전역 파일은?¦/etc/bashrc¦/etc/bash.bashrc¦/etc/environment.sh¦/etc/sysconfig/bash¦/etc/bashrc는 RHEL 계열, /etc/bash.bashrc는 Debian 계열의 전역 Bash 설정입니다.
environment¦PATH 맨 뒤에 /opt/bin 을 추가하는 올바른 명령은?¦export PATH=$PATH:/opt/bin¦export PATH=/opt/bin¦export PATH=$PATH;/opt/bin¦export PATH=$PATH/opt/bin¦경로는 콜론으로 구분하며 기존 값을 $PATH로 유지해야 합니다.
environment¦export PATH=/opt/bin:$PATH 로 바꾼 결과는?¦/opt/bin이 가장 먼저 검색된다¦/opt/bin이 가장 나중에 검색된다¦기존 PATH가 삭제된다¦현재 디렉터리가 먼저 검색된다¦앞에 둔 경로가 우선이므로 같은 이름이면 /opt/bin의 명령이 실행됩니다.
environment¦alias 에 대한 설명으로 옳은 것은?¦영구 적용하려면 셸 시작 파일에 기록한다¦모든 셸에 자동으로 적용된다¦환경변수와 같아서 자식 프로세스에 전달된다¦unalias 명령으로 별칭을 새로 만든다¦셸을 종료하면 사라지므로 ~/.bashrc 등에 써 두어야 합니다.
environment¦변수를 읽기 전용으로 고정하는 Bash 내장 명령은?¦readonly¦export -r¦const¦lock¦readonly로 선언한 변수는 값을 바꾸거나 unset할 수 없습니다.
environment¦LANG 환경변수가 결정하는 것은?¦기본 로케일(언어·문자 인코딩)¦로그인 셸의 종류와 위치¦부팅 시 사용할 키보드 레이아웃과 폰트¦프롬프트의 색상과 문자 모양¦LANG은 기본 로케일이며 LC_ALL이 있으면 그것이 우선합니다.
environment¦프롬프트 모양을 지정하는 환경변수는?¦PS1¦PWD¦HISTSIZE¦PROMPT_PWD¦PS1이 기본 프롬프트이고 PWD는 현재 디렉터리입니다.
streams¦표준 출력과 표준 오류를 모두 all.log 하나에 덮어쓰기로 저장하는 올바른 형태는?¦cmd > all.log 2>&1¦cmd 2>&1 > all.log¦cmd >> all.log 2>&1¦cmd 2> all.log 1> all.log¦리다이렉션은 왼쪽부터 처리되므로 먼저 1을 파일로 보낸 뒤 2>&1로 2를 1이 가리키는 파일에 맞춰야 합니다. >>는 추가, 마지막 보기는 같은 파일을 두 번 열어 서로 덮어씁니다.
streams¦cmd 2>&1 > out.txt 를 실행했을 때 일어나는 일은?¦오류는 화면으로, 출력은 out.txt로 간다¦출력과 오류가 모두 out.txt로 간다¦오류만 out.txt로 가고 출력은 화면에 나온다¦출력은 화면으로, 오류는 out.txt로 간다¦2>&1 시점에 1은 아직 화면이므로 오류는 화면에 남고 이후에 1만 파일로 바뀝니다.
streams¦에러 메시지를 화면에 보이지 않게 버리려면?¦cmd 2> /dev/null¦cmd > /dev/null 은 표준 출력과 오류를 모두 버린다¦cmd 2>&1 > /dev/null¦cmd | /dev/null¦/dev/null로 보낸 2번 스트림은 버려집니다. >만 쓰면 1번만 버려지고, 2>&1 > /dev/null은 오류가 화면에 남습니다.
streams¦표준 입력을 파일에서 읽게 하는 연산자는?¦<¦>¦>>¦|¦<는 파일 내용을 표준 입력(0)으로 연결합니다.
streams¦다음 중 here document를 시작하는 표기는?¦<< EOF¦<<< EOF¦>> EOF¦|| EOF¦<<는 지정한 종료 문자열 전까지의 줄을 표준 입력으로 전달하고, <<<는 한 문자열을 입력으로 주는 here string입니다.
streams¦ls -l | tee list.txt 의 동작으로 옳은 것은?¦화면에 출력하면서 list.txt에도 저장한다¦list.txt에만 저장하고 화면에는 아무것도 나오지 않는다¦list.txt의 내용을 읽어 ls -l의 입력으로 넣어 준다¦list.txt 끝에 표준 오류 메시지만 추가로 기록한다¦tee는 표준 입력을 표준 출력과 파일에 동시에 복사하며 -a를 주면 추가합니다.
streams¦기존 log.txt 끝에 출력을 이어 붙이면서 동시에 화면에도 보려는 명령은?¦cmd | tee -a log.txt¦cmd | tee log.txt 로 기존 내용 뒤에 이어 쓴다¦cmd >> log.txt | cat 으로 파일에 쓰며 화면에도 출력한다¦cmd > log.txt | more 로 파일에 추가하면서 본다¦tee -a는 덮어쓰지 않고 추가합니다. -a가 없으면 tee는 파일을 덮어씁니다.
streams¦[표준 입출력과 연결] 다음 중 옳지 않은 설명은?¦>> 는 기존 파일 내용을 지우고 새로 쓴다¦2>는 표준 오류를 리다이렉션한다¦|는 앞 명령 출력을 뒤 명령 입력으로 연결한다¦<는 파일을 표준 입력으로 읽게 한다¦>>는 파일 끝에 추가하며 덮어쓰기는 >입니다.
streams¦find / -name passwd 2>/dev/null 의 결과는?¦권한 거부 같은 오류 메시지 없이 찾은 경로만 보인다¦찾은 경로 출력이 모두 사라지고 오류 메시지만 화면에 보인다¦passwd 파일이 모두 삭제되어 /dev/null로 이동한다¦검색 결과가 /dev/null 파일에 저장되어 화면에는 없다¦표준 오류만 버리므로 정상 검색 결과는 화면에 출력됩니다.
streams¦다음 중 xargs의 용도로 가장 알맞은 것은?¦표준 입력으로 받은 항목을 다른 명령의 인자로 넘긴다¦명령의 표준 오류만 따로 모아 지정한 파일에 기록한다¦백그라운드 작업을 포그라운드로 옮겨 계속 실행한다¦파일 내용을 정렬하고 중복된 줄을 제거해 출력한다¦xargs는 입력 줄을 명령 인자로 변환하여 실행합니다.
streams¦set -o noclobber 가 설정된 bash에서 이미 있는 file에 echo hi > file 을 하면?¦덮어쓰기가 거부되고 오류가 난다¦내용이 hi로 덮어써지고 경고만 출력된다¦hi가 기존 내용 뒤에 추가된다¦file이 삭제되고 새 파일이 만들어진다¦noclobber는 > 로 기존 파일을 덮어쓰지 못하게 하며 >| 로 강제할 수 있습니다.
streams¦cat < a.txt > b.txt 와 가장 가까운 동작은?¦a.txt를 b.txt로 복사한다¦b.txt를 a.txt로 복사한다¦a.txt 끝에 b.txt의 내용을 추가한다¦두 파일의 이름을 서로 맞바꾼다¦a.txt가 표준 입력이 되고 cat의 출력이 b.txt로 저장됩니다.
streams¦다음 중 표준 스트림과 파일 디스크립터의 대응이 옳은 것은?¦stdin 0, stdout 1, stderr 2¦stdin 1, stdout 2, stderr 3¦stdin 0, stdout 2, stderr 1¦stdin 3, stdout 1, stderr 2¦표준 입력 0, 표준 출력 1, 표준 오류 2가 고정된 번호입니다.
text¦/etc/passwd에서 첫 번째 필드(사용자명)만 뽑는 올바른 명령은?¦cut -d: -f1 /etc/passwd¦cut -d: -c1 /etc/passwd¦cut -f1 /etc/passwd¦cut -s: -n1 /etc/passwd¦-d로 구분자를 :로 지정하고 -f로 필드 번호를 고릅니다. cut의 기본 구분자는 탭입니다.
text¦파일의 각 줄에서 앞 3글자만 출력하려면?¦cut -c1-3 file¦cut -f1-3 file¦cut -b3 file¦head -c3 file¦-c는 문자 위치 기준이며 -f는 필드 기준입니다. head -c3은 파일 전체의 앞 3바이트만 출력합니다.
text¦grep -i error log 의 의미는?¦대소문자를 구분하지 않고 error를 찾는다¦error를 포함하지 않는 줄만 골라서 출력한다¦error가 포함된 줄의 줄 번호만 출력한다¦error를 하위 디렉터리까지 재귀적으로 찾는다¦-i는 ignore-case 옵션입니다.
text¦디렉터리 /etc/ssh 아래 모든 파일에서 Port 문자열을 재귀적으로 찾는 명령은?¦grep -r Port /etc/ssh¦grep -c Port /etc/ssh¦grep -l Port /etc/ssh¦grep -w Port /etc/ssh¦-r은 하위 디렉터리까지 재귀 검색하고, -c는 개수, -l은 파일명 출력이며 디렉터리 인자에 -r이 없으면 오류가 납니다.
text¦grep -c root /etc/passwd 가 출력하는 것은?¦root가 포함된 줄의 개수¦root라는 문자열이 등장한 총 횟수¦root가 포함된 줄의 내용 전체¦root가 들어 있는 파일의 이름 목록¦-c는 일치한 줄의 수를 세며 한 줄에 여러 번 나와도 1로 계산합니다.
text¦sort 출력에서 숫자를 크기순으로 정렬하려면 필요한 옵션은?¦-n (numeric)¦-r¦-u¦-d¦-n은 숫자 비교이며 이것이 없으면 문자열 사전순으로 10이 2보다 앞섭니다.
text¦sort -t: -k3 -n /etc/passwd 가 하는 일은?¦: 구분 3번째 필드를 숫자순으로 정렬한다¦3번째 줄만 골라서 숫자순으로 정렬한다¦각 줄에서 : 앞의 3글자를 기준으로 정렬한다¦3번째 파일을 정렬해 다른 파일과 병합한다¦-t는 필드 구분자, -k는 정렬 키 필드, -n은 숫자 비교입니다.
text¦uniq -c 의 역할은?¦인접한 중복 줄을 세어 앞에 횟수를 붙인다¦파일 전체의 문자 수를 세어 마지막에 출력한다¦중복이 없는 줄만 남기고 나머지를 모두 삭제한다¦줄을 숫자 크기순으로 정렬한 뒤 개수를 센다¦uniq는 인접 줄만 비교하므로 보통 sort와 함께 쓰며 -c는 횟수 표시입니다.
text¦파일에서 단어별 출현 빈도를 구하는 데 알맞은 파이프 구성은? (단어는 줄마다 하나)¦sort | uniq -c¦uniq -c | sort -u¦sort -u | wc -l¦uniq | sort -c¦uniq는 인접 줄만 합치므로 먼저 sort로 같은 줄을 모아야 하며, sort -u | wc -l은 서로 다른 줄의 개수만 알려 줍니다.
text¦tr 'a-z' 'A-Z' 의 동작은?¦표준 입력의 소문자를 대문자로 바꾼다¦파일 이름을 인자로 받아 파일 안의 소문자를 대문자로 바꾼다¦표준 입력에서 a-z 범위의 문자를 모두 삭제한다¦표준 입력의 대문자를 소문자로 바꾼다¦tr은 표준 입력 문자를 치환·삭제하며 파일 인자를 받지 않습니다.
text¦sed 's/foo/bar/g' file 의 설명으로 옳은 것은?¦각 줄의 모든 foo를 bar로 바꿔 출력한다¦각 줄의 첫 foo만 bar로 바꾸고 file을 직접 수정한다¦foo가 포함된 줄을 모두 삭제하고 나머지를 출력한다¦bar를 foo로 바꾼 결과를 file에 저장한다¦g가 있으면 줄 안 모든 일치를 치환하며 -i 없이는 파일 자체를 수정하지 않습니다.
text¦sed -n '2,4p' file 의 출력은?¦2번째부터 4번째 줄¦2번째와 4번째 줄만¦2번째 줄을 제외한 나머지 모든 줄¦앞 4줄 중에서 2줄을 삭제한 결과¦-n은 자동 출력을 끄고 p로 지정한 범위 줄만 출력합니다.
text¦awk '{print $1}' file 이 출력하는 것은?¦각 줄의 첫 번째 필드¦각 줄의 마지막 필드¦파일의 첫 번째 줄 전체¦각 줄의 글자 수¦awk는 기본적으로 공백으로 필드를 나누며 $1은 첫 필드입니다.
text¦awk -F: '{print $NF}' /etc/passwd 는?¦각 줄의 마지막 필드를 출력한다¦각 줄의 필드 개수를 출력한다¦각 줄의 첫 번째 필드를 출력한다¦각 줄에서 : 문자를 모두 지워 출력한다¦-F로 구분자를 지정하고 NF는 필드 수이므로 $NF는 마지막 필드입니다.
text¦tail -f /var/log/messages 의 용도는?¦파일에 추가되는 내용을 계속 지켜본다¦파일의 마지막 한 줄을 삭제한다¦파일을 강제로 닫아 쓰기를 막는다¦파일의 처음부터 끝까지 한 번만 출력한다¦-f는 follow로 로그 실시간 확인에 쓰입니다.
text¦[텍스트·검색·정렬] 다음 중 옳지 않은 것은?¦wc -w는 줄 수를 센다¦cut -d는 구분자를 지정한다¦sort -r은 역순 정렬이다¦tail -n 3은 마지막 3줄을 출력한다¦wc -w는 단어 수, 줄 수는 wc -l입니다.
archive¦data.tar.gz를 현재 디렉터리에 풀 때 올바른 명령은?¦tar -xzf data.tar.gz¦tar -czf data.tar.gz¦tar -tzf data.tar.gz¦tar -xjf data.tar.gz¦x는 추출, z는 gzip 해제이며 c는 생성, t는 목록입니다.
archive¦tar -xf backup.tar -C /tmp 에서 -C의 의미는?¦지정한 디렉터리로 이동해 작업한다¦압축 수준을 지정한다¦체크섬을 검사하고 불일치 시 중단한다¦기존 파일을 복사 모드로 덮어쓴다¦-C는 change directory로 풀거나 묶을 기준 디렉터리를 바꿉니다.
archive¦tar -cjf a.tar.bz2 dir 에서 j는?¦bzip2 압축¦gzip 압축¦xz 압축¦압축 해제¦j는 bzip2, z는 gzip, J는 xz입니다.
archive¦tar -tvf a.tar 의 설명으로 옳은 것은?¦풀지 않고 자세한 목록을 출력한다¦자세한 로그를 출력하며 파일을 현재 위치에 풀어 낸다¦a.tar라는 이름의 새 아카이브를 만든다¦a.tar 아카이브에 파일을 추가한다¦t는 목록, v는 상세 출력이며 추출은 x입니다.
archive¦tar에서 기존 아카이브 끝에 파일을 추가하는 옵션은?¦-r¦-c¦-t¦-d¦-r은 append이며 -c는 새로 생성합니다.
archive¦gzip 으로 file.txt를 압축한 결과는?¦file.txt.gz가 만들어지고 원본은 기본적으로 삭제된다¦file.txt.gz가 만들어지고 원본이 그대로 유지된다¦file.txt.tar가 만들어지고 원본은 삭제된다¦file.gz.txt가 만들어진다¦gzip은 기본적으로 원본을 .gz로 대체하며 -k를 쓰면 원본을 유지합니다.
archive¦gunzip file.txt.gz 와 같은 동작은?¦gzip -d file.txt.gz¦gzip -c file.txt.gz¦gzip -9 file.txt.gz¦tar -z file.txt.gz¦-d는 decompress입니다. -c는 결과를 표준 출력으로 보냅니다.
archive¦bzip2로 압축한 파일의 일반적인 확장자는?¦.bz2¦.gz¦.xz¦.zip¦bzip2는 .bz2, gzip은 .gz, xz는 .xz를 씁니다.
archive¦unzip -l sample.zip 은 어떤 동작인가?¦압축을 풀지 않고 내용 목록을 본다¦sample.zip을 풀고 각 파일에 심볼릭 링크를 만든다¦로그만 남기고 sample.zip을 삭제한다¦압축 레벨을 낮추어 다시 압축한다¦-l은 list로 풀지 않고 들어 있는 항목을 표시합니다.
archive¦cpio 와 가장 관련 깊은 설명은?¦표준 입력으로 파일 목록을 받아 아카이브를 만들거나 푼다¦패키지의 의존성을 해결하고 설치 순서를 정한다¦파일 시스템을 마운트하고 /etc/fstab을 갱신한다¦시스템 시간을 NTP 서버와 맞춘다¦cpio는 find 등의 출력과 함께 쓰는 아카이브 도구로 initramfs 등에 사용됩니다.
archive¦xz 로 압축된 data.tar.xz를 풀려는 명령은?¦tar -xJf data.tar.xz¦tar -xjf data.tar.xz¦tar -xzf data.tar.xz¦tar -xcf data.tar.xz¦대문자 J가 xz, 소문자 j는 bzip2이며 z는 gzip입니다. (GNU tar는 -xf로 자동 인식도 가능)
archive¦[묶기와 압축] 다음 중 옳지 않은 것은?¦tar는 압축 기능이 전혀 없어 반드시 gzip을 따로 써야 한다¦tar -xvf는 상세 출력하며 푼다¦tar -cf는 압축 없이 묶는다¦tar -czf는 gzip 압축 아카이브를 만든다¦tar는 -z, -j, -J 옵션으로 압축 도구와 함께 쓸 수 있습니다.
process¦ps aux 에서 a, u, x 옵션 의미로 옳은 것은?¦모든 사용자 프로세스, 사용자 중심 형식, 터미널 없는 프로세스 포함¦모든 터미널의 프로세스, 누적 사용 시간 표시, 실행 중 프로세스만¦자동 갱신, 사용자 이름 필터, 확장된 열 보기¦아카이브된 로그, 업타임 정보, 교환 영역 사용량¦BSD 스타일 aux는 터미널 유무와 관계없이 전체 프로세스를 사용자 정보와 함께 보여 줍니다.
process¦ps -ef 의 -e와 -f 는?¦모든 프로세스와 자세한 형식¦오류 로그만 모아서 파일 목록 형식으로¦실행 중 프로세스만 골라 필터링¦환경변수와 FIFO 목록을 함께¦-e는 모든 프로세스, -f는 UID·PPID 등을 포함한 full 형식입니다.
process¦top 실행 중 프로세스에 종료 시그널을 보내는 대화형 키는?¦k¦q¦h¦d¦k는 PID를 입력해 시그널을 보내며 q는 top 종료, d는 갱신 주기, h는 도움말입니다.
process¦kill -9 1234 와 같은 의미는?¦kill -SIGKILL 1234¦kill -SIGTERM 1234¦kill -SIGHUP 1234¦kill -SIGSTOP 1234¦9번은 SIGKILL이며 15가 SIGTERM, 1이 SIGHUP, 19가 SIGSTOP입니다.
process¦프로세스에게 설정 파일 재읽기를 요청할 때 흔히 쓰는 시그널 번호는?¦1¦9¦15¦19¦SIGHUP(1)은 많은 데몬이 재로드 용도로 처리합니다.
process¦시그널 19(SIGSTOP)과 18(SIGCONT)의 관계로 옳은 것은?¦STOP은 일시 정지, CONT는 정지된 프로세스 재개¦STOP은 정상 종료 요청, CONT는 종료된 프로세스의 재시작¦STOP은 설정 재로드, CONT는 강제 종료¦둘 다 프로세스에 종료를 요청하는 시그널이다¦Linux x86에서 SIGSTOP은 19, SIGCONT는 18입니다.
process¦kill -l 의 결과는?¦사용 가능한 시그널 목록¦프로세스가 남긴 로그 파일 목록¦모든 PID를 정렬한 목록¦종료된 프로세스의 종료 기록¦-l은 시그널 이름과 번호를 나열합니다.
process¦프로세스 이름으로 일치하는 모든 프로세스에 종료 요청을 보내는 명령은?¦killall nginx¦kill nginx¦pgrep -9 nginx¦pkill -l nginx¦killall 또는 pkill은 이름으로 시그널을 보내며 kill은 PID가 필요합니다. pgrep은 PID만 출력합니다.
process¦pgrep -u alloy sshd 의 출력은?¦alloy 소유 sshd 프로세스의 PID¦sshd 설정 파일의 경로¦alloy 계정의 로그인 기록¦sshd 서비스의 활성 상태¦pgrep은 조건에 맞는 프로세스의 PID를 출력합니다.
process¦nice -n 10 cmd 의 의미는?¦nice 값 10으로 cmd를 시작한다¦cmd를 10번 반복해서 실행한다¦cmd를 10초 뒤에 실행한다¦cmd를 PID 10번으로 시작한다¦nice 값이 클수록 우선순위가 낮습니다.
process¦일반 사용자가 nice 값을 음수로 낮추려 할 때 결과는?¦권한이 필요해 거부된다¦허용되지만 0 미만은 경고가 표시된다¦자동으로 0으로 고정되어 실행된다¦자신의 프로세스에 한해 허용된다¦nice 값을 줄여 우선순위를 높이는 것은 root 권한이 필요합니다.
process¦nice 값의 일반 범위는?¦-20에서 19¦0에서 99¦-10에서 10¦1에서 1024¦-20이 가장 높은 우선순위, 19가 가장 낮은 우선순위입니다.
process¦이미 실행 중인 PID 3000의 nice 값을 5로 바꾸려면?¦renice -n 5 -p 3000¦nice -n 5 -p 3000¦renice -p 5 -n 3000¦kill -n 5 3000¦renice는 실행 중 프로세스의 우선순위를 변경하며, nice는 새 명령을 시작할 때만 씁니다.
process¦프로세스 상태 R, S, D 중 D에 해당하는 것은?¦인터럽트 불가능한 대기¦실행 중이거나 실행 가능한 상태¦인터럽트로 깨울 수 있는 잠든 상태¦작업 제어 시그널로 정지된 상태¦D는 주로 I/O를 기다리는 uninterruptible sleep입니다.
process¦Ctrl+C로 포그라운드 프로세스에 전달되는 시그널은?¦SIGINT¦SIGTERM¦SIGQUIT¦SIGTSTP¦Ctrl+C는 SIGINT, Ctrl+Z는 SIGTSTP, Ctrl+\는 SIGQUIT입니다.
process¦[프로세스와 시그널] 다음 중 옳지 않은 것은?¦SIGKILL은 프로세스가 핸들러로 잡아 처리할 수 있다¦PID 1은 보통 init 또는 systemd다¦SIGTERM은 정상 종료를 요청한다¦nice 값이 낮을수록 우선순위가 높다¦SIGKILL과 SIGSTOP은 잡거나 무시할 수 없습니다.
jobs¦sleep 100 & 직후 셸이 출력하는 [1] 4321 에서 4321은?¦PID¦작업 번호¦PPID¦종료 코드¦대괄호 안은 작업 번호, 뒤의 숫자는 PID입니다.
jobs¦작업 번호 2번을 포그라운드로 가져오는 명령은?¦fg %2¦bg %2¦jobs %2¦kill %2¦fg는 포그라운드, %는 작업 번호 표기입니다. bg는 백그라운드 재개입니다.
jobs¦Ctrl+Z로 멈춘 작업 1번을 백그라운드에서 계속 실행하려면?¦bg %1¦fg %1¦disown %1¦kill -9 %1¦bg는 정지된 작업을 백그라운드에서 다시 실행합니다.
jobs¦jobs -l 의 출력에 추가로 보이는 것은?¦PID¦작업의 로그 파일 경로¦작업의 메모리 사용량¦작업 소유자의 암호¦-l은 작업 번호와 함께 PID를 표시합니다.
jobs¦로그아웃해도 종료되지 않도록 명령을 실행하는 형태는?¦nohup cmd &¦cmd &> /dev/null¦bg cmd¦cmd | tee out.log¦nohup은 SIGHUP을 무시하게 하며 출력은 기본으로 nohup.out에 남습니다.
jobs¦nohup 으로 실행했고 리다이렉션이 없을 때 표준 출력이 저장되는 기본 파일은?¦nohup.out¦nohup.log¦/dev/null¦out.nohup¦기본 파일은 현재 디렉터리의 nohup.out입니다.
jobs¦명령 사이에 &&를 쓰면 의미는?¦앞 명령이 성공하면 뒤 명령 실행¦앞 명령을 백그라운드로 실행하고 뒤 명령을 이어서 실행¦앞 명령이 실패했을 때에만 뒤 명령 실행¦두 명령을 파이프로 연결해 출력을 넘겨 줌¦&&는 종료 코드가 0일 때만 이어서 실행하며 실패 시 실행은 ||입니다.
jobs¦jobs 출력에서 + 와 - 기호가 의미하는 것은?¦+는 현재 작업, -는 이전 작업¦+는 실행 중인 작업, -는 정지된 작업¦+는 성공 종료한 작업, -는 실패 종료한 작업¦+는 root가 실행한 작업, -는 일반 사용자 작업¦+는 현재(기본 대상) 작업, -는 그 다음 대상 작업입니다.
jobs¦작업 3번을 셸에서 종료시키기 위한 명령은?¦kill %3¦kill 3¦stop %3¦end 3¦%3처럼 %가 있어야 작업 번호로 해석되고 숫자만 쓰면 PID로 봅니다.
jobs¦disown 의 역할은?¦셸의 작업 목록에서 작업을 제거한다¦작업을 영구적으로 삭제하고 프로세스를 종료한다¦작업을 포그라운드로 가져온다¦작업을 일시 정지한다¦disown은 작업을 셸의 관리에서 분리해 셸 종료 시 HUP을 받지 않게 합니다.
jobs¦screen 또는 tmux가 필요한 상황으로 가장 알맞은 것은?¦SSH 연결이 끊겨도 세션을 유지하며 작업하고 싶다¦파일의 소유자와 권한을 한꺼번에 바꾸고 싶다¦패키지 저장소를 추가하고 의존성을 해결하고 싶다¦디스크를 포맷하고 파일 시스템을 만들고 싶다¦터미널 멀티플렉서는 분리했다가 다시 붙을 수 있는 세션을 제공합니다.
schedule¦crontab 항목 30 4 * * 1 의 실행 시점은?¦매주 월요일 04:30¦매월 1일 04:30¦매일 04:30에서 1시간 간격으로 반복¦4월 30일 01:00¦분 30, 시 4, 요일 1(월요일)입니다.
schedule¦crontab 의 요일 필드에서 일요일을 나타내는 값은?¦0 또는 7¦1만¦6만¦8 (0은 사용 불가)¦cron에서는 0과 7 모두 일요일로 허용됩니다.
schedule¦*/10 * * * * 의 의미는?¦10분마다 실행¦매시 10분에만 실행¦10시간마다 실행¦매월 10일마다 실행¦분 필드의 */10은 0, 10, 20분처럼 10분 간격입니다.
schedule¦0 0 1 * * 의 의미는?¦매월 1일 00:00¦매주 월요일 00:00¦매일 01:00¦매년 1월 1일 00:00¦일 필드가 1이므로 매월 1일 자정입니다.
schedule¦0 9-18 * * 1-5 의 의미는?¦평일 9시부터 18시까지 매시 정각¦평일 9분부터 18분까지 매 분마다¦주말 토·일요일의 9시와 18시¦9일부터 18일까지 매일 한 번¦시 필드 9-18, 요일 필드 1-5(월~금)입니다.
schedule¦사용자 crontab의 편집 명령은?¦crontab -e¦crontab -l¦crontab -r¦crontab -i¦-e는 편집, -l은 목록, -r은 삭제입니다.
schedule¦시스템 전역 crontab 파일 /etc/crontab 에서 사용자 crontab과 다른 점은?¦명령 앞에 실행 사용자 필드가 있다¦분 필드가 없고 시 필드부터 시작한다¦요일 필드가 없고 날짜 필드까지만 있다¦한 파일에 명령을 한 개만 쓸 수 있다¦/etc/crontab과 /etc/cron.d/ 파일은 6번째 필드에 사용자명을 씁니다.
schedule¦cron 서비스 이름으로 Rocky Linux 8에서 알맞은 것은?¦crond¦cron¦cronwatch¦atd¦RHEL 계열의 cron 데몬은 crond(cronie 패키지)이며 Debian은 cron, atd는 at 작업용입니다.
schedule¦at 명령으로 예약된 대기 작업 목록을 보는 명령은?¦atq¦at -d¦crontab -l¦jobs -a¦atq는 대기 작업 큐를 표시하고 atrm은 삭제합니다.
schedule¦at 으로 10분 뒤에 명령을 실행하려는 올바른 형태는?¦at now + 10 minutes¦at +10 min cron¦at every 10 minutes¦at */10 * * * *¦at는 now + 단위 표기를 지원하며 반복은 cron이 맡습니다.
schedule¦/etc/cron.daily 와 anacron 의 관계로 알맞은 것은?¦시스템이 꺼져 있던 동안 놓친 작업을 이후에 실행할 수 있다¦초 단위의 정확한 실행 시각을 항상 보장한다¦매분 단위 반복 실행을 위한 설정이다¦at 명령으로 등록한 일회성 작업만 관리한다¦anacron은 일 단위 주기의 작업을 놓쳤을 때 다음 부팅 후 실행할 수 있게 합니다.
schedule¦[반복·예약 작업] 다음 중 옳지 않은 것은?¦crontab 항목의 시간 필드는 6개이다¦at은 일회성 작업이다¦cron은 반복 작업이다¦crontab -l은 현재 사용자 항목을 본다¦사용자 crontab은 시간 필드 5개 뒤에 명령이 옵니다.
editors¦vi 명령 모드에서 현재 줄을 복사하는 키는?¦yy¦dd¦pp¦cc¦yy는 줄 복사(yank), p는 붙여넣기, dd는 줄 삭제(잘라내기)입니다.
editors¦vi 에서 위로 방향 검색을 시작하는 키 입력은?¦?pattern¦/pattern¦:s pattern¦*pattern¦/는 아래로, ?는 위로 검색하며 n으로 다음 결과로 이동합니다.
editors¦vi에서 문서 전체에서 old를 new로 모두 바꾸는 명령은?¦:%s/old/new/g¦:s/old/new/¦:%s/old/new¦:g/old/new/¦%는 전체 줄, g는 줄 안 모든 일치 치환입니다. g가 없으면 줄마다 첫 일치만 바뀝니다.
editors¦vi 에서 줄 번호 표시를 켜는 ex 명령은?¦:set nu¦:set ro¦:set ic¦:set ai¦nu는 number 약어이며 ic는 대소문자 무시, ai는 자동 들여쓰기입니다.
editors¦vi에서 현재 줄 아래에 새 줄을 열고 입력 모드로 들어가는 키는?¦o¦O¦a¦A¦소문자 o는 아래 줄, 대문자 O는 위 줄, a는 커서 뒤입니다.
editors¦vi에서 현재 파일을 other.txt로 저장하되 종료하지 않으려는 명령은?¦:w other.txt¦:wq other.txt¦:q other.txt¦:e other.txt¦:w 파일명은 다른 이름으로 저장이며 :e는 열기입니다.
editors¦GNU nano에서 저장하는 기본 단축키는?¦Ctrl+O¦Ctrl+X¦Ctrl+S¦Ctrl+W¦Ctrl+O는 쓰기, Ctrl+X는 종료이며 Ctrl+W는 검색입니다.
editors¦vim 에서 비주얼 모드로 줄 단위 선택을 시작하는 키는?¦V¦v¦Ctrl+V¦gv¦V는 줄 선택, v는 문자 선택, Ctrl+V는 블록 선택입니다.
editors¦vi 명령 모드에서 u 키의 동작은?¦직전 변경을 되돌린다¦현재 줄 전체를 삭제한다¦현재 파일을 저장하고 종료한다¦마지막 검색을 같은 방향으로 반복한다¦u는 undo이며 검색 반복은 n입니다.
editors¦vi에서 현재 줄 끝으로 커서를 옮기는 키는?¦$¦0¦G¦^¦$는 줄 끝, 0은 줄 처음, G는 파일 마지막 줄, ^는 첫 공백 아닌 문자입니다.
editors¦vi에서 줄 끝에 이어서 입력하려고 입력 모드로 들어가는 키는?¦A¦I¦o¦O¦대문자 A는 줄 끝에서, I는 줄 처음에서 입력을 시작합니다.
rpm¦/etc/hosts 파일을 설치해 준 패키지를 알고 싶을 때 쓰는 명령은?¦rpm -qf /etc/hosts¦rpm -ql /etc/hosts¦rpm -qi /etc/hosts¦rpm -qa /etc/hosts¦-qf는 파일 경로로 그 파일이 속한 설치 패키지를 역으로 조회합니다.
rpm¦아직 설치하지 않은 foo-1.0-1.el8.x86_64.rpm 파일의 상세 정보를 보려는 명령은?¦rpm -qip foo-1.0-1.el8.x86_64.rpm¦rpm -qi foo-1.0-1.el8.x86_64.rpm¦rpm -qf foo-1.0-1.el8.x86_64.rpm¦rpm -ql foo-1.0-1.el8.x86_64¦-p 옵션을 붙여야 설치 전 패키지 파일 자체를 조회할 수 있습니다.
rpm¦rpm -Uvh 패키지.rpm의 동작으로 옳은 것은?¦미설치면 새로 설치하고 이미 설치되어 있으면 새 버전으로 업그레이드한다¦이미 설치된 패키지만 업그레이드하고 미설치 패키지는 건너뛰고 넘어간다¦설치된 패키지를 같은 버전으로 의존성 검사 없이 강제로 재설치한다¦패키지 서명과 의존성만 검사하고 실제 설치는 하지 않고 종료한다¦-U는 설치와 업그레이드를 겸하며 설치된 것만 갱신하는 옵션은 -F입니다.
rpm¦시스템에 이미 설치된 패키지만 새 버전으로 갱신하고 미설치 패키지는 설치하지 않는 옵션은?¦rpm -Fvh¦rpm -Uvh¦rpm -ivh¦rpm -evh¦-F(freshen)는 설치된 패키지만 갱신합니다.
rpm¦설치된 httpd 패키지의 파일이 설치 후 변경되었는지 검증하는 명령은?¦rpm -V httpd¦rpm -K httpd¦rpm -qc httpd¦rpm -qd httpd¦-V는 설치 당시 정보와 현재 파일의 크기·권한·해시 등을 비교합니다.
rpm¦내려받은 RPM 파일의 서명과 무결성을 확인하는 옵션은?¦rpm -K 파일.rpm¦rpm -V 파일.rpm¦rpm -qi 파일.rpm¦rpm -Uvh 파일.rpm¦-K(--checksig)는 패키지 파일의 다이제스트와 서명을 검사합니다.
rpm¦패키지 서명 확인을 위해 배포자의 GPG 공개키를 등록하는 명령은?¦rpm --import 키파일¦rpm --addkey 키파일¦rpm -K --install 키파일¦rpm -ivh 키파일¦--import로 공개키를 RPM 키링에 가져옵니다.
rpm¦httpd 패키지의 설정 파일 목록만 확인하려는 명령은?¦rpm -qc httpd¦rpm -qd httpd¦rpm -ql httpd¦rpm -qi httpd¦-qc는 설정 파일, -qd는 문서 파일 목록이며 -ql은 전체 파일 목록입니다.
rpm¦rpm -ivh 패키지.rpm --nodeps 옵션의 의미는?¦의존성 검사를 생략하고 설치한다¦의존 패키지를 저장소에서 자동으로 받아 함께 설치한다¦패키지 GPG 서명 검사를 건너뛰고 설치한다¦설치는 하되 의존 관계를 RPM DB에 기록하지 않는다¦--nodeps는 의존성 검사를 하지 않으므로 실행 시 문제가 생길 수 있습니다.
rpm¦/usr/bin/dig 파일을 제공하는 패키지를 저장소에서 검색하려는 명령은?¦dnf provides /usr/bin/dig¦rpm -qf /usr/bin/dig¦dnf search /usr/bin/dig¦dnf info /usr/bin/dig¦dnf provides는 설치 여부와 무관하게 저장소 메타데이터에서 해당 파일의 제공 패키지를 찾습니다.
rpm¦dnf로 이전에 수행한 설치·삭제 작업 이력을 확인하는 명령은?¦dnf history¦dnf repolist¦dnf list installed¦dnf check-update¦dnf history는 트랜잭션 ID별 작업 내역을 보여 주며 undo로 되돌릴 수도 있습니다.
rpm¦비활성화된 저장소까지 모두 표시하는 명령은?¦dnf repolist --all¦dnf repolist¦dnf repolist --enabled¦dnf repoinfo¦기본 repolist는 활성 저장소만 보여 주고 --all을 붙이면 비활성도 나옵니다.
rpm¦Rocky Linux 8에서 개별 저장소 정의 파일이 위치하는 기본 디렉터리는?¦/etc/yum.repos.d/¦/etc/dnf/repos/¦/var/lib/rpm/¦/var/cache/dnf/¦저장소는 /etc/yum.repos.d/*.repo에 정의하고 /var/lib/rpm은 RPM 데이터베이스입니다.
rpm¦RPM 데이터베이스(설치된 패키지 정보)가 저장되는 기본 경로는?¦/var/lib/rpm¦/etc/rpm¦/var/cache/dnf¦/usr/lib/rpm¦설치 이력과 메타데이터는 /var/lib/rpm에 저장됩니다.
rpm¦dnf에 대한 설명 중 옳지 않은 것은?¦dnf install은 로컬 .rpm 파일 경로를 인자로 줄 수 없고 저장소 패키지만 설치한다¦저장소에서 의존성을 자동으로 해결해 필요한 패키지를 함께 설치한다¦dnf remove로 설치된 패키지를 제거할 수 있고 불필요해진 의존 패키지도 정리된다¦dnf update와 dnf upgrade는 Rocky Linux 8에서 같은 동작을 한다¦dnf install ./파일.rpm처럼 로컬 파일 설치도 가능하며 의존성은 저장소에서 해결합니다.
rpm¦rpm -q httpd 결과가 httpd-2.4.37-47.el8.x86_64일 때 47이 의미하는 것은?¦릴리즈 번호¦업스트림 버전¦CPU 아키텍처¦에포크¦이름-버전-릴리즈.아키텍처 구조에서 47은 패키저가 부여한 릴리즈입니다.
debian¦Debian 계열에서 설치된 패키지의 목록을 보는 명령은?¦dpkg -l¦dpkg -L¦dpkg -S¦apt-cache search¦-l은 설치 상태 목록, -L은 특정 패키지의 파일 목록입니다.
debian¦Debian 계열에서 설치된 openssh-server가 설치한 파일 목록을 보는 명령은?¦dpkg -L openssh-server¦dpkg -S openssh-server¦dpkg -l openssh-server¦apt-cache show openssh-server¦-L은 rpm -ql에 대응하는 패키지별 설치 파일 목록 조회입니다.
debian¦/bin/ls 파일이 어느 패키지에 속하는지 찾는 Debian 계열 명령은?¦dpkg -S /bin/ls¦dpkg -L /bin/ls¦dpkg -r /bin/ls¦apt-cache depends /bin/ls¦-S는 rpm -qf와 대응하여 파일의 소속 패키지를 찾습니다.
debian¦패키지를 설정 파일까지 완전히 삭제하는 dpkg 옵션은?¦dpkg -P¦dpkg -r¦dpkg -i¦dpkg -s¦-r은 설정 파일을 남기고 제거하며 -P(purge)는 설정 파일까지 지웁니다.
debian¦패키지의 설명·버전·의존성 등 상세 정보를 저장소 기준으로 보는 명령은?¦apt-cache show 패키지¦dpkg -L 패키지¦apt-get update 패키지¦dpkg -S 패키지¦apt-cache show는 저장소 메타데이터의 상세 정보를 출력합니다.
debian¦dpkg -i 설치 중 의존성 문제로 깨진 상태를 바로잡는 명령은?¦apt-get install -f¦apt-get clean¦dpkg -P -f¦apt-cache policy¦-f(--fix-broken)는 누락된 의존 패키지를 설치해 상태를 고칩니다.
debian¦APT가 사용하는 저장소 목록의 기본 설정 파일은?¦/etc/apt/sources.list¦/etc/yum.repos.d/base.repo¦/etc/dpkg/dpkg.cfg¦/var/lib/dpkg/status¦sources.list와 sources.list.d 아래 파일이 저장소를 정의합니다.
debian¦apt-get upgrade와 달리 필요하면 의존성 변화에 따라 패키지를 추가 설치·제거하며 업그레이드하는 명령은?¦apt-get dist-upgrade¦apt-get update¦apt-get autoclean¦apt-get install -f¦dist-upgrade는 의존성 변화에 맞춰 패키지 설치·제거까지 처리합니다.
debian¦더 이상 필요하지 않은 자동 설치 의존 패키지를 정리하는 명령은?¦apt-get autoremove¦apt-get clean¦dpkg -P¦apt-get update¦autoremove는 다른 패키지가 쓰지 않는 자동 설치 패키지를 제거합니다.
debian¦dpkg -i 와 apt install 의 큰 차이로 옳은 것은?¦apt는 저장소에서 의존 패키지를 자동으로 받아 함께 설치한다¦dpkg는 항상 의존 패키지를 저장소에서 자동으로 내려받아 설치한다¦apt는 로컬에 있는 .deb 파일은 어떤 경우에도 설치할 수 없다¦dpkg는 root 권한 없이도 시스템 패키지를 설치할 수 있다¦dpkg는 저장소를 조회하지 않아 의존성을 직접 해결해야 합니다.
debian¦Debian 계열에서 패키지의 설치 상태 정보를 조회하는 옵션은?¦dpkg -s 패키지¦dpkg -S 패키지¦dpkg -r 패키지¦dpkg -c 패키지¦소문자 -s는 상태 정보, 대문자 -S는 파일 소속 패키지 검색입니다.
debian¦/var/cache/apt/archives 에 쌓인 내려받은 .deb 파일을 삭제하는 명령은?¦apt-get clean¦apt-get update¦apt-get autoremove¦dpkg -P¦clean은 로컬 캐시의 패키지 파일을 삭제합니다.
debian¦Debian 계열 패키지 관리 설명 중 옳지 않은 것은?¦dpkg -l은 저장소의 설치 가능한 전체 패키지를 내려받아 설치한다¦apt update는 저장소의 패키지 목록 정보를 최신 상태로 갱신한다¦dpkg -r은 패키지를 제거하되 설정 파일은 시스템에 그대로 남긴다¦dpkg -L은 지정한 패키지가 설치한 파일의 목록을 보여 준다¦dpkg -l은 로컬에 알려진 패키지 상태 목록을 보여 줄 뿐 내려받지 않습니다.
debian¦dpkg가 설치된 패키지 상태 정보를 보관하는 디렉터리는?¦/var/lib/dpkg¦/etc/apt¦/var/cache/apt¦/usr/share/dpkg¦패키지 상태 파일과 정보는 /var/lib/dpkg에 있습니다.
source¦./configure 스크립트가 하는 일로 알맞은 것은?¦빌드 환경을 점검하고 Makefile을 생성한다¦소스를 컴파일해 실행 파일과 오브젝트 파일을 만든다¦만들어진 실행 파일을 시스템 디렉터리에 복사한다¦압축된 소스 아카이브를 현재 디렉터리에 해제한다¦configure는 환경 점검 후 Makefile을 만들며 컴파일은 make가 합니다.
source¦make install 단계에서 일어나는 일은?¦빌드한 결과물을 설치 경로로 복사한다¦Makefile을 환경에 맞게 새로 생성한다¦소스 아카이브를 해제해 빌드 디렉터리를 만든다¦오브젝트 파일을 삭제해 소스 트리를 정리한다¦install 목표가 실행 파일 등을 지정된 경로에 설치합니다.
source¦foo-1.0.tar.bz2 소스를 해제하는 명령은?¦tar xjf foo-1.0.tar.bz2¦tar xzf foo-1.0.tar.bz2¦tar xJf foo-1.0.tar.bz2¦tar cjf foo-1.0.tar.bz2¦j는 bzip2, z는 gzip, J는 xz 형식에 쓰이며 x는 해제입니다.
source¦bar-2.3.tar.xz 소스를 해제하는 명령은?¦tar xJf bar-2.3.tar.xz¦tar xjf bar-2.3.tar.xz¦tar xzf bar-2.3.tar.xz¦tar tf bar-2.3.tar.xz¦대문자 J가 xz 압축에 대응합니다.
source¦--prefix 옵션 없이 소스를 기본 설정으로 빌드해 설치할 때 흔히 쓰이는 기본 설치 경로는?¦/usr/local¦/usr/share¦/opt/src¦/var/lib¦많은 autotools 기반 소스는 기본 prefix가 /usr/local입니다.
source¦make clean의 역할은?¦빌드 과정에서 생성된 오브젝트 파일 등을 삭제한다¦설치된 프로그램을 시스템에서 모두 제거한다¦configure 설정을 초기화하고 소스를 배포용으로 되돌린다¦패키지 의존성을 점검한 뒤 필요한 것을 재설치한다¦clean은 빌드 산출물을 정리하며 설치 제거는 uninstall 목표의 몫입니다.
source¦소스 빌드 중 configure가 C compiler를 찾지 못한다는 오류를 낼 때 조치는?¦gcc 등 개발 도구를 설치한다¦make install을 먼저 실행해 본다¦rpm -e make 로 make를 제거한다¦/etc/fstab 의 컴파일 옵션을 수정한다¦컴파일러가 없으면 gcc와 make 등 개발 도구를 설치해야 합니다.
source¦make install을 보통 root 권한으로 실행하는 이유는?¦시스템 디렉터리에 파일을 써야 하기 때문이다¦컴파일러는 root 계정에서만 동작하기 때문이다¦Makefile이 root 소유 파일이어야 하기 때문이다¦tar 아카이브 해제에 root 권한이 필요하기 때문이다¦/usr/local 같은 시스템 경로에 설치하려면 쓰기 권한이 필요합니다.
source¦make -j4 옵션의 의미는?¦동시에 최대 4개 작업으로 병렬 빌드한다¦같은 빌드를 4번 반복해서 수행한다¦Makefile의 4번째 목표만 골라 빌드한다¦로그를 4단계 수준으로 상세히 출력한다¦-j는 병렬 작업 수를 지정해 빌드 시간을 줄입니다.
source¦소스로 설치한 프로그램을 제거하기 위해 확인해야 할 것은?¦Makefile에 uninstall 목표가 있는지¦rpm -e 로 항상 깨끗하게 제거되는지¦dnf remove 가 설치 파일을 자동으로 추적하는지¦/etc/yum.repos.d 에 해당 소스가 등록되어 있는지¦패키지 DB에 없으므로 make uninstall 제공 여부나 설치 파일 목록을 따로 확인해야 합니다.
source¦소스 트리에 diff로 만든 패치 파일 fix.patch를 적용하는 명령은?¦patch -p1 < fix.patch¦diff -p1 fix.patch¦make patch fix.patch¦tar xf fix.patch¦patch 명령이 패치 파일을 읽어 소스를 수정합니다.
source¦소스 설치에 대한 설명 중 옳지 않은 것은?¦make install로 설치한 프로그램은 rpm -qa 목록에 항상 나타난다¦configure의 옵션으로 설치 경로(prefix)를 지정할 수 있다¦빌드에는 컴파일러와 make 등 개발 도구가 필요하다¦설치 후 제거 방법을 직접 관리해야 할 수 있다¦소스 설치는 RPM DB에 등록되지 않으므로 rpm -qa로 조회되지 않습니다.
devices¦시스템의 PCI 버스에 연결된 네트워크 카드·그래픽 카드 등을 조회하는 명령은?¦lspci¦lsusb¦lsblk¦lsmod¦lspci는 PCI 장치, lsusb는 USB 장치 조사 명령입니다.
devices¦/dev/sda3 장치 이름의 의미로 옳은 것은?¦첫 번째 SCSI/SATA 디스크의 세 번째 파티션¦세 번째 SCSI/SATA 디스크의 첫 번째 파티션¦첫 번째 NVMe 디스크의 세 번째 네임스페이스¦세 번째로 연결된 USB 저장 장치 전체¦sd 다음 알파벳이 디스크, 숫자가 파티션 번호입니다.
devices¦첫 번째 NVMe 디스크의 두 번째 파티션을 나타내는 장치 이름은?¦/dev/nvme0n1p2¦/dev/nvme0p2¦/dev/nvme1n0p2¦/dev/nvme0n2¦NVMe는 컨트롤러 nvme0, 네임스페이스 n1, 파티션 p2 형식입니다.
devices¦의존 모듈까지 고려해서 커널 모듈을 적재하는 명령은?¦modprobe 모듈명¦insmod 모듈명.ko¦lsmod 모듈명¦depmod 모듈명¦modprobe는 의존성을 해석하지만 insmod는 지정한 파일만 적재합니다.
devices¦사용자 정의 udev 규칙을 두는 디렉터리는?¦/etc/udev/rules.d¦/etc/modprobe.d¦/dev/udev¦/etc/sysconfig/udev¦시스템 관리자가 만든 udev 규칙은 /etc/udev/rules.d에 둡니다.
devices¦읽으면 0x00 바이트가 계속 나오지만 쓴 데이터는 그냥 버려지는 특수 장치 파일은?¦/dev/zero¦/dev/null¦/dev/random¦/dev/urandom¦/dev/null은 읽으면 즉시 EOF이고 /dev/zero는 널 바이트를 무한히 공급합니다.
devices¦ls -l 출력이 brw-rw---- 1 root disk 8, 0 ... /dev/sda 일 때 맨 앞의 b가 뜻하는 것은?¦블록 장치 파일¦문자 장치 파일¦심볼릭 링크 파일¦바이너리 실행 파일¦b는 블록 장치, c는 문자 장치를 나타냅니다.
devices¦블록 장치별 파일시스템 종류와 UUID를 함께 보려는 명령은?¦lsblk -f¦lspci -v¦lsusb -v¦lsmod -f¦lsblk -f는 파일시스템 유형·레이블·UUID 등을 트리로 표시합니다.
devices¦현재 사용 중인 IRQ 번호와 할당 장치를 확인하는 파일은?¦/proc/interrupts¦/proc/ioports¦/proc/devices¦/proc/dma¦/proc/interrupts가 IRQ별 인터럽트 현황을 보여 줍니다.
devices¦장치가 사용하는 I/O 포트 주소 범위를 확인하는 파일은?¦/proc/ioports¦/proc/interrupts¦/proc/iomem¦/proc/dma¦ioports는 I/O 포트, iomem은 메모리 매핑 주소 영역입니다.
devices¦USB 메모리를 꽂은 뒤 새 디스크 이름과 파티션을 확인하는 데 알맞은 명령은?¦lsblk¦lsmod¦lspci¦lpstat¦lsblk는 블록 장치와 파티션 구성을 표시합니다.
devices¦장치 이름에 대한 설명 중 옳지 않은 것은?¦/dev/sda1은 두 번째 디스크의 첫 번째 파티션이다¦/dev/sdb2는 두 번째 디스크의 두 번째 파티션이다¦/dev/null은 문자 장치 파일이다¦/dev/nvme0n1p1은 NVMe 디스크의 파티션이다¦sda는 첫 번째 디스크이므로 sda1은 첫 번째 디스크의 첫 파티션입니다.
devices¦특정 커널 모듈이 자동으로 적재되지 않도록 blacklist를 쓰는 위치는?¦/etc/modprobe.d/*.conf¦/etc/modules-load.d/*.conf¦/etc/udev/rules.d/*.rules¦/etc/sysconfig/network¦modprobe.d에 blacklist를 두고 modules-load.d는 부팅 시 적재할 모듈 목록입니다.
printing¦기본 프린터가 무엇인지 확인하는 명령은?¦lpstat -d¦lpstat -o¦lpq -a¦lprm -d¦lpstat -d는 시스템 기본 목적지를 표시합니다.
printing¦lpr 명령에서 출력할 프린터를 지정하는 옵션은?¦-P¦-d¦-p¦-n¦lpr는 -P 프린터, lp는 -d 프린터를 사용합니다.
printing¦lp로 report.txt를 3부 인쇄하려는 명령은?¦lp -n 3 report.txt¦lp -c 3 report.txt¦lp -d 3 report.txt¦lpr -P 3 report.txt¦lp의 -n은 복사 매수이며 -c는 복사본 스풀링, -d는 프린터 지정입니다.
printing¦lpq 출력에 active alloy 12 report.pdf 가 나올 때 이 작업을 취소하는 명령은?¦lprm 12¦lpr 12¦lpq -a 12¦lpstat -c 12¦lprm에 작업 번호를 주어 대기 또는 진행 중 작업을 취소합니다.
printing¦CUPS의 주 서버 설정 파일은?¦/etc/cups/cupsd.conf¦/etc/printcap¦/etc/lp.conf¦/etc/cups.conf¦cupsd.conf에 서버 동작을 설정하며 printcap은 전통적 LPD 방식입니다.
printing¦CUPS 웹 관리 인터페이스에 접속하는 기본 포트는?¦631¦515¦9100¦80¦CUPS는 IPP를 위해 631을 쓰고 515는 LPD, 9100은 raw 인쇄 포트입니다.
printing¦Rocky Linux 8에서 CUPS 서비스를 재시작하는 명령은?¦systemctl restart cups¦systemctl restart lpd¦systemctl restart cupsd.conf¦systemctl restart lprd¦CUPS의 systemd 서비스 이름은 cups입니다.
printing¦CUPS가 기본으로 사용하는 인쇄 프로토콜은?¦IPP¦LPD¦SMTP¦SNMP¦IPP(Internet Printing Protocol)는 HTTP 위에서 동작하는 CUPS의 기본 프로토콜입니다.
printing¦PPD 파일은 무엇을 기술하는가?¦프린터의 기능과 옵션¦프린터의 IP 주소와 접속 포트 번호¦인쇄 문서의 페이지 크기와 여백 설정¦프린터 접근이 허용된 사용자 목록¦PPD는 PostScript Printer Description으로 프린터별 기능과 옵션 정보를 담습니다.
printing¦CUPS가 인쇄 작업 데이터를 임시로 저장하는 스풀 디렉터리는?¦/var/spool/cups¦/var/log/cups¦/etc/cups¦/usr/share/cups¦스풀은 /var/spool/cups, 로그는 /var/log/cups에 둡니다.
printing¦인쇄 명령 설명 중 옳지 않은 것은?¦lpq는 프린터에 새 인쇄 작업을 제출한다¦lpr는 파일을 프린터에 인쇄 작업으로 제출한다¦lprm은 대기열의 인쇄 작업을 삭제한다¦lpstat은 프린터와 작업 상태를 보여 준다¦lpq는 대기열을 조회하며 제출은 lp 또는 lpr가 합니다.
printing¦프린터 상태를 목록으로 확인하는 명령은?¦lpstat -p¦lpstat -o¦lpq -P¦lprm -p¦lpstat -p는 프린터 상태, -o는 출력 작업 목록입니다.
xwindow¦DISPLAY=192.168.0.5:0 이 의미하는 것은?¦192.168.0.5 호스트의 0번 디스플레이 X 서버에 연결¦192.168.0.5 호스트의 포트 0번으로 SSH 접속¦192.168.0.5 호스트를 프린터 서버로 지정¦192.168.0.5 호스트의 0번 사용자 세션을 종료¦호스트:디스플레이번호 형식으로 X 서버 위치를 지정합니다.
xwindow¦원격 호스트의 X 클라이언트가 내 X 서버를 사용하도록 허용하는 명령은?¦xhost +192.168.0.10¦xrandr 192.168.0.10¦xdpyinfo 192.168.0.10¦xev 192.168.0.10¦xhost는 X 서버 접근 허용 호스트를 관리합니다.
xwindow¦X 환경에서 해상도와 모니터 출력 설정을 조회하거나 변경하는 명령은?¦xrandr¦xhost¦xev¦xdpyinfo¦xrandr는 해상도·회전·출력 장치를 설정합니다.
xwindow¦X 창에서 키보드와 마우스 이벤트를 출력해 확인하는 도구는?¦xev¦xhost¦xrandr¦xauth¦xev는 창 위에서 발생하는 X 이벤트를 보여 줍니다.
xwindow¦Xorg 서버의 추가 설정 조각 파일을 두는 일반적 디렉터리는?¦/etc/X11/xorg.conf.d/¦/etc/xorg/display.d/¦/etc/gdm/xorg/¦/usr/share/X11/dpy.d/¦xorg.conf.d는 분리된 설정 조각, 메인은 /etc/X11/xorg.conf입니다.
xwindow¦원격 서버의 GUI 프로그램 창을 내 PC에 표시하도록 SSH 터널을 만드는 옵션은?¦ssh -X user@host¦ssh -L user@host¦ssh -D user@host¦ssh -R user@host¦-X는 X11 포워딩이며 -L, -R, -D는 포트 전달 방식입니다.
xwindow¦그래픽 로그인 화면을 제공하고 세션을 시작해 주는 구성 요소는?¦디스플레이 매니저¦윈도 매니저¦터미널 에뮬레이터¦X 클라이언트 라이브러리¦GDM, SDDM, LightDM이 디스플레이 매니저이며 윈도 매니저는 창 관리를 합니다.
xwindow¦윈도 매니저가 아닌 것은?¦GDM¦Openbox¦Fluxbox¦twm¦GDM은 로그인을 담당하는 디스플레이 매니저입니다.
xwindow¦startx가 사용자 X 세션 시작 때 읽는 대표 사용자 파일은?¦~/.xinitrc¦~/.bashrc¦~/.xsession-errors¦~/.Xdefaults.d¦startx는 xinit을 통해 ~/.xinitrc에 지정된 클라이언트를 실행합니다.
xwindow¦DISPLAY=:1 일 때 TCP로 연결하는 X 서버의 기본 포트는?¦6001¦6000¦6010¦7001¦X 서버의 TCP 포트는 6000에 디스플레이 번호를 더합니다.
xwindow¦X11을 대체하기 위해 설계된 현대적 디스플레이 프로토콜은?¦Wayland¦Mesa¦Cairo¦GTK¦Wayland는 컴포지터가 클라이언트와 직접 통신하는 프로토콜이며 GTK는 위젯 툴킷입니다.
xwindow¦텍스트 콘솔에서 GUI 프로그램 실행 시 Cannot open display 오류가 나는 가장 가능한 원인은?¦DISPLAY가 비어 있거나 접속할 X 서버가 없다¦윈도 매니저 패키지가 시스템에 설치되어 있지 않다¦GDM 디스플레이 매니저가 동시에 두 개 실행 중이다¦/etc/X11/xorg.conf 파일의 권한이 644가 아니다¦클라이언트가 접속할 X 서버 위치를 알 수 없을 때 이 오류가 납니다.
desktop¦KDE Plasma가 기반으로 하는 GUI 툴킷은?¦Qt¦GTK¦Tk¦Motif¦GNOME은 GTK, KDE는 Qt 기반입니다.
desktop¦경량 데스크톱 환경으로 알려진 것은?¦Xfce¦GDM¦LightDM¦Openbox¦GDM과 LightDM은 디스플레이 매니저, Openbox는 윈도 매니저입니다.
desktop¦KDE 환경에서 흔히 쓰는 디스플레이 매니저는?¦SDDM¦GDM¦Kate¦Dolphin¦SDDM은 KDE 계열, GDM은 GNOME 계열 디스플레이 매니저입니다.
desktop¦Rocky Linux 8에서 부팅 시 그래픽 로그인 화면이 기본으로 나오도록 설정하는 명령은?¦systemctl set-default graphical.target¦systemctl set-default multi-user.target¦systemctl isolate rescue.target¦systemctl enable gdm.target¦graphical.target이 GUI 로그인을 포함하는 기본 타깃입니다.
desktop¦SysV 런레벨 5에 대응하는 systemd 타깃은?¦graphical.target¦multi-user.target¦rescue.target¦poweroff.target¦런레벨 3은 multi-user, 5는 graphical, 1은 rescue에 대응합니다.
desktop¦Rocky Linux 8 최소 설치 서버에 GUI를 설치할 때 쓰는 명령은?¦dnf groupinstall "Server with GUI"¦dnf install gui-server gnome-shell¦dnf groupinstall "Development Tools"¦dnf install xorg-x11-utils xterm¦환경 그룹을 설치해야 GNOME 등 GUI 구성이 한꺼번에 들어옵니다.
desktop¦GNOME의 디스플레이 매니저인 GDM의 설정 파일은?¦/etc/gdm/custom.conf¦/etc/sddm.conf¦/etc/lightdm/lightdm.conf¦/etc/X11/Xwrapper.config¦GDM 설정은 /etc/gdm/custom.conf에 둡니다.
desktop¦데스크톱 메뉴에 응용프로그램 항목을 정의하는 파일 형식과 대표 위치는?¦.desktop 파일, /usr/share/applications¦.service 파일, /etc/systemd/system¦.repo 파일, /etc/yum.repos.d¦.rules 파일, /etc/udev/rules.d¦.desktop 파일이 실행기 이름·명령·아이콘을 정의합니다.
desktop¦LibreOffice Impress의 용도는?¦프레젠테이션 제작¦스프레드시트 작업¦데이터베이스 관리¦수식 편집¦Writer는 문서, Calc는 표 계산, Impress는 프레젠테이션, Base는 DB, Math는 수식입니다.
desktop¦벡터 그래픽 편집에 쓰는 오픈소스 프로그램은?¦Inkscape¦GIMP¦Thunderbird¦Evolution¦GIMP는 래스터 이미지 편집, Inkscape는 벡터 편집입니다.
desktop¦Mozilla 계열의 전자우편 클라이언트는?¦Thunderbird¦Firefox¦Nautilus¦Totem¦Firefox는 웹 브라우저, Thunderbird는 메일 클라이언트입니다.
desktop¦KDE의 기본 파일 관리자는?¦Dolphin¦Nautilus¦Thunar¦Konsole¦Nautilus는 GNOME, Thunar는 Xfce, Konsole은 KDE 터미널입니다.
network¦TCP 연결 설정의 3-way handshake 순서는?¦SYN → SYN+ACK → ACK¦SYN → ACK → FIN¦ACK → SYN+ACK → SYN¦SYN → SYN → ACK¦클라이언트 SYN, 서버 SYN+ACK, 클라이언트 ACK 순으로 연결이 성립합니다.
network¦ICMP echo 요청과 응답을 이용해 대상 호스트의 도달 여부를 확인하는 명령은?¦ping¦nslookup¦ssh¦curl¦ping은 ICMP echo request/reply를 사용하고 나머지는 DNS나 TCP 기반 응용 연결을 쓴다.
network¦목적지까지 거치는 라우터(홉) 경로를 추적하는 명령은?¦traceroute¦nslookup¦netstat -i¦hostname -I¦traceroute는 TTL을 증가시키며 경유 라우터를 표시합니다.
network¦[네트워크의 개념] 다음 중 옳지 않은 설명은?¦UDP는 데이터를 보내기 전에 3-way handshake로 연결을 먼저 설정한다¦TCP는 순서 번호와 재전송으로 신뢰성 있는 전송을 제공한다¦DNS 일반 질의는 주로 UDP 53번 포트로 전달된다¦ICMP는 오류 보고와 진단 메시지를 전달하는 데 쓰인다¦UDP는 비연결형이므로 handshake 없이 데이터그램을 보냅니다.
network¦L2 스위치가 프레임을 전달할 때 참조하는 주소는?¦MAC 주소¦TCP 포트 번호¦호스트 이름¦사용자 UID¦스위치는 데이터링크 계층에서 MAC 주소 테이블로 프레임을 전달합니다.
network¦OSI 4계층(전송 계층)에 해당하는 프로토콜 쌍은?¦TCP, UDP¦IP, ICMP¦HTTP, SMTP¦Ethernet, ARP¦IP·ICMP는 3계층, HTTP·SMTP는 7계층, Ethernet은 2계층 계열입니다.
network¦ARP의 역할은?¦IP 주소를 MAC 주소로 변환¦호스트 이름을 IP로 변환¦IP 주소를 자동 할당¦MAC 주소를 호스트 이름으로 변환¦ARP는 같은 링크에서 IP에 대응하는 MAC 주소를 찾습니다.
network¦TCP/IP 4계층 모델에서 IP가 속하는 계층은?¦인터넷 계층¦전송 계층¦응용 계층¦네트워크 접근 계층¦IP는 인터넷 계층이며 TCP·UDP는 전송 계층입니다.
network¦기본 게이트웨이의 역할로 가장 알맞은 것은?¦다른 네트워크로 가는 패킷을 전달하는 라우터¦호스트 이름을 IP 주소로 바꿔 주는 이름 서버¦IP 주소와 서브넷 마스크를 자동으로 배정하는 서버¦같은 서브넷 안의 IP와 MAC 주소 대응을 저장하는 장치¦목적지가 다른 네트워크이면 호스트는 기본 게이트웨이로 패킷을 보냅니다.
network¦NIC와 별개로 로컬 TCP/IP 스택이 동작하는지 점검하려는 상황에서 알맞은 명령은?¦ping 127.0.0.1¦ping 255.255.255.255¦ping 169.254.0.0¦ping 10.255.255.255¦127.0.0.1은 루프백 주소로 자기 호스트의 IP 스택을 확인합니다.
network¦Linux에서 ping을 4회만 보내고 끝내려는 옵션 사용은?¦ping -c 4 대상¦ping -n 4 대상¦ping -w 4 대상¦ping -s 4 대상¦Linux ping은 -c가 횟수이고 -w는 전체 제한 시간(초), -n은 숫자 출력, -s는 패킷 크기입니다.
network¦ping 결과가 "4 packets transmitted, 0 received, 100% packet loss"일 때의 해석으로 알맞은 것은?¦ICMP 응답을 받지 못했으므로 경로·방화벽·대상 상태를 점검해야 한다¦네 패킷 모두 정상적으로 도착해 왕복 시간이 측정되었다¦DNS 서버의 장애가 원인임이 확정되어 이름 해석부터 고쳐야 한다¦대상 호스트의 80번 포트만 닫혀 있어서 생긴 결과이다¦0개 수신은 ICMP 응답 부재이며 원인은 경로, 차단, 대상 다운 등 다양합니다.
network¦일반적으로 UDP를 기본 전송 프로토콜로 사용하는 것은?¦DNS 일반 질의¦SSH 세션¦SMTP 메일 전송¦FTP 제어 연결¦SSH·SMTP·FTP 제어는 TCP를 쓰고 일반 DNS 질의는 UDP 53을 씁니다.
network¦Well-known 포트의 번호 범위는?¦0~1023¦1~255¦1024~49151¦49152~65535¦0~1023이 Well-known, 1024~49151이 등록 포트, 그 위는 동적 포트입니다.
address¦IPv4 /26 네트워크에서 사용 가능한 호스트 주소 수는?¦62¦64¦30¦126¦호스트 비트 6개이므로 2^6 - 2 = 62입니다.
address¦서브넷 마스크 255.255.255.224의 접두어 길이는?¦/27¦/26¦/28¦/25¦224 = 11100000이므로 24 + 3 = 27비트입니다.
address¦192.168.10.77/26 호스트가 속한 네트워크 주소는?¦192.168.10.64¦192.168.10.0¦192.168.10.72¦192.168.10.76¦/26은 블록 크기가 64이므로 77은 64~127 블록에 속해 네트워크 주소는 .64입니다.
address¦192.168.10.77/26 호스트가 속한 서브넷의 브로드캐스트 주소는?¦192.168.10.127¦192.168.10.255¦192.168.10.126¦192.168.10.191¦블록 64~127에서 마지막 주소 64 + 64 - 1 = 127이 브로드캐스트입니다.
address¦10.1.1.130/25 호스트가 속한 서브넷의 브로드캐스트 주소는?¦10.1.1.255¦10.1.1.127¦10.1.1.129¦10.1.1.254¦/25는 블록 크기 128이므로 130은 128~255 블록이고 마지막 주소 255가 브로드캐스트입니다.
address¦/28 접두어에 해당하는 서브넷 마스크는?¦255.255.255.240¦255.255.255.248¦255.255.255.224¦255.255.255.252¦/28은 24 + 4비트이므로 마지막 옥텟 11110000 = 240입니다.
address¦172.16.5.200/27 호스트가 속한 네트워크 주소는?¦172.16.5.192¦172.16.5.160¦172.16.5.200¦172.16.5.224¦/27 블록 크기가 32이므로 200은 192~223 블록(32 x 6 = 192)에 속합니다.
address¦다음 중 사설 IPv4 주소가 아닌 것은?¦192.169.10.1¦10.200.3.4¦172.31.255.254¦192.168.100.5¦사설 대역은 10/8, 172.16~172.31, 192.168/16이며 192.169는 공인 대역입니다.
address¦192.168.1.130/26 호스트와 같은 서브넷에 속하는 주소는?¦192.168.1.190¦192.168.1.100¦192.168.1.200¦192.168.1.127¦/26 블록 128~191에 130과 190이 함께 속하며 127은 앞 블록, 200은 다음 블록입니다.
address¦DHCP 서버를 찾지 못한 클라이언트가 스스로 할당하는 링크 로컬 IPv4 대역은?¦169.254.0.0/16¦127.0.0.0/8¦224.0.0.0/4¦100.64.0.0/10¦APIPA 또는 링크 로컬 주소는 169.254.0.0/16입니다.
address¦2001:0db8:0000:0000:0000:0000:0000:0001을 올바르게 축약한 것은?¦2001:db8::1¦2001:db8:::1¦2001:db8::1::¦2001:db8:0:1¦연속된 0 그룹은 :: 로 한 번만 줄일 수 있고 앞자리 0도 생략합니다.
address¦IPv6 루프백 주소는?¦::1¦::¦fe80::1¦ff02::1¦::1은 루프백, ::은 미지정, fe80::/10은 링크 로컬, ff02::1은 링크 로컬 전체 노드 멀티캐스트입니다.
address¦IPv6 링크 로컬 주소의 대역은?¦fe80::/10¦fc00::/7¦ff00::/8¦2001:db8::/32¦fc00::/7은 ULA, ff00::/8은 멀티캐스트, 2001:db8::/32는 문서용입니다.
address¦클래스 B 범위(128~191)에 속하는 주소는?¦150.10.1.1¦192.168.1.1¦10.0.0.1¦224.0.0.5¦첫 옥텟 128~191이 B, 192~223이 C, 1~126이 A, 224~239가 D입니다.
address¦/30 네트워크에서 사용 가능한 호스트 주소 수는?¦2¦4¦6¦1¦호스트 비트 2개이므로 2^2 - 2 = 2입니다.
netconfig¦Rocky Linux 8에서 NetworkManager가 인식한 장치의 상태를 한눈에 보는 명령은?¦nmcli device status¦nmcli radio all¦nmcli general logging¦ip route get¦nmcli device status는 장치 이름, 유형, 상태, 연결 이름을 보여 줍니다.
netconfig¦NetworkManager에 저장된 연결 프로파일 목록을 보는 명령은?¦nmcli connection show¦nmcli device wifi list¦nmcli general hostname¦nmcli networking off¦connection show는 연결 프로파일과 활성 여부를 나열합니다.
netconfig¦nmcli로 ens160 연결에 고정 IPv4 주소 192.168.1.10/24를 설정하는 명령은?¦nmcli con mod ens160 ipv4.addresses 192.168.1.10/24 ipv4.method manual¦nmcli con mod ens160 ipv4.address 192.168.1.10/24 ipv4.method static¦nmcli con add ens160 ipv4.ip 192.168.1.10 ipv4.mask 24 method manual¦nmcli dev set ens160 ipv4.addresses 192.168.1.10/24 ipv4.method manual¦속성명은 ipv4.addresses이고 고정이면 ipv4.method를 manual로 지정합니다(static은 값이 아님).
netconfig¦Rocky Linux 8에서 ens160 인터페이스의 전통적 설정 파일 위치는?¦/etc/sysconfig/network-scripts/ifcfg-ens160¦/etc/network/interfaces.d/ens160.cfg¦/etc/netplan/50-cloud-init-ens160.yaml¦/etc/NetworkManager/ens160.conf¦RHEL 계열은 ifcfg-* 파일을 쓰고 interfaces는 Debian, netplan은 Ubuntu 계열입니다.
netconfig¦Debian 계열의 전통적인 네트워크 인터페이스 설정 파일은?¦/etc/network/interfaces¦/etc/sysconfig/network¦/etc/resolv.conf¦/etc/sysconfig/network-scripts/ifcfg-eth0¦Debian은 ifupdown 방식으로 /etc/network/interfaces를 사용합니다.
netconfig¦호스트 이름을 web01로 영구 변경하는 명령은?¦hostnamectl set-hostname web01¦hostname -f web01¦nmcli hostname set web01¦hostnamectl hostname-set web01¦hostnamectl set-hostname은 /etc/hostname에 반영되는 영구 변경입니다.
netconfig¦eth1 인터페이스를 활성(up) 상태로 올리는 명령은?¦ip link set eth1 up¦ip addr up eth1¦ip route set eth1 up¦ip link add eth1 up¦인터페이스 상태는 ip link set 장치 up/down으로 바꿉니다.
netconfig¦기본 게이트웨이 192.168.1.1을 임시로 추가하는 명령은?¦ip route add default via 192.168.1.1¦ip route add default gw 192.168.1.1¦ip route add gateway 192.168.1.1 dev eth0¦ip addr add default via 192.168.1.1¦기본 경로는 default via 게이트웨이 형식으로 추가합니다(gw는 route 명령 문법).
netconfig¦eth0에 192.168.1.50/24를 임시로 추가하는 명령은?¦ip addr add 192.168.1.50/24 dev eth0¦ip addr add 192.168.1.50 netmask 255.255.255.0 eth0¦ip link add 192.168.1.50/24 dev eth0¦ip route add 192.168.1.50/24 eth0¦ip 명령은 CIDR 접두어와 dev 키워드를 사용하며 netmask 옵션은 없습니다.
netconfig¦ip route 출력이 "default via 192.168.1.1 dev ens160 proto dhcp metric 100"일 때 해석으로 알맞은 것은?¦기본 게이트웨이는 192.168.1.1이며 DHCP로 설정되었다¦192.168.1.1은 이 호스트가 질의하는 DNS 서버 주소이다¦ens160은 루프백 장치이며 정적으로 지정된 경로이다¦192.168.1.1/24 대역으로 가는 정적 경로 하나만 등록되어 있다¦default via 뒤의 주소가 기본 게이트웨이이며 proto dhcp는 DHCP로 추가되었다는 뜻입니다.
netconfig¦ip addr 출력에 "inet 10.0.2.15/24 brd 10.0.2.255"가 있을 때 /24가 의미하는 것은?¦서브넷 마스크 255.255.255.0¦이 인터페이스가 사용할 수 있는 호스트 24대 제한¦이 주소가 사용하는 서비스 포트 번호 24¦서브넷 마스크 255.255.0.0과 같은 클래스 B 마스크¦/24는 네트워크 비트 24개로 255.255.255.0이며 brd는 브로드캐스트 주소입니다.
netconfig¦이름 해석과 관련해 옳지 않은 것은?¦/etc/hosts는 DNS 서버의 IP 주소를 지정하는 파일이다¦/etc/resolv.conf의 nameserver 줄이 질의할 DNS 서버를 지정한다¦/etc/nsswitch.conf의 hosts 항목이 조회 순서를 정한다¦/etc/hosts는 IP 주소와 호스트 이름을 한 줄씩 대응시킨다¦DNS 서버 지정은 resolv.conf이고 hosts는 정적 이름-주소 대응 파일입니다.
netconfig¦터미널에서 메뉴 방식으로 NetworkManager 연결을 편집하는 도구는?¦nmtui¦nmcli¦netstat¦ifconfig¦nmtui는 텍스트 기반 UI이고 nmcli는 명령행 인터페이스입니다.
netconfig¦Rocky Linux 8에서 NetworkManager 서비스를 재시작하는 명령은?¦systemctl restart NetworkManager¦systemctl restart networking.service¦systemctl restart systemd-networkd¦systemctl reload NetworkManager-wait-online¦Debian의 networking 서비스와 달리 RHEL 계열 기본 관리자는 NetworkManager입니다.
netconfig¦대기 중인 TCP 포트를 숫자 형태와 프로세스 정보와 함께 보는 명령은?¦ss -tlnp¦ss -ulnp¦ss -xlnp¦ss -s¦-t는 TCP, -l은 대기, -n은 숫자, -p는 프로세스이며 -u는 UDP, -x는 유닉스 소켓입니다.
services¦SMTP의 기본 포트 번호는?¦25¦110¦143¦53¦SMTP 25, POP3 110, IMAP 143, DNS 53입니다.
services¦POP3의 기본 포트 번호는?¦110¦143¦25¦995¦POP3는 110이고 995는 TLS를 쓰는 POP3S입니다.
services¦IMAP의 기본 포트 번호는?¦143¦110¦993¦25¦IMAP은 143이고 993은 TLS를 쓰는 IMAPS입니다.
services¦평문으로 원격 로그인하여 보안상 권장되지 않는 Telnet의 기본 포트는?¦23¦22¦21¦25¦Telnet은 23이고 SSH는 22입니다.
services¦FTP의 제어 연결에 쓰이는 기본 포트는?¦21¦20¦22¦69¦21은 제어, 20은 능동 모드 데이터 연결이며 22는 SSH, 69는 TFTP입니다.
services¦MySQL과 MariaDB의 기본 TCP 포트는?¦3306¦5432¦1433¦1521¦5432는 PostgreSQL, 1433은 MS SQL Server, 1521은 Oracle입니다.
services¦재부팅 후에도 유지되도록 방화벽에서 http 서비스를 허용하는 명령은?¦firewall-cmd --permanent --add-service=http¦firewall-cmd --add-service=http --timeout=3600¦firewall-cmd --permanent --add-port=http¦firewall-cmd --reload --add-service=http¦--permanent가 있어야 영구 설정이며 없으면 런타임에만 적용됩니다.
services¦--permanent로 저장한 firewalld 설정을 실행 중인 방화벽에 반영하는 명령은?¦firewall-cmd --reload¦firewall-cmd --list-all¦firewall-cmd --state¦firewall-cmd --get-default-zone¦--reload는 영구 설정을 다시 읽어 런타임에 적용합니다.
services¦httpd를 지금 시작하고 부팅 시 자동 시작까지 설정하는 명령은?¦systemctl enable --now httpd¦systemctl start --enable httpd¦systemctl enable httpd¦systemctl start httpd¦enable --now는 자동 시작 등록과 즉시 시작을 한 번에 합니다.
services¦sshd가 실행 중인지 active 또는 inactive 한 단어로 확인하는 명령은?¦systemctl is-active sshd¦systemctl is-enabled sshd¦systemctl mask sshd¦systemctl list-dependencies sshd¦is-enabled는 자동 시작 여부를, is-active는 현재 실행 여부를 알려 줍니다.
services¦Rocky Linux 8에서 BIND DNS 서버 데몬의 서비스 이름은?¦named¦dhcpd¦httpd¦smb¦BIND는 named, DHCP는 dhcpd, Apache는 httpd, Samba는 smb입니다.
services¦DHCP 서버가 클라이언트 요청을 수신하는 UDP 포트는?¦67¦68¦53¦69¦서버는 67, 클라이언트는 68을 사용하며 53은 DNS, 69는 TFTP입니다.
services¦Linux 디렉터리를 Windows 클라이언트와 SMB/CIFS로 공유할 때 쓰는 서비스는?¦Samba¦NFS¦NIS¦vsftpd¦Samba는 SMB 프로토콜을 구현하고 NFS는 주로 유닉스 계열 간 공유에 쓰입니다.
services¦Rocky Linux 8에서 Apache 웹 서버의 주 설정 파일은?¦/etc/httpd/conf/httpd.conf¦/etc/apache2/apache2.conf¦/etc/nginx/conf.d/httpd.conf¦/etc/sysconfig/httpd-main.conf¦RHEL 계열은 /etc/httpd/conf/httpd.conf이며 apache2.conf는 Debian 계열입니다.
services¦[인터넷 서비스] 다음 중 옳지 않은 설명은?¦SFTP는 FTP에 TLS를 입힌 프로토콜이다¦SSH의 기본 포트는 TCP 22이다¦POP3는 서버의 메일을 내려받는 수신 프로토콜이다¦SMTP는 메일 서버 간 전송에 쓰인다¦SFTP는 SSH 위에서 동작하며 FTP에 TLS를 입힌 것은 FTPS입니다.
services¦DNS 서버 8.8.8.8에 직접 질의하여 example.com을 조회하는 명령은?¦dig @8.8.8.8 example.com¦dig 8.8.8.8 example.com¦dig -s 8.8.8.8 example.com¦dig -dns 8.8.8.8 example.com¦dig는 @서버 형식으로 질의할 DNS 서버를 지정합니다.
virtualization¦리눅스 커널에 포함된 가상화 기능으로 하이퍼바이저 역할을 하는 것은?¦KVM¦Docker¦chroot¦cgroups¦KVM은 커널 모듈로 동작하며 Docker는 컨테이너 도구입니다.
virtualization¦정지된 가상 머신까지 포함하여 libvirt 도메인 목록을 보는 명령은?¦virsh list --all¦virsh list¦virsh start --all¦virsh dominfo¦virsh list는 실행 중인 것만, --all은 정지된 도메인까지 보여 줍니다.
virtualization¦호스트 OS 없이 하드웨어 위에서 직접 동작하는 Type 1 하이퍼바이저의 설명으로 알맞은 것은?¦베어메탈 형태로 하드웨어에서 직접 실행된다¦일반 응용 프로그램처럼 호스트 OS 위에서 실행된다¦컨테이너 이미지만 저장한다¦패키지 저장소를 관리한다¦Type 1은 베어메탈형이며 Type 2는 호스트 OS 위에서 실행됩니다.
virtualization¦docker run -d -p 8080:80 nginx에서 -p 8080:80의 의미는?¦호스트 8080을 컨테이너 80에 연결¦컨테이너 8080을 호스트 80에 연결¦CPU 8080개 할당¦프로세스 번호 8080 지정¦-p 호스트포트:컨테이너포트 순서입니다.
virtualization¦종료된 컨테이너까지 모두 목록으로 보는 명령은?¦docker ps -a¦docker ps¦docker images -a¦docker ls¦docker ps는 실행 중만, -a는 종료된 컨테이너까지 보여 줍니다.
virtualization¦Rocky Linux 8 저장소에서 제공하며 데몬 없이 컨테이너를 실행하는 Docker 호환 도구는?¦Podman¦Vagrant¦VirtualBox¦Docker Swarm¦Podman은 데몬리스 구조이고 CLI가 Docker와 유사합니다.
virtualization¦리눅스 컨테이너의 격리와 자원 제한에 핵심이 되는 커널 기능은?¦namespace와 cgroups¦SELinux와 iptables 규칙¦LVM과 RAID 구성¦GRUB과 initramfs 부팅 단계¦namespace는 보이는 자원을 분리하고 cgroups는 사용량을 제한합니다.
virtualization¦KVM 가상화에 관한 설명 중 옳지 않은 것은?¦하드웨어 가상화 확장 CPU 기능이 필요 없다¦libvirt로 가상 머신을 관리할 수 있다¦각 가상 머신은 별도의 게스트 OS를 실행한다¦스냅샷으로 특정 시점의 상태를 저장할 수 있다¦KVM은 Intel VT-x 또는 AMD-V 같은 CPU 확장을 사용합니다.
virtualization¦CPU가 하드웨어 가상화(Intel VT-x 또는 AMD-V)를 지원하는지 확인하는 명령은?¦grep -E 'vmx|svm' /proc/cpuinfo¦grep -E 'kvm|qemu' /etc/passwd¦lsmod | grep -E 'vmx|svm' /etc/fstab¦ip link | grep -E 'vmx|svm'¦cpuinfo의 vmx 플래그는 Intel, svm 플래그는 AMD 가상화 지원을 뜻합니다.
virtualization¦레지스트리에서 rockylinux:8 이미지를 내려받는 명령은?¦docker pull rockylinux:8¦docker push rockylinux:8¦docker commit rockylinux:8¦docker exec rockylinux:8¦pull은 내려받기, push는 업로드, commit은 컨테이너를 이미지로 만듭니다.
cloud¦웹메일처럼 사용자가 설치 없이 완성된 응용 프로그램을 이용하는 클라우드 서비스 모델은?¦SaaS¦IaaS¦PaaS¦DNS¦SaaS는 응용 프로그램 자체를 서비스로 제공합니다.
cloud¦SaaS, PaaS, IaaS 중 사용자가 OS부터 관리하는 범위가 가장 넓은 것은?¦IaaS¦SaaS¦PaaS¦모두 같다¦IaaS는 가상 인프라만 제공하므로 OS와 그 위 계층을 사용자가 관리합니다.
cloud¦사용한 만큼만 비용을 내는 클라우드의 특성은?¦종량제 과금¦고정 라이선스 영구 구매¦오프라인 설치 매체 판매¦디스크 파티션 단위 청구¦클라우드는 측정 가능한 서비스를 사용량에 따라 과금하는 경우가 많습니다.
cloud¦부하에 따라 자원을 자동으로 늘리고 줄일 수 있는 클라우드 특성은?¦탄력성¦영속성¦동기화¦압축성¦탄력성은 수요에 맞춰 자원을 확장하고 축소하는 성질입니다.
cloud¦한 조직만 전용으로 사용하는 클라우드 배치 모델은?¦프라이빗 클라우드¦퍼블릭 클라우드¦멀티 테넌트 클라우드¦커뮤니티 클라우드¦프라이빗은 단일 조직 전용이고 퍼블릭은 다수 고객이 공유 사용합니다.
cloud¦클라우드 인스턴스 첫 부팅 때 호스트 이름, 사용자, SSH 공개키 등을 초기 설정하는 도구는?¦cloud-init¦grub2-mkconfig¦dracut¦anaconda¦cloud-init은 사용자 데이터로 인스턴스를 초기화합니다.
cloud¦키 파일 key.pem으로 클라우드 인스턴스 203.0.113.10에 rocky 사용자로 접속하는 명령은?¦ssh -i key.pem rocky@203.0.113.10¦ssh -p key.pem rocky@203.0.113.10¦ssh -k key.pem rocky@203.0.113.10¦ssh -l key.pem rocky 203.0.113.10¦-i가 개인키 파일이고 -p는 포트 지정입니다.
cloud¦퍼블릭 클라우드에 관한 설명 중 옳지 않은 것은?¦이용자가 데이터센터의 물리 서버를 직접 유지보수한다¦자원 풀을 여러 이용자가 논리적으로 분리해 공유한다¦필요할 때 자원을 빠르게 확장하거나 축소할 수 있다¦사용한 만큼 비용을 내는 종량제 과금이 일반적이다¦물리 하드웨어 관리는 클라우드 제공자의 책임입니다.
cloud¦인스턴스에 디스크처럼 붙여 파일 시스템을 만들어 쓰는 클라우드 저장 방식은?¦블록 스토리지¦오브젝트 스토리지¦DNS 레코드¦CDN 캐시¦블록 스토리지는 디스크 장치처럼 연결하고 오브젝트 스토리지는 API로 객체를 저장합니다.
trends¦데이터가 생성되는 현장 가까이에서 처리하는 컴퓨팅 방식은?¦엣지 컴퓨팅¦배치 중앙 백업¦오프라인 인쇄¦BIOS 업데이트¦엣지는 지연을 줄이려고 장치 가까운 곳에서 처리합니다.
trends¦개발과 운영의 협업, 자동화, 빠른 릴리스를 강조하는 문화와 방법론은?¦DevOps¦RAID¦SELinux¦GPT¦DevOps는 개발과 운영을 연결해 배포 주기를 개선합니다.
trends¦코드 변경 시 빌드, 테스트, 배포를 자동화하는 파이프라인은?¦CI/CD¦IaC¦NAT¦LVM¦CI는 통합과 테스트 자동화, CD는 전달 또는 배포 자동화입니다.
trends¦SSH로 대상 서버에 접속하며 에이전트 설치 없이 구성 관리를 하는 도구는?¦Ansible¦Grafana¦Wireshark¦Logstash¦Ansible은 에이전트리스 방식으로 플레이북을 실행합니다.
trends¦여러 컨테이너의 배포, 확장, 복구를 자동화하는 오케스트레이션 플랫폼은?¦Kubernetes¦Podman 단독 실행 환경¦Docker 로컬 빌드 캐시¦Vagrant 박스 이미지¦Kubernetes는 컨테이너 오케스트레이션 시스템입니다.
trends¦작고 독립적인 서비스를 조합해 하나의 응용을 구성하는 아키텍처는?¦마이크로서비스¦모놀리식¦서버-클라이언트 2계층 구조¦공유 메모리 기반 멀티스레드 구조¦모놀리식은 하나로 묶인 구조이고 마이크로서비스는 서비스 단위로 분리합니다.
trends¦Rocky Linux에 대한 설명으로 알맞은 것은?¦RHEL과 바이너리 호환을 목표로 하는 커뮤니티 배포판¦Debian을 기반으로 파생된 커뮤니티 배포판¦SUSE에서 갈라져 나온 엔터프라이즈 배포판¦Arch를 기반으로 롤링 릴리스를 하는 배포판¦Rocky Linux는 CentOS의 변화 이후 등장한 RHEL 호환 배포판입니다.
trends¦대용량 데이터를 분산 저장하고 처리하는 오픈소스 프레임워크는?¦Hadoop¦Ansible¦SELinux¦GRUB¦Hadoop은 HDFS와 MapReduce 등으로 대규모 데이터를 분산 처리합니다.
trends¦GPL에 관한 설명 중 옳지 않은 것은?¦GPL 소프트웨어는 판매하거나 유료로 배포하는 것이 금지된다¦수정본을 배포하면 같은 조건으로 소스를 제공해야 한다¦리눅스 커널은 GPLv2 라이선스 아래 배포된다¦사용자는 소스를 받아 수정하고 재배포할 자유가 있다¦GPL은 유료 배포를 금지하지 않으며 소스 공개와 동일 조건 배포를 요구합니다.
trends¦서버 관리 없이 이벤트에 따라 함수 단위로 코드를 실행하는 모델은?¦서버리스(FaaS)¦베어메탈 서버 임대 모델¦가상 데스크톱(VDI) 서비스¦CDN 엣지 캐시 서비스¦FaaS는 인프라 관리를 추상화하고 함수 실행 단위로 과금합니다.
cloud¦둘 이상의 서로 다른 클라우드 제공자를 함께 사용하는 전략은?¦멀티 클라우드¦프라이빗 클라우드¦엣지 클라우드¦단일 테넌시¦멀티 클라우드는 여러 제공자를 사용하는 방식이고 하이브리드는 온프레미스와 퍼블릭의 결합입니다.
netconfig¦활성 연결 ens160의 DNS 서버를 nmcli로 1.1.1.1로 지정하는 속성은?¦nmcli con mod ens160 ipv4.dns 1.1.1.1¦nmcli con mod ens160 ipv4.nameserver 1.1.1.1¦nmcli con mod ens160 dns.server 1.1.1.1¦nmcli con mod ens160 ipv4.gateway 1.1.1.1¦DNS 서버는 ipv4.dns 속성이며 ipv4.gateway는 기본 게이트웨이입니다.
""".strip()
