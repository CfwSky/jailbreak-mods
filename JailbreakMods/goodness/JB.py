import os
from mitmproxy import http

SOUND_MAPPINGS = {
    "997febecea2203f2af482a7aea12df70": "assets/sounds/itemequip2.ogg",
    "a1555803077215105187fdd4ed96c487": "assets/sounds/gunsounds/HitSound.ogg", 
    "a00cc924a4e67dd40a3950fe5b458788": "assets/sounds/gunsounds/Sniper.ogg",
    "002eb85891bdc4ada7d68816b8f3e4b1": "assets/sounds/gunsounds/Flintlock.ogg",
    "2e570ba7f6eaeaa812e107c7c584e96f": "assets/sounds/gunsounds/Rifle.ogg", 
    "fce90c104be7fee2f21c6c62f0d01c20": "assets/sounds/gunsounds/Revolver.ogg",
    "2339655399214febfe318567d65955b6": "assets/sounds/gunsounds/JSR.ogg",
    "f2495a981b337f1c6d95988fb88c0109": "assets/sounds/gunsounds/Pistol.ogg",
    "92b8c1663f74c0deb47b035bf51856e8": "assets/sounds/gunsounds/Pistol.ogg", 
    "85e437e529e13bc749ca7f951901f06e": "assets/sounds/gunsounds/OldShotgun.ogg", 
    "483b091d1cc965e0c5cfb4bf052ed386": "assets/sounds/gunsounds/RocketLaunch.ogg",
    "ab2baead732831413adb006cf0ef5e2a": "assets/sounds/gunsounds/JSR.ogg",
    "8342227157539f3fec28553cb1734680": "assets/sounds/gunsounds/RocketLaunch.ogg",
    "17ae28a809256ffd28541ab16835ce2b": "assets/sounds/gunsounds/JSR.ogg", 
    "af2f3e753584bb7dca626197eeca21c0": "assets/sounds/gunsounds/RocketLaunch.ogg",
    "a1f8acbecd9094bd89fb60550f766417": "assets/sounds/gunsounds/plasmapistol.ogg",
    "433f8333405cadbef283637db9c8dc2d": "assets/sounds/gunsounds/PlasmaShotgun.ogg",
    "f3d9ee9a97ebe89bffd6a4d9ab0f64b0": "assets/sounds/wifi.mp3", 
    "b816721216acbb83fa474cbc05848a11": "assets/sounds/wifi.mp3", 
    "097e2058b0f52b886ae22eae27860861": "assets/sounds/wifi.mp3", 
    "188786c8b0be374207faa91be58ae1ad": "assets/sounds/wifi.mp3", 
    "ac4df693826b3d8fec56b91f8debd266": "assets/sounds/wifi.mp3", 
    "f58f48f6b90dc640f6345507ddd034e9": "assets/sounds/wifi.mp3", 
    "1b5daba38981c3fe8448c726ff8af620": "assets/sounds/wifi.mp3", 
    "393c8f33f7910a52fcbf1b810b152b80": "assets/sounds/wifi.mp3",
    "0521a44deadc0f9602bbc5ea20598008": "assets/sounds/wifi.mp3",  
    "3a9c49ea4a69c9cd325669932cba8e82": "assets/sounds/safeget.ogg",
    "33fd4385d6061164c68194727f7f76d4": "assets/sounds/safeget.ogg", 
    "f1dc6ba3bf0cb39edcd8535fc61e86e7": "assets/sounds/button.ogg",
    "e23a19dfb1e8f3deac09336f4fa8335f": "assets/sounds/saferoll.ogg",
    "2f147c63f05d7d4e85d3780c24e53d80": "assets/sounds/select.ogg",
    "3aed7650dfa0025234d3ae1c0446bb61": "assets/sounds/barrier.ogg",
    "1cd0a1a4eacb932ba6cd70827706041c": "assets/sounds/barrier.wav",
    "eccd8215eeeb37d8f2218b330bb916f0": "assets/sounds/question.mp3",
    "cd088328dae7f88957f44b2f6a845f63": "assets/sounds/starman.wav",
}

DECAL_MAPPINGS = {
    "ebcf906da0178ffa28f73f67c49205ca": "assets/decals/JBGuns/Rainbow/PistolRainbow.png",
    "b0a6f4c4ca076d457938974c6fff0545": "assets/decals/JBGuns/Rainbow/AKRainbow.png", 
    "9ebec68a72956ba881efe716f8abb50a": "assets/decals/JBGuns/Rainbow/ShotgunRainbow.png", 
    "c21d2603b59607e5d0ff2e019e714b02": "assets/decals/JBGuns/Rainbow/RifleRainbow.png",
    "358b83effdaadb431a9aefa20e2b3f4c": "assets/decals/JBGuns/Rainbow/ForcefieldLauncherRainbow.png",
    "4e5b21b7dc8188b5590cedd79918cc18": "assets/decals/JBGuns/Rainbow/RocketLauncherRainbow.png", 
    "8dc9f76a89cef81907c3c8caef097680": "assets/decals/JBGuns/Rainbow/C4NoAmmo.png", 
    "b4edc23778eb1b864dff0ab1b30cb521": "assets/decals/JBGuns/Rainbow/C4Ammo.png", 
    "14ee3799acb586fc6853db5a71522744": "assets/decals/JBGuns/Rainbow/RevolverRainbow.png", 
    "714c45b0b8fe0a8dd521d33273ee2dfd": "assets/decals/JBGuns/Rainbow/FlintlockRainbow.png",
    "78b0dc43b2015753fab1f7add86360b4": "assets/decals/JBGuns/Rainbow/SniperRainbow.png",
    "c4d4688cafebfd05408be4d40e8968d1": "assets/decals/JBGuns/Rainbow/PlasmaPistolRainbow.png",
    "94843501e0eb363b58a035724a80971d": "assets/decals/JBGuns/Juice/star.png",
}

def _serve_file(flow: http.HTTPFlow, file_path: str, content_type: str):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            flow.response = http.Response.make(200, f.read(), {"Content-Type": content_type})
    else:
        flow.response = http.Response.make(404, b"File not found", {"Content-Type": "text/plain"})

def request(flow: http.HTTPFlow) -> None:
    for target_hash, local_path in SOUND_MAPPINGS.items():
        if target_hash in flow.request.pretty_url:
            _serve_file(flow, local_path, "audio/ogg")
            print(f"[+] Served sound file: {local_path}")
            return

    for decal_hash, decal_path in DECAL_MAPPINGS.items():
        if decal_hash in flow.request.pretty_url:
            _serve_file(flow, decal_path, "image/png")
            print(f"[+] Served decal file: {decal_path}")
            return
