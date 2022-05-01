from flask import Flask, render_template, request
import spacy

app = Flask(__name__)

nlp = spacy.load('es_core_news_sm')

opt_ent = {'organization': 'ORG',
           'person' : 'PER',
           'localization' : 'LOC',
           'miscellaneous' : 'MISC'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST',])
def get_text():
    if request.method == 'POST':
        ents = []
        rawtext = request.form['rawtext']
        taskoption = request.form['taskoption']
        doc = nlp(rawtext)
        print(taskoption)
        if taskoption == 'Seleccionar opción':
            print(doc.ents)
            ents = doc.ents
        else:
            for ent in doc.ents:
                if ent.label_ == opt_ent[taskoption]:
                    ents.append(ent.text)

        return render_template('index.html', results=ents, num_of_results=len(ents))

if __name__ == '__main__':
    app.run(debug = True)
