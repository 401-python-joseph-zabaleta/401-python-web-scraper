import pytest
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report


def test_count_one():
    url = "https://en.wikipedia.org/wiki/Battle_of_the_Bulge"
    actual = get_citations_needed_count(url)
    expected = 9
    assert actual == expected


def test_report_one():
    url = "https://en.wikipedia.org/wiki/Battle_of_the_Bulge"
    actual = get_citations_needed_report(url)[0]
    expected = 'The Wehrmacht\'s code name for the offensive was Unternehmen Wacht am Rhein ("Operation Watch on the Rhine"), after the German patriotic hymn Die Wacht am Rhein, a name that deceptively implied the Germans would be adopting a defensive posture along the Western Front. The Germans also referred to it as "Ardennenoffensive" (Ardennes Offensive) and Rundstedt-Offensive, both names being generally used nowadays in modern Germany.[citation needed] The French (and Belgian) name for the operation is Bataille des Ardennes (Battle of the Ardennes). The battle was militarily defined by the Allies as the Ardennes Counteroffensive, which included the German drive and the American effort to contain and later defeat it. The phrase Battle of the Bulge was coined by contemporary press to describe the way the Allied front line bulged inward on wartime news maps.[38][39]'
    assert actual == expected


def test_count_two():
    url = "https://en.wikipedia.org/wiki/Battle_of_France"
    actual = get_citations_needed_count(url)
    expected = 2
    assert actual == expected


def test_report_two():
    url = "https://en.wikipedia.org/wiki/Battle_of_France"
    actual = get_citations_needed_report(url)[0]
    expected = """In the winter of 1939–40, the Belgian consul-general in Cologne had anticipated the angle of advance that Manstein was planning. Through intelligence reports, the Belgians deduced that German forces were concentrating along the Belgian and Luxembourg frontiers.
The Belgians anticipated that the Germans would try to land Fallschirmjäger (paratroops) and glider forces to capture Belgian fortifications but their warnings were not heeded by the French nor British.[citation needed]
In March 1940, Swiss intelligence detected six or seven Panzer divisions on the German-Luxembourg-Belgian border and more motorised divisions were detected in the area. French intelligence were informed through aerial reconnaissance that the Germans were constructing pontoon bridges about halfway over the Our river on the Luxembourg-German border. On 30 April, the French military attaché in Bern warned that the centre of the German assault would come on the Meuse at Sedan, sometime between 8 and 10 May. These reports had little effect on Gamelin, as did similar reports from neutral sources such as the Vatican and a French sighting of a 100-kilometre-long (60-mile) line of German armoured vehicles on the Luxembourg border trailing back inside Germany.[60][61]"""
    assert actual == expected
