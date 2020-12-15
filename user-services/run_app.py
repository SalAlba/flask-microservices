from app import create_app


if __name__ == '__main__'
    app = create_app()
    # app.run(host='', port=app.config['PORT'])
    app.run(host='127.0.0.1', port='2020', debug=True)