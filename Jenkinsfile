node {
    environment {
        DJANGO_DEBUG = credentials('booktime-django-debug')
        SECRET_KEY    = credentials('booktime-secret-key')
        DJANGO_ALLOWED_HOSTS = credentials('booktime-allowed-host')
        GEOCODER_DATABASE = credentials('geocoder_database')
        DJANGO_DATABASE_USER = credentials('django-database-user')
        DJANGO_DATABASE_PASS = credentials('django-database-pass')
        DJANGO_DATABASE_HOST = credentials('django-database-host')
        DJANGO_DATABASE_PORT = credentials('django-database-port')

    }

    stage ("Checkout") {
        git branch: 'main', url: 'https://github.com/BonfaceThaa/geocoder_proj.git'
        }

    stage ("Environment Setup") {
        sh 'python3 -m venv GeoEnv'
        withPythonEnv("${pwd()}/GeoEnv/bin/python3") {
        sh 'pip install -r geocoder/requirements.txt'
        }
    }

    stage ("Unit tests") {
        try {
            withPythonEnv("${pwd()}/GeoEnv/bin/python3") {
                sh 'python geocoder/manage.py test reverse_geo'}

        } catch (err) {
                throw err
            }
    }

}