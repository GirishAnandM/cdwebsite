import os
import urllib, hashlib


import jinja2
import webapp2

team = {
    'Nagarjun Redla':{'email':"nagarjunredla@gmail.com",'department':"Infrastructure",'gravatar':"",'facebook':"https://www.facebook.com/nagarjun.redla"},
    'Roopesh Naidu':{'email':"roopesh.pushpala@gmail.com",'department':"Student Coordinator",'gravatar':"",'facebook':"https://www.facebook.com/roopesh.pushpala"},
    'Girish Anand':{'email':"girishanand07@gmail.com",'department':"Design",'gravatar':"",'facebook':"https://www.facebook.com/girish.anand.7"},
    'Aneesha Bizzul':{'email':"aneeshabizzul@gmail.com",'department':"Public Relations",'gravatar':"",'facebook':"https://www.facebook.com/aneebizz"},
    'Pranav Attavar':{'email':"attavarpranav@gmail.com",'department':"Merchandise",'gravatar':"",'facebook':"https://www.facebook.com/pranav.attavar"},
    'Vidhula Thyagarajan':{'email':"vidhula.thyaga@gmail.com",'department':"Events and Informals",'gravatar':"",'facebook':"https://www.facebook.com/vidh28"},
    'Sai Sachin':{'email':"angalasachyn@gmail.com",'department':"Security",'gravatar':"",'facebook':"https://www.facebook.com/sai.sachin.39"},
    'Shubham Kedia':{'email':"shubham.kedia54@gmail.com",'department':"Editorial",'gravatar':"",'facebook':"https://www.facebook.com/shubham.rockrr"},
    'Bala Sahitya':{'email':"v.balasahitya@gmail.com",'department':"Events and Informals",'gravatar':"",'facebook':"https://www.facebook.com/bala.desai"},
    'Lakshita Reddy':{'email':"lakshitareddy93@gmail.com",'department':"Editorial",'gravatar':"",'facebook':"https://www.facebook.com/lakshita.reddy.9"},
    'Hemanth Chundi':{'email':"hemanthkrishnachundi@gmail.com",'department':"Transport",'gravatar':"",'facebook':"https://www.facebook.com/hemanth.2316"},
    'Jishnu Dantu':{'email':"jishnumaharshi9294@gmail.com",'department':"Food and Beverages",'gravatar':"",'facebook':"https://www.facebook.com/jishnu.m.dantu"},
    'Ananya Koduri':{'email':"ananya.koduri@gmail.com",'department':"Publicity",'gravatar':"",'facebook':"https://www.facebook.com/ananyakoduri"},
    'Sanketh Reddy':{'email':"sankethreddy9@gmail.com",'department':"Hospitality",'gravatar':"",'facebook':"https://www.facebook.com/sanketh.reddy.58"},
    'Neha Reddy':{'email':"neha.r206@gmail.com",'department':"Publicity",'gravatar':"",'facebook':"https://www.facebook.com/neha.reddyp"},
    'Nihal Nalla':{'email':"nihalnalla13@gmail.com",'department':"Security",'gravatar':"",'facebook':"https://www.facebook.com/nihalnalla13"},
    'Praveen Nori':{'email':"saipraveen.nori@gmail.com",'department':"Ticketing",'gravatar':"",'facebook':"https://www.facebook.com/praveen.nori.1"},
    'Sumanth Tittu':{'email':"sumanth.tittu@gmail.com",'department':"Media",'gravatar':"",'facebook':"https://www.facebook.com/sumanth.tittu"}
}


events = {

1:{'name':"Kill the Beat",
'date':"April 10th",
'registration':" ",
'prize':"Worth 20k",
'venue':"N-Block Sports Room",
'time':"3pm onwards",
'duration':"1-2 hours",
'judge':"Ram from Step Up Dance Studio",
'categories':"Solo, Group 3 or more",'theme':"NA",
'contact':"Kruthi-9652582832, Vamsi-9177492629",
'domain':"killthebeat"},

2:{'name':"Beyond the Blues",
'date':"April 11th",
'registration':" ",
'prize':"Worth 20k",
'venue':"N-Block Sports Room",
'time':"12pm onwards",
'duration':"1-2 hours",
'judge':" ",
'categories':"Singing, Instrument",'theme':"NA",
'domain':"beyondtheblues",
'contact':"Manitha-7347521150, Nikhila-7799515818"},

3:{'name':"Reel Steel",
'date':"April 10th | April 11th",
'registration':" ",
'prize':"Worth 10k",
'venue':"N-Block Seminar Hall",
'time':" ",
'duration':" ",
'judge':"Manjula Naidu",
'categories':" ",'theme':"NA",
'domain':"reelsteel",
'contact':" "},

4:{'name':"Picsel",
'date':" ",
'registration':" ",
'prize':"Worth 8k",
'venue':" ",
'time':" ",
'duration':" ",
'judge':" ",
'categories':" ",'theme':"NA",
'domain':"picsel",
'contact':" "},

5:{'name':"Verve",
'date':"April 10th",
'registration':" ",
'prize':"Worth 30k",
'venue':"Carnival Stage",
'time':" ",
'duration':"1 hour",
'judge':" ",
'categories':"Team",'theme':"Evolution",
'domain':"verve",
'contact':" "},

6:{'name':"Gaming",
'date':"April 10th | April 11th",
'registration':"200 INR, Re-Entry:300 INR ",
'prize':"5k",
'venue':"N-Block Sports Room",
'time':"3pm onwards",
'duration':"1-2 hours",
'judge':"NA",
'categories':"FIFA | CS",'theme':"NA",
'domain':"gaming",
'contact':"Jawad-8801528204,Saif-8143331356"},

7:{'name':"Scavenge",
'date':"April 10th | April 11th",
'registration':"150 INR ",
'prize':"Worth 2k",
'venue':"Starting Point - Open Audi",
'time':"12pm onwards",
'duration':"",
'judge':"NA",
'categories':"Team of 3",'theme':"NA",
'domain':"scavenge",
'contact':"Shriya-9618686483,Sukeerth-8686456239"},

8:{'name':"Couch Bags",
'date':"April 10th | April 11th",
'registration':"100 INR ",
'prize':"",
'venue':"M-Block Seminar Hall",
'time':"12:30pm onwards",
'duration':"Till 5pm",
'judge':"NA",
'categories':"Team of 2",'theme':"NA",
'domain':"couchbags",
'contact':"Abilash-9866507976,Kedari-9553573331"},

9:{'name':"Zorbing",
'date':"April 10th",
'registration':"",
'prize':"",
'venue':"",
'time':"",
'duration':"",
'judge':"",
'categories':" ",'theme':"NA",
'domain':"zorbing",
'contact':"Shriya-9618686483,Apoorva-8142941665"},

10:{'name':"30 Yard Cricket",
'date':"April 10th | April 11th",
'registration':"50 INR",
'prize':"NA",
'venue':" ",
'time':"12pm onwards",
'duration':" ",
'judge':"NA",
'categories':"Team of 5",'theme':"NA",
'domain':"cricket",
'contact':"Sushanth-8106944918,Revanth-9052206204"},

11:{'name':"Hackmania",
'date':"April 10th | April 11th",
'registration':"",
'prize':"NA",
'venue':" ",
'time':"10am onwards",
'duration':" ",
'judge':{'Vivek Anand':"http://hackmania.in/CBIT/img/vivek.jpg",'Mr. Chennapanaidu Darapaneni':"http://hackmania.in/CBIT/img/Naidu.jpg",'Mr. Jayaa Bharadwaj':"http://hackmania.in/CBIT/img/jayaa.jpg",'Mr. Pankaj Diwan':"http://hackmania.in/CBIT/img/pankaj.jpg"},
'categories':"",'theme':"NA",
'domain':"hackmania",
'contact':"Sushanth-8106944918,Revanth-9052206204"}

}

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index2.html')
        self.response.write(template.render())

class MobilePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('mobileindex.html')
        self.response.write(template.render())

class UpgradePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

class EventsPage(webapp2.RequestHandler):
    def get(self):

        template = JINJA_ENVIRONMENT.get_template('events.html')
        self.response.write(template.render())

class BoomPage(webapp2.RequestHandler):
    def get(self):

        template = JINJA_ENVIRONMENT.get_template('boom.html')
        self.response.write(template.render(events=events))

class EventPage(webapp2.RequestHandler):
    def get(self):
        url = self.request.path;
        user=team
        for i in events:
            if url=="/"+events[i]['domain']:
                template = JINJA_ENVIRONMENT.get_template('event.html')
                break
            else:
                template = JINJA_ENVIRONMENT.get_template('404.html')
        self.response.write(template.render(event=events[i]))

class TeamPage(webapp2.RequestHandler):
    def get(self):
        for user in team:
            team[user]['gravatar']=gravatar(team[user]['email'])
        template = JINJA_ENVIRONMENT.get_template('team.html')
        self.response.write(template.render(team=team))

class error404(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('404.html')
        self.response.write(template.render())


def gravatar(email,size=200,image_type='jpg'):
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':image_type, 's':str(size)})
    return gravatar_url

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/mobile', MobilePage),
    ('/boom', BoomPage),
    ('/ver2', UpgradePage),
    ('/events', EventsPage),
    ('/team', TeamPage),
    ('/.*',EventPage),
    ('/404',error404),
], debug=True)
