sudo apt update
sudo apt install python3-pip
pip3 install requests

git clone 

cd IPGeo

chmod +x ip_geolocator.py

python3 ip_geolocator.py 8.8.8.8
or
./ip_geolocator.py 8.8.8.8

สิ่งที่ควรทราบ 💡
การเชื่อมต่ออินเทอร์เน็ต (Internet Connection): สคริปต์นี้ต้องใช้การเชื่อมต่ออินเทอร์เน็ต เนื่องจากเป็นการเรียกข้อมูลตำแหน่งจากบริการ Public API ภายนอก (ในตัวอย่างคือ ip-api.com)

ความแม่นยำ (Accuracy)(ระดับต่ำระบุได้แค่เมืองหลวง)
    IP Address: 8.8.8.8 
    ประเทศ:     United States
    เมือง:       Mountain View
    ละติจูด (Lat): 37.386
    ลองจิจูด (Lon): -122.0838
    ผู้ให้บริการ (ISP): Google LLC
