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




