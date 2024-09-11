# Malaccan
Deployment Link PWS : http://ilham-satya-malaccanrevised.pbp.cs.ui.ac.id

Jawaban pertanyaan:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

--> saya membuat repo github baru untuk proyek ini. kemudian, saya hubungkan dengan local repository saya dengan git.

--> saya membuat requirements.txt yang berisi segala perlengkapan yang dibutuhkan. lalu saya download dengan melakukan hal berikut:

pip install -r requirements.txt

--> lalu saya memulai project django baru dengan melaksanakan kode berikut:

django-admin startproject malaccan .

--> saya kemudian membuat dokumen .gitignore untuk meng-exclude beberapa file pada direktori lokal saya.

--> setelah setup untuk proyek django sudah selesai, saya memulai aplikasi main pada proyek tersebut dengan menjalankan "python manage.py startapp main" dengan ini directory baru bernama main akan terbentuk

--> saya kemudian mendaftarkan app main pada installed app pada settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
]

--> saya kemudian menambah kelas pada models.py yaitu Product dengan attribute name, stock, price, description. saya juga menambah method untuk mengembalikan nama dari produk apabila produknya dipanggil

class Product(models.Model):
    name = models.CharField(max_length=255)  
    stock = models.IntegerField()
    price = models.IntegerField()  
    description = models.TextField()  

    def __str__(self):
        return self.name

--> setelah melakukan perubahan pada models.py, saya melakukan migration dengan command berikut:

python manage.py makemigrations
python manage.py migrate

-->saya kemudian membuat direktori templates yang saya isi dengan file main.html

-->saya kemudian membuat fungsi pada views.py yang berada dibawah direktori main untuk dihubungkan dengan main.html

berikut adalah isinya:

def show_main(request):
    products = Product.objects.all()  # Mengambil semua produk dari database
    context = {
        'shop_name': 'Malaccan',
        'npm' : '2306210714',
        'name' : 'Ilham Satya Nusabhakti',
        'class' : 'PBP C',
        'products': products,  # Produk-produk yang diambil dari model
    }
    return render(request, "main.html", context)

--> saya kemudian membuat file urls.py pada direktori main.

isinya adalah sebagai berikut:

from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

ini digunakan untuk menghubungkan URL root dari aplikasi main ke show_main

-->kemudian saya memodifikasi urls.py yang ada pada direktori malaccan (proyek saya) menjadi seperti berikut:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]

ini untuk menghubungkan URL dari aplikasi main ke proyek django

-->kemudian saya membuat proyek pada PWS. setelah itu saya hubungkan proyek tersebut dengan repositori git saya.

-->saya melakukan add, commit, dan push ke remote yang saya daftarkan pada git yaitu origin (github) dan pws


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan](https://i.ibb.co.com/vLStQM3/bagan-django.jpg)

User akan mengirim request dari web browser. Requestnya selanjutnya akan diterima server dan masuk ke urls.py dan kemudian diarahkan ke show_main. data-data dari context pada show_main kemudian akan masuk ke main.html yang berada di dalam direktori templates. selanjutnya show_main akan render main.html dan disalurkan sebagai response untuk user

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

--> git sebagai version control berperan untuk menyimpan berbagai versi dari program kita sendiri agar jalan pemrograman semakin terkontrol dan lebih aman dari modifikasi yang menyebabkan error atau kesalahan. git juga memungkinkan kolaborasi, yang sangat mungkin terjadi dalam konteks pengembangan perangkat lunak. fitur dari git juga banyak yang membantu seperti branching yang bisa kita gunakan untuk mengetes sebuah fitur baru yang belum kita ingin finalisasi dan integrasikan ke main branch.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

--> pertama, django menggunakan bahasa pemrograman yang kami, mahasiswa fasilkom, sudah familiar yaitu python. django memiliki struktur yang terorganisasi, memudahkan programmer untuk memahami dari dasar. Model ORM pada django juga memudahkan interaksi programmer dengan database, karena hanya perlu menggunakan python saja. Selain itu, django juga terkenal dengan keamanannya.

5. Mengapa model pada Django disebut sebagai ORM?

--> Model pada django disebut ORM (Object Relational Mapping) karena pada model, django memetakan atribut pada kelas python ke kolom-kolom dalam tabel database. Hal ini membuat programmer dapat berhubungan dengan database dengan menggunakan python.
