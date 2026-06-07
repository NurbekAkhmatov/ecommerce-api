echo "# E-Commerce API" > README.md
echo "" >> README.md
echo "FastAPI bilan yozilgan to'liq e-commerce API. JWT autentifikatsiya, admin/user rollari, mahsulotlar, savat, buyurtma va sharhlar bilan." >> README.md
echo "" >> README.md
echo "## 🚀 Texnologiyalar" >> README.md
echo "" >> README.md
echo "- **FastAPI** - Web framework" >> README.md
echo "- **PostgreSQL** - Asosiy ma'lumotlar bazasi" >> README.md
echo "- **SQLAlchemy** - ORM" >> README.md
echo "- **Alembic** - Migratsiyalar" >> README.md
echo "- **JWT** - Authentication" >> README.md
echo "- **Pytest** - Testing" >> README.md
echo "- **Docker** - Containerizatsiya" >> README.md
echo "" >> README.md
echo "## 📋 Talablar" >> README.md
echo "" >> README.md
echo "- Python 3.10+" >> README.md
echo "- PostgreSQL" >> README.md
echo "- Docker (ixtiyoriy)" >> README.md
echo "" >> README.md
echo "## 🔧 O'rnatish" >> README.md
echo "" >> README.md
echo "### 1. Repository ni klon qilish" >> README.md
echo '```bash' >> README.md
echo "git clone https://github.com/NurbekAkhmatov/ecommerce-api.git" >> README.md
echo "cd ecommerce-api" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "### 2. Virtual environment yaratish" >> README.md
echo '```bash' >> README.md
echo "python -m venv venv" >> README.md
echo "source venv/bin/activate  # Linux/Mac" >> README.md
echo "venv\\Scripts\\activate     # Windows" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "### 3. Paketlarni o'rnatish" >> README.md
echo '```bash' >> README.md
echo "pip install -r requirements.txt" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "### 4. PostgreSQL ni sozlash" >> README.md
echo '```bash' >> README.md
echo "sudo -u postgres psql" >> README.md
echo "CREATE DATABASE ecommerce_db;" >> README.md
echo "\\q" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "### 5. .env faylini sozlash" >> README.md
echo '```env' >> README.md
echo "DATABASE_URL=postgresql://postgres:1234567@localhost:5432/ecommerce_db" >> README.md
echo "SECRET_KEY=your-secret-key" >> README.md
echo "ALGORITHM=HS256" >> README.md
echo "ACCESS_TOKEN_EXPIRE_MINUTES=30" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "### 6. Migratsiyalarni qo'llash" >> README.md
echo '```bash' >> README.md
echo "alembic upgrade head" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "### 7. Serverni ishga tushirish" >> README.md
echo '```bash' >> README.md
echo "python -m uvicorn app.main:app --reload" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "## 📚 API Endpointlar" >> README.md
echo "" >> README.md
echo "### Autentifikatsiya" >> README.md
echo "| Method | Endpoint | Vazifasi |" >> README.md
echo "|--------|----------|----------|" >> README.md
echo "| POST | `/auth/register` | Ro'yxatdan o'tish |" >> README.md
echo "| POST | `/auth/login` | Tizimga kirish |" >> README.md
echo "" >> README.md
echo "### Kategoriyalar" >> README.md
echo "| Method | Endpoint | Vazifasi | Ruxsat |" >> README.md
echo "|--------|----------|----------|--------|" >> README.md
echo "| POST | `/categories/` | Yaratish | Admin |" >> README.md
echo "| GET | `/categories/` | Barcha kategoriyalar | Hamma |" >> README.md
echo "| GET | `/categories/{id}` | Kategoriya ma'lumotlari | Hamma |" >> README.md
echo "| PUT | `/categories/{id}` | Yangilash | Admin |" >> README.md
echo "| DELETE | `/categories/{id}` | O'chirish | Admin |" >> README.md
echo "" >> README.md
echo "### Mahsulotlar" >> README.md
echo "| Method | Endpoint | Vazifasi | Ruxsat |" >> README.md
echo "|--------|----------|----------|--------|" >> README.md
echo "| POST | `/products/` | Yaratish | Admin |" >> README.md
echo "| GET | `/products/` | Barcha mahsulotlar (filter, search, pagination) | Hamma |" >> README.md
echo "| GET | `/products/{id}` | Mahsulot ma'lumotlari | Hamma |" >> README.md
echo "| PUT | `/products/{id}` | Yangilash | Admin |" >> README.md
echo "| DELETE | `/products/{id}` | O'chirish | Admin |" >> README.md
echo "" >> README.md
echo "### Savat" >> README.md
echo "| Method | Endpoint | Vazifasi |" >> README.md
echo "|--------|----------|----------|" >> README.md
echo "| POST | `/cart/` | Savatga qo'shish |" >> README.md
echo "| GET | `/cart/` | Savatni ko'rish |" >> README.md
echo "| PUT | `/cart/{id}` | Miqdorni o'zgartirish |" >> README.md
echo "| DELETE | `/cart/{id}` | Savatdan o'chirish |" >> README.md
echo "| DELETE | `/cart/` | Savatni tozalash |" >> README.md
echo "" >> README.md
echo "### Buyurtmalar" >> README.md
echo "| Method | Endpoint | Vazifasi |" >> README.md
echo "|--------|----------|----------|" >> README.md
echo "| POST | `/orders/` | Buyurtma berish |" >> README.md
echo "| GET | `/orders/` | Buyurtmalar ro'yxati |" >> README.md
echo "| GET | `/orders/{id}` | Buyurtma ma'lumotlari |" >> README.md
echo "| PUT | `/orders/{id}/status` | Holatni yangilash (admin) |" >> README.md
echo "" >> README.md
echo "### Sharhlar" >> README.md
echo "| Method | Endpoint | Vazifasi |" >> README.md
echo "|--------|----------|----------|" >> README.md
echo "| POST | `/reviews/` | Sharh qoldirish |" >> README.md
echo "| GET | `/reviews/product/{id}` | Mahsulot sharhlari |" >> README.md
echo "| GET | `/reviews/my` | O'z sharhlari |" >> README.md
echo "| PUT | `/reviews/{id}` | Sharhni yangilash |" >> README.md
echo "| DELETE | `/reviews/{id}` | Sharhni o'chirish |" >> README.md
echo "" >> README.md
echo "## 🐳 Docker bilan ishga tushirish" >> README.md
echo "" >> README.md
echo '```bash' >> README.md
echo "docker-compose up --build" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "## 🧪 Testlarni ishga tushirish" >> README.md
echo "" >> README.md
echo '```bash' >> README.md
echo "pytest tests/ -v" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "## 📄 Hujjatlar" >> README.md
echo "" >> README.md
echo "API hujjatlari Swagger UI da: http://localhost:8000/docs" >> README.md
echo "" >> README.md
echo "## 👨‍💻 Muallif" >> README.md
echo "" >> README.md
echo "Nurbek Akhmatov" >> README.md
echo "" >> README.md
echo "## 📝 Litsenziya" >> README.md
echo "" >> README.md
echo "MIT" >> README.md