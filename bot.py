from pywhatsapp import WhatsApp

def callback(message):
    if message.content_type == "text":
        w.send_message(message.from_jid, "Hello, how can I help you?")

w = WhatsApp()
w.login()
w.set_message_callback(callback)
w.run()

Instal library PyWhatsApp dengan perintah "pip install pywhatsapp" di command prompt atau terminal.

Buat file Python baru dan import library PyWhatsApp dengan perintah "from pywhatsapp import WhatsApp".

Inisialisasi objek WhatsApp dengan perintah "w = WhatsApp()" dan masukkan nomor telepon Anda.

Jalankan perintah "w.login()" untuk masuk ke akun WhatsApp Anda.

Gunakan perintah "w.set_message_callback(callback)" untuk mendefinisikan fungsi callback yang akan dijalankan setiap ada pesan masuk. Dalam fungsi callback tersebut, Anda dapat menuliskan logika bot untuk membalas pesan secara otomatis.

Jalankan perintah "w.run()" untuk menjalankan bot Anda.
