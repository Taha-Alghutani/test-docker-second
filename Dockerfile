# استخدام صورة Python كبيئة أساسية
FROM python:3.12.6

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع إلى داخل الحاوية
COPY . /app
COPY wait_for_postgres.py /app/wait_for_postgres.py

# نسخ ملف المتطلبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# فتح المنفذ (في حال تستخدم runserver)
EXPOSE 8000

# أمر بدء التشغيل
CMD ["sh", "-c", "python wait_for_postgres.py && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
