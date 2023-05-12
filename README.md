# Slack-Manager

<div align=center>
	<h3>📚 Tech Stacks 📚</h3>
	<p>✨ Platforms & Languages ✨</p>
</div>
<div align="center">
</div>
<br>
<div align=center>
	<p>🛠 Tools 🛠</p>
</div>
<div align=center>
		<img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white" />
			<img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=python&logoColor=white" />
				<img src="https://img.shields.io/badge/YAML-CB171E?style=flat&logo=YAML&logoColor=white" />
	<br>
	<img src="https://img.shields.io/badge/AWS-232F3E?style=flat&logo=AmazonAWS&logoColor=white" />
	<img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white" />
		<img src="https://img.shields.io/badge/PyCharm-000000?style=flat&logo=PyCharm&logoColor=white" />
		<img src="https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=flat&logo=VisualStudioCode&logoColor=white" />
	<br>
	<br>
	<div align=center>
	<p>👩‍💻 Profile. 👩‍💻</p>
</div>
		<img src="https://img.shields.io/badge/Instagram-E4405F?style=flat&logo=Instagram&logoColor=white" />
	<img src="https://img.shields.io/badge/Facebook-1877F2?style=flat&logo=Facebook&logoColor=white" />
</div>


### 🏁 Issue subject : Somma DevOps 통합 관리 플랫폼 개발
<br>

### 🏁 Issue description : 
Somma 개발 업무 프로세스에 대한 관리를 Slack을 통해 통합하고 자동화하여 사용할 수 있도록,
1개의 data platform에서 관리될 수 있도록 구현한다.
<br>

### 🏁 Issue expect result :
ws-OOO repo 1개(ws-OOO 파이프라인에 대한 Class 1개, 각 파이프라인에 대한 python 코드 모듈 n개)
<br>

### 🏁 Issue sub-task :
Slack-Somma 연동 모듈
기본 채널 알림, 메세지 폼 수정 기능, Slack 외부 APP에 대한 관리 문서
ws-ooo에 구현된 모듈에 지정한 채널을 통해 안전하고 지속적으로 동작할 수 있어야 함
<br>

아래 subtask들은 Slack 채널에서 최종 in/output이 동작하는 것을 기반으로 합니다.
목표 산출물은 Slack APP 형태(ex. Somma bot)로 모든 기능이 포함되면 좋습니다.
구현이 필요한 모든 모듈에 대해 API가 제공되는 것을 확인하고 작성하였습니다.
<br>

### 📌 기능 1. Jira 및 Confulence 연동 모듈
1️⃣ Jira 이슈에 대한 전반적인 관리 기능
- 이슈 생성
- 이슈 workflow 상태 변경
- 이슈 worklog 자동화
- 이슈 기한 알림
<br>
2️⃣ Confulence 문서에 대한 배포 알림 기능
- Confulence 문서 내 상태 값이 release일 경우 Slack 채널을 통한 알림
<br>

### 📌 기능 2. Github 연동 모듈
1️⃣ Github commit에 대한 전반적인 관리 기능
- commit 메세지에 대한 폼 검사
- commit 내용 확인
<br>
2️⃣ Github branch PR에 대한 전반적인 관리 기능
- PR 내용 확인
- PR 처리 기능
<br>

### 📌 기능 3. Monster/Cheiron 연동 모듈
1️⃣ CI/CD 프로세스 관리 기능
- 자동화 빌드 결과에 대한 알림 메세지
- 자동화 배포에 대한 알림 메세지
- 배포 결과물에 대한 CDN 다운로드 주소 연동
<br>

### 📌 기능 4. NAS 연동 모듈
1️⃣ Synology NAS에 대한 전반적인 관리 기능
- NAS 폴더/파일 조회
- NAS 파일 공유 및 URL 생성 기능
<br>

### 📌 기능 5. Dooray 연동 모듈
1️⃣ 출퇴근에 대한 전반적인 관리 기능
- 출근 기능
- 퇴근 기능
<br>
2️⃣ 문서 기안에 대한 관리 기능
- 휴가 신청
- 경비 신청
<br>

3️⃣ 점심 메뉴 확인 기능
