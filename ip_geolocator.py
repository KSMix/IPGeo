#!/usr/bin/env python3

import requests
import sys

def geolocate_ip(ip_address):
    """
    ดึงข้อมูล Geolocation (ละติจูดและลองจิจูด) จาก IP Address
    โดยใช้บริการ ip-api.com
    """
    # API endpoint สำหรับการเรียกข้อมูลแบบ JSON
    api_url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,city,lat,lon,isp"
    
    try:
        # ส่ง HTTP GET request ไปยัง API
        response = requests.get(api_url)
        response.raise_for_status() # ตรวจสอบ Error
        data = response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"[-] เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
        return

    # ตรวจสอบสถานะการตอบกลับ
    if data.get('status') == 'success':
        print("\n[+] ข้อมูล Geolocation สำเร็จ:")
        print(f"    IP Address: {ip_address}")
        print(f"    ประเทศ:     {data.get('country')}")
        print(f"    เมือง:       {data.get('city')}")
        print(f"    ละติจูด (Lat): {data.get('lat')}")
        print(f"    ลองจิจูด (Lon): {data.get('lon')}")
        print(f"    ผู้ให้บริการ (ISP): {data.get('isp')}")
        
    else:
        print(f"\n[-] ไม่สามารถค้นหาตำแหน่งของ IP '{ip_address}' ได้")
        print(f"    ข้อความแจ้งเตือน: {data.get('message', 'ไม่ทราบข้อผิดพลาด')}")

def main():
    if len(sys.argv) != 2:
        print(f"การใช้งาน: python3 {sys.argv[0]} <IP_Address>")
        print(f"ตัวอย่าง:  python3 {sys.argv[0]} 8.8.8.8")
        sys.exit(1)
    
    ip_to_check = sys.argv[1]
    geolocate_ip(ip_to_check)

if __name__ == "__main__":
    main()
