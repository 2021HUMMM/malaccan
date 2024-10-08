# Malaccan: Delivering Goods Across the Globe with Generational Trust, Like the Malacca Strait's Legacy in Global Trade.
# Personal Data

- Nama  : Ilham Satya Nusabhakti
- NPM   : 2306210714
- Kelas : PBP C
- PWS Link : http://ilham-satya-malaccan.pbp.cs.ui.ac.id
#


# Contents:
- [Jawaban Tugas 2](#tugas-2)
- [Checklist Tugas 2](#checklist-tugas-2)
- [Jawaban Tugas 3](#tugas-3)
- [Screenshot Postman](#screenshot-postman)
- [Checklist Tugas 3](#checklist-tugas-3)
- [Jawaban Tugas 4](#tugas-4)
- [Checklist Tugas 4](#checklist-tugas-4)
- [Jawaban Tugas 5](#tugas-5)
- [Checklist Tugas 5](#checklist-tugas-5)
- [Jawaban Tugas 6](#tugas-6)
- [Checklist Tugas 6](#checklist-tugas-6)

#
# Tugas 2 
[Back to Contents](#contents)
## Jawaban pertanyaan:
1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

    - saya membuat repo github baru untuk proyek ini. kemudian, saya hubungkan dengan local repository saya dengan git.

    - saya membuat requirements.txt yang berisi segala perlengkapan yang dibutuhkan. lalu saya download dengan melakukan hal berikut:
        ```bash
        pip install -r requirements.txt
        ``` 

    - lalu saya memulai project django baru dengan melaksanakan kode berikut:
        ```bash
        django-admin startproject malaccan .
        ```

    - saya kemudian membuat dokumen .gitignore untuk meng-exclude beberapa file pada direktori lokal saya.

    - setelah setup untuk proyek django sudah selesai, saya memulai aplikasi main pada proyek tersebut dengan menjalankan "python manage.py startapp main" dengan ini directory baru bernama main akan terbentuk

    - saya kemudian mendaftarkan app main pada installed app pada settings.py
        ```bash
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'main'
        ]
        ```

    - saya kemudian menambah kelas pada models.py yaitu Product dengan attribute name, stock, price, description. saya juga menambah method untuk mengembalikan nama dari produk apabila produknya dipanggil
        ```bash
        class Product(models.Model):
            name = models.CharField(max_length=255)  
            stock = models.IntegerField()
            price = models.IntegerField()  
            description = models.TextField()  

            def __str__(self):
                return self.name
        ```

    - setelah melakukan perubahan pada models.py, saya melakukan migration dengan command berikut:
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```

    - saya kemudian membuat direktori templates yang saya isi dengan file main.html

    - saya kemudian membuat fungsi pada views.py yang berada dibawah direktori main untuk dihubungkan dengan main.html. berikut adalah isinya:
        ```bash
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
        ```

    - saya kemudian membuat file urls.py pada direktori main. isinya adalah sebagai berikut:
        ```bash
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```
        ini digunakan untuk menghubungkan URL root dari aplikasi main ke show_main

    - kemudian saya memodifikasi urls.py yang ada pada direktori malaccan (proyek saya) menjadi seperti berikut:
        ```bash
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('main.urls'))
        ]
        ```
        ini untuk menghubungkan URL dari aplikasi main ke proyek django

    - kemudian saya membuat proyek pada PWS. setelah itu saya hubungkan proyek tersebut dengan repositori git saya.

    - saya melakukan add, commit, dan push ke remote yang saya daftarkan pada git yaitu origin (github) dan pws


2. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

    ![Bagan](https://i.ibb.co.com/vLStQM3/bagan-django.jpg)

User akan mengirim request dari web browser. Requestnya selanjutnya akan diterima server dan masuk ke urls.py dan kemudian diarahkan ke show_main. data-data dari context pada show_main kemudian akan masuk ke main.html yang berada di dalam direktori templates. selanjutnya show_main akan render main.html dan disalurkan sebagai response untuk user

3. **Jelaskan fungsi git dalam pengembangan perangkat lunak!**

git sebagai version control berperan untuk menyimpan berbagai versi dari program kita sendiri agar jalan pemrograman semakin terkontrol dan lebih aman dari modifikasi yang menyebabkan error atau kesalahan. git juga memungkinkan kolaborasi, yang sangat mungkin terjadi dalam konteks pengembangan perangkat lunak. fitur dari git juga banyak yang membantu seperti branching yang bisa kita gunakan untuk mengetes sebuah fitur baru yang belum kita ingin finalisasi dan integrasikan ke main branch.

4. **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

pertama, django menggunakan bahasa pemrograman yang kami, mahasiswa fasilkom, sudah familiar yaitu python. django memiliki struktur yang terorganisasi, memudahkan programmer untuk memahami dari dasar. Model ORM pada django juga memudahkan interaksi programmer dengan database, karena hanya perlu menggunakan python saja. Selain itu, django juga terkenal dengan keamanannya.

5. **Mengapa model pada Django disebut sebagai ORM?**

Model pada django disebut ORM (Object Relational Mapping) karena pada model, django memetakan atribut pada kelas python ke kolom-kolom dalam tabel database. Hal ini membuat programmer dapat berhubungan dengan database dengan menggunakan python.
#
# Checklist Tugas 2
[Back to Contents](#contents)
- [x] Membuat sebuah proyek Django baru.
- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
- [x] Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.
- [x] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut:
  - `name`
  - `price`
  - `description`
- [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [x] Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
- [x] Melakukan _deployment_ ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [x] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-_deploy_, serta jawaban dari beberapa pertanyaan berikut:
  - Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).
  - Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
  - Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
  - Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
  - Mengapa model pada Django disebut sebagai _ORM_?

# Tugas 3
[Back to Contents](#contents)
## Jawaban pertanyaan:
1. **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Data delivery dilakukan untuk pertukaran informasi antarsistem, seperti antara server dan client. Tentu hal ini penting untuk interaksi antarkomponen platform, sinkronisasi data, dan interaksi yang dinamis.

2. **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

Saat ini JSON lebih umum penggunaannya. Hal ini terjadi karena formatnya sederhana dan mudah dibaca manusia. Penggunaannya yang lebih umum ini juga membuatnya lebih mudah diintegrasikan dengan teknologi web modern.

3. **Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?**

Sesuai namanya, method `is_valid` digunakan untuk memvalidasi input yang diberikan. Method ini memastikan hanya bentuk data yang diinginkan yang akan diproses. Jika tidak digunakan, maka 1 lapisan perlindungan akan hilang, karena method `is_valid()` digunakan sebagai proteksi dari input data rusak, atau hal seperti injeksi sql. Jika tidak ada method `is_valid()`, akan lebih sulit juga untuk memastikan konsistensi data sesuai dengan format yang diharapkan. 

4. **Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**


`csrf_token` penting untuk proteksi aplikasi web dari serangan CSRF. Serangan CSRF (Cross-Site Request Forgery token) adalah serangan yang dilakukan oleh pelaku dengan membuat pengguna situs asli melakukan hal yang tidak pengguna itu inginkan dan ketahui. Jika menggunakan `csrf_token`, token unik akan menyertai setiap form yang dikirim ke server. Token tersebut hanya diketahui server dan klien legit serta token tersebut harus dicocokkan saat memproses request, dimana jika tidak cocok maka request ditolak.

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

    - pertama-tama, saya membuat base.html pada root project
        ```bash
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            {% block meta %} {% endblock meta %}
        </head>

        <body>
            {% block content %} {% endblock content %}
        </body>
        </html>
        ```
    
    - kemudian, saya menambah line berikut pada settings.py bagian templates untuk set lokasi template yang digunakan pada proyek
        ```bash
        'DIRS': [BASE_DIR / 'templates'],
        ```
    - kemudian, saya set template yang ada pada direktori main/templates/ , yaitu main.html untuk `extends` base.html yang telah kita buat tadi.
    - kemudian, saya memodifikasi class Product pada `models.py` di direktori main dengan menambahkan attribute id. line yang ditambahkan adalah sebagai berikut:
        ```bash
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        ```
    - lalu saya lakukan migrasi setelah memodifikasi models
    - saya membuat `forms.py` pada direktori main untuk menangkap data product baru. berikut kodenya:
        ```bash
        from django.forms import ModelForm
        from main.models import Product

        class ProductForm(ModelForm):
            class Meta:
                model = Product
                fields = ["name", "stock", "price", "description"]
        ```
    - saya kemudian memodifikasi `views.py` dengan menambah method untuk membuat form yang bisa menambah produk ketika data produk di-submit dari form. saja juga menambah line pada method `show_main()` untuk menangkap seluruh instance of Product. berikut kodenya:
        ```bash
        from django.shortcuts import render, redirect
        from main.models import Product
        from main.forms import ProductForm

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

        def create_product_entry(request):
            form = ProductForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                form.save()
                return redirect('main:show_main')

            context = {'form': form}
            return render(request, "create_product_entry.html", context)
        ```
    -  saya kemudian memodifikasi `urls.py` yang berada di direktori main untuk import fungsi yang telah kita buat sebelumnya dan menambahkan path URL pada urlpatterns agar fungsi tersebut dapat kita akses.

    - kemudian saya membuat berkas html baru pada direktori main/templates bernama `create_product_entry.html` untuk tampilan ketika aplikasi web meminta input untuk produk baru. berikut kodenya:
        ```bash
        {% extends 'base.html' %} 
        {% block content %}
        <h1>Add New Product Entry</h1>

        <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product Entry" />
            </td>
            </tr>
        </table>
        </form>

        {% endblock %}
        ```
    - saya kemudian memodifikasi `main.html` pada direktori main/templates supaya mendisplay setiap data products. saya juga mendekorasi tabelnya sehingga lebih mudah dibaca. berikut kodenya:
        ```bash
        {% extends 'base.html' %}
        {% block content %}
        <h1>{{ shop_name }}</h1>

        <h5>NPM: </h5>
        <p>{{ npm }}</p> 

        <h5>Name: </h5>
        <p>{{ name }}</p> 

        <h5>Class: </h5>
        <p>{{ class }}</p> 

        {% if not products %}
        <p>Belum ada data product pada malaccan.</p>
        {% else %}
        <table class="product-table">
        <tr>
            <th>Product Name</th>
            <th>Stock</th>
            <th>Price</th>
            <th>Description</th>
        </tr>

        {% for product in products %}
        <tr>
            <td>{{ product.name }}</td>
            <td>{{ product.stock }}</td>
            <td>{{ product.price }}</td>
            <td>{{ product.description }}</td>
        </tr>
        {% endfor %}
        </table>
        {% endif %}

        <br />

        <a href="{% url 'main:create_product_entry' %}">
        <button>Add New Product Entry</button>
        </a>

        <style>
        .product-table {
            width: 75%;
            border-collapse: collapse;
            margin: 20px 0;
        }

        .product-table th, .product-table td {
            border: 1px solid black;
            padding: 10px;
            text-align: left;
        }

        .product-table th {
            background-color: #ebb134;
            color: black;
            padding-top: 10px;
            padding-bottom: 10px;
        }

        .product-table td {
            background-color: white;
            color: black;
            padding-top: 10px;
            padding-bottom: 10px;
        }
        </style>

        {% endblock content %}
        ```
    - saya kemudian memodifikasi kode pada `views.py` untuk dapat mendisplay data dalam format XML dan JSON, serta mendisplay data sesuai id yang ter-generate. berikut kodenya:
        ```bash
        # Create your views here.
        from django.shortcuts import render, redirect
        from main.models import Product
        from main.forms import ProductForm
        from django.http import HttpResponse
        from django.core import serializers

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

        def create_product_entry(request):
            form = ProductForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                form.save()
                return redirect('main:show_main')

            context = {'form': form}
            return render(request, "create_product_entry.html", context)

        def show_xml(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        def show_json(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

        def show_xml_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        def show_json_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")       
        ```
    - tentu setelah perubahan ini saya harus memodifikasi lagi kode pada `urls.py` supaya meng-import function yang kita buat dan menambahkan path URL pada urlpatterns. berikut kodenya:
        ```bash
        from django.urls import path
        from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
            path('create-product-entry', create_product_entry, name='create_product_entry'),
            path('xml/', show_xml, name='show_xml'),
            path('json/', show_json, name='show_json'),
            path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
        ]
        ```
#

# Screenshot Postman
[Back to Contents](#contents)

**show_xml**
![show_xml](https://i.ibb.co.com/MVt98g7/xml.png)
**show_json**
![show_json](https://i.ibb.co.com/yBwJHKp/json.png)
**xml_by_id**
![xml_by_id](https://i.ibb.co.com/VDSfWYm/xml-by-id.png) 
**json_by_id**
![json_by_id](https://i.ibb.co.com/M6fgYsM/json-by-id.png)

# Checklist Tugas 3
[Back to Contents](#contents)

- [x] Membuat input `form` untuk menambahkan objek model pada app sebelumnya.
- [x] Tambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
- [x] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.
- [x] Menjawab beberapa pertanyaan berikut pada `README.md` pada root folder.
  - [x] Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
  - [x] Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
  - [x] Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
  - [x] Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
  - [x] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] Mengakses keempat URL di poin 2 menggunakan Postman, membuat _screenshot_ dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.
- [x] Melakukan `add`-`commit`-`push` ke GitHub.

# Tugas 4
[Back to Contents](#contents)
1. **Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`**

`HttpResponseRedirect()` tidak bisa melakuan fungsi `reverse()` secara otomatis, sementara redirect bisa. Fungsi `reverse()` adalah fungsi yang digunakan untuk mendapat url dari nama views nya secara otomatis, membuat program lebih fleksibel. Perbedaan selanjutnya ada pada asalnya, yaitu `HttpResponsRedirect()` berasal dari `django.http`, sementara `redirect()` berasal dari `django.shortcuts`. 

2. **Jelaskan cara kerja penghubungan model `Product` dengan `User`!**

Product dikaitkan dengan user menggunakan `ForeignKey`. cara kerjanya adalah setiap produk baru dibuat, datanya akan dikaitkan dengan user yang sedang login. `ForeignKey` dapat menghubungkan banyak product dengan 1 user.

3. **Apa perbedaan antara *authentication* dan *authorization*, apakah yang dilakukan**

*Authentication* digunakan untuk verifikasi user, sementara *authorization* digunakan untuk menentukan hak akses pengguna. Ibaratnya, *authentication* adalah seperti perkenalan diri, sementar *authorization* adalah seperti menentukan apa saja yang bisa user lakukan.

4. **Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari *cookies* dan apakah semua cookies aman digunakan?**

Django mengingat user yang telah login dengan menggunakan session. saat user berhasil log in, django akan membuat session baru yang berisi informasi user (seperti id user). django juga membuat sebuah session id untuk identifikasi session tersebut. session id ini kemudian disimpan pada cookies client. setiap user memberi request, browser akan mengirimkan cookie berisi session id kembali pada server, sehingga server bisa menemukan session yang tepat untuk user. dengan begini, django dapat mengetahui mana user yang sedang log in tanpa harus meminta user untuk login ulang.

kegunaan lain dari cookies:
- menjaga status login dengan sessionid
- menyimpan preferensi pengguna seperti bahasa dan theme web untuk memudahkan personalization user di session selanjutnya
- cookies dapat membantu mengumpulkan data mengenai perilaku pengguna di situs, seperti laman yang sering dikunjungi, dll.
- cookies dapat menyimpan informasi mengenai minat user, sehinga dapat digunakan untuk peningkatan relevansi iklan

tidak semua cookies aman. cookies yang tidak ditangani dengan baik dapat disusupi atau dicuri. ada beberapa cara untuk meningkatkan keamanan cookies. pertama, menggunakan secure flag untuk memastikan cookie hanya dikirim melalui https. kemudian, HttpOnly flag untuk mencegah akses javascript dari sisi client untuk masuk ke cookie

5. **Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).**
- pertama-tama, saya membuat fungsi dan form registrasi, dan menambahkan fungsi tersebut pada `views.py` berikut kodenya:
```bash
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
- kemudian saya membuat `register.html` pada `main/templates`. berikut adalah kodenya:
```bash
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
- kemudian saya import fungsi register pada `urls.py`, dan memasukkannya ke `urlpatterns`
- kemudian saya membuat fungsi login. saya menambahkan method berikut pada `views.py` (setelah import fungsi yang diperlukan seperti `UserCreationForm`, `AuthenticationForm`, dll):
```bash
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
- lalu saya membuat file `login.html` pada `main/templates`. isinya adalah sebagai berikut:
```bash
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
- kemudian saya import fungsi `login_user` dari `views.py` ke `urls.py` dan kemudian menambahkannya ke `urlpatterns`
- setelah membuat fungsi login, saya membuat fungsi logout. 

import yang diperlukan pada `views.py`:
```bash
from django.contrib.auth import logout
```

fungsi baru:
```bash
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
- saya kemudian menambahkan button untuk logout pada `main.html`
- saya kemudian import fungsi `logout_user()` pada `urls.py` di main dan menambahkannya pada `urlpatterns`
- saya kemudian import login_required pada `views.py` dan menambahkan decorator `@login_required(login_url='/login')` diatas `show_main()` sehingga `show_main()` hanya muncul jika sudah log in.
- saya kemudian membuka `views.py` dan import `HttpResponseRedirect`,`reverse`, dan `datetime`
- saya kemudian mengubah fungsi `login_user` menjadi seperti berikut:
```bash
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```

ini berguna untuk redirect laman ke show_main setelah berhasi log in dan menambah cookies `last_login`

- saya pun menambahkan data pada `context` yaitu `last_login`
- saya kemudian mengubah fungsi `logout_user` di `views.py` menjadi seperti ini:
```bash
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

ini berguna untuk menghapus cookie `last_login` saat user logout
- saya kemudian membuka `models.py` dan `import User`
- saya kemudian menambahkan attribute pada class `Product` yaitu `user`. hal ini dilakukan untuk menghubungkan instance of product dengan user yang sedang login.
- saya kemudian mengubah fungsi `create_product_entry()` menjadi seperti ini:
```bash
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
- saya kemudian mengubah value dari `product_entry` dan `context` pada `show_main()` menjadi seperti berikut:
```bash
def show_main(request):
    products = Product.objects.filter(user=request.user) 
    context = {
        'name': request.user.username,
    ...
    ...
    }
```
- saya kemudian membuat user bernama Ilham
- lalu saya laksanakan makemigrations dan migrate
- kemudian, saya import os pada settings.py pada directory malaccan, dan saya ganti variabel DEBUG menjadi seperti ini:
```bash
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```
- lalu saya membuat 1 akun lagi dengan nama Ilham2. pada masing masing Ilham dan Ilham2 saya masukkan 3 data baru.
- terakhir, saya laksanakan git add, commit, dan push.

# Checklist Tugas 4
[Back to Contents](#contents)
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
- [x] Membuat **dua** akun pengguna dengan masing-masing **tiga** dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun **di lokal**.
- [x] Menghubungkan model Product dengan User.
- [x] Menampilkan detail informasi pengguna yang sedang *logged in* seperti *username* dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.
- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
    - [x] Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
    - [x] Jelaskan cara kerja penghubungan model `Product`  dengan `User`!
    - [x] Apa perbedaan antara *authentication* dan *authorization*, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
    - [x] Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari *cookies* dan apakah semua cookies aman digunakan?
    - [x] Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
- [x] Melakukan `add`-`commit`-`push` ke GitHub.

# Tugas 5
[Back to Contents](#contents)
1. **Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

Dalam CSS, terdapat aturan prioritas untuk menentukan selector mana yang digunakan. Urutan prioritasnya adalah sebagai berikut:

- Aturan !important dapat mengesampingkan semua aturan lainnya, memberikan prioritas tertinggi pada suatu properti.
- Inline styles, seperti style="background-color:red;", memiliki prioritas tertinggi setelah aturan !important.
- ID Selector, misalnya #header, memiliki prioritas lebih tinggi dibandingkan dengan class atau elemen.
- Class Selector, seperti .highlight, lebih tinggi dari selector tag HTML.
- Tag Selector, contohnya p, memiliki prioritas terendah di antara semua selector.

2. **Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**

Responsive design penting dalam pengembangan aplikasi web karena memungkinkan tampilan yang menyesuaikan dengan berbagai ukuran layar, seperti desktop, tablet, dan smartphone. Ini memberikan pengalaman pengguna yang konsisten dan nyaman tanpa perlu membuat versi situs terpisah untuk setiap perangkat. Contohnya, aplikasi seperti Instagram sudah menerapkan responsive design dengan baik, sehingga tampilan tetap nyaman di semua perangkat. Sebaliknya, beberapa situs lama mungkin belum responsif, menyebabkan tampilan yang tidak optimal di perangkat mobile.

3. **Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

Margin, border, dan padding adalah elemen kunci dalam desain CSS yang digunakan untuk mengatur ruang di sekitar elemen. Margin mengacu pada jarak di luar border, yang membantu menciptakan spasi antara elemen yang berbeda dan dapat diatur dengan properti margin, seperti `margin: 10px;`. Border adalah garis yang mengelilingi elemen dan dapat disesuaikan dalam hal ketebalan, warna, serta gaya menggunakan properti border, contohnya `border: 2px solid black;`. Sementara itu, padding adalah ruang yang memisahkan konten dari border, memberikan spasi di dalam elemen dan dapat diatur dengan properti padding, seperti `padding: 15px;`. Untuk menerapkan ketiga konsep ini, kita dapat menggabungkan properti CSS tersebut dalam stylesheet. Berikut contoh kodenya:
```bash
.element {
    margin: 10px;
    border: 2px solid black;
    padding: 15px;
}
```

4. **Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

Flexbox dan Grid Layout adalah dua model tata letak dalam CSS yang memudahkan pengaturan elemen responsif. Flexbox berfungsi untuk mengatur elemen dalam satu dimensi (horizontal atau vertikal), ideal untuk menu navigasi dan tombol yang perlu menyesuaikan dengan ukuran layar. Sementara itu, Grid Layout adalah sistem dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom, cocok untuk desain kompleks seperti halaman web terstruktur atau grid foto. Kedua model ini membantu pengembang menciptakan antarmuka yang dinamis dan menarik.

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**

- Untuk implementasi fungsi hapus & edit product, saya tambahkan kode berikut pada `views.py`:
```bash
def edit_product(request, id):
    # Get mood entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get mood berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus mood
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
```
- Saya juga melakukan kustomisasi terhadap web menggunakan tailwind.
    - berikut kode untuk halaman login (`login.html`):
    ```bash
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <div class="min-h-screen flex items-center justify-center w-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
        <div>
        <h2 class="mt-6 text-center text-black text-3xl font-extrabold text-gray-900">
            Login to your account
        </h2>
        </div>
        <form class="mt-8 space-y-6" method="POST" action="">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
            <div>
            <label for="username" class="sr-only">Username</label>
            <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Username">
            </div>
            <div>
            <label for="password" class="sr-only">Password</label>
            <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password">
            </div>
        </div>

        <div>
            <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Sign in
            </button>
        </div>
        </form>

        {% if messages %}
        <div class="mt-4">
        {% for message in messages %}
        {% if message.tags == "success" %}
                <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                    <span class="block sm:inline">{{ message }}</span>
                </div>
            {% elif message.tags == "error" %}
                <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                    <span class="block sm:inline">{{ message }}</span>
                </div>
            {% else %}
                <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                    <span class="block sm:inline">{{ message }}</span>
                </div>
            {% endif %}
        {% endfor %}
        </div>
        {% endif %}

        <div class="text-center mt-4">
        <p class="text-sm text-black">
            Don't have an account yet?
            <a href="{% url 'main:register' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
            Register Now
            </a>
        </p>
        </div>
    </div>
    </div>
    {% endblock content %}
    ```
    - berikut kode untuk halaman registrasi (`register.html`):
    ```bash
    {% extends 'base.html' %}

    {% block meta %}
    <title>Register</title>
    {% endblock meta %}

    {% block content %}
    <div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 form-style">
        <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
            Create your account
        </h2>
        </div>
        <form class="mt-8 space-y-6" method="POST">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
            {% for field in form %}
            <div class="{% if not forloop.first %}mt-4{% endif %}">
                <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
                {{ field.label }}
                </label>
                <div class="relative">
                {{ field }}
                <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    {% if field.errors %}
                    <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                    {% endif %}
                </div>
                </div>
                {% if field.errors %}
                {% for error in field.errors %}
                    <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                {% endfor %}
                {% endif %}
            </div>
            {% endfor %}
        </div>

        <div>
            <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Register
            </button>
        </div>
        </form>

        {% if messages %}
        <div class="mt-4">
        {% for message in messages %}
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <span class="block sm:inline">{{ message }}</span>
        </div>
        {% endfor %}
        </div>
        {% endif %}

        <div class="text-center mt-4">
        <p class="text-sm text-black">
            Already have an account?
            <a href="{% url 'main:login' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
            Login here
            </a>
        </p>
        </div>
    </div>
    </div>
    {% endblock content %}
    ```
    - saya juga sudah mengkustomisasi halaman daftar produk. jika belum ada produk tersimpan, maka akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar. Jika sudah ada, maka akan menampilkan detail dari produk. berikut adalah kodenya:
    ```bash
    {% extends 'base.html' %}
    {% load static %}

    {% block meta %}
    <title>Product Tracker</title>
    {% endblock meta %}

    {% block content %}
    {% include 'navbar.html' %}
    <div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-gray-100 flex flex-col">

    <!-- Information cards for NPM, Name, Class -->
    <div class="p-2 mb-6 relative">
        <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">
        {% include "card_info.html" with title='NPM' value=npm %}
        {% include "card_info.html" with title='Name' value=name %}
        {% include "card_info.html" with title='Class' value=class %}
        </div>
        <div class="w-full px-6 absolute top-[44px] left-0 z-20 hidden md:flex">
        <div class="w-full min-h-4 bg-indigo-700"></div>
        </div>
        <div class="h-full w-full py-6 absolute top-0 left-0 z-20 md:hidden flex">
        <div class="h-full min-w-4 bg-indigo-700 mx-auto"></div>
        </div>
    </div>

    <!-- Last login -->
    <div class="px-3 mb-4">
        <div class="flex rounded-md items-center bg-indigo-600 py-2 px-4 w-fit">
        <h1 class="text-white text-center">Last Login: {{last_login}}</h1>
        </div>
    </div>

    <!-- Add new product button -->
    <div class="flex justify-end mb-6">
        <a href="{% url 'main:create_product_entry' %}" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
        Add New Product Entry
        </a>
    </div>
    
    <!-- Product entries display -->
    {% if not products %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
        <p class="text-center text-gray-600 mt-4">No products available in the tracker.</p>
    </div>
    {% else %}
    <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
        {% for product in products %}
        {% include 'card_product.html' with product=product %}
        {% endfor %}
    </div>
    {% endif %}
    </div>
    {% endblock content %}
    ```
    - saya juga sudah membuat dua button untuk edit/delete product pada setiap card product. Berikut kodenya:
    ```bash
    <div class="relative break-inside-avoid">
        <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
        <div class="w-[3rem] h-8 bg-gray-300 rounded-md opacity-80 -rotate-90 shadow-md"></div>
        <div class="w-[3rem] h-8 bg-gray-300 rounded-md opacity-80 -rotate-90 shadow-md"></div>
        </div>
        <div class="relative top-5 bg-indigo-50 shadow-lg rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform rotate-1 hover:rotate-0 transition-transform duration-300 ease-in-out">
        <div class="bg-indigo-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-indigo-300 shadow-inner">
            <h3 class="font-bold text-2xl mb-2">{{product.name}}</h3>
        </div>
        <div class="p-4">
            <p class="font-semibold text-lg mb-2">Description</p> 
            <p class="text-gray-700 mb-2">
            <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{product.description}}</span>
            </p>
            <div class="mt-4">
            <p class="text-gray-700 font-semibold mb-2">Price</p>
            <div class="relative pt-1">
                <div class="flex mb-2 items-center justify-between">
                <div>
                    <span class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-indigo-600 bg-indigo-200">
                    ${{product.price}}
                    </span>
                </div>
                </div>
            </div>
            </div>
        </div>
        </div>
        <div class="absolute top-0 -right-4 flex space-x-2">
        <a href="{% url 'main:edit_product' product.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition-transform transform hover:scale-110 duration-300 shadow-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
            </svg>
        </a>
        <a href="{% url 'main:delete_product' product.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition-transform transform hover:scale-110 duration-300 shadow-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
            </svg>
        </a>
        </div>
    </div>
    ```
    - saya juga sudah membuat navbar, dan sudah dibuat agar responsive terhadap perbedaan ukuran device. berikut kodenya:
    ```bash
    <nav class="bg-indigo-600 shadow-lg fixed top-0 left-0 z-40 w-screen"></nav>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
            <div class="flex items-center">
            <h1 class="text-2xl font-bold text-center text-white">Malaccan</h1>
            </div>
            <div class="hidden md:flex items-center">
            {% if user.is_authenticated %}
                <span class="text-gray-300 mr-4">Welcome, {{ user.username }}</span>
                <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                Logout
                </a>
            {% else %}
                <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
                Login
                </a>
                <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                Register
                </a>
            {% endif %}
            </div>
            <div class="md:hidden flex items-center">
            <button class="mobile-menu-button">
                <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                <path d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
            </div>
        </div>
        </div>
        <!-- Mobile menu -->
        <div class="mobile-menu hidden md:hidden  px-4 w-full md:max-w-full">
        <div class="pt-2 pb-3 space-y-1 mx-auto">
            {% if user.is_authenticated %}
            <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
            <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                Logout
            </a>
            {% else %}
            <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
                Login
            </a>
            <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                Register
            </a>
            {% endif %}
        </div>
        </div>
        <script>
        const btn = document.querySelector("button.mobile-menu-button");
        const menu = document.querySelector(".mobile-menu");
        
        btn.addEventListener("click", () => {
            menu.classList.toggle("hidden");
        });
        </script>
    </nav>
    ```



# Checklist Tugas 5
[Back to Contents](#contents)
- [x] Implementasikan fungsi untuk menghapus dan mengedit product.
- [x] Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
  - [x] Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
  - [x] Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
    - [x] Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
    - [x] Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
  - [x] Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
  - [x] Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
- [x] Menjawab beberapa pertanyaan berikut pada `README.md` pada root folder (silakan modifikasi `README.md` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
  - [x] Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
  -  [x] Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
  -  [x] Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
  - [x] Jelaskan konsep flex box dan grid layout beserta kegunaannya!
  - [x] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- [x] Melakukan `add`-`commit`-`push` ke GitHub.

# Tugas 6
[Back to Contents](#contents)
## Jawaban pertanyaan:

1. **Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**

JavaScript memberikan manfaat utama seperti meningkatkan interaktivitas, membuat halaman web lebih responsif, dan memungkinkan modifikasi konten secara dinamis tanpa perlu memuat ulang halaman. Selain itu, JavaScript memudahkan validasi form langsung di browser, mempercepat pengalaman pengguna, dan memungkinkan integrasi dengan berbagai API untuk menambah fitur lebih lanjut.

2. **Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?**

await digunakan untuk menunggu hasil dari operasi asynchronous, seperti fetch(), sebelum melanjutkan ke kode berikutnya. Tanpa await, kode setelah fetch() akan langsung dieksekusi tanpa menunggu respons dari server, yang bisa menyebabkan error atau data yang belum siap digunakan. Dengan await, kode menjadi lebih mudah dipahami karena mirip dengan alur kode synchronous, memastikan bahwa data yang diterima dari fetch() sudah lengkap sebelum digunakan.

3. **Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?**

Decorator @csrf_exempt digunakan untuk menonaktifkan pemeriksaan CSRF pada view tertentu, yang sering dibutuhkan saat menangani permintaan AJAX POST. Ini memungkinkan aplikasi untuk menerima data dari sumber yang tepercaya tanpa memerlukan verifikasi token CSRF. Meskipun berguna untuk kasus tertentu, menonaktifkan CSRF dapat memperkenalkan potensi kerentanannya, sehingga perlu diterapkan dengan hati-hati dan hanya pada situasi yang benar-benar aman.

4. **Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?**

Pembersihan data di backend penting karena pengguna bisa mengubah atau melewati validasi di frontend. Dengan membersihkan data di backend, kita memastikan bahwa data yang masuk ke sistem aman dan bebas dari potensi ancaman seperti XSS atau SQL Injection, yang bisa membahayakan aplikasi.

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**

**AJAX GET**
- saya menambah fungsi `add_product_entry_ajax()`. disini saya menggunakan saya juga mengubah beberapa fungsi berikut isi views.py saya setelah diubah:
```bash
# Create your views here.
from django.shortcuts import render, redirect
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import reverse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': request.user.username,
        'shop_name': 'Malaccan',
        'npm' : '2306210714',
        'name' : 'Ilham Satya Nusabhakti',
        'class' : 'PBP C',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductForm(request.POST,  request.FILES)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Wrong username or password')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get product entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    # Mengambil data dari request POST
    name = strip_tags(request.POST.get("name"))
    stock = request.POST.get("stock")
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    user = request.user  # User yang sedang login
    
    # Mengambil file gambar jika ada
    image = request.FILES.get("image")  # Untuk file yang diupload

    # Buat product baru
    new_product = Product(
        name=name,
        stock=stock,
        price=price,
        description=description,
        user=user,
        image=image  # Set gambar jika ada
    )
    new_product.save()

    # Kembalikan response sukses
    return HttpResponse(b"CREATED", status=201)
```
- tidak lupa, lakukan routing url setelah membuat fungsi baru.
- kemudian ke main.html, saya menghapus conditionals products yang seperti productsnya kosong atau tidak. saya ubah menjadi line ini:
```bash 
<div id="product_entry_cards"></div>
```
- kemudian, masih di main.html, buat blok script dengan fungsi-fungsi sebagai berikut:
```bash
<script>
  async function getProductEntries(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }

  async function refreshProductEntries() {
    document.getElementById("product_entry_cards").innerHTML = "";
    document.getElementById("product_entry_cards").className = "";
    const productEntries = await getProductEntries();
    let htmlString = "";
    let classNameString = "";

    if (productEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/no-product.png' %}" alt="No product" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada produk yang ditambahkan ke toko.</p>
            </div>
        `;
    }
    else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full";
        productEntries.forEach((item) => {
            htmlString += `
            <div class="relative break-inside-avoid">
                <div class="relative top-5 bg-green-100 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-green-300 transform rotate-1 hover:rotate-0 transition-transform duration-300">
                    <div class="bg-green-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-green-300">
                        <h3 class="font-bold text-xl mb-2">${item.fields.name}</h3>
                        <p class="text-gray-600">Harga: Rp${item.fields.price}</p>
                    </div>
                    <div class="p-4">
                        <p class="font-semibold text-lg mb-2">Deskripsi Produk</p>
                        <p class="text-gray-700 mb-2">
                            ${item.fields.description}
                        </p>
                        <div class="mt-4">
                            <p class="text-gray-700 font-semibold mb-2">Stok</p>
                            <span class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-green-600 bg-green-200">
                                ${item.fields.stock > 0 ? item.fields.stock : 'Habis'}
                            </span>
                        </div>
                    </div>
                    ${item.fields.image ? `<img src="${item.fields.image}" alt="${item.fields.name}" class="w-full h-48 object-cover rounded-b-lg" />` : ''}
                </div>
                <div class="absolute top-0 -right-4 flex space-x-1">
                    <a href="/edit-product/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                        </svg>
                    </a>
                    <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                        </svg>
                    </a>
                </div>
            </div>
            `;
        });
    }

    document.getElementById("product_entry_cards").className = classNameString;
    document.getElementById("product_entry_cards").innerHTML = htmlString;
  }
  ...
  </script>
```

**AJAX POST**
- tambah kode berikut dibawah `<div id="product_entry_cards"></div>`
```bash
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
    <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
      <!-- Modal header -->
      <div class="flex items-center justify-between p-4 border-b rounded-t">
        <h3 class="text-xl font-semibold text-gray-900">
          Add New Product
        </h3>
        <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
          <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
          </svg>
          <span class="sr-only">Close modal</span>
        </button>
      </div>
      <!-- Modal body -->
      <div class="px-6 py-4 space-y-6 form-style">
        <form id="productEntryForm" enctype="multipart/form-data">
          <!-- Nama Produk -->
          <div class="mb-4">
            <label for="name" class="block text-sm font-medium text-gray-700">Product Name</label>
            <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product name" required>
          </div>
          <!-- Harga Produk -->
          <div class="mb-4">
            <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
            <input type="number" id="price" name="price" min="0" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product price" required>
          </div>
          <!-- Stok Produk -->
          <div class="mb-4">
            <label for="stock" class="block text-sm font-medium text-gray-700">Stock</label>
            <input type="number" id="stock" name="stock" min="0" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter available stock" required>
          </div>
          <!-- Deskripsi Produk -->
          <div class="mb-4">
            <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
            <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product description" required></textarea>
          </div>
          <!-- Gambar Produk -->
          <div class="mb-4">
            <label for="image" class="block text-sm font-medium text-gray-700">Product Image (optional)</label>
            <input type="file" id="image" name="image" class="mt-1 block w-full text-sm text-gray-500 border border-gray-300 rounded-md file:bg-indigo-500 file:text-white file:mr-4 file:py-2 file:px-4 hover:file:bg-indigo-600">
          </div>
        </form>
      </div>
      <!-- Modal footer -->
      <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
        <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
        <button type="submit" id="submitProductEntry" form="productEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
      </div>
    </div>
  </div>
```
- tambahkan fungsi-fungsi berikut pada script:
```bash
refreshProductEntries();
  const modal = document.getElementById('crudModal');
  const modalContent = document.getElementById('crudModalContent');

  function showModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modal.classList.remove('hidden'); 
      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50); 
  }

  function hideModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modalContent.classList.remove('opacity-100', 'scale-100');
      modalContent.classList.add('opacity-0', 'scale-95');

      setTimeout(() => {
        modal.classList.add('hidden');
      }, 150); 
  }

  document.getElementById("cancelButton").addEventListener("click", hideModal);
  document.getElementById("closeModalBtn").addEventListener("click", hideModal);

  function addProductEntry() {
    fetch("{% url 'main:add_product_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#productEntryForm')),
    })
    .then(response => refreshProductEntries()) // Panggil fungsi untuk refresh daftar produk

    // Reset form setelah entri berhasil
    document.getElementById("productEntryForm").reset(); 
    // Menutup modal setelah entri berhasil
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
  }

  document.getElementById("productEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addProductEntry();
  })
```
- tambahkan juga tombol untuk add new product entry by ajax:
```bash
<a href="{% url 'main:create_product_entry' %}" class="bg-yellow-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
      Add New Product
    </a>
    <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" style ="margin-left :4px;" onclick="showModal();">
      Add New Product Entry by AJAX
    </button>
```


