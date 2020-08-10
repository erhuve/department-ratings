# EFFECTIVE Department Ratings
This is a visualization of the effective ratings of departments at NYU, as voted by students on ratemyprofessors.com. 


The scraping and visualizing code can easily be modified with one change of ID in order to create this visualization for any school.


The inspiration for this project came from an observation my girlfriend made, that our school's (NYU) Psychology department was highly rated amongst colleges. However, her personal experience in class did not match the expectations this ranking would provide. We figured this is of course because those rankings given to departments are solely based off their research. But that's not the first thing students look for when they want to know about a department at their school. Thus, this visualization democratizes the ratings of departments by scraping reviews of professors at a given school, grouping them by department, and finally showing the rating of each department on a 1-5 scale. An effective rating is calculated with knowledge informed by Bayes Theorem to account for the number of reviews that produce the department's rating, so we can get a more accurate depiction of both large and small departments against each other. Not only do these ratings reflect the opinions of students directly, but they also do not falter for smaller and lesser-known departments.


Of course, this dataset is not without its flaws. While using ratemyprofessors.com allows us to look at any school we choose, the data will suffer from volunteer bias, as these are reviews left by students voluntarily- in many cases, reviews are left on a love-or-hate basis. Still, I chose to make this trade-off to allow anyone to look at any college’s data.
