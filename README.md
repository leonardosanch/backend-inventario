# Backend Inventario

Este proyecto contiene el backend para la gestión de inventarios utilizando Django REST Framework y PostgreSQL.

## Requisitos previos

- Docker
- Docker Compose

## Instrucciones

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/backend-inventario.git
cd backend-inventario

### 2. Construir y ejecutar los contenedores
docker-compose build
docker-compose up -d

### 3. Restaurar la base de datos
Copiar backup.sql al contenedor de PostgreSQL:
docker cp backup.sql gestion_inventario-db-1:/backup.sql
Acceder al contenedor de PostgreSQL y restaurar la base de datos:
docker exec -it gestion_inventario-db-1 bash
psql -U postgres -d inventario -f /backup.sql

### 4. Aplicar las migraciones
Abrir otro pantalla de la terminal sin parar el contenedor y ejecutar :
 docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

5. Verificar que el backend está funcionando
Abre tu navegador y navega a http://localhost:8000 para verificar que el backend está funcionando correctamente.
usuario de prueba con acceso de administrador: leonardosanch@hotmail.com
contraseña: Colombia4$
