from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	personal = {"name":"Marry James","emailCollege":"marryjames17em@student.mes.ac.in","contact":7040062012,
				"emailPersonal":"marryjames@gmail.com","objective":"To work in a company that enhances my knowledge and skills to give my best for the growth of the company."}

	grad = {"year":"Third Year Graduate","branch":"Department of Mechanical Engineering",
			"college":"Pillai College Of Engineering", "CGPI": "5.6275 / 10", "acronym":"PCE"}

	ssc ={"school":"St. Joseph High School and Junior College","board":"Maharashtra State Board","percentage":"90.8"}

	hsc ={"school":"St. Joseph High School and Junior College","board":"Maharashtra State Board","percentage":"81.8"}

	diploma ={"school":"St. Joseph College of Diploma","university":"Mumbai Univeristy","percentage":"91.8"}

	skills ={ "Technical Domain": [["Mobile App Development","Intermediate"],["Internet of Things(IoT)", "Advanced"],
	            ["Java", "Basic"],["Web Development", "Advanced"]],
			"Soft Skills": [["Decision Making","Intermediate"],["Time Management", "Basic"],
			["Self Motivation", "Basic"],["Problem Solving", "Advanced"]]}

	certi = [{"name":"Fundamentals of Digital Marketing by Google","sem":"1","duration":40.00,"days":5,"type":0},
	{"name":"Fundamentals of Psycho","sem":"4","duration":60.00,"days":15,"type":1},
	{"name":"Blockchain & Cryptocurrency","sem":"5","duration":120.00,"days":30,"type":0},
	{"name":"Resume Writing","sem":"3","duration":10.00,"days":3,"type":1}]

	proj = [{"title":"Intelligent IoT based Farming System (Jan 2019 - ongoing)","description":"Develop an intelligent IoT system to help farmers in irrigation, fertilisation and disease detection in crops.","sem":"6"},
	{"title":"Medical Application (Feb 19 - March 19)","description":"It provides every type of medically related information like nearby hospitals, book an appointment, call an ambulance, check blood status in a blood bank etc.","sem":"7"}]

	intern = [{"companyName":" Allinonecyberteam (Dec 18-Jan 19)","duration":"30","type":0,"sem":4,"description":"Built an Android application to earn money by watching advertisements"},
	{"companyName":" Samhita NGO (Dec 19-Jan 20)","duration":"60","type":1,"sem":6,"description":"Data collection using web scraping."}]

	achiv = [{"description":"Winner of Smart India Hackathon 2019","sem":6},{"description":"4th Place in web weaving competition held by CSI-PCE","sem":5},{"description":"PBL certificate for best project in Python","sem":4}]

	activ = [{"description":"Project Presentation for CSI during the launch of magazine 'Bytestream'.","sem":6},{"description":"Was a part of the team selected for the final round of Smart India Hackathon","sem":5}]

	activOthers = [{"description":"Participated in Mes's UBER RANG Talent show'.","sem":6},{"description":"Participated in Foodthan","sem":5}]

	activExtra = [{"description":"Event Head of FIFA (Gaming Event) for Alegria'.","sem":4},{"description":"Supported a Mr. Fresher Contestant (Played Guitar)","sem":1}]

	goals = [{"description":"Become world leader","type":"Long Term"},{"description":"Become payer xux","type":"Short Term"},
	    {"description":"Complete Masters'","type":"Short Term"}, {"description":"Get job in Good Company","type":"Long Term"}]

	member = {'one':'Anupama Rai', 'two':'Rutuja Pujare'}

	links = [{"description":"LinkedIn - https://www.linkedin.com/in/abhi1"},
			{"description":"Github - https://github.com/mahe"}]

	testi = [{"name":"Anonymous","description":"You made it so simple. My new site is so much faster and easier to work with than my old site."},
	         {"name":"Anonymous","description":"Ready to help everyone. You are very talented and a good Team leader."},
	         {"name":"Anonymous","description":"Puts 100% efforts into any work assigned. Disciplined an obedient person."}]


	hobbies = ["Playing Chess", "Coding", "Reading books"]

	lang = ["English", "German", "Hindi", "Marathi"]
	college_links = [{"description":"PCE - https://www.pce.ac.in/"},
	                {"description":"LinkedIn - https://www.linkedin.com/school/pillaiengineering/"},
	                {"description":"Facebook - https://www.facebook.com/pillaicollege/"},
					{"description": "Twitter - https://twitter.com/pillaicollege"},
					{"description":"Instagram - https://www.instagram.com/pillaicollege/"},
					{"description": "Youtube - https://www.youtube.com/channel/UC4rZoXnH9doGK10M9pEGi6A?"}]


	collegeLinks = [{"Pillai College of Engineering":{"ACR":"PCE","website_link":"https://www.pce.ac.in/","linkedin":"https://www.linkedin.com/school/pillaiengineering/","facebook":"https://www.facebook.com/pillaicollege/","twitter":"https://twitter.com/pillaicollege","instagram":"https://www.instagram.com/pillaicollege/","youtube":"https://www.youtube.com/channel/UC4rZoXnH9doGK10M9pEGi6A?"}},
	                {"Pillai College of Architecture":{"ACR":"PCEA","website_link":"https://www.pasa.ac.in/","linkedin":"https://www.linkedin.com/school/pillsaering/","facebook":"https://www.facebook.com/pillaisasge/","twitter":"https://twitter.com/pilsaollege","instagram":"https://www.instagram.com/pillasalege/","youtube":"https://www.youtube.com/channel/UC4rZoXnH9doGK10M9pEasA?"}}]

	return render_template('ep3/index.html', member=member, personal=personal, grad=grad,links=links,
							college_links=college_links, hsc=hsc, ssc=ssc,diploma=diploma,proj=proj,
							intern=intern,achiv=achiv,activ=activ,activOthers=activOthers,
							activExtra=activExtra,goals=goals, skills=skills, certi=certi,
							collegeLinks=collegeLinks, testi=testi, hobbies=hobbies, lang = lang)

if __name__ == '__main__':
    app.run(debug=True)
