def send_data():
    global index
    if index < len(data_list):
        # 리스트의 다음 요소를 가져와서 클라이언트에게 전송
        data_to_send = data_list[index]
        # 여기서 data_to_send를 클라이언트로 전송하는 방법을 구현해야 합니다.
        # 이 예시에서는 jsonify를 사용하여 간단하게 데이터를 JSON 형식으로 반환합니다.
        # 실제로는 SocketIO나 다른 방법으로 클라이언트에게 데이터를 보내야 합니다.
        print(data_to_send)  # 예시로 출력
        index += 1

# APScheduler 설정
scheduler = BackgroundScheduler()
scheduler.add_job(send_data, 'interval', seconds=10)  # 10초마다 send_data 함수 실행
scheduler.start()