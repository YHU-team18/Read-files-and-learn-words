sh -c "echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('name18', 'userEmail', 'pass18')\" | python3 manage.py shell"
python3 for_dev_CR.py 5
