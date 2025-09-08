import cv2
from ultralytics import YOLO


model = YOLO("best1.pt")

# 웹캠 열기
cap = cv2.VideoCapture(0)
labels = []
saved_frame = None

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while (len(labels)<10):
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # YOLO 추론
    results = model(frame)

    for box in results[0].boxes:
        cls = int(box.cls[0])        # 클래스 인덱스
        label = model.names[cls]     # 클래스 이름
        labels.append(label)

    # 화면에 YOLO 결과 출력
    annotated_frame = results[0].plot()
    cv2.imshow("YOLO Webcam", annotated_frame)

    if saved_frame is None:
        saved_frame = frame.copy()
        cv2.imwrite("saved_frame.jpg", saved_frame)
        print("프레임 저장 완료: saved_frame.jpg")
   

    # 현재 프레임의 라벨들 출력
    if labels:
        print("Detected Labels:", labels)

    # ESC 키(27)를 누르면 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

newlist=[]
for i in range(3):
    newlist.append(labels[i])



for i in range(len(labels)):
    a=newlist[0]
    b=newlist[1]
    c=newlist[2]

print("인식 한 것 : {}, {}, {} ".format(a,b,c))

cap.release()
cv2.destroyAllWindows()


