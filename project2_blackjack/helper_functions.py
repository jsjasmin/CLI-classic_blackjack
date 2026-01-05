import random
import string


def ask_player_input(string_input="",data_type="", condition="", player_balance=0):
    '''
    Docstring for ask_player_input
    
    Asks player input, validates it, and returns player input if input is okay.
    If input is not okay, asks another input, until input is okay.

    string_input -- string beside the input bar
    data_type -- data type of the expected input
    condition -- changes the behaviour of validation, 
    player_balance -- during condition "player_bet", checks if bet is within the balance range
    '''
    if data_type == "blank" and condition == "continue":
        player_input = input(f" {string_input} ".center(100, "~"))
        valid_input_format = validate_format_player_input(player_input, data_type, condition, player_balance)
        while valid_input_format == False:
            player_input = input(f" {string_input} ".center(100, "~"))
            valid_input_format = validate_format_player_input(player_input, data_type, condition, player_balance)

    elif data_type == "blank":
        player_input = input(f" {string_input} ".center(100, " "))
        valid_input_format = validate_format_player_input(player_input, data_type, condition, player_balance)
        while valid_input_format == False:
            player_input = input(f" {string_input} ".center(100, " "))
            valid_input_format = validate_format_player_input(player_input, data_type, condition, player_balance)

    else:
        print(string_input)
        player_input = input(">>> ")
        valid_input_format = validate_format_player_input(player_input, data_type, condition, player_balance)
        while valid_input_format == False:
            player_input = input(">>> ")
            valid_input_format = validate_format_player_input(player_input, data_type, condition, player_balance)
    
    return player_input

def validate_format_player_input(player_input, data_type, condition, player_balance):
    '''
    Docstring for validate_format_player_input
        
    Validates player input, and checks if input is acceptable depending on the condition.
    Returns True if acceptable, returns False if not.

    data_type -- changes the behaviour of validation, whether string or int
    condition -- changes the behaviour of validation, 
                "decision" during player turn, 1 if hit, 2 if stand.
                "yes_or_no" after round, continues to play if y, breaks the loop if n.
                "player_bet" during place_bets, checks if bet is below the balance.
                "blank" enter empty space
    player_balance -- during condition "player_bet", checks if bet is within the balance range
        '''
    if data_type == "integer" and (condition == "number_of_computer_players" or condition == "player_bet"):
        valid_input_format = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        invalid_characters = []

        for char in player_input:
            if char not in valid_input_format:
                invalid_characters.append(char)

        if len(invalid_characters) != 0:
            print(f"The input/s: {", ".join(invalid_characters)} is invalid.")
            return False
        elif not(len(player_input) >= 1):
            print(f"The input cannot be empty.")
            return False
        elif condition == "number_of_computer_players" and int(player_input) > 9:
            print(f"The number of computer players cannot be greater than 9.")
            return False
        
        else:
            if condition == "player_bet":
                if int(player_input) > player_balance:
                    print(f"The bet input ( $ {player_input} ) is greater than player balance ( $ {player_balance} )")
                    return False
            else:
                return True
            
    elif data_type == "integer" and condition == "decision":
        valid_input_format = ["1", "2"]

        invalid_characters = []

        for char in player_input:
            if char not in valid_input_format:
                invalid_characters.append(char)

        if len(invalid_characters) != 0:
            print(f"The input/s: {", ".join(invalid_characters)} is invalid.")
            return False
        elif not(len(player_input) >= 1):
            print(f"The input cannot be empty.")
            return False
        elif len(player_input) > 1:
            print(f"The input must only be 1 or 2.")
            return False
        else:
            return True
            
    elif data_type == "string" and condition == "yes_or_no":
        valid_input_format = ["y", "n"]

        invalid_characters = []

        for char in player_input:
            if char not in valid_input_format:
                invalid_characters.append(char)

        if len(invalid_characters) != 0:
            print(f"The character/s: {", ".join(invalid_characters)} is invalid.")
            return False
        elif len(player_input) == 0:
            print(f"The input cannot be empty.")
            return False
        elif len(player_input) > 1:
            print(f"The input must only be 'y' or 'n'.")
            return False
        else:
            return True
        
    elif data_type == "string":
        valid_input_format = list(string.ascii_letters) + list(string.digits) + list(string.whitespace)

        invalid_characters = []

        for char in player_input:
            if char not in valid_input_format:
                invalid_characters.append(char)

        if len(invalid_characters) != 0:
            print(f"The character/s: {", ".join(invalid_characters)} is invalid.")
            return False
        elif not(len(player_input) >= 1):
            print(f"The name cannot be empty.")
            return False
        else:
            return True

    elif data_type == "blank":
        if len(player_input) > 0:
            print(f"The input must be empty.")
            return False
        else:
            return True


# credits to https://parade.com/1032891/marynliles/funny-usernames/
possible_names = [
    "shaquille.oatmeal",
    "hanging_with_my_gnomies",
    "hoosier-daddy",
    "fast_and_the_curious",
    "averagestudent",
    "BadKarma",
    "google_was_my_idea",
    "cute.as.ducks",
    "casanova",
    "real_name_hidden",
    "HairyPoppins",
    "fedora_the_explorer",
    "OP_rah",
    "YellowSnowman",
    "Joe Not Exotic",
    "username_copied",
    "whos_ur_buddha",
    "unfinished_sentenc",
    "AllGoodNamesRGone",
    "Something",
    "me_for_president",
    "tinfoilhat",
    "oprahwindfury",
    "anonymouse",
    "Definitely_not_an_athlete",
    "HeartTicker",
    "YESIMFUNNY",
    "BenAfleckIsAnOkActor",
    "magicschoolbusdropout",
    "Everybody",
    "regina_phalange",
    "PawneeGoddess",
    "pluralizes_everythings",
    "chickenriceandbeans",
    "test_name_please_ignore",
    "IYELLALOT",
    "heyyou",
    "laugh_till_u_pee",
    "aDistraction",
    "crazy_cat_lady",
    "banana_hammock",
    "thegodfatherpart4",
    "unfriendme",
    "babydoodles",
    "fluffycookie",
    "buh-buh-bacon",
    "ashley_said_what",
    "LactoseTheIntolerant",
    "ManEatsPants",
    "Twentyfourhourpharmacy",
    "applebottomjeans",
    "Babushka",
    "toastedbagelwithcreamcheese",
    "baeconandeggz",
    "FartinLutherKing",
    "coolshirtbra",
    "kentuckycriedfricken",
    "REVERANDTOAST",
    "kim_chi",
    "idrinkchocolatemilk",
    "SaintBroseph",
    "chin_chillin",
    "ghostfacegangsta",
    "bigfootisreal",
    "santas_number1_elf",
    "thehornoftheunicorn",
    "iNeed2p",
    "abductedbyaliens",
    "actuallynotchrishemsworth",
    "nachocheesefries",
    "personallyvictimizedbyreginageorge",
    "just-a-harmless-potato",
    "FrostedCupcake",
    "Avocadorable",
    "fatBatman",
    "quailandduckeggs",
    "PaniniHead",
    "mandymooressingingvoice",
    "catsordogs",
    "FartnRoses",
    "RedMonkeyButt",
    "FreddyMercurysCat",
    "MasterCheif",
    "FreeHugz",
    "ima.robot",
    "actuallythedog",
    "notthetigerking",
    "pixie_dust",
    "ChopSuey",
    "turkey_sandwich",
    "B.Juice",
    "Chris_P_Bacon",
    "LtDansLegs",
    "WookiesrPpl2",
    "hogwartsfailure",
    "CourtesyFlush",
    "MomsSpaghetti",
    "spongebobspineapple",
    "garythesnail",
    "nothisispatrick",
    "CountSwagula",
    "SweetP",
    "PNUT",
    "Snax",
    "Nuggetz",
    "colonel_mustards_rope",
    "baby_bugga_boo",
    "joancrawfordfanclub",
    "fartoolong",
    "loliateyourcat",
    "rawr_means_iloveyou",
    "ihavethingstodo.jpg",
    "heresWonderwall",
    "UFO_believer",
    "ihazquestion",
    "SuperMagnificentExtreme",
    "It’s_A _Political_Statement",
    "TheAverageForumUser",
    "just_a_teen",
    "OmnipotentBeing",
    "GawdOfROFLS",
    "loveandpoprockz",
    "2_lft_feet",
    "Bread Pitt",
    "rejectedbachelorcontestant",
    "Schmoople",
    "LOWERCASE GUY",
    "Unnecessary",
    "joan_of_arks_angel",
    "InstaPrincess",
    "DroolingOnU",
    "Couldnt_Find_Good_Name",
    "AngelWonderland",
    "Born-confused",
    "SargentSaltNPepa",
    "DosentAnyoneCare",
    "quaratineinthesejeans",
    "thanoslefthand",
    "ironmansnap",
    "chalametbmybae",
    "peterparkerspuberty",
    "severusvape",
    "theotherharrypotter",
    "GrangerDanger",
    "BlueIvysAssistant",
    "Ariana_Grandes_Ponytail",
    "HotButteryPopcorn",
    "MelonSmasher",
    "morgan_freeman_but_not",
    "potatoxchipz",
    "FoxtrotTangoLove",
    "ElfishPresley",
    "WustacheMax",
    "JuliusSeizure",
    "HeyYouNotYouYou",
    "OneTonSoup",
    "HoneyLemon",
    "LoveMeKnot",
    "Bud Lightyear",
    "takenbyWine",
    "taking0ver",
    "Unic0rns",
    "in_jail_out_soon",
    "hotgirlbummer",
    "behind_you",
    "itchy_and_scratchy",
    "not_james_bond",
    "a_collection_of_cells",
    "CowabungaDude",
    "TeaBaggins",
    "bill_nye_the_russian_spy",
    "intelligent_zombie",
    "imma_rage_quit",
    "kiss-my-axe"
    ]

def give_random_name():
    '''
    Docstring for give_random_name
    
    Returns a random name from possible_names
    '''
    return random.choice(possible_names)

def give_random_number_bet(balance):
    '''
    Docstring for give_random_number_bet
    
    For Computer_players, gives a random bet below their balance.
    Removes ones digits for tidiness.

    balance -- acts as the max possible value for the bet
    '''

    number = int(random.randint(1, int(balance)))
    random_chance = int(random.randint(1, 2))

    if number > 10:
        number = remove_tens_or_ones_digit(number, random_chance)

    return number

def remove_tens_or_ones_digit(number, random_chance):
    '''
    Docstring for remove_tens_or_ones_digit

    Either removes ones digit (for >10) or tens digits (for >100).

    random_chance -- decides for >100, if removing ones of tens
    '''
    if number > 100: 
        if random_chance == 1:
            number = number // 100 * 100

        elif random_chance == 2:
            number = number // 10 * 10
    
    elif number < 100:
        number = number // 10 * 10

    return number

def title_screen():
    '''
    Displays an ASCII art of "Classic BlackJack: CLI Edition".

    Generated from https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+&x=none&v=4&h=4&w=80&we=false,
    with font "Big".
    '''
    print("   _____ _               _        ____  _            _        _            _        ".center(100, " "))
    print("  / ____| |             (_)      |  _ \\| |          | |      | |          | |     _ ".center(100, " "))
    print(" | |    | | __ _ ___ ___ _  ___  | |_) | | __ _  ___| | __   | | __ _  ___| | __ (_)".center(100, " "))
    print(" | |    | |/ _` / __/ __| |/ __| |  _ <| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /    ".center(100, " "))
    print(" | |____| | (_| \\__ \\__ \\ | (__  | |_) | | (_| | (__|   < |__| | (_| | (__|   <   _ ".center(100, " "))
    print("  \\_____|_|\\__,_|___/___/_|\\___| |____/|_|\\__,_|\\___|_|\\_\\____/ \\__,_|\\___|_|\\_\\ (_)".center(100, " "))
    print("              _____ _      _____   ______    _ _ _   _                              ".center(100, " "))
    print("             / ____| |    |_   _| |  ____|  | (_) | (_)                             ".center(100, " "))
    print("            | |    | |      | |   | |__   __| |_| |_ _  ___  _ __                   ".center(100, " "))
    print("            | |    | |      | |   |  __| / _` | | __| |/ _ \\| '_ \\                  ".center(100, " "))
    print("            | |____| |____ _| |_  | |___| (_| | | |_| | (_) | | | |                 ".center(100, " "))
    print("             \\_____|______|_____| |______\\__,_|_|\\__|_|\\___/|_| |_|                 ".center(100, " "))
    print()
    print("Welcome to Classic BlackJack: CLI Edition".center(100, " "))



