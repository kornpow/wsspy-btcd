import asyncio
import ssl
import websockets
import json


from time import sleep

username = "testuser"
password = "testpass"
host_url = "localhost:8334"
cert_path = "/home/user/Desktop/rpc.cert"

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_verify_locations(cert_path)


async def main():
    uri = f"wss://{username}:{password}@{host_url}/ws"
    async with websockets.connect(uri, ssl=ssl_context) as websocket:

        def payload(idname):
            return {
                "jsonrpc": "1.0",
                "id": idname,
                "method": "getconnectioncount",
                "params": [],
            }

        while True:
            await websocket.send(json.dumps(payload("take1")))
            await websocket.send(json.dumps(payload("take2")))
            await websocket.send(json.dumps(payload("take3")))
            response = await websocket.recv()
            print(response)
            response = await websocket.recv()
            print(response)
            response = await websocket.recv()
            print(response)


asyncio.get_event_loop().run_until_complete(main())
