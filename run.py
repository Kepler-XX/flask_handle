from api import create_app
import sys

# environment = sys.argv[1] if len(sys.argv) == 2 else 'dev'
# print(environment)
app = create_app('dev')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
