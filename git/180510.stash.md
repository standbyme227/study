# Git Stash

## 공부하게된 시점

>git 사용을 하던 중, branch 에러로 인해서  
dev commit이 master로 push되는 현상을 겪게되어   
물어물어 보던중 기능을 알게 됨

## Stash란??

>흔히 개발을 하던 중 commit이 불가하지만  
branch를 변경해야하는 상황에서 임시저장(?)의 느낌으로 사용한다.

- ### 사용방법
  >git stash 라고 입력한다.
- ### 기능
  >스택에 새로운 stash가 만들어지  
  커밋하기 애매했던 파일들이 저장된다.  

  >그리고 워킹 디렉토리는 깨끗해진다.

  >git stash list 명령어로 저장된 Stash 목록을 확인가능하다.
- ### 적용범위
  >1. Modified + Tracked 파일.  
  (한번이라도 add 한적이 있는 추적가능한 파일)
  >2. Staging Area에 있는 파일.

## Stash를 다시 적용 시키려면??

> 일반적으로 긴급하거나 먼저 처리할 부분이 정리되면  
이전의 stash 파일들을 다시 적용시켜야할 순간이 올수도 있다.

- ### 적용 명령어
  >git stash apply

  >git stash list로 목록을 확인한 뒤에  
  git stash apply(가장 최근 stash 적용) 혹은  
  git stash apply StashName 으로 적용가능하다.

  - #### 옵션
    > git stash apply --index 로  
    Staged 상태까지 적용 시킬 수 있다.

    > git stash -u untracked 파일도 함께 저장시켜준다.

## Stash를 삭제하고 싶다면?

> 모든 처리를 완료한 뒤에  
임시저장을 위해 처리한 stash가  
필요없음을 알게된다면,  
삭제를 해서 헷갈리지 않게 처리해 둬야한다.

- ### 삭제 명령어
  >git stash drop StashName  
  명시된 stash를 삭제한다.

  >git stash pop은  
  **적용** 후 삭제 명령어이다.

## Stash를 새로운 브랜치에 적용하고 싶다면??

> 앞서 처리할건 다 처리되었지만  
아직 stash 부분이 애매하다면,  
새로운 브랜치에 적용해서 시행해보고 판단하는게 좋을거 같다.

- ### 브랜치 생성 후 적용 명령어
  >git stash branch
  새로운 브랜치를 생성하고  
  그 부분에 적용을 시키는 명령어이다.

  >stash를 생성할 때 실행시키는 명령어로써  
  따로 스택에 저장하는게 아닌
  새로운 branch에 바로 적용을 시키는거라
  적용된 stash는 삭제된다.


## 활용도

>아직 branch의 이동만으로도  
충분히 여러 문제를 해결하고 있지만
이건 아마도 아직 프로젝트가 엄청 대규모가 아니기에  
가능한 부분인거 같다.  

>고로 현재 바로 적용시키진 않겠지만
나중엔 꼭 사용할 기능이지 않을까 싶다.

# 20.18.05.10
