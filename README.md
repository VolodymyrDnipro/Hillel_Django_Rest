## Hillel_Django_Rest

#### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```
#### Step 2: Apply Migrations
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

#### Step 3: Run the Development Server
```bash
python manage.py runserver
```

#### Step 4: Create Superuser
```bash
python manage.py createsuperuser
```

#### Step 5: Generate Sample Data (Optional)
```bash
python manage.py generate_fixtures 10 
```