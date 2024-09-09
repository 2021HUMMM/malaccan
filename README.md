# Malaccan
Checklist Tugas
Checklist untuk tugas ini adalah sebagai berikut.

 Membuat sebuah proyek Django baru.
 Membuat aplikasi dengan nama main pada proyek tersebut.
 Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
 Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
name
price
description
 Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
 Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
 Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
 Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.

Deployment Link PWS : http://ilham-satya-malaccanrevised.pbp.cs.ui.ac.id

Jawaban pertanyaan:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

--> saya membuat proyek django baru setelah melakukan "pip install -r requirements.txt" untuk mendownload segala perlengkapan yang dibutuhkan dengan melaksanakan "django-admin startproject malaccan ."

--> setelah setup untuk proyek django sudah selesai, saya memulai aplikasi main pada proyek tersebut dengan menjalankan "python manage.py startapp main" dengan ini directory baru bernama main akan terbentuk

--> saya kemudian mendaftarkan app main pada installed app

--> pada models.py yang berada di bawah direktori main, saya menambahkan kelas bernama Products yang memiliki attribute berupa data-data yang akan disimpan oleh program, yaitu name, price, description, dan stock. saya juga menambah method untuk mengembalikan nama dari produk apabila dipanggil.

berikut kodenya:

class Product(models.Model):
    name = models.CharField(max_length=255)  
    stock = models.IntegerField()
    price = models.IntegerField()  
    description = models.TextField()  

    def __str__(self):
        return self.name

-->saya kemudian membuat fungsi pada views.py yang berada dibawah direktori main.py


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

--> pertama, django menggunakan bahasa pemrograman yang kami, mahasiswa fasilkom, sudah familiar yaitu python. django memiliki struktur yang terorganisasi, memudahkan programmer untuk memahami dari dasar. Model ORM pada django juga memudahkan interaksi programmer dengan database, karena hanya perlu menggunakan python saja. Selain itu, django juga terkenal dengan keamanannya.

5. Mengapa model pada Django disebut sebagai ORM?

--> Model pada django disebut ORM (Object Relational Mapping) karena pada model, django memetakan atribut pada kelas python ke kolom-kolom dalam tabel database. Hal ini membuat programmer dapat berhubungan dengan database dengan menggunakan python.
