from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import http.server
import socketserver

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов.
            Всегда возвращает содержимое файла 'contact.html'.
        """
        
        file_to_serve = "contact.html" 

        try:
            # Пытаемся открыть и прочитать файл в бинарном режиме
            with open(file_to_serve, "rb") as f:
                content = f.read()
            
            # Если файл успешно прочитан, отправляем код 200 и заголовки
            self.send_response(200)
            # Тип контента text/html с указанием кодировки UTF-8 (как и требовалось)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            # Отправляем содержимое файла в ответ
            self.wfile.write(content)
            
        except Exception as e:
            # Обработка других возможных ошибок сервера
            error_message_detail = f"Внутренняя ошибка сервера при попытке обслужить {file_to_serve}: {str(e)}"
            self.send_error(500, "Internal Server Error", error_message_detail)
            print(f"Ошибка при обслуживании файла {file_to_serve}: {e}") # Лог на стороне сервера

if __name__ == "__main__":


    webServer = HTTPServer((hostName, serverPort), Handler)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:

        webServer.serve_forever() # Эта строка заставляет сервер работать постоянно
    except KeyboardInterrupt:

        pass

    webServer.shutdown()

    print("Server stopped.")