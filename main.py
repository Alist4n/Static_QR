from flask import Flask, redirect, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


current_url = 'https://renident.ru/'

@app.route('/redirect')
def redirect_to_url():
    return redirect(current_url)


@app.route('/update-url', methods=['GET', 'POST'])
def update_url():
    global current_url
    if request.method == 'POST':
        new_url = request.form['url']
        if "http" in new_url:
            current_url = new_url
        else:
            current_url = "https://" + new_url
        return redirect('/update-url')

    return render_template('update_url.html', current_url=current_url)

if __name__ == '__main__':
    app.run(debug=True)
