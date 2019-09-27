from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

id_to_url = {}
url_to_id = {}
curr_idx = 0

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create_shortened_url():
    # TODO: Implement me
    global urls
    global curr_idx
    orig_url = request.form["url"]
    if orig_url in url_to_id:
        return render_template('index.html', url="localhost:5000/" + str(url_to_id[orig_url]))
    id_to_url[curr_idx] = orig_url
    url_to_id[orig_url] = curr_idx
    url_alias = curr_idx
    curr_idx += 1
    return render_template('index.html', url="localhost:5000/" + str(url_alias))


@app.route('/<url_alias>')
def redirect_to_original_url(url_alias):
    """
    GET http://127.0.0.1/<url_alias>
      => http://example.org/original/url
    """
    orig_url = get_protocol(id_to_url[int(url_alias)])
    print(id_to_url)
    print(url_to_id)
    print(orig_url)
    return redirect(orig_url, code=302)

def get_protocol(url):
    print(url)
    protocols = ["http://", "https://"]
    for protocol in protocols:
        if protocol == url[:len(protocol)]:
            return url
    return protocols[0] + url

if __name__ == '__main__':
    app.run(debug = True)
