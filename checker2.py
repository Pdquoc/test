import socket
import requests
import concurrent.futures

def check_proxy(proxy):
    try:
        socket.setdefaulttimeout(5)
        host, port = proxy.split(':')
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, int(port)))
        return True
    except:
        pass
    return False

def get_proxy_info(proxy):
    try:
        url = f"https://ipinfo.io/{proxy.split(':')[0]}/json"
        response = requests.get(url)
        data = response.json()
        country = data.get('country', 'N/A')
        isp = data.get('org', 'N/A')
        return country, isp
    except:
        return 'N/A', 'N/A'

def remove_dead_proxies(input_file):
    with open(input_file, 'r') as file:
        proxies = file.readlines()

    alive_proxies = []
    proxy_count = len(proxies)
    live_proxy_count = 0
    die_proxy_count = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for proxy in proxies:
            future = executor.submit(check_proxy, proxy.strip())
            futures.append((proxy.strip(), future))

        for proxy, future in futures:
            if future.result():
                country, isp = get_proxy_info(proxy)
                alive_proxies.append(proxy)
                live_proxy_count += 1
                print(f'| Live \x1b[38;5;255m| \x1b[38;5;119m{proxy} \x1b[38;5;226m> \x1b[38;5;119m{country} \x1b[38;5;226m> \x1b[38;5;119m{isp}\x1b[38;5;255m')
            else:
                print(f'| \x1b[38;5;196mDie \x1b[38;5;255m| \x1b[38;5;196m{proxy}\x1b[38;5;255m')
                if remove_proxy(proxy):
                    print(f'| \x1b[38;5;196mDelete \x1b[38;5;255m| \x1b[38;5;196m{proxy}\x1b[38;5;255m')
                    die_proxy_count += 1
                else:
                    print(f'| \x1b[38;5;196mDie \x1b[38;5;255m| \x1b[38;5;196m{proxy}\x1b[38;5;255m')

    with open(input_file, 'w') as file:
        file.write('\n'.join(alive_proxies))

    print(f'\n\x1b[38;5;226mTotal \x1b[38;5;255m{proxy_count} > \x1b[38;5;119mLive\x1b[38;5;255m/\x1b[38;5;196mDie \x1b[38;5;255m(\x1b[38;5;119m{live_proxy_count}\x1b[38;5;255m/\x1b[38;5;196m{die_proxy_count}\x1b[38;5;255m)')

def remove_proxy(proxy):
    try:
        with open(input_file, 'r') as file:
            proxies = file.readlines()

        with open(input_file, 'w') as file:
            for line in proxies:
                if line.strip() != proxy:
                    file.write(line)

        return True
    except:
        return False

input_file = input("> Nhập File Proxies: ")

remove_dead_proxies(input_file)