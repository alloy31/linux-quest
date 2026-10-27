from .model import Topic

SOURCE = "https://www.ihd.or.kr/introducesubject1.do"
BASELINE = "2026 · Rocky Linux 8 / Debian 계열 비교"

_LESSONS = [
("overview", "리눅스의 개요", "general", "리눅스 커널은 CPU·메모리·장치·프로세스를 관리합니다. 배포판은 커널에 셸, 라이브러리, 설치·패키지 도구 등을 묶은 운영체제입니다. 다중 사용자와 선점형 멀티태스킹을 지원하며 GUI 없이도 사용할 수 있습니다."),
("history", "리눅스의 역사", "general", "리누스 토르발스가 1991년 리눅스 커널 개발을 시작했습니다. GNU 프로젝트는 자유 운영체제의 도구들을 개발했고, 리눅스 커널과 GNU 도구가 함께 널리 사용됩니다. UNIX의 영향을 받았으며 MINIX와 리눅스는 서로 다른 운영체제입니다."),
("license", "철학과 라이선스", "general", "자유 소프트웨어는 실행·연구·수정·재배포의 자유를 중시합니다. 리눅스 커널은 GPLv2입니다. GPL의 소스 제공 의무는 배포 방식과 라이선스 조건에 따라 판단하며, GPL 소프트웨어의 유료 판매도 가능합니다. 오픈소스와 무료 서비스는 같은 개념이 아닙니다."),
("distros", "배포판 계열", "general", "RHEL·Rocky Linux·Fedora는 RPM 계열, Debian·Ubuntu는 Debian 계열입니다. Rocky Linux 8에서는 rpm과 dnf/yum을, Debian 계열에서는 dpkg와 APT를 구분합니다. 패키지 형식·관리 명령·설정 경로는 배포판마다 다를 수 있습니다."),
("installation", "설치와 설치 유형", "general", "설치 전 CPU 아키텍처, 메모리, 저장 공간, 데이터 보존 여부를 확인합니다. 최소 설치와 GUI 설치는 포함 패키지가 다릅니다. ISO·네트워크 설치 등 방법을 구분하고 시간대·사용자·네트워크·설치 대상을 확인합니다. 이 게임은 OS 설치 자체를 수행하지 않는 상황형 학습입니다."),
("partition", "파티션과 스왑", "general", "파티션은 디스크의 논리적 구획입니다. MBR과 GPT는 파티션 테이블 형식이며 GPT는 큰 디스크와 다수 파티션에 적합합니다. /는 루트 디렉터리이고 /boot는 부팅 파일을 담습니다. swap은 메모리 부족 시 페이지를 저장하는 공간이며 RAM과 속도가 같지 않습니다."),
("boot", "부팅과 Boot Manager", "general", "일반적인 흐름은 펌웨어(BIOS/UEFI) → 부트 로더(GRUB2) → 커널·initramfs → init/systemd → 서비스 시작입니다. 부트 로더는 커널을 메모리로 불러옵니다. systemd의 multi-user.target은 일반적인 비그래픽 다중 사용자 환경, graphical.target은 그래픽 환경입니다."),
("files", "디렉터리와 파일", "general", "pwd는 현재 위치, ls는 목록, cd는 이동입니다. /로 시작하면 절대경로, 현재 위치 기준이면 상대경로입니다. .은 현재, ..은 상위, ~는 홈입니다. cp는 복사, mv는 이동·이름 변경, rm은 삭제, mkdir은 디렉터리 생성입니다. *는 여러 글자, ?는 한 글자에 대응하며 숨김 파일은 보통 .으로 시작합니다."),
("basics", "기타 기본 명령어와 도움말", "general", "man 명령어로 설명서를 읽고 q로 닫습니다. --help는 명령별 간단 도움말입니다. whoami는 현재 사용자, id는 UID·GID·그룹, uname은 시스템 정보, date는 시각, hostname은 호스트 이름입니다. which는 PATH에서 실행 파일을, whereis는 실행·소스·매뉴얼 위치를 찾습니다. find는 조건으로 파일을 검색합니다."),
("users", "사용자·계정·그룹", "general", "/etc/passwd는 계정 정보, /etc/shadow는 암호 해시 등 보호 정보, /etc/group은 그룹 정보를 담습니다. useradd는 계정 생성, usermod는 수정, passwd는 암호 변경입니다. usermod -aG 그룹 사용자는 기존 보조 그룹을 보존하며 추가합니다. root의 UID는 0이고 일반 사용자와 권한이 다릅니다."),
("permissions", "권한·소유권·umask", "ops", "권한은 소유자·그룹·기타 사용자 순으로 r=4, w=2, x=1입니다. chmod 640은 rw-r-----입니다. 디렉터리 x는 탐색, r은 이름 목록 읽기입니다. chown은 소유자, chgrp는 그룹을 바꿉니다. umask는 새 파일·디렉터리 기본 권한에서 비트를 제거합니다. 기본 파일 666과 umask 022의 결과는 644입니다."),
("filesystem", "파일 시스템 관리", "ops", "df는 파일시스템별 사용량, du는 경로별 사용량을 봅니다. 하드 링크는 같은 inode를 참조하며 보통 파일시스템을 넘을 수 없습니다. 심볼릭 링크는 경로를 참조하며 원본 삭제 시 끊어질 수 있습니다. mkfs는 파일시스템 생성, fsck는 검사, mount·umount는 연결·해제입니다. /etc/fstab은 정적 마운트 설정입니다. 실제 포맷·마운트는 이 게임에서 실행하지 않습니다."),
("shell", "셸의 개념과 종류", "ops", "셸은 명령을 해석합니다. Bash, sh, zsh, csh 등이 있으며 커널과 구별합니다. 작은따옴표는 변수 확장을 막고 큰따옴표는 $변수 확장을 허용합니다. 명령 치환은 $(명령)이며 alias는 별칭입니다. ;는 순차 실행, &&는 앞 명령 성공 시, ||는 실패 시 다음 명령을 실행합니다."),
("environment", "셸 환경 설정", "ops", "NAME=value는 셸 변수 대입이며 = 양옆에 공백을 두지 않습니다. export NAME은 자식 프로세스에 환경변수를 전달합니다. PATH는 실행 파일 검색 경로, HOME은 홈 디렉터리입니다. Bash 로그인 셸은 /etc/profile과 사용자 로그인 설정을, 대화형 비로그인 셸은 ~/.bashrc를 사용합니다. source 파일은 현재 셸에 설정을 반영합니다."),
("streams", "표준 입출력과 연결", "ops", "표준 입력은 0, 표준 출력은 1, 표준 오류는 2입니다. >는 덮어쓰기, >>는 추가, <는 파일 입력입니다. |는 앞 명령의 표준 출력을 다음 명령의 입력에 연결합니다. 2>는 오류를 파일로 보냅니다. >/dev/null 2>&1의 순서처럼 리다이렉션 순서도 결과에 영향을 줍니다."),
("text", "텍스트·검색·정렬", "ops", "cat은 내용, head·tail은 앞뒤 일부, less는 페이지 탐색입니다. grep은 패턴에 맞는 줄을 찾고 -n은 줄 번호, -v는 반대 조건입니다. sort -u는 정렬과 중복 제거를 함께 합니다. uniq는 인접 중복을 처리하므로 보통 sort와 조합합니다. wc -l은 줄 수, cut -d 구분자 -f 필드는 필드 추출입니다."),
("archive", "묶기와 압축", "ops", "tar -cf는 묶기, -tf는 목록, -xf는 풀기입니다. -z는 gzip, -j는 bzip2, -J는 xz를 사용합니다. tar -czf backup.tar.gz 디렉터리는 gzip 압축된 묶음을 만듭니다. gzip은 보통 단일 파일 압축 도구이고 tar의 묶기와 역할이 다릅니다. 풀기 전 목록과 경로를 확인합니다."),
("process", "프로세스와 시그널", "ops", "프로세스는 실행 중인 프로그램입니다. PID는 프로세스 번호, PPID는 부모 번호입니다. ps·top으로 상태를 확인하고 kill은 시그널을 보냅니다. 기본 SIGTERM(15)은 정상 종료를 요청하고 SIGKILL(9)은 프로세스가 처리·무시할 수 없습니다. 일반 nice 범위는 -20~19이며 숫자가 높을수록 우선순위가 낮아집니다."),
("jobs", "포그라운드·백그라운드", "ops", "&는 명령을 백그라운드로 실행합니다. jobs는 현재 셸의 작업 목록, fg·bg는 포그라운드·백그라운드 전환입니다. Ctrl+Z는 보통 작업을 정지시키고 Ctrl+C는 보통 SIGINT를 보냅니다. nohup은 터미널 종료 시 SIGHUP에 영향받지 않게 실행하는 데 사용합니다."),
("schedule", "반복·예약 작업", "ops", "crontab -e는 반복 일정을 편집하고 -l은 목록을 봅니다. 일반 사용자 crontab의 시간 필드는 분·시·일·월·요일 순서입니다. 0 2 * * *는 매일 02:00입니다. at은 일회성 예약, atq는 대기 작업 목록입니다. 데몬은 보통 백그라운드에서 서비스를 수행합니다."),
("editors", "에디터 종류와 활용", "ops", "vi는 명령 모드·입력 모드·마지막 행 명령을 구별합니다. i로 입력, Esc로 명령 모드, :wq로 저장 후 종료, :q!로 변경을 버리고 종료합니다. dd는 줄 삭제, yy는 줄 복사, p는 붙여넣기, /문자열은 검색입니다. nano는 화면의 단축키 안내를, Emacs는 확장 가능한 편집 환경을 제공합니다."),
("rpm", "RPM 계열 설치·삭제", "ops", "rpm -q는 설치 여부, -qa는 설치된 전체 목록, -qi는 패키지 정보, -ql은 설치 파일 목록입니다. rpm -ivh 파일.rpm은 설치, -Uvh는 갱신, -e 이름은 제거입니다. dnf/yum은 저장소와 의존성 해결을 함께 다룹니다. 실습은 인터넷 없이 동봉된 quest-backup RPM을 설치합니다."),
("debian", "Debian 계열 패키지", "ops", "Debian·Ubuntu는 .deb와 dpkg/APT를 사용합니다. dpkg -i 파일.deb는 로컬 패키지를 설치하고 dpkg -l은 목록을 봅니다. apt update는 저장소 목록 갱신, apt upgrade는 설치 패키지 업그레이드입니다. apt install은 의존성을 고려합니다. Rocky 실습에서 apt가 실제로 실행된다고 가정하지 않습니다."),
("source", "소스 설치", "ops", "일반적인 소스 빌드 흐름은 압축 해제 → ./configure → make → make install입니다. 프로젝트마다 CMake 등 다른 빌드 도구를 쓸 수 있습니다. configure는 환경·설치 위치를 설정하고 make는 의존 관계에 따라 빌드합니다. 패키지 관리자 밖의 설치는 파일 추적·삭제가 어려울 수 있습니다."),
("devices", "장치 연결·설정·활용", "ops", "장치는 /dev 아래 장치 파일로 표현될 수 있습니다. lsblk는 블록 장치, lspci는 PCI, lsusb는 USB 장치를 조사합니다. udev는 장치 이벤트와 이름·권한을 관리합니다. lsmod는 모듈 목록, modprobe는 의존성을 고려한 모듈 적재입니다. 스캐너는 SANE, 사운드는 ALSA 등의 구성 요소를 구분합니다. 물리 장치·커널 모듈은 상황형으로 학습합니다."),
("printing", "프린터와 출력 관리", "ops", "CUPS는 인쇄 시스템입니다. lp·lpr은 인쇄 요청, lpstat·lpq는 상태·대기열 확인, cancel·lprm은 작업 취소에 사용합니다. 기본 프린터, 작업 번호, 대기열을 구분합니다. 게임에서 호스트 프린터로 실제 인쇄하지 않습니다."),
("xwindow", "X 윈도 구조", "use", "X 서버는 디스플레이·입력 장치를 관리하고 X 클라이언트는 화면을 사용하는 응용프로그램입니다. DISPLAY는 X 서버의 디스플레이 위치를 지정합니다. 윈도 매니저는 창 배치·테두리 등을 관리하고 디스플레이 매니저는 그래픽 로그인에 관여합니다. 원격 X에서는 응용프로그램이 원격에서, X 서버가 화면 있는 컴퓨터에서 동작할 수 있습니다."),
("desktop", "X 윈도와 데스크톱 활용", "use", "GNOME·KDE Plasma는 데스크톱 환경입니다. GDM·SDDM 같은 디스플레이 매니저와 역할이 다릅니다. startx는 설정된 X 세션을 시작하는 명령입니다. Firefox는 웹 브라우저, LibreOffice는 사무 프로그램입니다. CLI 게임의 GUI 내용은 모의 상황과 개념 문제로 표시합니다."),
("network", "네트워크의 개념", "use", "LAN은 근거리 네트워크입니다. OSI 참조 모델은 7계층, TCP/IP는 인터넷 프로토콜 구조입니다. 스위치는 보통 MAC 주소로 프레임을, 라우터는 IP 경로로 패킷을 전달합니다. TCP는 연결·신뢰성, UDP는 비연결 데이터그램을 제공합니다. DNS는 이름 조회, DHCP는 주소 설정 자동화에 사용합니다."),
("address", "주소와 서브넷", "use", "IPv4는 32비트, IPv6는 128비트 주소입니다. IPv4 /24의 마스크는 255.255.255.0이고 일반 서브넷의 전체 주소는 256개입니다. 127.0.0.1은 루프백입니다. 사설 IPv4 범위는 10/8, 172.16/12, 192.168/16입니다. 기본 게이트웨이는 다른 네트워크로 나갈 때 사용하는 다음 경로입니다."),
("netconfig", "네트워크 설정·진단", "use", "ip addr는 주소, ip route는 경로, ss는 소켓을 확인합니다. ping은 ICMP 응답, dig·host는 DNS 조회, traceroute는 경로 조사에 사용됩니다. /etc/hosts는 로컬 이름 대응, /etc/resolv.conf는 resolver 설정입니다. Rocky 8의 NetworkManager/nmcli와 Ubuntu의 netplan은 방식이 다르며 구형 ifconfig·netstat도 구분해 학습합니다."),
("services", "인터넷 서비스", "use", "SSH는 보안 원격 접속(기본 TCP 22), HTTP는 웹(80), HTTPS는 TLS 기반 웹(443)입니다. DNS는 보통 53, SMTP는 메일 전송, POP3·IMAP은 수신에 사용합니다. FTP와 SSH 기반 SFTP를 구별합니다. curl·wget은 데이터를 요청·저장할 수 있습니다. 실습 서비스는 외부 인터넷과 분리된 내부망의 quest-vault:8080입니다."),
("virtualization", "가상화와 컨테이너", "use", "가상 머신은 가상 하드웨어 위에 게스트 운영체제를 구동합니다. 컨테이너는 호스트 커널을 공유하며 프로세스·파일·네트워크 등을 격리합니다. 하이퍼바이저와 컨테이너 런타임은 역할이 다릅니다. 이 게임의 컨테이너 안 uname 커널은 Rocky 배포판의 별도 커널을 뜻하지 않습니다."),
("cloud", "클라우드 활용", "use", "IaaS는 컴퓨팅·네트워크 같은 인프라, PaaS는 개발·배포 플랫폼, SaaS는 완성된 소프트웨어 서비스를 제공합니다. 퍼블릭·프라이빗·하이브리드는 배치 모델입니다. 확장성·탄력성·종량제를 구분하며 사용 비용이 항상 0이라는 뜻은 아닙니다."),
("trends", "응용분야·활용기술", "use", "리눅스는 서버, 임베디드 장치, IoT, 슈퍼컴퓨터·HPC 등에 사용됩니다. IoT는 연결된 사물의 데이터 수집·제어, 빅데이터는 큰 데이터의 저장·처리, 클러스터는 여러 노드의 협력입니다. SDN은 네트워크 제어와 전달의 분리, NFV는 네트워크 기능의 소프트웨어 가상화라는 관점에서 구분합니다."),
]

TOPICS = {row[0]: Topic(*row) for row in _LESSONS}

# Official examination rows → teachable topic identifiers. Kept separate from the campaign.
OFFICIAL_COVERAGE = {
    "리눅스의 개요·역사·철학": ("overview", "history", "license", "distros"),
    "기본 설치 및 유형": ("installation",),
    "파티션과 파일 시스템": ("partition", "filesystem"),
    "Boot Manager": ("boot",),
    "사용자 생성 및 계정 관리": ("users",),
    "디렉터리 및 파일": ("files",),
    "기타 명령어": ("basics", "text", "archive"),
    "권한 및 그룹 설정": ("permissions", "users"),
    "파일 시스템의 관리": ("filesystem",),
    "Shell 개념 및 종류·환경 설정": ("shell", "environment", "streams"),
    "프로세스 개념 및 유형·Utility": ("process", "jobs", "schedule"),
    "에디터 종류·활용": ("editors",),
    "S/W 개념·설치·삭제": ("rpm", "debian", "source"),
    "주변장치 연결·설정·활용": ("devices", "printing"),
    "X 윈도 개념·사용법·활용": ("xwindow", "desktop"),
    "네트워크 개념": ("network", "address"),
    "인터넷 서비스 종류·설정": ("netconfig", "services"),
    "응용분야 기술동향·활용기술": ("virtualization", "cloud", "trends"),
}
