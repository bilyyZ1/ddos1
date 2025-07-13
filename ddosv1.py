import os
import time
import signal

# Blok CTRL+C
def block_ctrl_c(signum, frame):
    print("\n❌ Tidak bisa keluar. Termux masih dikunci.")

signal.signal(signal.SIGINT, block_ctrl_c)

def clear():
    os.system("clear")

def play_alarm():
    os.system("termux-volume music 15")
    os.system("termux-media-player play ~/butzlock/alarm.mp3")

def stop_alarm():
    os.system("termux-media-player stop")

def banner():
    print("\033[1;31m")
    print(r"""
████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║
   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║
   ██║   ██╔══╝  ██╔═══╝ ██║╚██╔╝██║██║   ██║
   ██║   ███████╗██║     ██║ ╚═╝ ██║╚██████╔╝
   ╚═╝   ╚══════╝╚═╝     ╚═╝     ╚═╝ ╚═════╝ 
    \033[0m
    [!] Termux dikunci oleh butzXploit
    [!] Masukkan password untuk membuka akses.
    """)

def permanent_lock():
    clear()
    play_alarm()
    print("\033[1;41m")
    print("\n[💀] Gagal 3x! TERMUX DIKUNCI TOTAL!")
    print("[❌] Tidak bisa lanjut.")
    print("[🔁] Tutup dan buka Termux pun tetap terkunci.")
    print("\033[0m")
    while True:
        time.sleep(1)

def lock_terminal():
    correct_password = "butz"
    play_alarm()
    attempts = 0
    while attempts < 3:
        pwd = input("\n🔐 Password: ")
        if pwd == correct_password:
            stop_alarm()
            print("\n✅ Akses diterima. Termux dibuka.")
            time.sleep(1)
            return True
        else:
            print("❌ Salah! Termux tetap terkunci.")
            attempts += 1
            time.sleep(1)
            clear()
            banner()
    permanent_lock()
    return False

def main():
    clear()
    banner()
    lock_terminal()

if __name__ == "__main__":
    main()