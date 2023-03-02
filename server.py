import asyncio

from tornado import web, websocket, options


class HomeHandler(web.RequestHandler):
    def get(self):
        self.render('home.html')


class Socket(websocket.WebSocketHandler):
    def on_message(self, message):
        self.write_message(message)


async def main():
    app = web.Application(
            [
              ("/", HomeHandler),
              ("/socket", Socket),
            ],
            debug=True,
            static_path="static",
            )
    app.listen(8000)
    await asyncio.Event().wait()


if __name__ == "__main__":
    options.parse_command_line()
    asyncio.run(main())

