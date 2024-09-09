# Malaccan


Deployment Link PWS : belum tersedia, PWS masih down

Jawaban pertanyaan:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

-->

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

-->

Berikut bagannya:

CLIENT ----------> BROWSER ----------> VIEW ----------> MODEL
                                        |
                                        |
                                        |
                                        |-------------> TEMPLATE


3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

--> git sebagai version control berperan untuk menyimpan berbagai versi dari program kita sendiri agar jalan pemrograman semakin terkontrol dan lebih aman dari modifikasi yang menyebabkan error atau kesalahan. git juga memungkinkan kolaborasi, yang sangat mungkin terjadi dalam konteks pengembangan perangkat lunak. fitur dari git juga banyak yang membantu seperti branching yang bisa kita gunakan untuk mengetes sebuah fitur baru yang belum kita ingin finalisasi dan integrasikan ke main branch.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

--> pertama, django menggunakan bahasa pemrograman yang kami, mahasiswa fasilkom, sudah familiar yaitu python. fitur fitur bawaan dari django memudahkan programmer yang baru belajar menjadi lebih mudah paham. model ORM pada django juga memudahkan interaksi programmer dengan database, karena hanya perlu menggunakan python saja.

5. Mengapa model pada Django disebut sebagai ORM?

--> Model pada django disebut ORM (Object Relational Mapping) karena pada model, django memetakan atribut pada kelas python ke kolom-kolom dalam tabel database. Hal ini membuat programmer dapat berhubungan dengan database dengan menggunakan python.
