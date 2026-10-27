# README 이미지

| 파일 | 제작 방식 |
| --- | --- |
| `linux-quest-cover.png` | built-in `image_gen`으로 생성한 소개용 픽셀 아트. 생성 결과를 변형 없이 저장했습니다. |
| `start-screen.png` | 실제 CLI를 PTY에서 실행해 받은 ANSI 출력을 PNG로 렌더링했습니다. |
| `first-mission.png` | 실제 Docker 실습의 첫 미션 출력을 같은 방식으로 렌더링했습니다. |

메인 화면은 선택된 1번 슬랜트 로고와 오른쪽 펭귄, 회색 `made by alloy` 크레딧을 보여줍니다.
실행 화면 이미지는 가상의 UI 문구를 합성한 목업이 아닌 프로그램의 실제 출력입니다. 터미널 창 장식과 색상 팔레트는 문서용으로 렌더링했습니다.

## 커버 생성 프롬프트

```text
Use case: stylized-concept.
Asset type: a polished wide GitHub README cover illustration for Linux Quest, a Korean terminal learning game for Linux Master level 2.
Composition: landscape 2.5:1 banner, about 1600x640, generous breathing room, readable when displayed 850px wide. A large slanted monospaced title on the left, a friendly black-and-white Linux penguin seated to the RIGHT, recalling a classic terminal mascot. Make this a designed pixel-art game title screen illustration, not a fabricated screenshot of the application.
Scene: restrained dark navy archive/server room, subtle racks and cyan terminal light, tiny amber accent, crisp intentional pixel clusters and clean silhouette. Premium retro computer-game aesthetic, warm and approachable rather than hacker menace. Keep foreground objects simple and uncluttered.
Text must be exactly: "LINUX" on the first large line and "QUEST" on the second large line. Small lower-center gray author credit: "made by alloy". No other words, numbers, badges or metrics. Do not add mock buttons or screenshots. No glossy 3D, no gradients that obscure the text, no watermarks. The penguin must be clearly recognizable and must not overlap the title.
```

## 실행 화면 다시 만들기

Pillow가 설치된 개발 환경에서 실행합니다. 게임 실행에는 Pillow가 필요하지 않습니다.

```bash
python3 scripts/capture-readme.py
```

기본 글꼴 경로는 macOS 기준입니다. 다른 환경에서는 `--mono-font`와 `--cjk-font`로 글꼴을 지정하세요.
스크립트는 임시 저장 디렉터리를 사용하며, 개인 진도나 설정을 읽지 않습니다. 첫 미션 캡처에는 준비된 Docker 실습 이미지가 필요합니다.
