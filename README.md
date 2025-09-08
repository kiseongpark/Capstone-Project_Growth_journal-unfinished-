## 해야할 것

Gemini api 사용하도록 코드 변경


[참고 링크](https://www.magicaiprompts.com/docs/develop-ai-service/gemeni-multimodal-api/)


** 특히 2번 잘 참고해서 만들어 보기


0. api 사용환경 잘 구축하기

1. image_path 잘 설정하기(이 폴더에 있는 웹캠에서 촬영한 이미지 사용하도록)

2. 아래 코드 잘 수정해서 성장일지 내용 제공받기


```
response = model.generate_content([
    "Describe this image in detail:",# 여긴 지시문이다. 우리가 원하는 내용 얻을 수 있도록 만들기(ex 어느 정도 성장?, 팁 얻기)
    {"mime_type": "image/jpeg", "data": image_data} # level이 저장된 변수 주기, 촬영한 프레임 주기(image_path에 저장) - 다양한 방식으로 데이터 전달해보기)
])

```


3. 위 코드에서 level에 대한 설명도 지시문에 넣어야 할듯


4. print(response.text)에서 원하는 답변 잘 나오는지 확인


---
위에 알고리즘은 클래스 10개만 배열에 저장하고, 그중 초반에 인식된 3개의 클래스만 변수에 저장하여 사용하는 방식


동시에 첫 프레임은 이미지 파일로 저장한다.
