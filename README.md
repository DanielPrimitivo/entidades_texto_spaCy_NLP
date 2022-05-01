# Entidades_texto_spaCy_NLP

Entidades_texto_spaCy_NLP trata de una app en Flask, en la cual, podemos introducir texto y extraer todas las entidades que tiene con el uso de NLP (spaCy). Es posible extraer todas o seleccionar un tipo de entidad.

## Installation

La app (Flask) es levantada en un entorno virtual y las librerías utilizadas las podemos encontrar en requimerents.txt

## Usage

Crear entorno virtual en app e instalar las librerías que podemos encontrar en requirements.txt

```bash
# activar entorno virtual
# Linux:
app$ source venvPr/bin/activate
# Windows:
app$ venvPr\Scripts\activate.bat
(venvPr) app/code$ python -m pip install -r requirements.txt

export FLASK_APP=app
export FLASK_ENV=development

# levantar app
(venvPr) app/code$ flask run
```
