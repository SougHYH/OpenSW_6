# OpenSW_6 - Opsdroid

## 프로젝트 계획 이유
>조원들의 코딩 지식을 기반으로 협업하여, 채팅하는 bot을 만들기 위한 도구 혹은 틀(chat bot Framework)인 'opsdroid'라는 오픈 소스 코드를 분석한다. 특히 opsdroid에 핵심 기능인 skil, build, connector 부분으로 나눈어 자세히 분석한다. 이를 통해 코드 이해력과 실무 능력을 향상시키고, 동시에 분석한 오픈 소스의 문제점을 도출하고 새로운 기능을 추가하여 더 발전된 코드를 작성하는 것이다. 또한 팀원들은 오픈 소스 분석을 통한 실무 경험을 얻으며 개발 역량을 강화할 수 있다. 팀원 간의 협업은 소프트웨어 개발에 대한 이해도를 높이고, 코드 분석 능력을 기반으로 다양한 소스 코드의 이해와 개선에 기여할 것으로 기대된다. 이 프로젝트 경험을 통해 팀원들은 소프트웨어 개발 생태계에 참여하여 전문성을 증진할 것으로 기대된다.


## 개발 기간
#### 2023.11.20 ~ 2023.12.10

## 멤버 구성
황윤혁 - 총괄, 발표, opsdroid skill 개발  

신유진 - 계획서 작성, opsdroid skill 개발

이가영 - ppt 제작, opsdroid skill 개발

장익빈 - 계획서 작성, opsdroid skill 개발

이주영 - README.md 작성, opsdroid skill 개발

## 운영 환경 구축

자세한 내용을 다음 문서를 참조
[Opsdroid 공식문서](https://docs.opsdroid.dev/en/stable/quickstart.html)

## Opsdroid 실행 설명
+ ### linux 기준
    + Opsdroid 실행 방법
    ```
    $ opsdroid start
    ```
    + Opsdroid 종료 방법
    ```
    $ ^c
    ```

## Opsdroid 명령어 설명

+ ### !intro
    + Opsdroid 기반의 챗봇에서 사용자가 !intro 명령어를 입력하면  정해진 형식의 소개 메시지를 출력하는 Skill

+ ### !help
    + Opsdroid 기반의 챗봇에서 사용자가 !help 명령어를 입력하면 정의된 명령어 목록을 출력하는 Skill

+ ### !web
    + Opsdroid 기반의 챗봇에서 사용자가 !web 명령어를 입력하면 명지대학교의 공식 웹사이트로 이동할 수 있는 버튼을 Slack 블록 메시지로 출력하는 Skill

+ ### !map
    + Opsdroid 기반의 챗봇에서 사용자가 !map 명령어를 입력하면 명지대학교 캠퍼스 맵으로 이동할 수 있는 버튼을 Slack 블록 메시지로 출력하는 Skill

+ ### !menu
    + Opsdroid 기반의 챗봇에서 사용자가 !menu 명령어를 입력하면 명지대학교의 다양한 식당 메뉴에 대한 링크가 포함된 버튼을 Slack 블록 메시지로 출력하는 Skill

+ ### !room
    + Opsdroid 기반의 챗봇에서 사용자가 !room 명령어를 입력하고 이후에 강의실 번호를 입력하면 해당 강의실의 정보를 제공하는 Skill

+ ### !bus
    + Opsdroid 기반의 챗봇에서 사용자가 !bus 명령어를 입력하면 명지대학교 자연캠퍼스의 셔틀버스 정보를 확인할 수 있는 버튼이 Slack 블록 메시지로 출력되는 Skill

+ ### !calendar
    + Opsdroid 기반의 챗봇에서 사용자가 !calendar 명령어를 입력하면 명지대학교의 학사 일정을 확인할 수 있는 버튼이 Slack 블록 메시지로 출력되는 Skill

+ ### !library
    + Opsdroid 기반의 챗봇에서 사용자가 !library 명령어를 입력하면 명지대학교 자연캠퍼스 도서관의 정보를 Slack 블록 메시지로 출력하는 Skill

+ ### !calculator
    + Opsdroid 기반의 챗봇에서 사용자가 계산기 모드를 활성화하고 수학적인 표현식을 입력하면 해당 표현식을 계산하여 결과를 출력하는 Skill

+ ### !weather
    + Opsdroid 기반의 챗봇에서 사용자가 !weather 명령어를 입력하면 OpenWeatherMap API를 사용하여 현재 서울의 기온 및 습도를 가져와서 사용자에게 알려주는 Skill
