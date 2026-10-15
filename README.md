# 모아록 홈페이지 (moarok.com)

GitHub Pages 로 배포한다. `main` 에 push 하면 1분 안팎으로 https://moarok.com 에 반영된다.
**이 저장소는 공개다** — 비밀 값, 실제 회의 내용, 실명이 보이는 스크린샷을 넣지 않는다.

## 구조

| 경로 | 내용 |
|---|---|
| `src/template.html` | **고치는 곳.** 페이지 원본(문구·스타일·스크립트) |
| `src/brand/` | 로고 SVG — 앱 저장소 `branding/Moa-rok_brand_kit_v1_1/assets/svg` 에서 복사 |
| `assets/screenshots/` | 앱 스크린샷(합성 데이터 화면만) |
| `build.py` | `src/template.html` + 로고 → `index.html` |
| `index.html` | **빌드 결과.** 직접 고치지 않는다 |
| `CNAME` · `.nojekyll` | 도메인 연결·Pages 설정. 지우지 않는다 |

## 수정 순서

1. `src/template.html` 수정
2. `python build.py`
3. 브라우저로 `index.html` 확인(데스크톱·휴대폰 폭)
4. commit → push

## 내용 기준

- 대표 문구는 브랜드 키트 확정본(「대화에 집중하고 / 기억은 가볍게.」)을 쓴다.
- 요금: Free 0원·월 2시간(가입일 기준, 이월 없음) · Pro 14,900원/월·149,000원/년·월 10시간 ·
  Premium 24,900원/월·249,000원/년·월 25시간 · 추가 +5시간 5,900원·+10시간 9,900원.
  바뀌면 요금표와 아래 안내 문구를 함께 고친다.
- 숫자 실적·사용자 후기·언론 보도를 지어내지 않는다.
- 법적 문서(개인정보처리방침·이용약관·계정 삭제 안내)는 확정·검토 전까지 "게시 예정"으로 둔다.
  원본 초안은 앱 저장소 `web/`, 앱이 쓰는 주소는 앱 저장소 `constants/legal.ts`.
