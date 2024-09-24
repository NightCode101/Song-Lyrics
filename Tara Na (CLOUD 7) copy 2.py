# Jeylo Tangaro 

import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed,)

def sing_song():
    lyrics = [
        ("\n\n\nSimula na nga ang bago nating pahina", 0.08),
        ("Dating panaginip , ako'y nandino na", 0.08),
        ("Alam kong mahirap dahil sa duda", 0.08),
        ("Salamat, 'di ka bumitaw sa musika", 0.08),
        ("Parang mahiwagang ika'y narito", 0.08),
        ("Sa paraisong Kanyang binuo", 0.09),

        ("\nWake me up", 0.08),
        ("Bring me up", 0.08),
        ("Tara na't sumabay tayo sa musika", 0.07),
        ("Dreams do come true", 0.08),
        ("If you're scared, it's okay I'm with you", 0.07),

        ("\nTara na sa biyahe kong medyo malayo", 0.04),
        ("Pero kahit  kailan 'di nagig malabo, uh", 0.04),
        ("Entablado'y nasa atin na", 0.07),
        ("My dreams are waking up", 0.07),
        ("Come on and bring me up", 0.07),
        ("Tara na't sumabay tayo sa musika", 0.08),
        ("My dreams are waking up", 0.07),
        ("Come on and bring me up", 0.07),
        ("Tara na't sumabay tayo sa musika, eh eh", 0.04),

        ("\nBata man ako ay alam kona", 0.04),
        ("Ang musika ay para sa'kin at ako ay and tala", 0.04),
        ("Mga bituin na nag niningning", 0.03),
        ("Sabay-sabay nating abutin ng 'di na palihim, at", 0.03),
        ("Di mo na kailangan pang mag tago", 0.04),
        ("Nasa'yo ang tunay na hinihiling panalo", 0.04),
        ("Tuloy lang ang lakad kahit malayo pa", 0.04),
        ("Dalangin ko lang sana ay hindi ka bumitaw, uh", 0.04),
        ("Parang mahiwagang ika'y narito", 0.07),
        ("Sa paraisong Kanyaang binuo", 0.07),

        ("\nWake me up", 0.08),
        ("Bring me up", 0.08),
        ("Tara na't sumabay tayo sa musika", 0.07),
        ("Dreams do come true", 0.08),
        ("If you're scared, it's okay I'm with you", 0.07),

        ("\nTara na sa biyahe kong medyo malayo", 0.04),
        ("Pero kahit  kailan 'di nagig malabo, uh", 0.04),
        ("Entablado'y nasa atin na", 0.07),
        ("My dreams are waking up", 0.07),
        ("Come on and bring me up", 0.07),
        ("Tara na't sumabay tayo sa musika", 0.08),
        ("My dreams are waking up", 0.07),
        ("Come on and bring me up", 0.07),
        ("Tara na't sumabay tayo sa musika, eh eh", 0.05),

        ("Di mona kailangan mag duda", 0.11),
        ("Sabay natin abutin kumikinang na tala, eh eh eh", 0.11),
        ("Di mona kailangan mag duda", 0.11),
        ("Ikaw at ako, atin ang mundo, eh eh", 0.11),

        ("Buksan mo ang 'yong mga mata", 0.11),
        ("Pitong tala ay nandito na", 0.11),

        # ("Haba man ng biyahe ko minsan", 0.11),
        # ("pero kahit kailan di kapa lumisan", 0.11),
        # ("Naliligaw nung una, pero di nag duda, uh", 0.11),
        # ("Hawak sa kamay, sayaw sumabay", 0.11),
        # ("TARA NA!", 0.11),

        # ("My dreams are waking up", 0.11),
        # ("Come on and bring me up", 0.11),
        # ("Tara na't sumabay tayo sa musika, eh eh", 0.11),
        # ("Di mona kailangan mag duda", 0.11),
        # ("Sabay natin abutin kumikinang na tala, eh eh eh", 0.11),
        # ("Di mona kailangan mag duda", 0.11),
        # ("Ikaw at ako, atin ang mundo, oh oh oh", 0.11),
    ]
    delay = [0, 3.9, 7.8, 12.2, 15.9, 19.5, 
             
             23.7, 26.2, 27.8, 32.2, 36.8,

             38.6, 41.3, 44.8, 47.8, 48.8, 51.8, 55.2, 57.5, 59.5,

             63.2, 65.5, 67.7, 69.5, 72, 73.9, 75.5, 77.9, 79.5, 83.5, # To be fixed

             86.9, 88.9, 91.6, 95.4, 100.5,

             103.3,105.4, 109.2, 111.6, 113.6, 115.3, 119.4, 121.3, 123.2,

             127.3, 131.2, 135.5, 139.4,
             
             144.3, 146.2
             ]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delay[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()