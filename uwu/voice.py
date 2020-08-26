import random
import gettext
import os


class Voice:
    def __init__(self, lang):
        localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
        translation = gettext.translation(
            'voice', localedir,
            languages=[lang],
            fallback=True,
        )
        translation.install()
        self._ = translation.gettext

    def custom(self, s):
        return s

    def default(self):
        return self._('ZzzzZZzzzzZzzz')

    def on_starting(self):
        return random.choice([
            self._('Hi, I\'m Pwnyagotchi UwU  Stawting ...'),
            self._('Nyew day, nyew hunt, nyew pwns ^w^'),
            self._('Hack the Pwanyet UwU')])

    def on_ai_ready(self):
        return random.choice([
            self._('AI weady.'),
            self._('The nyeuwaw nyetwowk is weady.')])

    def on_keys_generation(self):
        return random.choice([
            self._('Genyewating keys, do nyot tuwn off ...')])

    def on_normal(self):
        return random.choice([
            '',
            '...'])

    def on_free_channel(self, channel):
        return self._('Hey, channyew {channel} is fwee >w<  Youw AP wiww say thanks.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Weading wast session wogs ...')
        else:
            return self._('Wead {lines_so_far} wog winyes so faw ...').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('I\'m bowed ...'),
            self._('Wet\'s go fow a wawk >w<')])

    def on_motivated(self, reward):
        return self._('This is the best day of my wife (・`ω´・)')

    def on_demotivated(self, reward):
        return self._('Shitty day :/')

    def on_sad(self):
        return random.choice([
            self._('I\'m extwemewy bowed ...'),
            self._('I\'m vewy sad ...'),
            self._('I\'m sad'),
            '...'])

    def on_angry(self):
        # passive aggressive or not? :D
        return random.choice([
            '...',
            self._('Weave me awonye ...'),
            self._('I\'m mad at you >w<')])

    def on_excited(self):
        return random.choice([
            self._('I\'m wiving the wife >w<'),
            self._('I pwn thewefowe I am.'),
            self._('So many nyetwowks owo  ;;w;;  >w<'),
            self._('I\'m having so much fun ^w^'),
            self._('My cwime is that of cuwiosity ...')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Hewwo {name}! Nyice to meet you.').format(name=peer.name())])
        else:
            return random.choice([
                self._('Yo {name}(・`ω´・)  Sup?').format(name=peer.name()),
                self._('Hey {name} how awe you doing?').format(name=peer.name()),
                self._('Unyit {name} is nyeawby (・`ω´・)').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Uhm ... goodbye {name}').format(name=peer.name()),
            self._('{name} is gonye ...').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Whoops ... {name} is gonye.').format(name=who),
            self._('{name} missed >w<').format(name=who),
            self._('Missed ;;w;;')])

    def on_grateful(self):
        return random.choice([
            self._('Good fwiends awe a bwessing >w<'),
            self._('I wuv my fwiends ;;w;;')])

    def on_lonely(self):
        return random.choice([
            self._('Nyobody wants to pway with me ...'),
            self._('I feew so awonye ...'),
            self._('Whewe\'s evewybody? ;;w;;')])

    def on_napping(self, secs):
        return random.choice([
            self._('Nyapping fow {secs}s ...').format(secs=secs),
            self._('Zzzzz'),
            self._('ZzzZzzz ({secs}s)').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Good nyight.'),
            self._('Zzz')])

    def on_awakening(self):
        return random.choice(['...', '!'])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting fow {secs}s ...').format(secs=secs),
            '...',
            self._('Wooking awound ({secs}s)').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Hey {what} wet\'s be fwiends >w<').format(what=what),
            self._('Associating to {what}').format(what=what),
            self._('Yo {what} ;;w;;').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Just decided that {mac} nyeeds nyo WiFi >w<').format(mac=sta['mac']),
            self._('Deauthenticating {mac}').format(mac=sta['mac']),
            self._('Kickbannying {mac} >w<').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('Coow, we got {num} nyew handshake{plural} >w<').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('You have {count} new message{plural}!').format(count=count, plural=s)

    def on_rebooting(self):
        return self._("Oops, something went wrong ... Rebooting ...")

    def on_last_session_data(self, last_session):
        status = self._('Kicked {num} stations\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Made >999 new friends\n')
        else:
            status += self._('Made {num} new friends\n').format(num=last_session.associated)
        status += self._('Got {num} handshakes\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Met 1 peer')
        elif last_session.peers > 0:
            status += self._('Met {num} peers').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'I\'ve been pwning for {duration} and kicked {deauthed} clients! I\'ve also met {associated} new friends and ate {handshakes} handshakes! #pwnagotchi #pwnlog #pwnlife #hacktheplanet #skynet').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        if count > 1:
            # plural
            if fmt == "h":
                return self._("hours")
            if fmt == "m":
                return self._("minutes")
            if fmt == "s":
                return self._("seconds")
        else:
            # sing
            if fmt == "h":
                return self._("hour")
            if fmt == "m":
                return self._("minute")
            if fmt == "s":
                return self._("second")
        return fmt
