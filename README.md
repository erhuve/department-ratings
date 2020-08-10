# EFFECTIVE Department Ratings
This is a visualization of the effective ratings of departments at NYU, as voted by students on ratemyprofessors.com.
The scraping and visualizing code can easily be modified with one change of ID in order to create this visualization for any school.

The inspiration for this project came from an observation my girlfriend made, that our school's (NYU) Psychology department was highly rated amongst colleges. However, her personal experience in class did not match the expectations this ranking would provide. We figured this is of course because those rankings given to departments are solely based off their research. But that's not the first thing students look for when they want to know about a department at their school. Thus, this visualization democratizes the rankings by scraping reviews of professors at a given school, grouping them by department, and finally showing the rating of each department on a 1-5 scale. An effective rating is calculated with knowledge informed by Bayes Theorem to account for the number of reviews that produce the department's rating, so we can get a more accurate depiction of both large and small departments against each other.