# 🤖 MPTB_vshell

**MPTB_vshell** es un framework de bot de Telegram modular y robusto, diseñado para integrar la potencia de **OpenAI (ChatGPT)** con capacidades avanzadas de gestión de medios. Su arquitectura flexible permite una fácil extensión y personalización.

## 🚀 Características Principales

- **🤖 Integración Profunda con Telegram**: Construido sobre `python-telegram-bot` para una interacción fluida y reactiva.
- **🧠 Inteligencia Artificial**: Soporte nativo para **OpenAI (ChatGPT)**, permitiendo conversaciones naturales y procesamiento de lenguaje.
- **📂 Gestión de Medios Avanzada**: Descarga y subida de archivos grandes y gestión de medios utilizando la eficiencia de `Pyrogram`.
- **👤 Sistema de Usuarios y Roles**: Gestión completa de usuarios, estados y permisos (Admin, Usuario, Banned, etc.).
- **🧩 Arquitectura Modular**: Código organizado en módulos independientes (`brain`, `core`, `downup`, etc.) para facilitar el mantenimiento y la escalabilidad.
- **💾 Persistencia de Datos**: Sistema de base de datos simple pero efectivo para mantener el estado.

## 📋 Requisitos

- 🐍 **Python 3.8** o superior.
- 📱 Una cuenta de **Telegram** y un **Bot Token** (obtenido de @BotFather).
- 🔑 **API ID** y **API Hash** de Telegram (para Pyrogram, obtenible en my.telegram.org).
- 🤖 **OpenAI API Key** (opcional, para funcionalidades de IA).

## 🛠️ Instalación

1. **Clona el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd MPTB_vshell
   ```

2. **Crea un entorno virtual (recomendado):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Linux/Mac
   # .venv\Scripts\activate  # En Windows
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuración

El bot utiliza variables de entorno para su configuración. Puedes establecerlas en tu sistema o crear un archivo `.env` (si usas una librería para cargarlo) o exportarlas antes de ejecutar.

Las variables requeridas son:

| Variable | Descripción |
|----------|-------------|
| `TOKEN` | Token del bot de Telegram. |
| `API_ID` | ID de aplicación de Telegram. |
| `API_HASH` | Hash de la API de Telegram. |
| `OPEN_AI` | Clave de API de OpenAI. |
| `ADMIN` | ID numérico del administrador principal. |
| `HTTP_PROXY` | (Opcional) Proxy HTTP. |
| `HTTPS_PROXY` | (Opcional) Proxy HTTPS. |
| `GROQ_API_KEY` | (Opcional Para tener [groq](https://console.groq.com/home) disponible). |
| `CEREBRAS_API_KEY` | (Opcional) Para tener [cerebras](https://console.groq.com/home) disponible. |
| `OPEN_ROUTER_API_KEY` | (Opcional) Para tener [OpenAI](https://openrouter.ai/) disponible. | 


## ▶️ Uso

Una vez configurado, inicia el bot con el siguiente comando:

```bash
python bot.py
```

## 📂 Estructura del Proyecto

```text
MPTB_vshell/
├── bot.py                  # 🚀 Punto de entrada principal del bot
├── clean.sh                # 🧹 Script de limpieza de archivos temporales
├── database.csv            # 💾 Base de datos simple (CSV)
├── requirements.txt        # 📦 Lista de dependencias
├── runtests.py             # 🧪 Script para ejecutar pruebas
├── modules/                # 🧩 Lógica modular del bot
│   ├── brain.py            # 🧠 Cerebro: Procesamiento de mensajes
│   ├── chatgpt.py          # 🤖 IA: Integración con OpenAI
│   ├── database.py         # 🗄️ DB: Manejo de base de datos
│   ├── gvar.py             # ⚙️ Config: Variables globales y entorno
│   ├── utils.py            # 🛠️ Utils: Herramientas varias
│   ├── core/               # ⚡ Core: Comandos, colas y workers
│   ├── downup/             # 📥 DownUp: Descarga y subida de medios
│   ├── entity/             # 👤 Entity: Definición de objetos (User, etc.)
│   └── fuse/               # 🔌 Fuse: Módulos adicionales/experimentales
├── services/               # 📋 Servicios extrenos
│   ├── cerebras.py         # Servicio con Cerebras SDK 
│   ├── groq.py             # Servicio con groq SDK 
│   └── open_ai.py          # Servicio con OpenAI sdk
├── types/                  # Tipado
├── web/                    # 🌐 Web: Interfaz web de administración
│   ├── web.py
│   └── src/
└── tests/                  # 🧪 Tests: Pruebas unitarias
```
