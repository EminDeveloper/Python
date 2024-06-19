# Flask Framework - Changing Host IP Address

Hey, so you know how when you make something using Flask, it usually only works on your own computer? That's because it listens to a special address called the "host IP address" by default. This address is like the ID for your computer on a network.

Normally, Flask hangs out at an address called "localhost," which is `127.0.0.1:5000`. That means it only talks to your own computer. But sometimes, you want others on the same Wi-Fi or even from the internet to see what you've made. To do that, you can change Flask's address to let other devices connect.

Here's how you can do it:

1. Open your Flask project in a text editor.
2. Find where it says `app.run()` in your main file.
3. Add something like `app.run(host='183.16.251.236')`. This number (`'183.16.251.236'`) is a special address for your computer on your own Wi-Fi.

But remember, if you set this, only devices using that specific address can see your Flask thing.
