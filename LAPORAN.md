# Sumber

[https://github.com/davidaparicio/swarm-ollama/](https://github.com/davidaparicio/swarm-ollama/)

# Pendahuluan

Ini adalah implementasi algoritma *swarm optimization*. Proyek ini menggunakan konsep optimasi swarm, yang mengambil inspirasi dari perilaku koloni semut. Dalam optimasi swarm, beberapa "agregat" (seperti semut) bekerja bersama untuk mencari solusi terbaik untuk suatu masalah. Dalam konteks proyek ini, agregat-agregat ini mencari cara terbaik untuk mengurangi error atau loss pada model LLM. Dengan menggabungkan optimasi swarm dan model LLM, proyek ini bertujuan untuk meningkatkan akurasi dan efisiensi model LLM, sehingga dapat digunakan lebih baik dalam berbagai aplikasi.

  

Swarm optimization asli dari OpenAI adalah salah satu framework yang digunakan untuk mengelola dan mengatur sistem multi-agent. Proyek swarm-ollama adalah implementasi khusus dari swarm optimization untuk model Ollama.

  

Berikut adalah beberapa perbedaan utama dan keunggulan dari swarm optimization di OpenAI dan Ollama:

-   Swarm optimization di OpenAI biasanya digunakan untuk berbagai model OpenAI seperti GPT-3 dan GPT-4, sedangkan swarm-ollama khusus untuk model Ollama.
    
-   OpenAI lebih berfokus pada aplikasi besar dan beragam, sementara swarm-ollama lebih terfokus pada penggunaan lokal dan eksperimental.
    
-   Swarm-ollama dirancang untuk menjadi lebih ringan, mudah dikontrol, dan mudah diuji, sehingga cocok untuk pengembangan dan eksperimen.
    

  

Keunggulan Swarm-ollama:

-   Kemudahan Penggunaan: Swarm-ollama dirancang untuk penggunaan lokal, yang artinya kamu bisa menjalankan model tanpa perlu mengirim data ke server cloud. Ini memberi keuntungan dalam hal privasi dan keamanan data.
    
-   Menggunakan swarm-ollama bisa lebih hemat biaya dibandingkan OpenAI, terutama untuk penggunaan yang intensif.
    
-   Swarm-ollama menawarkan kontrol yang lebih baik atas sistem multi-agent, memungkinkan kamu untuk mengembangkan solusi yang skala besar namun tetap mudah digunakan.
    

# Multi-agent

Sistem *multi-agent* adalah kumpulan dari agen-agen yang bekerja bersama untuk menyelesaikan tugas atau masalah tertentu. Agen adalah program atau perangkat lunak yang dapat mengambil keputusan dan bertindak secara mandiri atau berinteraksi dengan agen lain dan lingkungan sekitarnya untuk mencapai tujuan tertentu. Agen dapat berkomunikasi dengan agen lain, berbagi informasi, dan bekerja sama.

  

Cara Kerja Multi-Agent:

-   Inisialisasi Agen
    

	-   Setiap agen diinisialisasi dengan tugas atau fungsi spesifik
    
	-   Misalnya, satu agen mungkin bertanggung jawab untuk pemesanan tiket, sementara agen lain menangani layanan pelanggan.
    

-   Interaksi Antar Agen:
    

	-   Agen-agen ini berkomunikasi melalui pesan atau protokol komunikasi tertentu.
    
	-   Mereka dapat meminta bantuan, berbagi data, atau mengoordinasikan tindakan mereka.
    

-   Kolaborasi dan Koordinasi:
    

	-   Agen-agen bekerja bersama untuk mencapai tujuan bersama
    
	-   Mereka mungkin harus bernegosiasi, merencanakan, dan menyusun strategi untuk menyelesaikan tugas dengan efisien.
    

-   Pengambilan Keputusan:
    

	-   Agen dapat mengambil keputusan secara mandiri berdasarkan informasi yang mereka miliki dan tujuan yang ingin dicapai
    
	-   Mereka dapat menggunakan algoritma optimasi, aturan logika, atau metode lain untuk membuat keputusan.

Dengan ini, sistem multi-agent memungkinkan solusi yang lebih fleksibel dan efisien untuk menangani berbagai masalah yang kompleks.

 Keunggulan Sistem Multi-Agent:

-   Dengan menggunakan beberapa agen yang bekerja bersama, sistem ini dapat menangani banyak permintaan pelanggan secara bersamaan, sehingga lebih efisien.
    
-   Sistem ini dirancang untuk mudah digunakan, sehingga pelanggan dapat dengan cepat mendapatkan jawaban atau solusi atas permintaan mereka.
    
-   Dengan menggunakan model LLM, aplikasi ini dapat memberikan jawaban yang lebih alami dan sesuai dengan konteks, meningkatkan kualitas layanan pelanggan.
    
Contoh Penerapan Multi-Agent

-   Sistem Pemesanan Tiket: Beberapa agen bekerja bersama untuk mencari penerbangan, memesan tiket, dan mengelola check-in.
    
-   Manajemen Rantai Pasokan: Agen-agen yang berbeda mengelola produksi, distribusi, dan inventaris dalam sebuah perusahaan.
    
-   Robotika: Beberapa robot (agen) bekerja bersama untuk menyelesaikan tugas-tugas kompleks, seperti pembersihan atau pencarian dan penyelamatan.
    
Dengan sistem multi-agent ini, AI dapat memberikan layanan yang lebih baik dan responsif kepada pelanggan mereka.  

# Adaptasi

-   Lakukan `ollama pull llama3.2:3b` pada terminal karena itu adalah model yang digunakan
    
-   Aplikasi yang diadaptasikan adalah `airline.py` dan dan `triage_agent.py`
    
-   Agar kedua aplikasi tersebut bisa berjalan
	-   Directory `swarm_ollama` yang berada di bagian paling depan repository tersebut harus dipindahkan ke dalam directory `airline` dan `triage_agent` agar kedua aplikasi tersebut dapat menggunakan kode dari swarm_ollama
    
-   Pada `swarm_ollama/core.py` `handle_tool_calls()`, kode berikut ditambahkan pada baris ke-134 sebelum variabel `raw_result`

```py    
if not args:
	args = {}
```

-   Pada `swarm_ollama/repl/repl.py`, ganti `message['sender']` pada baris ke-43 jadi `message['role']`
    
-   Tambahkan `**kwargs` pada dalam kurung dari setiap function yang agent pada `agents.py` & `tools.py`
    

# Cara menggunakan github tersebut

-   Buat directory baru
```bash
mkdir swarm
```
-   Clone repository tersebut
```bash    
git clone https://github.com/davidaparicio/swarm-ollama.git
cd swarm/swarm-ollama
```
-   Buat enviroment & jalankan
```bash
conda create -n swarm
pip install -r requirements.txt
```

# Implementasi

## airline.py

Aplikasi airline dalam repository ini adalah sebuah sistem multi-agent yang dirancang untuk menangani berbagai permintaan layanan pelanggan dalam konteks maskapai penerbangan.

 Fungsi utama:

-   Pengelolaan Permintaan Pelanggan: Aplikasi ini dapat mengelola berbagai permintaan pelanggan, seperti pemesanan tiket, perubahan jadwal, dan pertanyaan lainnya.
-   Interaksi Multi-Agent:
	-   Aplikasi ini menggunakan sistem multi-agent, yang berarti beberapa "agent" (seperti bot atau sistem otomatis) bekerja bersama untuk memenuhi permintaan pelanggan   
	-   Dalam sistem multi-agent untuk aplikasi airline, berbagai "agent" (atau agen) bekerja bersama untuk menangani berbagai aspek operasional maskapai penerbangan.
	-   Berikut adalah beberapa agen dan fungsi mereka:
    
| Agen-agen          | Kegunaan                         |
| ------------------ | --------------------------------- |
| Triase | Menentukan agen mana yang harus menjawab permintaan pengguna |
| Modifikasi penerbangan | Permintaan untuk modifikasi penerbangan. Agen ini dibagi lagi menjadi: Agen pembatalan penerbangan dan agen perubahan penerbangan |
| Kehilangan bagasi | Agen ini memantau status penerbangan secara real-time, memberikan update kepada pelanggan tentang kapan pesawat akan lepas landas atau tiba. |
-   Penggunaan Model LLM: Aplikasi ini menggunakan model LLM (Large Language Model) untuk berinteraksi dengan pelanggan dengan bahasa yang alami dan mudah dipahami.

Keunggulan Aplikasi:

-   Dengan menggunakan sistem multi-agent, aplikasi ini dapat menangani banyak permintaan pelanggan secara bersamaan, sehingga lebih efisien.
-   Aplikasi ini dirancang untuk mudah digunakan, sehingga pelanggan dapat dengan cepat mendapatkan jawaban atau solusi atas permintaan mereka.
-   Dengan menggunakan model LLM, aplikasi ini dapat memberikan jawaban yang lebih alami dan sesuai dengan konteks serta meningkatkan kualitas layanan pelanggan.
    
Dengan aplikasi airline ini, maskapai penerbangan dapat memberikan layanan yang lebih baik dan responsif kepada pelanggan mereka.

### Cara menggunakan
```bash
cd examples/airline
python3 main.py
```

### Pengujian

Kita mencoba untuk mengubah jadwal penerbangan kita:

-   Kita menyebutkan nomor tiket
-   Tanggal dan waktu penerbangan sebelum dan sesudah diubah  
-   Bot dapat mencarikan alternatif jadwal penerbangan yang sesuai jika tidak sesuai dengan yang kita inginkan.
-   Botnya punya inisiatif untuk mencari info yang sekiranya kita butuhkan
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf-gGRvOzM2F6oKdjggG_UXKGg0lPHp46A70siItMO9wy2xqb-LxGj2VcIOgMOZaTJW-9VM8ggkdbEXQz5P1lrux5ES1RAVI7_IbMiyHIY6y8epeL7j1wU-50iRpQcQGWbfS0Fnyw?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfSy5Y_57Stv0XlAjMbB93nFrAurmUBvp8Pk2opVnAIKMqNuWdgvtQmLq01lo8F8D5_L6dOkiUgBOgDNCewZnPSbqb9czANWjXiZDb7iLPBIon3nNddL_z6oKlMTd8mknTzVbt4Jg?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf6fgxqxzLG18xznWfnVysk2SHcoserKoZ9lsqxb9kzWPUHBX8ak_xyUdGsZGYFe6BWZa6LfP1Fbv2L0bsKLIZeH4_-btI0ulUEUVTD0RG4f5EdIqOPKx2qfpAl6ssUm4YRR2Xekw?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeGI9X0shvLHpafgO-7E4SN-G6mC0oTWBS-7s3cQKCxq11asoE-9EQaj7PMdL-rDreSEMTRUFrYDHVKqzJoVlcZBzqp9BmQe2k2MzsaS8kg_KQRvr_QosJVZWhhZXppNavDI_nb?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXenoD475uW7M2WBQOY_YpP1PPg6RHf1y7idgsOHMXNAgX7xXQHIgNAakWHlHEvNScWHaOOyREQmv6QJUZ0VxQXVgdSymSwk6TfZbhrYfQ9R9XsNSlywycO6MWdxAAsCnGvVGS3W_A?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfNLHx5m_2MD1PKvLsJcP5EAjxs7-RqpmcMzL-tQH-m_wqN1Y59TZ7cMMgUunScmKufTyMJMEOWfiOUwaNYFdVEOqk3lVQAt_dkkiTVvt7nDHder6wG6EkxBNWis-hGarD7s6qRkA?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcUs7IifPOlon843ijpYP9qAgeFJIlmeemz4zBol2xYqi0sxhK4ATGHEEmYn8ZenCb8B424TIrX7Mu7doubiYpY2F1ODLO_Gi-65VnIArU369P3ftz1l5nzkdKcbYZcCqpU1-Rb?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcS0PucBnYHRji4G6vLvMDwv06lbm87WdEmEb3OeFHRmvTRj0s_EVlCy5J16ZPDrXo4pEd5MxauFQwDXYoxAY7koL0f2myM0wIxVhYc_rrG3AOQD9wtfHODTrShzkQb1iMl7SGfpw?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcCbE9SEIBdHlinhk6PABh_Ivxo9yhzDCI5mLorE2KoFZ5emEIdZM5_euNZ-QucVMySryWfmImcSEvbAKk_TOw31opyCnr44U9uOf430auaD7MdlmsIX7iJgHS1m5oJ0RkQQ1XFUQ?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdz3WXTnIHfX27L0noe6gxMuGmAvAffe6YGS69nxxMFq-Gac5pDJ8IBmsoSAdNkmEQI41zn0grXOuURi_njbZvYImoFMf3wJ_2iU6fOCRQ5zP6RGhRkS6MyFc8tsikIzro8cfdttA?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXec5Sr0Vi-zlbhS3voB_qzv1zpJQCabWE_jqzsTPTBcIeMoKXmKTV0x6khZghxDRJI-kyKLOih9ZkjaHWISd4z7Bjadp6Li85LkpPzydW6WHblU_vj9euhK4DETCXzpjGHOmOVdsg?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfgvZXPHuz_fYVTwzxzyZ7OgLQvlcSpX3fwFhfO8g-dzwSIS_1Pa2jH6PBhAVTc0fGPyg43uNFPDtBPHmlS7ODpXRg3hXBjto9g1loPbwZznypz1y3MOLAz7qQZ7PBvLX-rM1vDAQ?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcPV2_hSxE1rAIydWr6dfNmKo4i2wrynGv_JVy4GQd6uyX3ibk7rugFkQONFSAmxUaq9EvPLfMVw9yl1LF-AapMWnBzvlabrxuBOxvC_F6vN9QT7_eQVQiOEZ09jJi9IJrBksHsPA?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdZ8Ki7y_90ONBOmgsVL1Sgcu6urOaNoCSN4BhMpTCMHC3-bFF084pbJQC2Bq3lPRCq8lD1cSBH-LkdhHLM4-ClvsEwyuW0CcueYoeKSquANHPlPcwYGogN1qHAl4uY-kCL4XRQGA?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeUE2zQMW4r-5n7CLaNEVHxgZu5zoPwPF5-ldl2xJEXjwMsn53effTFHI18r6HyxSmoq0R6DF10Zu3TQiKFNRvpk6Lzp7JbcMWSRrEqSZ56JjP0rxJrwbXOZKZayzjjB-5n9euw?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdxL8Gbl9-8dcv0bpl2N16SJ63YnGnRjHa5DI1rciE6V8Akb6KudT6ZF-N7SyjjKcdh7Io4t7nLJBYLuvsEocWLO0MATjm7YoJe_lwuGGJKPOEcQ3B4VHlTFsjxjH-j6MQu6H2ZrA?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXexMte7M6-GVVvoq-uRiD4QxGzwULGMXlFzl7C2C7_idtX7l3Qoy9dwvGpzS22aJjz34_DJCtqIyGN9Z-XpV3pIktG0SpizA5gNVJ4BpEmp396QJFBfq8pDiIqw79j9hVwoiJ_P?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc25HkpODI1gseZSh4XsYtY4l0LHmhwSzSdWqMHFcJKtcJHru-3EmmeGDWJ-OzWeJ_bH8dXuJuXwM2ZUx3mCS_htiNJrNybPpJB8QBG400yOinb7ZNXN6gODN_8K1ZSQO2Ch5-Mzg?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc33g0xedpQX0I0auccZ9OEz8GgK99VxkKW_Uq8tU99U77yRPpmm-RLDTUKmpO1kjTPJJNIoG5Vl5YvtCxS4F3Gm6JcCqVa0n_P6vzuG4qX9HKtHeXPjeW-Fq6zRZXCsQopzVeP?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdC2w8o56k2vcWQKmbATQIgDmQC96m3D8n9TSkeO2xwSlLyHwiBJL7bUiqlnXLU_6XWsE_WCmPxZYWBd3yTZVGx4a_x-SE80UGxePXY4ZL5sxZ_qBcEID05jJcR7-JbF9-Cgb9r?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdQ-JlUYVuMKl6Z2E55wAPXTMSDw0rINPHKE5gQPfIVuXsJ2MXi9kO4zZlJILi0sCDBhqHBi2Bsj4llVDcfK73QpmWQwdMP-tpyVWegsvMC3BqudnSckfO09gKlbyAbWbxx0pMyxw?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfbKx5h6fuTjd3OH6lF9fpVKMbKPvuGOQJSEs4EPlKy5cV0mQzBZ4D93oBQQID87k7QgAb6OWz6PR6X0cGA_hA0MqwnS7w1fy_-fIsHuAG3T_8qIVe71l_Qa2GuMCER0rCTF3Pssg?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcKiGd95bLHOc7C1RS2goqQBmn3N0jvLB0DL2lMmNySIqgN4-vpA_xV2zUpP4nh_kCct0hfPgLbaiKAYFQ5LPUZqFrZSn8tmkELn6Mw2zvJ0D9c7bmICTiEoliB0BX12-lV_Qf4ww?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXePmbP8eg4d9IoKqAXcr-6buIJsEmtVchc4D5aYpNNqZW7b7PRZyndNbcCZojVArd6PuvEx038urS9_IiKp8RPVnGexIU3MfBezAbIXslrgqwcE_EvjGNFDMPt7B08gWTfdhZCauQ?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXenLDwn0jZiwU-lwe4A5NjpVTxVlatT2A3vAC964XKEShzZgXp4bzeEfddvipbP1MNC0kCv_uKcpI7jBiTtL6k0Eb41xzQfa9hC5F-wG9Lmc54KRNjr4okU8pGGyqJywRmDzwtKYw?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdljYn_7zZcRpnhjioBAzE5PxfoeYteB3ly9ZD5dS07vHy4JCjguwdL7krI12UeJdS2xJfP7Yp09_i_xqCawJIz1AKnrnByzH_0ek00gTB8vzSoDKZabg0huRsP8Q6_y5h1sI0Qlw?key=cYUWrp72V1wWrECYsGp9iLNA)![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXenwwOREUJ5HqLuynBOMHYUgFPxpdoNkAKqb91BAS2T-fzGXosCDKtm7V9z4liWhd4teHiJDGPzK57GeNRHCw2e7k_EtN6WYT9x101kFoFxuefd6r2dkXzsPGU42a_U8LOs78tS8Q?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcY8f8Izg5LC7dIzxvZgDEFzQjsdlt4CIUwnbkO2gfDkTvNEhTeBz61i3J02JmJFsjt3W38ye8uNzPSPKOOB5NLk9dEU9KXTZBFvdp0VFqOIcuo1EC5MQxYFN3rp17dRXmsAtmR?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe0p_Jtu5clmeKMGj9cbvFezSnwY1U5O8ZayW8mQAI-ZJu7c8vt3l3N-GPovEi0JKG6kUKMpr_GFxm5bev0hEXWNJ29ojlcHoOjkQec7R0kthj8sSbS0yiqSknHNdgBc1JxkoGiZg?key=cYUWrp72V1wWrECYsGp9iLNA)

## triage_agent.py

| Agen-agen          | Kegunaan                         |
| ------------------ | --------------------------------- |
| Triase | Mengevaluasi permintaan dan menentukan agen mana yang paling sesuai untuk menangani permintaan tersebut. |
| Sales | Permintaan untuk modifikasi penerbangan. Agen ini dibagi lagi menjadi: Agen pembatalan penerbangan dan agen perubahan penerbangan |
| Pengembalian dana | Membantu pengguna untuk pengembalian dana, termasuk dengan kode pengembalian dana. |

Cara kerja:

-  Setiap agen diinisialisasi dengan spesifikasi tertentu, seperti nama, model yang digunakan, dan instruksi yang diberikan.
-  Agen triase menangani permintaan pertama dan menentukan agen penanganan tugas yang sesuai.
-  Setelah agen triase menentukan agen penanganan tugas, tugas tersebut diteruskan ke agen penanganan untuk diproses.
    
Dengan ini, sistem multi-agent dapat bekerja secara efisien untuk menangani berbagai permintaan dengan cara yang terorganisir dan efisien.

### Cara menggunakan
```bash
cd examples/triage_agent
python3 run.py
```

### Pengujian

-  Pelayanan yang disediakan:
	-  Pembelajaran dan penjualan barang-barang tentang *beekeeping* & *beeyard*
	- Macam-macam peralatan tentang *beekeeping* & *beeyard*
	- Panduan tentang manajemen sarang lebah   
	- Kursus dan *workshop* daring untuk mengembangkan kemampuan kita
-   Mencarikan diskon yang cocok untuk kita
-   Penjelasan cara kerja dari peralatan-peralatan yang tersedia
-   Membantu dalam proses pembayaran untuk metode pembayaran apa pun

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcQIjew_v1vvsUh0dwUjo2BxS9ABvnovx2_FkLAH3TlVsAe0Lsj4gGmBSS190KDh6oSc79R1IHTKy9TObmBvk6AswjM2DbDa2MO7Qt19T1DVNnhC4zlnMiQGh0YUNV2Q0VuGNf3?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeKVdO0ocLYLRLvDYnmApWatACMtdUIBjUj8yLAKIYC40a0A7qLv_crthnz4dqzIyrJyktJSIL4iX2tm_ZsEmxANmxmYezV2evsughcOMwKUQiREdzkynBptb9d-Hda_qXKpN9PIg?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeRyqKWrjv0k6MdvKBweNZswcaEj4dqkNe7FDQ38aRW1-JkTHlLMjBeWiowtW2iObIaQWmOWc1SMavnGPi7b4kKpf1JUHJnXxCv4lk352nfxJXWVzZ0bpVAW7UXIRxOV5Dz6NAUAA?key=cYUWrp72V1wWrECYsGp9iLNA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcyeG3CDfndeHnbXVriN9rLrJ0XMBt1B_ImCAImGTVZXhPTUa20aGup_BurXn_46gMRMIvkxMdglRMkmZwAGEtKaUmkBxYdSP16XlC9CLCM5bojRZJX3xr7u6YjItoXlsY-vVqsQw?key=cYUWrp72V1wWrECYsGp9iLNA)
