# 개발과 검증

게임 실행에 필요한 설치 방법은 [README](../README.md)를 참고하세요.

## 현재 검증

2026-10-28 변경 미리보기 검증은 `grep` 출력 보존, 파일 생성·수정·삭제·권한 diff,
실제 `vi` 수정과 `quest diff` 재조회, 결과 확인 중 종료해도 완료 기록 유지까지 포함합니다.
심볼릭 링크를 따라가지 않고 FIFO를 열지 않으며, 큰 파일·많은 경로의 생략 범위를 표시합니다.
로컬 Docker/PTY를 포함한 전체 **58개 검사 통과**(skip 없음).

2026-10-27: Docker와 실제 PTY를 포함한 전체 **42개 검사 통과**(skip 없음).
선택한 큰 로고와 오른쪽 펭귄, 80×24 메뉴 배치, 작은 화면 대체 표시를 포함합니다.
README는 GitHub GFM 렌더링, 상대 링크, PNG 파일, 실제 CLI 출력 미리보기를 확인했습니다.

## 검사 실행

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
python3 linux-quest --build-lab
PYTHONPATH=src RUN_DOCKER_TESTS=1 python3 -m unittest discover -s tests -v
```

Docker 검사는 실습 26개 × 3개 난이도·변형 조합의 초기 실패·풀이 성공, 여러 권한 풀이,
일부 조건 실패, 컨테이너 격리·중단 복구를 확인합니다. PTY 검사는 실제 방향키 메뉴,
작은 터미널, 시작·힌트·초기화·이어하기, 셸 변수 유지, Ctrl+C/D, 실제 vi 편집을 확인합니다.
Docker 환경변수가 없으면 관련 검사는 명시적으로 skip합니다.

GitHub Actions도 콘텐츠 검사·이미지 빌드·실제 Docker/PTY 검사를 실행합니다.
콘텐츠 구조와 자동 검증 결과가 모든 문제의 교육적 완성도나 합격 가능성을 보증하지는 않습니다.

2026-10-27 로컬 검증: macOS ARM64, Python 3.15.0, Docker 29.8.2에서
Docker/PTY를 포함한 **26개 검사 전부 통과(건너뛴 검사 없음)**.
실습 풀이 검사는 26개 실습 × 3개 난이도·변형 조합, 총 78개 환경을 확인했습니다.
Windows 기본 환경, 실제 OS 설치·부팅·물리 장치는 검증 대상이 아닙니다.

같은 날 가독성 개선 후에는 총 **32개 검사**를 통과했습니다. 한글·긴 경로 줄바꿈,
색상 강제/해제, 미션·문제 전환 시 화면 초기화, 해설 확인 전 대기를 추가로 검증했습니다.
시작 화면 설정 추가 후에는 **40개 검사**를 통과했습니다. 설정 저장·재실행 적용,
기본 난이도 선택, 임시 CLI 옵션, 설정 복원 시 진도 보존을 포함합니다.

## 기준과 구조

2026년 리눅스마스터 2급을 기준으로 합니다. 기본 실습은 Rocky Linux 8이며 Debian 계열은
비교 설명·문제로 다룹니다. 문제는 자체 제작이며 공식 기출문제를 복제하지 않았습니다.
2027년 이후 응시에는 변경된 출제 환경을 별도로 확인해야 합니다.

- [KAIT 시험 안내·출제기준](https://www.ihd.or.kr/introducesubject1.do)
- [GNU Coreutils 매뉴얼](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [GNU Bash 매뉴얼](https://www.gnu.org/software/bash/manual/bash.html)
- [Rocky Linux 컨테이너](https://hub.docker.com/r/rockylinux/rockylinux)
- [Docker 보안·기본 seccomp 제약](https://docs.docker.com/engine/security/seccomp/)

`src/linux_quest/`의 campaign은 미션·초기 파일·조건·힌트, lessons/questions는 설명·평가,
runtime은 실제 Docker/PTY 연결, progress는 저장, app/ui는 화면과 학습 흐름을 담당합니다.
게임은 로컬에서 동작하며 계정·랭킹·원격 분석·유료 AI 연동은 없습니다.
