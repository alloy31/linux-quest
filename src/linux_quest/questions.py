"""Original practice questions, not copies of official exam papers.

Each row is topic ¦ stem ¦ correct answer ¦ three alternatives ¦ explanation.
Choice order is shuffled when displayed; topic identifiers preserve coverage.
"""
from .model import Question
from .questions_extra import EXTRA_ROWS

_ROWS = """
overview¦CPU·메모리·장치를 직접 관리하는 핵심 구성 요소는?¦커널¦브라우저¦텍스트 에디터¦패키지 저장소¦커널은 하드웨어 자원과 프로세스를 관리합니다.
overview¦리눅스 배포판을 가장 잘 설명한 것은?¦커널과 사용자 도구 등을 묶은 운영체제¦커널 소스의 파일 한 개¦반드시 유료인 프로그램¦하드웨어 CPU의 종류¦배포판은 커널·라이브러리·설치 및 관리 도구 등을 제공합니다.
overview¦여러 계정이 시스템 자원을 함께 사용하는 특성은?¦다중 사용자¦단일 작업¦읽기 전용¦비네트워크¦계정과 권한으로 여러 사용자의 접근을 구분합니다.
overview¦리눅스 서버의 GUI에 관한 올바른 설명은?¦GUI 없이도 운영할 수 있다¦GUI 없이는 로그인 불가¦모든 명령은 마우스로 실행¦GUI는 커널 자체다¦셸·원격 접속으로 GUI 없는 서버를 운영할 수 있습니다.
overview¦실행 중인 여러 작업에 CPU 시간을 나누는 기능은?¦멀티태스킹¦파일 압축¦디스크 포맷¦화면 캡처¦커널 스케줄러가 프로세스 실행 시간을 배분합니다.
history¦리눅스 커널 개발을 시작한 사람은?¦리누스 토르발스¦팀 버너스리¦귀도 반 로섬¦브렌던 아이크¦리누스 토르발스가 리눅스 커널 개발을 시작했습니다.
history¦리눅스 커널 개발이 시작된 해는?¦1991년¦1969년¦2005년¦2018년¦UNIX의 시작과 리눅스의 시작을 혼동하지 않습니다.
history¦GNU 프로젝트와 리눅스의 관계로 적절한 것은?¦GNU 도구와 리눅스 커널이 함께 사용된다¦GNU는 CPU 제조사다¦GNU는 리눅스의 파일 확장자다¦둘은 반드시 함께 사용할 수 없다¦커널과 사용자 공간 도구의 역할을 구별합니다.
history¦UNIX와 리눅스의 관계로 적절한 설명은?¦리눅스는 UNIX 설계의 영향을 받았다¦리눅스는 웹 브라우저의 이름이다¦UNIX는 2010년 리눅스에서 시작됐다¦둘은 파일 경로 개념이 없다¦리눅스는 UNIX 계열의 설계·사용 방식에서 영향을 받았습니다.
history¦MINIX와 리눅스에 대한 설명으로 옳은 것은?¦서로 다른 운영체제다¦동일한 커널의 동일한 이름이다¦MINIX는 리눅스 패키지 관리자다¦리눅스는 MINIX의 설정 파일이다¦역사적 영향과 운영체제의 동일성은 다릅니다.
license¦리눅스 커널의 라이선스는?¦GPLv2¦전용 비공개 라이선스만 사용¦MIT만 사용¦CC BY 사진 라이선스¦리눅스 커널은 GPLv2를 사용합니다.
license¦자유 소프트웨어의 자유와 가장 가까운 것은?¦실행·연구·수정·재배포의 자유¦항상 무조건 무료라는 뜻¦저작권이 없다는 뜻¦소스 열람이 언제나 금지됨¦자유는 사용자의 권리와 관련되고 가격과 구별합니다.
license¦오픈소스에 관한 올바른 설명은?¦라이선스 조건을 확인해야 한다¦모든 조건이 사라진다¦저작권자가 존재할 수 없다¦수정본은 언제나 비밀로만 보관한다¦공개된 소스도 배포·수정 조건이 있습니다.
license¦GPL 소프트웨어와 유료 판매의 관계는?¦조건을 지키며 유료 판매할 수 있다¦유료 판매가 항상 금지다¦GPL은 결제 통화다¦구매하면 저작권이 자동 소멸한다¦GPL은 판매 자체를 금지하지 않습니다.
license¦커널과 응용프로그램 라이선스의 관계는?¦각 소프트웨어의 라이선스를 구분한다¦모두 커널과 반드시 동일하다¦응용프로그램에는 라이선스가 없다¦파일 이름으로 라이선스가 확정된다¦배포판에는 여러 라이선스의 구성 요소가 있습니다.
distros¦Rocky Linux 8의 패키지 계열은?¦RPM 계열¦Debian 계열만 해당¦APK 계열만 해당¦macOS 전용¦Rocky는 RPM 패키지와 dnf/yum을 사용합니다.
distros¦Debian 계열 배포판은?¦Ubuntu¦Rocky Linux¦RHEL¦Fedora¦Ubuntu는 Debian 계열입니다.
distros¦.deb 파일을 직접 다루는 기본 도구는?¦dpkg¦rpm¦tar만 가능¦grub2¦Debian 패키지와 RPM 패키지는 형식·도구가 다릅니다.
distros¦Fedora와 Rocky의 공통점은?¦RPM 계열 패키지를 사용한다¦반드시 같은 패키지 버전만 갖는다¦모두 Debian의 별칭이다¦커널이 없다¦계열이 같아도 버전·지원 정책은 다릅니다.
distros¦배포판을 바꿀 때 확인할 내용은?¦패키지 명령과 설정 경로 차이¦CPU 시리얼만 확인¦모든 설정 파일이 동일하다고 가정¦기존 명령은 전부 의미가 같다고 가정¦배포판과 버전별 차이를 확인합니다.
installation¦설치 대상을 선택하기 전 가장 먼저 확인할 것은?¦기존 데이터와 대상 디스크¦배경화면 색만 확인¦브라우저 즐겨찾기 순서¦터미널 글꼴만 확인¦잘못된 대상 선택은 데이터를 잃게 할 수 있습니다.
installation¦최소 설치와 GUI 설치의 차이로 적절한 것은?¦포함되는 패키지 구성이 다르다¦최소 설치에는 커널이 없다¦GUI 설치는 파일을 저장 못 한다¦최소 설치는 네트워크 불가다¦설치 유형은 목적에 맞는 패키지 구성을 선택합니다.
installation¦설치 이미지와 CPU의 어떤 특성을 맞춰야 하는가?¦아키텍처¦바탕화면 해상도만¦계정 표시 이름만¦프린터 용지 크기¦aarch64와 x86_64 등 CPU 아키텍처를 구분합니다.
installation¦네트워크 설치의 일반적인 특징은?¦네트워크로 설치 자료를 받는다¦LAN 케이블이 항상 불필요하다¦디스크가 없어도 영구 설치가 자동 완료된다¦모든 패키지가 BIOS에 들어 있다¦설치 자료를 가져오는 경로와 연결 상태가 중요합니다.
installation¦서버 설치 시 시간대를 확인하는 이유는?¦로그와 예약 작업 시각 해석에 영향을 준다¦파일 권한 숫자가 바뀌어서¦커널 라이선스를 바꾸려고¦디스크 용량이 늘어서¦시간대는 로그·운영 일정 해석과 관련됩니다.
partition¦디스크를 논리적 영역으로 구획한 것은?¦파티션¦프로세스¦셸¦시그널¦파티션은 저장 장치의 논리적 구획입니다.
partition¦GPT와 MBR은 무엇의 형식인가?¦파티션 테이블¦셸 스크립트¦텍스트 인코딩¦사용자 암호¦파티션 정보를 저장하는 형식입니다.
partition¦일반적으로 큰 디스크와 다수 파티션에 유리한 방식은?¦GPT¦FAT라는 사용자 계정¦crontab¦ASCII¦GPT는 MBR보다 큰 주소 공간과 다수 파티션을 지원합니다.
partition¦/ 경로가 의미하는 것은?¦루트 디렉터리¦항상 root의 홈 디렉터리¦현재 계정 이름¦명령 기록 파일¦/와 /root는 다릅니다.
partition¦부팅 관련 파일을 담는 대표 경로는?¦/boot¦/tmp/mail¦/home/bin-only¦/dev/null¦/boot에는 커널·부트 로더 관련 파일이 놓입니다.
partition¦swap의 설명으로 적절한 것은?¦메모리 페이지를 저장하는 보조 공간¦RAM과 언제나 같은 속도¦CPU 캐시의 다른 이름¦모든 파일의 백업본¦swap은 RAM 확장에 도움을 줄 수 있지만 성능이 다릅니다.
boot¦일반적인 부팅 순서에서 커널보다 먼저 동작하는 것은?¦부트 로더¦사용자 브라우저¦로그인 후 실행한 vi¦crontab 편집 화면¦부트 로더가 커널과 초기 이미지를 불러옵니다.
boot¦GRUB2의 주된 역할은?¦부팅할 커널 선택·적재¦패키지 압축¦사용자 암호 해시 생성¦PDF 인쇄¦GRUB2는 부트 로더입니다.
boot¦initramfs의 역할에 가까운 것은?¦초기 부팅에 필요한 사용자 공간 제공¦웹 페이지 캐시만 저장¦모든 홈 디렉터리를 영구 백업¦프로세스 우선순위 숫자 저장¦루트 파일시스템 준비 등에 필요한 초기 환경을 제공합니다.
boot¦systemd 기반 일반 시스템에서 PID 1의 역할은?¦초기화와 서비스 관리¦사용자 브라우저 전용¦네트워크 주소 그 자체¦매번 실행한 ls¦systemd는 일반적으로 PID 1로 초기화와 서비스를 관리합니다.
boot¦일반적인 비그래픽 다중 사용자 target은?¦multi-user.target¦graphical.target만 가능¦poweroff.target¦reboot.target¦graphical.target과 비그래픽 운용 목표를 구별합니다.
files¦현재 디렉터리의 절대경로를 확인하는 명령은?¦pwd¦passwd¦mkdir¦who¦pwd는 현재 작업 디렉터리를 출력합니다.
files¦상위 디렉터리로 이동하려면?¦cd ..¦cd .¦ls ..¦pwd ..¦..은 상위 디렉터리입니다.
files¦숨김 파일까지 목록에 포함하는 옵션은?¦ls -a¦ls -d만¦ls -i만¦ls -t만¦-a는 .으로 시작하는 항목도 포함합니다.
files¦절대경로는 무엇으로 시작하는가?¦/¦.. 만 가능¦계정 암호¦항상 ./¦절대경로는 루트 디렉터리부터 표현합니다.
files¦파일 복사 명령은?¦cp¦mv¦cd¦pwd¦cp는 복사, mv는 이동·이름 변경입니다.
files¦파일 이름을 변경할 때 사용하는 명령은?¦mv¦cat¦uname¦whoami¦같은 디렉터리 안에서 mv로 이름을 바꿀 수 있습니다.
files¦여러 단계 디렉터리를 함께 만들 때 적절한 것은?¦mkdir -p a/b¦pwd a/b¦ls -p a/b¦cd -p a/b¦mkdir -p는 필요한 상위 디렉터리도 만듭니다.
files¦셸 패턴에서 보통 한 글자와 대응하는 것은?¦?¦*만 가능¦/¦~¦?는 한 글자, *는 여러 글자에 대응합니다.
files¦사용자 홈 디렉터리를 나타내는 셸 표기는?¦~¦/boot¦.. 만 가능¦/etc¦~는 홈 디렉터리로 확장됩니다.
files¦비어 있는 디렉터리를 제거하는 명령은?¦rmdir¦touch¦mkdir¦id¦rmdir는 비어 있는 디렉터리를 제거합니다.
basics¦현재 실행 계정의 이름을 출력하는 명령은?¦whoami¦hostname¦uname -r¦date¦whoami와 호스트·커널 정보 명령을 구분합니다.
basics¦UID·GID·보조 그룹을 확인하는 명령은?¦id¦cd¦gzip¦head¦id는 계정과 그룹 식별 정보를 출력합니다.
basics¦커널 릴리스를 확인하는 명령은?¦uname -r¦pwd -r¦ls -r¦date -r¦uname의 -r은 커널 릴리스입니다.
basics¦man 페이지를 읽다가 종료하는 일반 키는?¦q¦i¦dd¦Ctrl+Z만 가능¦기본 pager에서 q로 종료합니다.
basics¦PATH에서 실행 파일 위치를 찾는 대표 명령은?¦which¦who¦wc¦write¦which는 명령 검색 경로에서 위치를 찾습니다.
basics¦호스트 이름을 출력하는 대표 명령은?¦hostname¦whoami¦passwd¦umask¦사용자 이름과 호스트 이름은 다릅니다.
basics¦파일 이름 조건으로 디렉터리 트리를 검색하려면?¦find¦date¦fg¦kill¦find는 경로 아래 파일을 조건으로 탐색합니다.
basics¦현재 시스템 시각을 출력하는 명령은?¦date¦df¦du¦dd¦date는 날짜와 시각을 다룹니다.
users¦계정 기본 정보가 저장되는 대표 파일은?¦/etc/passwd¦/etc/fstab¦/etc/hosts¦/etc/resolv.conf¦passwd 파일은 계정 정보이며 암호 해시는 보통 shadow에 있습니다.
users¦암호 해시 등을 보호해 저장하는 대표 파일은?¦/etc/shadow¦/etc/group¦/etc/hosts¦/etc/profile¦shadow 파일은 일반 사용자 접근이 제한됩니다.
users¦root의 UID는?¦0¦1만 가능¦1000 고정¦65535 고정¦UID 0이 최고 권한 계정의 식별자입니다.
users¦계정을 새로 만드는 명령은?¦useradd¦usermod¦userdel¦groups¦useradd는 계정 생성입니다.
users¦기존 보조 그룹을 보존하며 그룹을 추가하는 옵션은?¦usermod -aG¦usermod -G만¦userdel -r¦passwd -d¦-a와 -G를 조합해 기존 보조 그룹을 유지합니다.
users¦사용자의 암호를 변경하는 대표 명령은?¦passwd¦pwd¦ps¦paste¦pwd는 디렉터리이고 passwd는 암호 관리입니다.
users¦그룹 정보를 담는 대표 파일은?¦/etc/group¦/etc/fstab¦/etc/issue¦/etc/hostname¦그룹 이름·GID·멤버 등의 정보를 담습니다.
users¦계정의 홈 디렉터리와 로그인 셸을 함께 확인할 파일은?¦/etc/passwd¦/etc/resolv.conf¦/etc/hosts¦/proc/meminfo¦passwd의 각 필드에 홈과 셸 경로가 있습니다.
permissions¦chmod 640의 소유자 권한은?¦읽기·쓰기¦읽기·실행¦쓰기·실행¦실행만¦6은 4+2이므로 읽기·쓰기입니다.
permissions¦파일의 소유자를 변경하는 명령은?¦chown¦chmod¦umask¦ls¦chown은 소유자, chmod는 권한입니다.
permissions¦umask 022에서 보통 새 일반 파일 권한은?¦644¦755¦777¦000¦일반 파일 기본 666에서 마스크 비트를 제거합니다.
permissions¦디렉터리의 x 권한 의미는?¦경로 탐색¦무조건 파일 내용 수정¦디렉터리 압축¦새 사용자 생성¦디렉터리 x는 진입·탐색 권한입니다.
permissions¦소유자만 읽고 쓸 수 있는 권한은?¦600¦644¦666¦755¦600은 rw-------입니다.
filesystem¦파일시스템별 남은 공간 확인 명령은?¦df¦du¦dd¦diff¦df는 파일시스템의 공간 통계입니다.
filesystem¦특정 디렉터리의 사용량을 확인하는 명령은?¦du¦df만 가능¦date¦who¦du는 경로별 사용량을 계산합니다.
filesystem¦심볼릭 링크의 설명으로 옳은 것은?¦대상 경로를 참조한다¦반드시 같은 inode다¦파일시스템을 넘을 수 없다¦원본이 없으면 생성도 불가능하다¦심볼릭 링크는 경로 참조이며 끊어진 링크도 존재할 수 있습니다.
filesystem¦하드 링크의 일반적인 제약은?¦다른 파일시스템으로 만들 수 없다¦동일 파일시스템에서도 불가¦항상 디렉터리에만 생성¦링크마다 원본 데이터가 완전히 복사됨¦하드 링크는 같은 파일시스템 inode를 참조합니다.
filesystem¦정적 마운트 설정 파일은?¦/etc/fstab¦/etc/passwd¦/etc/hosts¦/etc/profile¦fstab은 장치·마운트 지점·유형·옵션 등을 기록합니다.
shell¦Bash와 커널의 관계는?¦Bash는 명령 해석기다¦Bash가 CPU 하드웨어다¦Bash와 커널은 항상 같은 프로세스다¦커널은 텍스트 에디터다¦셸은 사용자 명령을 해석하고 커널과 역할이 다릅니다.
shell¦변수 확장을 막는 따옴표는?¦작은따옴표¦큰따옴표¦괄호만¦백슬래시 없는 $¦작은따옴표 안에서는 일반적인 변수 확장이 일어나지 않습니다.
shell¦앞 명령이 성공했을 때 다음 명령을 실행하는 연산자는?¦&&¦||¦;만 가능¦&만 가능¦&&는 종료 상태 0일 때 다음 명령을 실행합니다.
shell¦명령 출력으로 치환하는 표기는?¦$(명령)¦${항상 명령}¦#명령¦@명령¦$(...)는 명령 치환입니다.
environment¦자식 프로세스에 변수를 전달하려면?¦export¦alias만¦unset¦history¦export한 변수는 환경으로 전달됩니다.
environment¦Bash에서 올바른 변수 대입은?¦NAME=value¦NAME = value¦$NAME = value¦set NAME = value만 가능¦대입의 = 양옆에는 공백을 두지 않습니다.
environment¦실행 파일 검색 경로를 담는 변수는?¦PATH¦HOME¦PWD만¦TERM¦PATH의 디렉터리들에서 명령을 검색합니다.
environment¦설정 파일을 현재 셸에 반영하는 방법은?¦source 파일¦새 파일 이름을 ls¦파일을 gzip¦파일을 rm¦source 또는 . 명령은 현재 셸에서 읽습니다.
streams¦표준 오류의 파일 디스크립터는?¦2¦0¦1¦3 고정¦0은 입력, 1은 출력, 2는 오류입니다.
streams¦파일 끝에 표준 출력을 추가하는 연산자는?¦>>¦>¦<¦2<¦>는 덮어쓰기, >>는 추가입니다.
streams¦파이프가 기본적으로 전달하는 것은?¦앞 명령의 표준 출력¦모든 환경변수¦앞 명령의 PID만¦반드시 표준 오류만¦파이프는 표준 출력을 다음 표준 입력에 연결합니다.
streams¦표준 오류만 error.log로 보내려면?¦2> error.log¦1> error.log¦< error.log¦>> /dev/stdin¦2>가 표준 오류 리다이렉션입니다.
text¦패턴과 일치하지 않는 줄을 찾는 grep 옵션은?¦-v¦-n만¦-c만¦-l만¦-v는 일치 조건을 뒤집습니다.
text¦정렬하면서 중복 줄을 제거하는 명령은?¦sort -u¦uniq만 항상 충분¦wc -l¦head -u¦uniq는 인접한 중복만 처리합니다.
text¦파일 끝부분을 확인하는 명령은?¦tail¦head¦touch¦cut -f만¦tail은 끝부분, head는 앞부분을 읽습니다.
text¦줄 수를 세는 명령은?¦wc -l¦wc -c¦wc -w¦ls -l¦-l은 줄, -w는 단어, -c는 바이트입니다.
archive¦gzip 압축 tar 파일을 만드는 옵션 조합은?¦tar -czf¦tar -xzf¦tar -tzf¦tar -df만¦c는 생성, z는 gzip, f는 파일 지정입니다.
archive¦tar 묶음의 목록을 확인하는 옵션은?¦-t¦-x¦-c¦-r만¦-t는 목록을 읽습니다.
archive¦tar에서 xz 압축을 사용하는 옵션은?¦-J¦-j¦-z¦-v만¦대문자 J는 xz, 소문자 j는 bzip2입니다.
archive¦묶기와 압축에 대한 적절한 설명은?¦tar와 gzip은 역할을 구분한다¦gzip은 항상 디렉터리 트리를 직접 묶는다¦tar는 항상 압축까지 강제한다¦압축하면 파일 권한이 모두 777이 된다¦tar는 묶기 도구이며 압축 도구와 결합할 수 있습니다.
process¦kill에 시그널을 지정하지 않을 때 기본값은?¦SIGTERM¦SIGKILL¦SIGSTOP¦SIGHUP만¦기본은 정상 종료를 요청하는 SIGTERM입니다.
process¦프로세스가 처리하거나 무시할 수 없는 종료 시그널은?¦SIGKILL¦SIGTERM¦SIGHUP¦SIGINT¦SIGKILL은 사용자 프로세스가 처리·무시할 수 없습니다.
process¦일반 nice 값이 0에서 10으로 커지면?¦스케줄링 우선순위가 낮아진다¦항상 실시간 프로세스가 된다¦반드시 PID가 바뀐다¦메모리가 10배 증가한다¦nice 값이 높을수록 다른 작업에 양보합니다.
process¦PPID가 뜻하는 것은?¦부모 프로세스 ID¦프린터 포트¦페이지 크기¦패키지 버전¦PID와 부모 PID를 구분합니다.
jobs¦명령 끝의 &가 일반적으로 하는 일은?¦백그라운드 실행¦무조건 삭제¦표준 입력 파일 생성¦로그아웃¦&로 셸이 명령 완료를 기다리지 않게 합니다.
jobs¦현재 셸의 작업 목록을 확인하는 명령은?¦jobs¦lsmod¦rpm -qa¦whoami¦jobs는 그 셸이 관리하는 작업을 봅니다.
jobs¦보통 Ctrl+Z를 누르면 실행 작업은?¦정지한다¦항상 정상 종료한다¦디스크에 압축된다¦새 UID가 된다¦정지된 작업은 bg나 fg로 계속할 수 있습니다.
jobs¦정지한 작업을 포그라운드로 가져오는 명령은?¦fg¦bg¦nohup만¦kill -9만¦fg는 포그라운드 실행으로 전환합니다.
schedule¦crontab 시간 필드 순서는?¦분 시 일 월 요일¦시 분 월 일 년¦초 분 시 일 월¦요일 년 시 분 초¦사용자 crontab은 다섯 시간 필드 뒤에 명령이 옵니다.
schedule¦0 2 * * * 의 의미는?¦매일 02:00¦매시간 02분¦2월 0일¦매주 월요일 00:02¦분 0, 시 2이며 나머지는 모든 값입니다.
schedule¦일회성 작업 예약에 적절한 도구는?¦at¦crontab -l¦jobs만¦nice¦at은 지정 시각의 일회성 작업을 예약합니다.
schedule¦현재 사용자의 crontab 목록을 확인하는 옵션은?¦crontab -l¦crontab -e¦crontab -r¦crontab -u만¦-l은 조회, -e는 편집, -r은 제거입니다.
editors¦vi에서 입력 모드로 들어가는 대표 키는?¦i¦Esc¦:q!¦dd¦i로 입력하고 Esc로 명령 모드에 돌아옵니다.
editors¦vi에서 저장하고 종료하는 명령은?¦:wq¦:q!¦dd¦/q¦:wq는 저장 후 종료합니다.
editors¦vi에서 변경을 버리고 종료하려면?¦:q!¦:wq¦:w¦yy¦느낌표를 붙인 q는 저장되지 않은 변경을 버립니다.
editors¦vi에서 한 줄을 삭제하는 명령 모드 키는?¦dd¦yy¦p¦i¦dd는 줄 삭제, yy는 줄 복사입니다.
editors¦nano와 Emacs에 관한 올바른 설명은?¦둘 다 텍스트 에디터다¦둘 다 파일시스템 종류다¦둘 다 커널 모듈이다¦둘 다 패키지 확장자다¦에디터별 사용 방식과 키 구성을 구분합니다.
rpm¦설치된 패키지 전체를 조회하는 명령은?¦rpm -qa¦rpm -e¦rpm -ivh¦rpm -Uvh¦q는 조회, a는 전체입니다.
rpm¦설치된 패키지를 제거하는 명령은?¦rpm -e 이름¦rpm -qi 이름¦rpm -ql 이름¦rpm -q 이름¦-e는 제거입니다.
rpm¦설치된 RPM의 파일 목록을 확인하는 옵션은?¦rpm -ql¦rpm -qi¦rpm -qa¦rpm -e¦-ql은 설치 파일 목록입니다.
rpm¦dnf와 rpm을 비교한 설명으로 적절한 것은?¦dnf는 저장소·의존성 해결을 함께 다룬다¦rpm은 Debian 전용이다¦dnf는 파일시스템 포맷 도구다¦둘 다 오직 암호만 변경한다¦상위 패키지 관리자와 저수준 도구의 차이를 구분합니다.
debian¦Debian 패키지 파일 확장자는?¦.deb¦.rpm¦.iso만¦.ko¦.deb는 Debian 계열 패키지입니다.
debian¦로컬 .deb 파일 설치 명령은?¦dpkg -i 파일.deb¦rpm -ivh 파일.deb¦apt update 파일.deb만¦tar -i 파일.deb¦dpkg -i는 로컬 패키지를 설치합니다.
debian¦apt update의 역할은?¦저장소 패키지 목록 갱신¦설치 패키지 전부 즉시 업그레이드¦커널 소스 자동 삭제¦계정 암호 변경¦목록 갱신과 apt upgrade를 구별합니다.
debian¦설치 패키지를 업그레이드하는 APT 명령은?¦apt upgrade¦apt update만¦dpkg -l만¦apt search만¦upgrade는 설치 패키지 갱신입니다.
source¦전통적인 소스 빌드 순서로 적절한 것은?¦configure → make → make install¦make install → configure → make¦rpm -e → fsck → cd¦passwd → useradd → tar¦프로젝트 설명에 따라 설정·빌드·설치를 진행합니다.
source¦Makefile을 읽어 의존 관계에 따라 빌드하는 도구는?¦make¦man¦mount¦mail¦make는 목표와 의존 관계에 따라 작업합니다.
source¦./configure --prefix의 주된 용도는?¦설치 경로 지정¦시그널 번호 지정¦IP 주소 고정¦프로세스 강제 종료¦많은 configure 스크립트에서 설치 경로를 설정합니다.
source¦패키지 관리자 밖에서 소스 설치할 때 고려할 점은?¦설치 파일 추적·삭제 방법¦어떤 파일도 생성되지 않는다는 가정¦항상 자동으로 rpm DB에 등록됨¦컴파일러가 항상 불필요함¦설치 방식과 관리·제거 방법을 함께 확인합니다.
devices¦블록 장치 목록을 조사하는 명령은?¦lsblk¦lsmod¦lsusb만¦lspci만¦디스크·파티션 같은 블록 장치를 봅니다.
devices¦USB 장치를 조사하는 명령은?¦lsusb¦lspci¦jobs¦lpq¦장치 버스와 조사 명령을 구별합니다.
devices¦udev의 역할에 가까운 것은?¦장치 이벤트·이름·권한 관리¦사용자 메일 수신¦tar 압축¦브라우저 북마크 동기화¦udev는 장치 이벤트를 처리합니다.
devices¦적재된 커널 모듈 목록을 보는 명령은?¦lsmod¦modprobe만¦mkdir¦lpstat¦lsmod는 목록, modprobe는 적재·제거에 사용합니다.
devices¦스캐너 지원과 관련 있는 구성 요소는?¦SANE¦GRUB2¦APT¦Bash alias¦스캐너 SANE와 사운드 ALSA를 구분합니다.
printing¦리눅스 인쇄 시스템으로 널리 쓰이는 것은?¦CUPS¦GRUB¦SSHFS만¦GPT¦CUPS는 프린터와 인쇄 작업을 관리합니다.
printing¦인쇄 요청에 쓰는 대표 명령은?¦lpr¦lpq¦lsmod¦fdisk¦lpr/lp는 요청, lpq/lpstat은 조회입니다.
printing¦인쇄 대기열 확인 명령은?¦lpq¦lpr만¦rmdir¦umount¦대기 작업 번호를 확인한 뒤 취소할 수 있습니다.
printing¦인쇄 작업 취소에 쓰는 명령은?¦lprm¦lpr만¦lpq만¦lsusb¦lprm 또는 cancel로 인쇄 작업을 취소합니다.
xwindow¦X 서버가 주로 관리하는 것은?¦디스플레이와 입력 장치¦HTTP 문서만¦사용자 암호 해시만¦파티션 테이블만¦X의 서버는 화면·입력 장치를 제공합니다.
xwindow¦X 클라이언트에 해당하는 것은?¦X 화면을 사용하는 응용프로그램¦반드시 모니터 하드웨어만¦GRUB 설정 파일¦스왑 파티션¦X 클라이언트는 X 서버에 화면 처리를 요청합니다.
xwindow¦DISPLAY 환경변수의 용도는?¦연결할 X 디스플레이 지정¦패키지 저장소 선택¦기본 게이트웨이 지정¦프린터 용지 선택¦호스트·디스플레이 번호 등을 표현합니다.
xwindow¦윈도 매니저의 역할은?¦창 배치와 테두리 관리¦IP 라우팅만¦커널 적재¦계정 암호 생성¦창 관리와 그래픽 로그인 관리의 역할을 구분합니다.
xwindow¦원격 X 응용프로그램을 내 PC 화면에 표시할 때 X 서버 위치는?¦화면·입력 장치가 있는 내 PC¦반드시 원격 응용 서버만¦반드시 DNS 서버만¦반드시 라우터만¦X의 서버·클라이언트는 일반 웹의 감각과 다를 수 있습니다.
desktop¦GNOME의 분류는?¦데스크톱 환경¦파티션 테이블¦패키지 확장자¦IP 주소¦GNOME과 KDE Plasma는 데스크톱 환경입니다.
desktop¦GDM의 역할에 가까운 것은?¦그래픽 로그인 관리¦파일시스템 포맷¦패키지 압축¦프로세스 시그널 전송¦디스플레이 매니저는 로그인 세션과 관련됩니다.
desktop¦설정된 X 세션을 시작하는 대표 명령은?¦startx¦lsblk¦useradd¦mount -a¦startx는 X 시작 스크립트를 사용합니다.
desktop¦LibreOffice의 용도는?¦사무 문서 작업¦커널 모듈 적재¦패키지 서명 전용¦하드디스크 파티션 전용¦워드프로세서·스프레드시트 등 사무 도구를 제공합니다.
desktop¦Firefox의 분류는?¦웹 브라우저¦부트 로더¦파일시스템¦디스플레이 매니저¦데스크톱 환경과 개별 응용프로그램을 구분합니다.
network¦TCP의 일반적인 특징은?¦연결과 신뢰성 제공¦항상 비연결이며 순서 무시¦IP 주소를 파일로 암호화¦오직 하드디스크 내부에서 동작¦TCP는 연결·재전송·순서 등을 제공합니다.
network¦UDP의 일반적인 특징은?¦비연결 데이터그램¦TCP와 동일한 연결 확립 필수¦파일 권한 설정¦패키지 의존성 해결¦UDP는 애플리케이션 목적에 맞게 선택합니다.
network¦이름을 IP 주소 등으로 조회하는 시스템은?¦DNS¦DHCP만¦CUPS¦GPT¦DNS는 여러 유형의 이름 정보를 조회합니다.
network¦주소 등 네트워크 설정을 자동 배정하는 것은?¦DHCP¦DNS만¦SMTP¦NFS만¦DHCP와 이름 조회 DNS를 구분합니다.
network¦OSI 참조 모델의 계층 수는?¦7¦4만¦2¦10¦OSI는 7계층 참조 모델입니다.
network¦일반적인 라우터가 경로 선택에 사용하는 주소는?¦IP 주소¦inode 번호¦UID¦프린터 작업 번호¦라우터는 네트워크 계층의 경로를 다룹니다.
address¦IPv4 주소 길이는?¦32비트¦128비트¦16비트¦64비트¦IPv6는 128비트입니다.
address¦IPv6 주소 길이는?¦128비트¦32비트¦48비트¦8비트¦IPv4와 IPv6 주소 공간을 구분합니다.
address¦IPv4 /24의 서브넷 마스크는?¦255.255.255.0¦255.0.0.0¦255.255.0.0¦0.0.0.255¦상위 24비트가 네트워크 비트입니다.
address¦루프백 IPv4 주소의 대표값은?¦127.0.0.1¦8.8.8.8¦192.168.1.255만¦0.0.0.0만¦루프백으로 자기 호스트와 통신합니다.
address¦사설 IPv4 범위에 속하는 주소는?¦172.20.1.2¦172.40.1.2¦8.8.8.8¦1.1.1.1¦172.16.0.0/12는 172.16~172.31 범위입니다.
address¦일반적인 /24 서브넷의 전체 주소 개수는?¦256¦254¦24¦255¦호스트에 흔히 쓰는 254개와 전체 주소 수 256개를 구별합니다.
netconfig¦현재 IP 주소를 조회하는 ip 하위 명령은?¦ip addr¦ip route만¦ip link delete¦ip netns delete¦주소 조회와 경로 조회를 구분합니다.
netconfig¦라우팅 정보를 조회하는 명령은?¦ip route¦ip addr만¦whoami¦rpm -q¦기본 게이트웨이 등 라우팅을 확인합니다.
netconfig¦소켓 정보를 확인하는 명령은?¦ss¦ps만¦ls만¦df¦ss는 소켓·연결 상태를 조사합니다.
netconfig¦로컬 호스트 이름 대응을 기록하는 파일은?¦/etc/hosts¦/etc/passwd¦/etc/shadow¦/etc/fstab¦hosts와 resolver 설정을 구분합니다.
netconfig¦resolver의 nameserver 설정을 볼 대표 파일은?¦/etc/resolv.conf¦/etc/group¦/etc/profile¦/etc/issue¦실제 파일은 관리 도구에 의해 생성될 수도 있습니다.
netconfig¦DNS 조회를 수행하는 대표 명령은?¦dig¦du¦dd¦df¦dig와 host는 DNS 질의에 사용합니다.
services¦SSH의 기본 TCP 포트는?¦22¦23¦25¦80¦SSH와 비암호화 Telnet의 포트를 구분합니다.
services¦HTTPS의 기본 TCP 포트는?¦443¦80¦53¦110¦HTTPS는 TLS를 사용하는 웹 통신입니다.
services¦메일 전송 서비스는?¦SMTP¦POP3만¦IMAP만¦DHCP¦SMTP는 전송, POP3·IMAP은 수신에 사용됩니다.
services¦DNS가 일반적으로 사용하는 포트 번호는?¦53¦22¦443¦631¦DNS는 용도에 따라 UDP와 TCP를 사용합니다.
services¦SSH 기반 파일 전송 방식은?¦SFTP¦일반 FTP¦HTTP만¦SMTP¦SFTP와 일반 FTP는 같은 프로토콜이 아닙니다.
services¦URL 내용을 파일로 저장할 때 적절한 예는?¦curl -o status.txt URL¦cd -o status.txt URL¦pwd URL¦chmod URL¦curl의 -o로 출력 파일을 지정합니다.
virtualization¦컨테이너와 가상 머신의 대표 차이는?¦컨테이너는 호스트 커널을 공유한다¦컨테이너마다 반드시 별도 게스트 커널 부팅¦가상 머신은 게스트 OS를 실행 못 한다¦둘은 무조건 같은 디스크만 사용¦컨테이너와 하이퍼바이저의 격리 단위가 다릅니다.
virtualization¦하이퍼바이저의 역할은?¦가상 머신 실행·자원 관리¦텍스트 정렬¦사용자 메일 수신¦파일 모드 계산¦가상 하드웨어와 게스트 실행을 관리합니다.
virtualization¦컨테이너 안 uname의 커널 정보 해석은?¦호스트 측 공유 커널 정보일 수 있다¦배포판 이름과 항상 동일¦컨테이너가 반드시 커널을 새로 설치했다는 뜻¦컨테이너 사용자 암호다¦사용자 공간 배포판과 커널을 구분해야 합니다.
virtualization¦컨테이너 이미지와 실행 컨테이너의 관계는?¦이미지는 실행 환경의 기반이다¦이미지는 오직 화면 스크린샷이다¦컨테이너는 이미지 수정 이력과 항상 같다¦이미지는 하드웨어 CPU다¦같은 이미지로 격리된 실행 인스턴스를 만들 수 있습니다.
cloud¦가상 서버·스토리지 같은 인프라 제공 모델은?¦IaaS¦SaaS만¦POP3¦CUPS¦IaaS는 인프라 자원을 제공합니다.
cloud¦완성된 소프트웨어를 서비스로 제공하는 모델은?¦SaaS¦IaaS만¦GRUB¦GPT¦SaaS는 응용프로그램 사용을 서비스로 제공합니다.
cloud¦애플리케이션 개발·배포 플랫폼을 제공하는 모델은?¦PaaS¦DNS¦MBR¦SMTP¦PaaS는 플랫폼 제공 모델입니다.
cloud¦프라이빗·퍼블릭을 결합한 배치 방식은?¦하이브리드 클라우드¦무조건 단일 로컬 디스크¦하드 링크¦파이프¦서비스 모델과 배치 모델을 구분합니다.
trends¦IoT의 설명으로 적절한 것은?¦연결된 사물의 데이터 수집·제어¦오직 종이 문서 인쇄¦CPU의 레지스터 한 개¦파일 이름 규칙만¦IoT는 사물의 연결과 데이터 활용을 다룹니다.
trends¦HPC와 가장 가까운 활용은?¦고성능 과학 계산¦오직 사용자 암호 변경¦터미널 글자 색 변경¦디스크 파티션 이름 변경¦여러 노드·가속기 등을 활용한 고성능 계산입니다.
trends¦SDN의 핵심 관점은?¦네트워크 제어와 전달의 분리¦파일 압축과 묶기의 결합¦디스크와 파티션의 동일시¦CPU와 계정의 동일시¦소프트웨어로 네트워크 제어를 다루는 관점입니다.
trends¦NFV가 다루는 것은?¦네트워크 기능의 소프트웨어 가상화¦파일 확장자 정렬¦사용자 홈 디렉터리 이동¦인쇄 용지 크기¦네트워크 기능과 전용 장비의 관계를 가상화합니다.
trends¦클러스터의 설명으로 적절한 것은?¦여러 노드가 협력하는 구성¦단 하나의 파일 권한 비트¦항상 같은 프로세스 번호¦브라우저 주소 표시줄¦클러스터는 목적에 따라 가용성·처리량·계산 등을 위해 구성합니다.
""".strip()

_FIRST_ONLY = {"overview", "history", "license", "distros", "installation", "partition", "boot"}
_BOTH = {"files", "basics", "users"}


def load_questions():
    counts, questions = {}, []
    for row in (_ROWS + "\n" + EXTRA_ROWS).splitlines():
        topic, stem, correct, a, b, c, explanation = row.split("¦")
        counts[topic] = counts.get(topic, 0) + 1
        stages = (1,) if topic in _FIRST_ONLY else ((1, 2) if topic in _BOTH else (2,))
        questions.append(Question(f"{topic}-{counts[topic]:02}", topic, stem,
                                  (correct, a, b, c), 0, explanation, stages))
    return tuple(questions)


QUESTIONS = load_questions()
QUESTION_BY_ID = {q.id: q for q in QUESTIONS}
