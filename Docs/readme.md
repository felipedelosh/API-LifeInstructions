# LifeInstructions API

## Introducción

Simulates a simple life, be you want to be. Smile, Hate, Love and death. you hav freewill.

## Requisitos previos
- Python
- Flask
- Dependencies (see `requirements.txt`)

## Autenticación

In construction.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Excecute server

```bash
python run.py
```

## Base URL in local

```
http://localhost:5000
```

# Respuestas de la API

Todas las respuestas de la API siguen el siguiente estándar:

```json
{
    "status": true | false,
    "data": [],
    "code": 200 | 400 | 401 | 404 | 500
}
```

## Endpoints

### Health Check

Verifica el estado de la API.

- **URL**: `/health`
- **Método**: `GET`
- **Respuesta Exitosa**:
  - **Código**: 200 OK
  - **Contenido**: 