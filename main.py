from flask import Flask, render_template, request
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def mainPage():
    return render_template('index.html')


@app.route("/equipo")
def teamPage():
    return render_template('equipo.html')


@app.route("/precios")
def preciosPage():
    return render_template('precios.html')


@app.route("/ubicacion")
def mapPage():
    return render_template('ubicacion.html')


@app.route("/ubicacion_variable", methods=['POST'])
def mapPage_variable():
    linkmapas = ["embed?pb=!1m18!1m12!1m3!1d3327.5127784061388!2d-70.70535178428042!3d-33.48803360682927!2m3!1f0!2f0"
                 "!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662c4b06a0a9777%3A0xb3321d1fb943bcbe!2sPiloto%20Lazo%20120"
                 "%2C%20Cerrillos%2C%20Región%20Metropolitana!5e0!3m2!1ses-419!2scl!4v1636060602939!5m2!1ses-419!2scl",
                 "embed?pb=!1m14!1m8!1m3!1d4500.228969046637!2d-70.7285094!3d-33.4347858!3m2!1i1024!2i768!4f13.1!3m3"
                 "!1m2 "
                 "!1s0x0%3A0x3f8db00dcdfd1518!2sFarmacia%20Popular%20Cerro%20Navia!5e0!3m2!1ses-419!2scl"
                 "!4v1636048411922!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.5521806779147!2d-70.68496676545868!3d-33.37610147775876!2m3!1f0!2f0"
                 "!3f0!3m2 "
                 "!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662c6e58c1e11d1%3A0x68458d5fbd9d0ebd!2sFarmacia%20Popular%20Conchal"
                 "%C3%AD!5e0!3m2!1ses-419!2scl!4v1636054465437!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.2260187522551!2d-70.66614308320396!3d-33.555868550160014!2m3!1f0!2f0"
                 "!3f0 "
                 "!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662da4a8878c089%3A0x9679b342f8a4121f!2sMunicipalidad%20de%20El"
                 "%20Bosque!5e0!3m2!1ses-419!2scl!4v1636055432360!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.8306283971492!2d-70.68987291305788!3d-33.45424556711132!2m3!1f0!2f0"
                 "!3f0!3m2 "
                 "!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662c57e1f772315%3A0x74da15d41891d61!2sFarmacia%20Comunal%20estacion"
                 "%20central!5e0!3m2!1ses-419!2scl!4v1636055498318!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.2900053665047!2d-70.63734385377685!3d-33.37365786237839!2m3!1f0!2f0"
                 "!3f0!3m2 "
                 "!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662c63c78203e65%3A0x98787299ee63b277!2sAlcald%C3%ADa%20de"
                 "%20Huechuraba!5e0!3m2!1ses-419!2scl!4v1636055574181!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.465869592002!2d-70.65564229992583!3d-33.42076093960936!2m3!1f0!2f0"
                 "!3f0!3m2 "
                 "!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662c5c7aaa2c469%3A0x9a37d3896f32c3df!2sFarmacia%20Municipal%20Dr"
                 ".%20Carlos%20lorca%20Tobar!5e0!3m2!1ses-419!2scl!4v1636055666577!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.4286526252884!2d-70.66474407950979!3d-33.53480491581529!2m3!1f0!2f0"
                 "!3f0!3m2 "
                 "!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662dae1f3b8eddd%3A0x15fab39c58e4d63d!2sIlustre%20Municipalidad%20de"
                 "%20La%20Cisterna!5e0!3m2!1ses-419!2scl!4v1636055791949!5m2!1ses-419!2scl",
                 "d/u/0/embed?mid=130jzCtN_-wYJokoSd58DyY_FdkAVwuop",
                 "embed?pb=!1m18!1m12!1m3!1d4500.3466931546051!2d-70.63308135497496!3d-33.54332594608842!2m3!1f0!2f0"
                 "!3f0!3m2 "
                 "!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662da71c7244ab3%3A0xb5f5c6fec5a7d7dc!2sIlustre%20Municipalidad%20de"
                 "%20La%20Granja!5e0!3m2!1ses-419!2scl!4v1636056017791!5m2!1ses-419!2scl",
                 "embed?pb=!1m14!1m8!1m3!1d4500.6911532277848!2d-70.62990218578818!3d-33.58421204046435!3m2!1i1024"
                 "!2i768 "
                 "!4f13.1!3m3!1m2!1s0x9662d9d7255d0d09%3A0xcf99515fe67a7ab5!2sMunicipalidad%20de%20La%20Pintana!5e0!3m2"
                 "!1ses-419!2scl!4v1636056960134!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.8216255641674!2d-70.54333936239861!3d-33.4510930762406!2m3!1f0!2f0"
                 "!3f0!3m2 "
                 "!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662ce1336589d49%3A0x3c304120ff1bc599!2sFarmacia%20Comunitaria%20La"
                 "%20Reina!5e0!3m2!1ses!2scl!4v1636060428158!5m2!1ses!2scl",
                 "embed?pb=!1m14!1m8!1m3!1d4500.2961477423881!2d-70.5099455!3d-33.3517845!3m2!1i1024!2i768!4f13.1!3m3"
                 "!1m2 "
                 "!1s0x9662cbc4148b2f5f%3A0xc99194d265046273!2sPadre%20Alfredo%20Arteaga%20Barros%2C%20Centro%20de"
                 "%20Salud%20Familiar%20Lo%20Barnechea%2C%20Lo%20Barnechea%2C%20Regi%C3%B3n%20Metropolitana!5e0!3m2"
                 "!1ses-419!2scl!4v1636061402087!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.9615550087494!2d-70.73061446473335!3d-33.450609508015724!2m3!1f0!2f0"
                 "!3f0 "
                 "!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662c39ae0a909e3%3A0xa82e6b87806702a7!2sCentro%20de%20Salud"
                 "%20Familiar%20Pablo%20Neruda!5e0!3m2!1ses-419!2scl!4v1636061499223!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.5530767212084!2d-70.59817614001254!3d-33.48435831358676!2m3!1f0!2f0"
                 "!3f0!3m2 "
                 "!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662d01f4548cb1f%3A0x828b885683d30f60!2sMunicipalidad%20de%20Macul"
                 "!5e0!3m2!1ses-419!2scl!4v1636061614136!5m2!1ses-419!2scl",
                 "embed?pb=!1m14!1m8!1m3!1d4500.9266546236895!2d-70.76178801363578!3d-33.50753513699084!3m2!1i1024"
                 "!2i768 "
                 "!4f13.1!3m3!1m2!1s0x0%3A0x878eb7ef5a45c623!2sFarmacia%20Familiar%20La%20Receta!5e0!3m2!1ses!2scl"
                 "!4v1636061085846!5m2!1ses!2scl",
                 "embed?pb=!1m14!1m8!1m3!1d4500.0506379351543!2d-70.5937143411045!3d-33.45425092432533!3m2!1i1024"
                 "!2i768!4f13 "
                 ".1!3m3!1m2!1s0x9662cfbe94d720cd%3A0x32fffec4770746ea!2sMunicipalidad%20de%20%C3%91u%C3%B1oa!5e0!3m2"
                 "!1ses-419!2scl!4v1636061937401!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.55767528345325!2d-70.68121563252082!3d-33.502048102682515!2m3!1f0"
                 "!2f0!3f0 "
                 "!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662db2fd3e52921%3A0xbb34e50922fc9d1a!2sSapu%20Villa%20Sur!5e0"
                 "!3m2!1ses-419!2scl!4v1636061818261!5m2!1ses-419!2scl",
                 "embed?pb=!1m14!1m8!1m3!1d4500.854522569012!2d-70.54153004330682!3d-33.47629764871098!3m2!1i1024"
                 "!2i768!4f13 "
                 ".1!3m3!1m2!1s0x0%3A0xf40ad6243d7453f9!2sFarmacia%20Comunitaria%20de%20Pe%C3%B1alol%C3%A9n!5e0!3m2"
                 "!1ses-419!2scl!4v1636057987698!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.572634430288!2d-70.61913317636451!3d-33.44250127411606!2m3!1f0!2f0"
                 "!3f0!3m2 "
                 "!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662c57fbd749743%3A0xebe9cb4135268e98!2sFarmacia%20Comunitaria%20de"
                 "%20Providencia!5e0!3m2!1ses-419!2scl!4v1636062187274!5m2!1ses-419!2scl",
                 "embed?pb=!1m14!1m8!1m3!1d4500.14531657142425!2d-70.7443083!3d-33.4450718!3m2!1i1024!2i768!4f13.1"
                 "!3m3!1m2 "
                 "!1s0x9662c370382fa219%3A0x1da788254e0d4a2d!2sI%20Municipalidad%20de%20Pudahuel!5e0!3m2!1ses-419!2scl"
                 "!4v1636062288364!5m2!1ses-419!2scl",
                 "embed?pb=!1m14!1m8!1m3!1d4500.1221177931084!2d-70.73325916115874!3d-33.369503392657265!3m2!1i1024"
                 "!2i768 "
                 "!4f13.1!3m3!1m2!1s0x0%3A0xa72fa1f789854f24!2sFamarcia%20Municipal%20Solidaria%20Quilicura!5e0!3m2"
                 "!1ses!2scl!4v1636061231807!5m2!1ses!2scl",
                 "embed?pb=!1m14!1m8!1m3!1d4500.12654468961003!2d-70.6933606!3d-33.4226!3m2!1i1024!2i768!4f13.1!3m3!1m2"
                 "!1s0x9662c415de7d5637%3A0xc3f5185045b40f9d!2sMunicipalidad%20de%20Quinta%20Normal!5e0!3m2!1ses-419"
                 "!2scl!4v1636062587094!5m2!1ses-419!2scl",
                 "embed?pb=!1m14!1m8!1m3!1d4500.330779590171!2d-70.643772!3d-33.4015288!3m2!1i1024!2i768!4f13.1!3m3!1m2"
                 "!1s0x0%3A0xe6d3f3d0a149fbef!2sFarmacia%20Popular%20Ricardo%20Silva%20Soto!5e0!3m2!1ses-419!2scl"
                 "!4v1636058195361!5m2!1ses-419!2scl",
                 "d/u/0/embed?mid=1OxX9EPoJi1RAubxGLw_7Dpra2-2a6Ni-",
                 "embed?pb=!1m14!1m8!1m3!1d4500.5770402709688!2d-70.64136208476877!3d-33.478932668424164!3m2!1i1024"
                 "!2i768 "
                 "!4f13.1!3m3!1m2!1s0x9662c548e757f95f%3A0x725d103de14e5c49!2sFarmacia%20Popular%20San%20Joaqu%C3%ADn"
                 "%2F%20Unidad%20de%20Atenci%C3%B3n%20Primaria%20Oftalmol%C3%B3gica%20("
                 "UAPO)!5e0!3m2!1ses!2scl!4v1636060859623!5m2!1ses!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.196586213338!2d-70.65538744786743!3d-33.49246880079045!2m3!1f0!2f0!3f0"
                 "!3m2 "
                 "!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662dacda19907fb%3A0xb018095f2c2e7d5!2sFarmacia%20Comunal%20De%20San"
                 "%20Miguel!5e0!3m2!1ses-419!2scl!4v1636062723147!5m2!1ses-419!2scl",
                 "embed?pb=!1m14!1m8!1m3!1d4500.67420678669475!2d-70.6437639!3d-33.5431471!3m2!1i1024!2i768!4f13.1!3m3"
                 "!1m2 "
                 "!1s0x9662da41d1b5f7bf%3A0x1521a4c8e8b67675!2sI.%20Municipalidad%20de%20San%20Ram%C3%B3n!5e0!3m2!1ses"
                 "-419!2scl!4v1636062806206!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.004556364796!2d-70.65897373022462!3d-33.43624799999999!2m3!1f0!2f0!3f0"
                 "!3m2 "
                 "!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662c5ac4d61f0c5%3A0x743b0780afe3c6ea!2sBotica%20Comunitaria%20Dra"
                 ".%20Elo%C3%ADsa%20D%C3%ADaz!5e0!3m2!1ses-419!2scl!4v1636062894041!5m2!1ses-419!2scl",
                 "embed?pb=!1m18!1m12!1m3!1d4500.5792713282403!2d-70.55417538420134!3d-33.38204848079368!2m3!1f0!2f0"
                 "!3f0!3m2 "
                 "!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662cfa9da43d483%3A0xaf3bb73d74e1ab6d!2sVITABOTICA!5e0!3m2!1ses-419"
                 "!2scl!4v1636062958005!5m2!1ses-419!2scl"]
    comuna = int(request.form['comuna'])
    print(comuna)
    return render_template("ubicacion.html", mapcomuna=linkmapas[comuna])


if __name__ == "__main__":
    app.run(debug=True)
    
