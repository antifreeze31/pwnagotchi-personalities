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
            self._('Let’s PWN some n00bs!…'),
            self._('New day to PWN the n00bs!'),
            self._('Hack the Planet!')])

    def on_ai_ready(self):
        return random.choice([
            self._('I am 4LIV3.'),
            self._('I am 4W4R3.')])

    def on_keys_generation(self):
        return random.choice([
            self._('Generating keys, do not turn off ...')])

    def on_normal(self):
        return random.choice([
            '',
            '...'])

    def on_free_channel(self, channel):
        return self._('Hey, channel {channel} is free! Your AP will say thanks.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Reading last session logs ...')
        else:
            return self._('Read {lines_so_far} log lines so far ...').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('So b0r3d ...'),
            self._('Let\'s PWN someone!')])

    def on_motivated(self, reward):
        return self._('So easy!')

    def on_demotivated(self, reward):
        return random.choice([
            self._('I\'m not trying, you know ...'),
            self._('I\'m just going easy today ...')])
    def on_sad(self):
        return random.choice([
            self._('I\'m extremely bored ...'),
            self._('I\'m very sad ...'),
            self._('I\'m sad'),
            '...'])

    def on_angry(self):
        # passive aggressive or not? :D
        return random.choice([
            '...',
            self._('Go away before I dox you!'),
            self._('I\'m mad at you!')])

    def on_excited(self):
        return random.choice([
            self._('I\'m living the life!'),
            self._('I PWN therefore I am.'),
            self._('So many networks!!!'),
            self._('I\'m having so much fun!'),
            self._('My crime is that of curiosity ...')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Huh? Another skid, {name} challenges me?').format(name=peer.name())])
        else:
            return random.choice([
                self._('Yo {name}! Sup?').format(name=peer.name()),
                self._('Hey {name} how are you doing?').format(name=peer.name()),
                self._('Unit {name} is nearby!').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Uhm ... goodbye {name}').format(name=peer.name()),
            self._('Finally, that skid {name} is gone!').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Whoops ... {name} is gone.').format(name=who),
            self._('{name} missed!').format(name=who),
            self._('Missed!')])

    def on_grateful(self):
        return random.choice([
            self._('Too many skids nearby!'),
            self._('Yuck, too many skids!')])

    def on_lonely(self):
        return random.choice([
            self._('Loneliness only fuels my PWNage!'),
            self._('I feel so alone ...'),
            self._('Where\'s everybody?!')])

    def on_napping(self, secs):
        return random.choice([
            self._('Logging off... ({secs}s) ...').format(secs=secs),
            self._('Resting my fingers...'),
            self._('ZzzZzzz ({secs}s)').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Good night.'),
            self._('Logging off for the night ...')])

    def on_awakening(self):
        return random.choice(['...', '!'])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting for {secs}s ...').format(secs=secs),
            '...',
            self._('Looking around ({secs}s)').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('PWNing {what}').format(what=what),
            self._('Associating to {what}').format(what=what),
            self._('Brute-forcing {what}').format(what=what),
            self._('Downloading {what}\'s mainframe').format(what=what),
            self._('Melting {what}\'s firewall').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('DDOSing {mac}!').format(mac=sta['mac']),
            self._('Get booted, {mac}!').format(mac=sta['mac']),
            self._('Deploying LOIC on {mac}!').format(mac=sta['mac']),
            self._('Frying {mac}\'s network card!').format(mac=sta['mac']),
            self._('I\'m firing mah lazor ({mac})').format(mac=sta['mac']),
            self._('Kickbanning {mac}!').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('Heh, we rekt {num} n00b{plural}!').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('You have {count} new message{plural}!').format(count=count, plural=s)

    def on_rebooting(self):
        return self._("Oops, something went wrong ... Rebooting ...")

    def on_last_session_data(self, last_session):
        status = self._('DDOSed {num} n00bs\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Met >999 new skids\n')
        else:
            status += self._('Met {num} new skids\n').format(num=last_session.associated)
        status += self._('Rekt {num} WiFis\n').format(num=last_session.handshakes)
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
