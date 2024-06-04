from app import create_app, socketio

app = create_app()

if __name__ == '__main__':
    print("App running on: http://localhost:5000/")
    socketio.run(app, host='0.0.0.0', port=5000)
