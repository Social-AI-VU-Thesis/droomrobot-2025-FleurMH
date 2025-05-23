from os.path import abspath, join
from time import sleep

from sic_framework.services.openai_gpt.gpt import GPTRequest

from droomrobot import Droomrobot, AnimationType


class Bloedafname4:
    
    def __init__(self, mini_ip, mini_id, mini_password, redis_ip,
                 google_keyfile_path, sample_rate_dialogflow_hertz=44100, dialogflow_language="nl",
                 google_tts_voice_name="nl-NL-Standard-D", google_tts_voice_gender="FEMALE",
                 openai_key_path=None, default_speaking_rate=1.0,
                 computer_test_mode=False):
        
        self.droomrobot = Droomrobot(mini_ip, mini_id, mini_password, redis_ip,
                                google_keyfile_path, sample_rate_dialogflow_hertz, dialogflow_language,
                                google_tts_voice_name, google_tts_voice_gender,
                                openai_key_path, default_speaking_rate,
                                computer_test_mode)

    def run(self, child_name: str, child_age: int, child_gender: str, robot_name: str="Hero"):

        # INTRODUCTIE
        self.droomrobot.say(f'Hallo, ik ben {robot_name} de droomrobot!')
        self.droomrobot.animate(AnimationType.ACTION, "random_short3")
        self.droomrobot.say('Wat fijn dat ik je mag helpen vandaag.')
        self.droomrobot.say('Wat is jouw naam?')
        sleep(3)
        self.droomrobot.say(f'{child_name}, wat leuk je te ontmoeten.')
        self.droomrobot.say('En hoe oud ben je?')
        sleep(3)
        self.droomrobot.say(f'{str(child_age)} jaar. Oh wat goed, dan ben je al oud genoeg om mijn speciale trucje te leren.')
        self.droomrobot.say('Het is een truukje dat kinderen helpt om zich fijn en sterk te voelen in het ziekenhuis.')
        self.droomrobot.say('Ik ben benieuwd hoe goed het bij jou gaat werken.')
        self.droomrobot.say('We gaan samen iets leuks bedenken dat jou gaat helpen.')
        self.droomrobot.say('Nu ga ik je wat meer vertellen over het truukje wat ik kan.')
        self.droomrobot.say('Let maar goed op, ik ga je iets bijzonders leren.')
        self.droomrobot.say('Ik kan jou meenemen op een droomreis!')
        self.droomrobot.say('Een droomreis is een trucje waarbij je aan iets heel leuks denkt.')
        self.droomrobot.say('Dat helpt je om rustig en sterk te blijven.')
        #self.droomrobot.say('Ik ga het liefst in gedachten naar de wolken.')
        #self.droomrobot.say('Kijk maar eens in mijn ogen, daar zie je wat ik bedoel.')
        #self.droomrobot.say('cool he.')
        #self.droomrobot.say('Maar het hoeft niet de wolken te zijn. Iedereen heeft een eigen fijne plek.')
        self.droomrobot.say('Nu mag jij kiezen waar je heen wil in gedachten.')
        #self.droomrobot.say('Wil je naar het strand, het bos, de speeltuin of de ruimte.')

        # droomplek = self.droomrobot.ask_entity('Wat is een plek waar jij je fijn voelt? Het strand, het bos, de speeltuin of de ruimte?',
        #                             {'droom_plek': 1},
        #                             'droom_plek',
        #                             'droom_plek')

        droomplek = self.droomrobot.ask_entity_llm('Wil je naar het strand, het bos, de speeltuin of de ruimte? Of wil je ergens anders naartoe?')

        if droomplek:
            if 'strand' in droomplek:
                self.strand(child_name, child_age, child_gender)
            elif 'bos' in droomplek:
                self.bos(child_name, child_age, child_gender)
            elif 'speeltuin' in droomplek:
                self.speeltuin(child_name, child_age, child_gender)
            elif 'ruimte' in droomplek:
                self.ruimte(child_name, child_age, child_gender)
            else:
                self.nieuwe_droomplek(droomplek, child_name, child_age, child_gender)
        else:
            droomplek = 'strand'  # default
            self.droomplek_not_recognized(child_name, child_age, child_gender)
        droomplek_lidwoord = self.droomrobot.get_article(droomplek)

        # SAMEN OEFENEN
        self.droomrobot.say(f'Oke {child_name}, laten we samen gaan oefenen.')
        self.droomrobot.say('Ga even lekker zitten zoals jij dat fijn vindt.')
        sleep(1)
        zit_goed = self.droomrobot.ask_yesno("Zit je zo goed?")
        if 'yes' in zit_goed:
            self.droomrobot.say('En nu je lekkSSer bent gaan zitten.')
        else:
            self.droomrobot.say('Het zit vaak het lekkerste als je stevig gaat zitten.')
            self.droomrobot.say('met beide benen op de grond.')
            self.droomrobot.say('Ga maar eens kijken hoe goed dat zit.')
            sleep(1)
            self.droomrobot.say('Als je goed zit.')
        self.droomrobot.say('mag je je ogen dicht doen.')
        self.droomrobot.say('dan werkt het truukje het beste.')

        self.droomrobot.say('Stel je voor, dat je op een hele fijne mooie plek bent in je eigen gedachten.')
        self.droomrobot.say(f'Misschien is het weer {droomplek_lidwoord} {droomplek}, of een nieuwe droomwereld')
        self.droomrobot.say('Kijk maar eens om je heen, wat je allemaal op die mooie plek ziet.')
        self.droomrobot.say('Misschien ben je er alleen of is er iemand bij je.')
        self.droomrobot.say('Kijk maar welke mooie kleuren je allemaal om je heen ziet.')
        self.droomrobot.say('Misschien wel groen, of paars, of regenboog kleuren.')
        self.droomrobot.say('En merk maar hoe fijn jij je op deze plek voelt.')
        self.droomrobot.say('Nu je zo fijn op je fijne plek bent, kunnen we je ook wat superkrachten gaan geven.')
        self.droomrobot.say('We gaan samen oefenen hoe je die kracht gebruikt.')
        self.droomrobot.say('Jij mag kiezen wel kracht je hebt.')
      #niet in originele script, in 4-6 word kracht niet uit gekozen maar alleen gepraat over een kracht. hier nu laten kiezen is betere (personalisatie)
        superkracht = self.droomrobot.ask_entity_llm('Welke kracht kies je?')
        if superkracht:
            superkracht_question = self.droomrobot.generate_question(child_age, "Welke superkracht zou je willen?", superkracht)
            superkracht_child_response = self.droomrobot.ask_open(superkracht_question)
            superkracht_robot_response = self.droomrobot.personalize(superkracht_question, child_age, superkracht_child_response)
            self.droomrobot.say(superkracht_robot_response)
            self.droomrobot.say(f'Laten we samen oefenen hoe je jouw superkracht {superkracht} gebruikt.')
        else:
            self.droomrobot.say('Laten we samen oefenen hoe je die kracht gebruikt.')
        self.droomrobot.say('Adem diep in door je neus.')
        self.droomrobot.play_audio('resources/audio/breath_in.wav')
        self.droomrobot.say('en blaas zachtjes uit door je mond.')
        self.droomrobot.play_audio('resources/audio/breath_out.wav')
        self.droomrobot.say(f'Goed zo {child_name}, dat doe je al heel knap.')
        self.droomrobot.say('Kijk eens, op je arm komt een klein warm lichtje tevoorschijn.')
        self.droomrobot.say('Dat lichtje is magisch en maakt je sterk.')
        self.droomrobot.say('Stel je eens voor hoe dat lichtje eruit ziet.')
        self.droomrobot.say('Is het geel, oranje of misschien jouw lievelingskleur?')
        kleur = self.droomrobot.ask_entity_llm('Welke kleur heeft jouw lichtje?')
        self.droomrobot.say(f'{kleur}, wat goed.')
        self.droomrobot.say(f'Kijk maar eens goed… het {kleur} lichtje maakt jou supersterk.')
        self.droomrobot.say('Je kunt alles aan, want je hebt nu je superkracht.')
        self.droomrobot.say('Als je wil, kun je diep in en uitademen om het lichtje aan te zetten en je kracht te laten groeien.')
        self.droomrobot.say('Hartstikke goed, ik ben benieuwd hoe goed het lichtje je zometeen gaat helpen.')
        self.droomrobot.say('Als je klaar bent, mag je je oogjes weer open doen.')
        self.droomrobot.say('En zeggen: “Mijn lichtje gaat mij helpen!”')


        oefenen_goed = self.droomrobot.ask_yesno('Ging het oefenen goed?')
        if 'yes' in oefenen_goed:
            experience = self.droomrobot.ask_open('Wat fijn. Wat vond je goed gaan?')
            if experience:
                personalized_response = self.droomrobot.personalize('Wat fijn. Wat vond je goed gaan?', child_age, experience)
                self.droomrobot.say(personalized_response)
            else:
                self.droomrobot.say("Wat knap van jou.")
            self.droomrobot.say(f'Ik vind {kleur} een hele mooie kleur, die heb je goed gekozen.')
        else:
            experience = self.droomrobot.ask_open('Wat ging er nog niet zo goed?')
            if experience:
                personalized_response = self.droomrobot.personalize('Wat ging er nog niet zo goed?', child_age, experience)
                self.droomrobot.say(personalized_response)
            else:
                pass
            self.droomrobot.say(f'Gelukkig wordt het steeds makkelijker als je het vaker oefent.')
        self.droomrobot.say('Ik ben benieuwd hoe goed het zometeen gaat.')
        self.droomrobot.say('Je zult zien dat dit je gaat helpen.')
        self.droomrobot.say('Als je zometeen aan de beurt bent ga ik je helpen om het lichtje weer samen aan te zetten zodat je weer die superheld bent.')

        ### INTERVENTIE
            #dit deel staat niet in originele script, die begint gelijk met weer terug op de fijne plek. 
        sleep(5)
        self.droomrobot.say('Wat fijn dat ik je weer zie! We gaan weer op droomreis.')
        self.droomrobot.say('Je hebt net al zo goed geoefend. Nu gaat het nóg makkelijker!')
        self.droomrobot.say('Ga maar lekker zitten en doe je oogjes dicht.')
        sleep(1)
        self.droomrobot.say('Luister maar naar mijn stem. De andere geluiden worden stiller.')
        self.droomrobot.say('Adem rustig in.')
        self.droomrobot.play_audio('resources/audio/breath_in.wav')
        self.droomrobot.say('en rustig uit.')
        self.droomrobot.play_audio('resources/audio/breath_out.wav')
            #dit deel boven personaliseren op leeftijd? 4-6
        self.droomrobot.say(f'Stel je maar voor dat je bij {droomplek_lidwoord} {droomplek} bent.')S
        self.droomrobot.say('Kijk maar weer naar alle mooie kleuren die om je heen zijn en voel hoe fijn het is om daar te zijn.')
        self.droomrobot.say('Luister maar naar alle fijne geluiden op die plek.')
        # Sound should be here but this is not possible with the LLM generated content
        self.droomrobot.say('Nu gaan we je superkracht weer aanzetten net zoals je hebt geleerd.')
        self.droomrobot.say('Adem in door je neus.')
        self.droomrobot.play_audio('resources/audio/breath_in.wav')
        self.droomrobot.say('en blaas rustig uit via je mond.')
        self.droomrobot.play_audio('resources/audio/breath_out.wav')
        self.droomrobot.say('Je lichtje verschijnt weer op je arm in precies de kleur die je nodig hebt.')
        self.droomrobot.say('Zie het lichtje steeds sterker worden.')
        self.droomrobot.say('Zo word jij weer een superheld en kun je jezelf helpen.')
        self.droomrobot.say('En als je het nodig hebt, stel je voor dat je lichtje nog helderder gaat schijnen.')
        self.droomrobot.say('Dat betekent dat jouw kracht helemaal opgeladen is.')
        self.droomrobot.say('je kunt het lichtje nog sterker maken door met je tenen te wiebelen.')
        self.droomrobot.say('Het geeft een zachte, veilige gloed om je te helpen.')
        self.droomrobot.say('Als je iets voelt op je arm, dan werkt de superkracht helemaal.')
        self.droomrobot.say('Adem diep in.')
        self.droomrobot.play_audio('resources/audio/breath_in.wav')
        self.droomrobot.say('en blaas uit.')
        self.droomrobot.play_audio('resources/audio/breath_out.wav')
        self.droomrobot.say('Merk maar hoe goed jij jezelf kunt helpen, je bent echt een superheld.')
        self.droomrobot.say('En nu je lichtje goed aan staat, kan jij weer verder spelen op je fijne plek.')

        ### AFSCHEID
        self.droomrobot.say(f'{child_name}, Wat heb je jezelf goed geholpen om alles makkelijker te maken.')
        ging_goed = self.droomrobot.ask_opinion_llm("Hoe goed is het gegaan?")
        if 'positive' in ging_goed:
            self.droomrobot.say('Wat fijn! je hebt jezelf echt goed geholpen.')
        else:
            self.droomrobot.say('Dat geeft niets.')
            self.droomrobot.say('Je hebt goed je best gedaan.')
            self.droomrobot.say('En kijk welke stapjes je allemaal al goed gelukt zijn.')
        self.droomrobot.say(f'je kon al goed een {kleur} lichtje uitzoeken.')
        self.droomrobot.say(f'je bent echt een sterke {child_gender}.')
        self.droomrobot.say('En weet je wat nu zo fijn is, hoe vaker je dit truukje oefent, hoe makkelijker het wordt.')
        self.droomrobot.say('Je kunt dit ook zonder mij oefenen.')
        self.droomrobot.say('Je hoeft alleen maar je ogen dicht te doen en aan je lichtje te denken.')
        self.droomrobot.say('Dan word jij weer een superheld met extra kracht.')
        self.droomrobot.say('Ik ben benieuwd hoe goed je het de volgende keer gaat doen.')
        self.droomrobot.say('Je doet het op jouw eigen manier, en dat is precies goed.')
        self.droomrobot.say('Ik ga nu een ander kindje helpen, net zoals ik jou nu heb geholpen.')
        self.droomrobot.say('Misschien zien we elkaar de volgende keer!')

    def strand(self, child_name: str, child_age: int, child_gender: str):
        self.droomrobot.say('Ah, het strand! Ik kan de golven bijna horen en het zand onder mijn voeten voelen.')
        self.droomrobot.say('Weet je wat ik daar graag doe? Een zandkasteel bouwen met een vlag er op.')
        motivation = self.droomrobot.ask_open(f'Wat zou jij daar willen doen {child_name}?')
        if motivation:
            personalized_response = self.droomrobot.personalize('Wat zou jij op het strand willen doen?', child_age, motivation)
            self.droomrobot.say(personalized_response)
        else:
            self.droomrobot.say("Oke, super.")

    def bos(self, child_name: str, child_age: int, child_gender: str):
        self.droomrobot.say('Het bos, wat een rustige plek! Ik hou van de hoge bomen en het zachte mos op de grond.')
        self.droomrobot.say('Weet je wat ik daar graag doe? Ik zoek naar dieren die zich verstoppen, zoals vogels of eekhoorns.')
        motivation = self.droomrobot.ask_open(f'Wat zou jij daar willen doen {child_name}?')
        if motivation:
            personalized_response = self.droomrobot.personalize('Wat zou jij in het bos willen doen?', child_age, motivation)
            self.droomrobot.say(personalized_response)
        else:
            self.droomrobot.say("Oke, super.")

    def speeltuin(self, child_name: str, child_age: int, child_gender: str):
        self.droomrobot.say('De speeltuin, wat een vrolijke plek! Ik hou van de glijbaan en de schommel.')
        self.droomrobot.say('Weet je wat ik daar graag doe? Heel hoog schommelen, bijna tot aan de sterren.')
        motivation = self.droomrobot.ask_open(f'Wat vind jij het leukste om te doen in de speeltuin {child_name}?')
        if motivation:
            personalized_response = self.droomrobot.personalize('Wat vind jij het leukste om te doen in de speeltuin?', child_age, motivation)
            self.droomrobot.say(personalized_response)
        else:
            self.droomrobot.say("Oke, super.")

    def ruimte(self, child_name: str, child_age: int, child_gender: str):
        self.droomrobot.say('De ruimte, wat een avontuurlijke plek! Ik stel me voor dat ik in een raket zit en langs de sterren vlieg.')
        self.droomrobot.say('Weet je wat ik daar graag zou doen? Zwaaien naar de planeten en zoeken naar aliens die willen spelen.')
        motivation = self.droomrobot.ask_open(f'Wat zou jij in de ruimte willen doen {child_name}?')
        if motivation:
            personalized_response = self.droomrobot.personalize('Wat zou jij in de ruimte willen doen?', child_age,
                                                     motivation)
            self.droomrobot.say(personalized_response)
        else:
            self.droomrobot.say("Oke, super.")

    def nieuwe_droomplek(self, droomplek: str, child_name: str, child_age: int, child_gender: str):
        gpt_response = self.droomrobot.gpt.request(
                        GPTRequest(f'Je bent een sociale robot die praat met een kind van {str(child_age)} jaar oud. '
                        f'Het kind heet {child_name} en ligt in het ziekenhuis. '
                        f'Jij bent daar om {child_name} op te vrolijken en af te leiden met een leuk, vriendelijk gesprek. '
                        f'Gebruik warme, positieve taal die past bij een kind van {child_age} jaar. '
                        f'Zorg dat je praat zoals een lieve, grappige robotvriend, niet als een volwassene. '
                        f'Het gesprek gaat over een fijne plek waar het kind zich blij en veilig voelt. '
                        f'De fijne plek voor het kind is: "{droomplek}". '
                        f'Jouw taak is om twee korte zinnen te maken over deze plek. '
                        f'De eerste zin is een observatie over wat deze plek zo fijn maakt. '
                        f'De tweede zin gaat over wat jij, als droomrobot, daar graag samen met {child_name} zou doen. '
                        f'Bijvoorbeeld als de fijne plek de speeltuin is zouden dit de twee zinnen kunnen zijn.'
                        f'"De speeltuin, wat een vrolijke plek! Ik hou van de glijbaan en de schommel."'
                        f'Weet je wat ik daar graag doe? Heel hoog schommelen, bijna tot aan de sterren."'
                        f'Gebruik kindvriendelijke verbeelding wat te maken heeft met de plek. '))
        self.droomrobot.say(gpt_response.response)
        motivation = self.droomrobot.ask_open(f'Wat zou jij daar willen doen {child_name}?')
        if motivation:
            personalized_response = self.droomrobot.personalize(f'Wat zou jij op jouw droomplek {droomplek} willen doen?', child_age, motivation)
            self.droomrobot.say(personalized_response)
        else:    
            self.droomrobot.say("Oke, super.")

    def droomplek_not_recognized(self, child_name: str, child_age: int, child_gender: str):
        self.droomrobot.say('Geeft niks, soms hoor ik het even niet goed.')
        self.droomrobot.say('Weet je wat? Ik vind het strand zó leuk!')
        self.droomrobot.say('Ik neem je mee naar het strand in je droom.')
        self.strand(child_name, child_age)


if __name__ == '__main__':
    bloedafname4 = Bloedafname4(mini_ip="192.168.178.111", mini_id="00167", mini_password="alphago",
                                redis_ip="192.168.178.84",
                                google_keyfile_path=abspath(join("..", "conf", "dialogflow", "google_keyfile.json")),
                                openai_key_path=abspath(join("..", "conf", "openai", ".openai_env")),
                                default_speaking_rate=0.8, computer_test_mode=False)
    bloedafname4.run('Tessa', 5, 'meid')
