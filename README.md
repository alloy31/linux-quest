# Linux Quest

리눅스마스터 2급을 준비하며 실제 Linux 명령어를 사용하는 한국어 CLI 학습 게임입니다.
가상 기록 보관소의 신입 관리자가 백업 실패와 사라진 인수인계 기록을 조사합니다.

## 개발

Python 3.11 이상, macOS/Linux, Docker가 필요합니다. 호스트 Python 패키지 의존성은 없습니다.

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
docker build -t linux-quest:2026.1 src/linux_quest/assets/docker
```

메뉴·콘텐츠·통합 검증을 순차적으로 추가하고 있습니다. 실행 방법과 검증 결과는 구현과 함께 갱신합니다.

## 학습 기준

- 2026년 리눅스마스터 2급, 기본 실습 배포판 Rocky Linux 8
- [KAIT 시험 안내·출제기준](https://www.ihd.or.kr/introducesubject1.do)
- 설치·부팅·물리 장치는 상황형 학습, 명령어는 격리된 Docker 실습
- 모의문제는 자체 제작이며 공식 기출문제를 복제하지 않습니다.
