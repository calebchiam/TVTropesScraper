import json

caleb_tuples = [("2001aspaceodyssey", "TwoThousandOneASpaceOdyssey"),
          ("starskyhutch", "StarskyAndHutch"),
          ("batmanrobin", "BatmanAndRobin"),
          ("48hrs", "FortyEightHours"),
          ("amosandrew", "AmosAndAndrew"),
          ("28weekslater", "TwentyEightWeeksLater"),
          ("10thingsihateaboutyou", "TenThingsIHateAboutYou"),
          ("memyselfirene", "MeMyselfAndIrene"),
          ("thecookthethiefhiswifeherlover", "TheCookTheThiefHisWifeAndHerLover"),
          ("petsemataryii", "PetSemataryTwo"),
          ("bennyjoon", "BennyAndJoon"),
          ("3ninjas", "ThreeNinjas"),
          ("thelordoftheringsthefellowshipofthering", "TheLordOfTheRings"),
          ("thecircle", "TheCircle2017"),
          ("horriblebosses2", "HorribleBosses"),
          ("300", "ThreeHundred"),
          ("fx2", "FXMurderByIllusion"),
          ("54", "FiftyFour"),
          ("fathersday", "FathersDay2011"),
          ("1114", "ElevenFourteen"),
          ("marleyme", "MarleyAndMe"),
          ("batmanthedarkknightreturnspart1", "BatmanTheDarkKnightReturns"),
          ("28dayslater", "TwentyEightDaysLater"),
          ("inout", "InAndOut"),
          ("pokémonthefirstmovie", "PokemonTheFirstMovie"),
          ("manonofthespring", "ManonDesSources"),
          ("mccabemrsmiller", "McCabeAndMrsMiller"),
          ("oblivion", "Oblivion2013"),
          ("thechroniclesofnarniaprincecaspian", "PrinceCaspian"),
          ("lagaanonceuponatimeinindia", "Lagaan"),
          ("thecreaturefromtheblacklagoon", "CreatureFromTheBlackLagoon"),
          ("gnomeojuliet", "GnomeoAndJuliet"),
          ("nationaltreasurebookofsecrets", "NationalTreasure"),
          ("wallacegromitacloseshave", "ACloseShave"),
          ("christmasvacation", "NationalLampoonsChristmasVacation"),
          ("12angrymen", "TwelveAngryMen"),
          ("tuckerdalevsevil", "TuckerAndDaleVsEvil"),
          ("sunsetblvd", "SunsetBoulevard"),
          ("thelegendofdrunkenmaster", "DrunkenMaster"),
          ("5centimeterspersecond", "FiveCentimetersPerSecond"),
          ("500daysofsummer", "FiveHundredDaysOfSummer"),
          ("dumbdumber", "DumbAndDumber"),
          ("blacksheep", "BlackSheep2007"),
          ("garfieldthemovie", "Garfield"),
          ("thelmalouise", "ThelmaAndLouise"),
          ("williamshakespearesromeojuliet", "WilliamShakespearesRomeoAndJuliet"),
          ("turnerhooch", "TurnerAndHooch"),
          ("batmanthedarkknightreturnspart2", "BatmanTheDarkKnightReturns"),
          ("8women", "EightWomen"),
          ("brüno", "Bruno"),
          ("1984", "NineteenEightyFour"),
          ("johnwickchaptertwo", "JohnWickChapter2"),
          ("legallyblonde2redwhiteblonde", "LegallyBlonde"),
          ("elitesquadtheenemywithin", "TheEliteSquad"),
          ("problemchild2", "ProblemChild"),
          ("thebenchwarmers", "Benchwarmers"),
          ("mrmrssmith", "MrAndMrsSmith2005"),
          ("familyguypresentsstewiegriffintheuntoldstory", "StewieGriffinTheUntoldStory"),
          ("avpraliensvspredatorrequiem", "AliensVsPredatorRequiem"),
          ("pokémon3themovie", "Pokemon3"),
          ("misérablesles","LesMiserables2012"),
          ("8mm", "EightMM"),
          ("winniethepoohandtheblusteryday", "TheManyAdventuresOfWinnieThePooh"),
          ("cowboybebopthemovie", "CowboyBebop"),
          ("guardiansofthegalaxy2", "GuardiansOfTheGalaxyVol2"),
          ("1408", "FourteenOhEight"),
          ("tremorsiiaftershocks", "Tremors2Aftershocks"),
          ("thefogofwarelevenlessonsfromthelifeofrobertsmcnamara", "TheFogOfWar"),
          ("elitesquad", "TheEliteSquad"),
          ("heavenearth", "HeavenAndEarth"),
          ("hanselgretelwitchhunters", "HanselAndGretelWitchHunters"),
          ("2012", "TwoThousandTwelve"),
          ("lilya4ever", "LilyaFourEver"),
          ("alien³", "Alien3"),
          ("30daysofnight", "ThirtyDaysOfNight"),
          ("thesis", "Tesis"),
          ("2guns", "TwoGuns"),
          ("drseussthelorax", "TheLorax"),
          ("21", "TwentyOne"),
          ("misscongeniality2armedandfabulous", "MissCongeniality"),
          ("starwarstheclonewars", "StarWarsTheCloneWars"),
          ("meninblackiii", "MenInBlack"),
          ("allegiantpart1", "Divergent"),
          ("boratculturallearningsofamericaformakebenefitgloriousnationofkazakhstan", "Borat")
           ]

#
#
#
# with open("fixednames_caleb.json", 'w') as f:
#     for t in caleb_tuples:
#         entry = {"name": t[0], "trope": t[1]}
#         json.dump(entry, f)
#         f.write("\n")


# with open("fixednames_alena.json", 'r') as f:
#     sets = set()
#     for line in f:
#         if line in sets: print(line)
#         else: sets.add(line)

with open("combined_fixednames.json", 'w') as f:
    for file in ["fixednames_caleb.json", "fixednames_alena.json", "fixednames_hartek.json"]:
        with open(file, 'r') as f2:
            for line in f2:
                f.write(line)