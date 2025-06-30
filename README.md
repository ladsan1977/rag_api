# RAG_API

Estructura de proyecto FastAPI modular y mantenible.

## Estructura

- `app/`
  - `main.py`: Instancia la app FastAPI y carga los routers.
  - `routers/`: Endpoints divididos por contexto (`drive.py`, `rag.py`, `utils.py`).
  - `services/`: Lógica de negocio de cada endpoint.
  - `models/`: Esquemas Pydantic para request y response.
  - `core/`: Configuración general (`config.py`) y clientes comunes (`openai_client.py`).
- `requirements.txt`: Dependencias principales.
- `.gitignore`: Archivos y carpetas a ignorar por git.
- `README.md`: Documentación del proyecto.

## Instrucciones para iniciar la aplicación

1. **Clona el repositorio y entra a la carpeta del proyecto:**
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd rag_api
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno:**
   - Renombra el archivo `.env.example` a `.env` si existe, o crea uno nuevo basado en las variables necesarias (ver sección de configuración).
   - Asegúrate de completar los valores requeridos para Azure, Google Drive, etc.

5. **Inicia la aplicación FastAPI:**
   ```sh
   uvicorn app.main:app --reload
   ```

6. **Accede a la documentación interactiva:**
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Ejemplo de uso de endpoints

- **Listar archivos de Google Drive:**
  - Método: `GET`
  - URL: `http://localhost:8000/drive/list-drive-files`

- **Realizar pregunta al pipeline RAG:**
  - Método: `POST`
  - URL: `http://localhost:8000/rag/ask`
  - Body (JSON):
    ```json
    {
      "question": "¿Cuál es la función de FastAPI?"
    }
    ```

---
