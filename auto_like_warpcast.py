Baik, berikut adalah versi script Python yang menghilangkan fungsi login dan memungkinkan pengguna untuk mengunggah daftar target secara manual. Script ini akan fokus pada pembacaan daftar target dari file, pengiriman "like" ke setiap target dengan authorization token yang disediakan oleh pengguna, dan jeda acak antara likes.

### Script Python:

```python
import requests
import time
import random

# Fungsi untuk membaca daftar target dari file
def read_targets(file_path):
    with open(file_path, 'r') as file:
        targets = [line.strip() for line in file.readlines()]
    return targets

# Fungsi untuk mengirim "like" ke setiap target
def send_like(target, token):
    like_url = f"{target}/like"  # Pastikan endpoint like sesuai dengan API Warpcast
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(like_url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

# Fungsi utama
def main():
    # Dapatkan token dari pengguna
    token = input("Enter your Warpcast token: ")
    
    # Baca daftar target dari file
    file_path = input("Enter the path to your target file: ")
    targets = read_targets(file_path)
    
    # Jeda acak dalam detik
    min_delay = int(input("Enter minimum delay in seconds: "))
    max_delay = int(input("Enter maximum delay in seconds: "))
    
    # Memulai proses liking
    for idx, target in enumerate(targets, start=1):
        if send_like(target, token):
            print(f"[{idx}/{len(targets)}] Status Like: Success => like {target}")
        else:
            print(f"[{idx}/{len(targets)}] Status Like: Failed => like {target}")
        
        # Jeda acak antara likes
        delay = random.randint(min_delay, max_delay)
        print(f"Information: Waiting Delay {delay} Seconds")
        time.sleep(delay)

if __name__ == "__main__":
    main()
```

### Penjelasan Kode:

1. **Fungsi `read_targets`:**
   - Membaca daftar target dari file teks yang diberikan oleh pengguna. Setiap baris file diambil sebagai satu target.

2. **Fungsi `send_like`:**
   - Mengirimkan permintaan "like" ke setiap target dengan menyertakan token authorization yang diberikan oleh pengguna.

3. **Fungsi `main`:**
   - Mengumpulkan token authorization dari pengguna.
   - Membaca daftar target dari file yang diinputkan pengguna.
   - Mengatur jeda acak antara likes.
   - Mengirimkan "like" ke setiap target dan menampilkan status.

4. **Menggunakan `requests`:**
   - Untuk mengirim permintaan HTTP POST ke endpoint "like".

5. **Menggunakan `time` dan `random`:**
   - Untuk mengatur jeda acak antara likes.

### Cara Menjalankan:

1. Simpan script di atas dalam file, misalnya `auto_like_warpcast.py`.
2. Jalankan script dengan perintah:
   ```bash
   python auto_like_warpcast.py
   ```
3. Ikuti petunjuk yang muncul di terminal:
   - Masukkan token authorization.
   - Masukkan path ke file yang berisi daftar target.
   - Masukkan jeda minimum dan maksimum dalam detik.

### Format File Target

File target (`targets.txt` misalnya) harus berisi satu URL per baris, seperti ini:

```
https://warpcast.com/user1/like/0xabcdef
https://warpcast.com/user2/like/0x123456
https://warpcast.com/user3/like/0x789abc
...
```

Pastikan endpoint dan URL yang digunakan sesuai dengan dokumentasi dan kebutuhan API Warpcast.