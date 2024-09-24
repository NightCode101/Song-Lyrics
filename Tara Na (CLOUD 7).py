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
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        # ("\n\n\nSimula na nga ang bago nating pahina", 0.08),
        # ("Dating panaginip , ako'y nandino na", 0.08),
        # ("Alam kong mahirap dahil sa duda", 0.08),
        # ("Salamat, 'di ka bumitaw sa musika", 0.08),
        # ("Parang mahiwagang ika'y narito", 0.08),
        # ("Sa paraisong Kanyang binuo", 0.11),
        ("Wake me up", 0.11),
        ("Brinh me up", 0.11),
        ("Tara na't sumabay tayo sa musika", 0.11),
        ("Deams do come true", 0.11),
        ("If you're scared, its okay I'm with you", 0.11),
        ("Tara na sa byahe kong medyo malayo", 0.11),
        ("Pero kahit  kailan 'di nagig malabo, uh", 0.11),
        ("Entablado'y nasa atin na", 0.11),
        ("My dreams are waking up", 0.11),
        ("Come on and bring  me up", 0.11),
        ("Tara na't sumabay tayo sa musika", 0.11),
        ("My dreams are wakng up", 0.11),
        ("Come on and bring me up", 0.11),
        ("Tara na't sumabay tayo sa musika, eh eh", 0.11),
        ("Bata man ako ay alam kona", 0.11),
        ("Ang musika ay para sa'kin at ako ay and tala", 0.11),
        ("Mga bituin na nag niningning", 0.11),
        ("sabay-sabay nating abutin ng 'di na palihim, at", 0.11),
        ("Di mo na kailangan pang mag tago", 0.11),
        ("Nasa'yo ang tunay na hinihiling panalo", 0.11),
        ("Tuloy lang ang lakad kahit malayo pa", 0.11),
        ("dalangin ko lang sana ay hindi ka bumitaw, uh", 0.11),
        ("Parang mahiwagang ika'y narito", 0.11),
        ("sa paraisong Kanyaang binuo", 0.11),
        ("Wake me up", 0.11),
        ("Bring me up", 0.11),
        ("Tara na't sumabay tayo sa musika", 0.11),
        ("Dreams do come true", 0.11),
        ("If you're scared, it's okay I'm wih you", 0.11),
        ("Tara na sa biyahe kong medyo malayo", 0.11),
        ("Pero kahit kailan 'di naging malabo, uh", 0.11),
        ("Entablado'y nasa atin na", 0.11),
        ("My dreams are waking up", 0.11),
        ("Come on and bring  me up", 0.11),
        ("Tara na't sumabay tayo sa musika", 0.11),
        ("My dreams are wakng up", 0.11),
        ("Come on and bring me up", 0.11),
        ("Tara na't sumabay tayo sa musika, eh eh", 0.11),
        ("Di mona kailangan mag duda", 0.11),
        ("Sabay natin abutin kumikinang na tala, eh eh eh", 0.11),
        ("Di mona kailangan mag duda", 0.11),
        ("Ikaw at ako, atin ang mundo, eh eh", 0.11),
        ("Buksan mo ang 'yong mga mata", 0.11),
        ("Pitong tala ay nandito na", 0.11),
        ("Haba man ng biyahe ko minsan", 0.11),
        ("pero kahit kailan di kapa lumisan", 0.11),
        ("Naliligaw nung una, pero di nag duda, uh", 0.11),
        ("Hawak sa kamay, sayaw sumabay", 0.11),
        ("TARA NA!", 0.11),
        ("My dreams are waking up", 0.11),
        ("Come on and bring me up", 0.11),
        ("Tara na't sumabay tayo sa musika, eh eh", 0.11),
        ("Di mona kailangan mag duda", 0.11),
        ("Sabay natin abutin kumikinang na tala, eh eh eh", 0.11),
        ("Di mona kailangan mag duda", 0.11),
        ("Ikaw at ako, atin ang mundo, oh oh oh", 0.11),
    ]
    delay = [0, 3.7, 7.6, 12.2, 16.5, 20.2]

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