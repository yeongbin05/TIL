# 이미지(Image) 조회 / 삭제

### ✅ 다운받은 모든 이미지 조회

```bash
$ docker image ls
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e35a8144-c5ff-40f0-b123-384a331e35bb/8f83cc63-5793-438d-acb9-5ce8c0047175/Untitled.png)

- `ls` : list의 약자
- `REPOSITORY` : 이미지 이름(이미지명)
- `TAG` : 이미지 태그명
- `IMAGE ID` : 이미지 ID
- `CREATED` : 이미지가 생성된 날짜 (다운받은 날짜 X)
- `SIZE` : 이미지 크기

### ✅ 이미지 삭제

**[특정 이미지 삭제]**

```bash
$ docker image rm [이미지 ID 또는 이미지명]
```

- `rm` : remove의 약자
- `이미지 ID`를 입력할 때 전체 ID를 다 입력하지 않고 ID의 일부만 입력해도 된다.
(단, ID의 일부만 입력했을 때, 입력한 ID의 일부를 가진 이미지가 단 1개여야 한다.)
- 컨테이너에서 사용하고 있지 않은 이미지만 삭제가 가능하다.

**[중지된 컨테이너에서 사용하고 있는 이미지 강제 삭제하기]**

```bash
$ docker image rm -f [이미지 ID 또는 이미지명]
```

- 실행 중인 컨테이너에서 사용하고 있는 이미지는 강제로 삭제할 수 없다.

**[전체 이미지 삭제]**

```bash
# 컨테이너에서 사용하고 있지 않은 이미지만 전체 삭제
$ docker image rm $(docker images -q)

# 컨테이너에서 사용하고 있는 이미지를 포함해서 전체 이미지 삭제
$ docker image rm -f $(docker images -q)
```

- `docker images -q` : 시스템에 있는 모든 이미지의 ID를 반환한다. 여기서 `-q` 옵션은 quite를 의미하며, 상세 정보 대신에 각 이미지의 고유한 ID만 표시하도록 지시한다.