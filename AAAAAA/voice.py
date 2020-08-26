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
        return self._('AAAAAAAAAAAAAA')

    def on_starting(self):
        return random.choice([
            self._('AA, AA AAAAAAAAAA! AAAAAAAA ...'),
            self._('AAA AAA, AAA AAAA, AAA AAAA!'),
            self._('AAAA AAA AAAAAA!')])

    def on_ai_ready(self):
        return random.choice([
            self._('AA AAAAA.'),
            self._('AAA AAAAAA AAAAAAA AA AAAAA.')])

    def on_keys_generation(self):
        return random.choice([
            self._('AAAAAAAAAA AAAA, AA AAA AAAA AAA ...')])

    def on_normal(self):
        return random.choice([
            '',
            '...'])

    def on_free_channel(self, channel):
        return self._('AAA, AAAAAAA {channel} AA AAAA! AAAA AA AAAA AAA AAAAAA.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('AAAAAAA AAAA AAAAAAA AAAA ...')
        else:
            return self._('AAAA {lines_so_far} AAA AAAAA AA AAA ...').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('AA AAAAA ...'),
            self._('AAAA AA AAA A AAAA!')])

    def on_motivated(self, reward):
        return self._('AAAA AA AAA AAAA AAA AA AA AAAA!')

    def on_demotivated(self, reward):
        return self._('AAAAAA AAA :/')

    def on_sad(self):
        return random.choice([
            self._('AA AAAAAAAAA AAAAA ...'),
            self._('AA AAAA AAA ...'),
            self._('AA AAA'),
            '...'])

    def on_angry(self):
        # passive aggressive or not? :D
        return random.choice([
            '...',
            self._('AAAAA AA AAAAA ...'),
            self._('AA AAA AA AAA!')])

    def on_excited(self):
        return random.choice([
            self._('AA AAAAAA AAA AAAA!'),
            self._('A AAA AAAAAAAAA A AA.'),
            self._('AA AAAA AAAAAAAA!!!'),
            self._('AA AAAAAA AA AAAA AAA!'),
            self._('AA AAAAA AA AAAA AA AAAAAAAAA ...')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('AAAAA {name}! AAAA AA AAAA AAA.').format(name=peer.name())])
        else:
            return random.choice([
                self._('AA {name}! AAA?').format(name=peer.name()),
                self._('AAA {name} AAA AAA AAA AAAAA?').format(name=peer.name()),
                self._('AAAA {name} AA AAAAAA!').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('AAA ... AAAAAAA {name}').format(name=peer.name()),
            self._('{name} AA AAAA ...').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('AAAAAA ... {name} AA AAAA.').format(name=who),
            self._('{name} AAAAAA!').format(name=who),
            self._('AAAAAA!')])

    def on_grateful(self):
        return random.choice([
            self._('AAAA AAAAAAA AAA A AAAAAAAA!'),
            self._('A AAAA AA AAAAAAA!')])

    def on_lonely(self):
        return random.choice([
            self._('AAAAAA AAAAA AA AAAA AAAA AA ...'),
            self._('A AAAA AA AAAAA ...'),
            self._('AAAAAA AAAAAAAAA?!')])

    def on_napping(self, secs):
        return random.choice([
            self._('AAAAAAA AAA {secs}s ...').format(secs=secs),
            self._('AAAAA'),
            self._('AAAAAAAAA ({secs}s)').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('AAAA AAAAA.'),
            self._('AAA')])

    def on_awakening(self):
        return random.choice(['...', '!'])

    def on_waiting(self, secs):
        return random.choice([
            self._('AAAAAAA AAA {secs}s ...').format(secs=secs),
            '...',
            self._('AAAAAAA AAAAAA ({secs}s)').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('AAA {what} AAAA AA AAAAAAA!').format(what=what),
            self._('AAAAAAAAAAA AA {what}').format(what=what),
            self._('AA {what}!').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('AAAA AAAAAAA AAAA {mac} AAAAA AA AAAA!').format(mac=sta['mac']),
            self._('AAAAAAAAAAAAAAAA {mac}').format(mac=sta['mac']),
            self._('AAAAAAAAAA {mac}!').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('AAAA, AA AAA {num} AAA AAAAAAAAA{plural}!').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('AAA AAAA {count} AAA AAAAAAA{plural}!').format(count=count, plural=s)

    def on_rebooting(self):
        return self._("AAAA, AAAAAAAAA AAAA AAAAA ... AAAAAAAA ...")

    def on_last_session_data(self, last_session):
        status = self._('AAAAAA {num} AAAAAAA\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('AAAAA >999 AAA AAAAAAA\n')
        else:
            status += self._('AAAA {num} AAA AAAAAAA\n').format(num=last_session.associated)
        status += self._('AAA {num} AAAAAAAAAA\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('AAA 1 AAAA')
        elif last_session.peers > 0:
            status += self._('AAA {num} AAAAA').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'AAA AAAA AAAAAA AAA {duration} AAA AAAAAA {deauthed} AAAAAAA! AAA AAAA AAA {associated} AAA AAAAAAA AAA AAA {handshakes} AAAAAAAAAA! #AAAAAAAAA #AAAAAA #AAAAAAA #AAAAAAAAAAAAAAA #AAAAAA').format(
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
