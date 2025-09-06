import time
import ssl, certifi
import pandas as pd
from geopy.geocoders import Nominatim

libraries = ['Addison Township Public Library', 'Adrian District Library',
                         'Aitkin Memorial District Library', 'Alanson Area Public Library', 'Albion District Library',
                         'Alcona County Library', 'Alden District Library', 'Allegan District Library',
                         'Allen Park Public Library', 'Allendale Township Library', 'Alma Public Library',
                         'Almont District Library', 'Alpena County Library', 'Alvah N. Belding Memorial Library',
                         'Ann Arbor District Library', 'Armada Free Public Library', 'Ashley District Library',
                         'Athens Community Library', 'Auburn Hills Public Library',
                         'Augusta-Ross Township District Library', 'Bacon Memorial District Library',
                         'Bad Axe District Library', 'Baldwin Public Library', 'Barryton Public Library',
                         'Bath Township Public Library', 'Bay County Library System', 'Beaver Island District Library',
                         'Bellaire Public Library', 'Belleville Area District Library', 'Bellevue Township Library',
                         'Benton Harbor Public Library', 'Benzie Shores District Library', 'Benzonia Public Library',
                         'Berkley Public Library', 'Berrien Springs Community Library', 'Bessemer Public Library',
                         'Betsie Valley District Library', 'Big Rapids Community Library', 'Blair Memorial Library',
                         'Bloomfield Township Public Library', 'Boyne District Library', 'Branch District Library',
                         'Brandon Township Public Library', 'Bridgeport Public Library', 'Bridgman Public Library',
                         'Briggs District Library', 'Brighton District Library', 'Brown City District Library',
             'Buchanan District Library', 'Bullard Sanford Memorial Library', 'Burlington Township Library',
             'Burr Oak Township Library', 'Cadillac-Wexford County Public Library', 'Calumet Public School Library',
             'Camden Township Library', 'Canton Public Library', 'Capital Area District Libraries',
             'Caro Area District Library', 'Carp Lake Township Library', 'Carson City Public Library',
             'Cass District Library', 'Cedar Springs Public Library', 'Center Line Public Library',
             'Central Lake District Library', 'Charles A. Ransom District Library', 'Charlevoix Public Library',
             'Charlotte Community Library', 'Chase Township Public Library', 'Cheboygan Area Public Library',
             'Chelsea District Library', 'Chesterfield Township Library', 'Chippewa River District Library System',
             'Clarkston Independence District Library', 'Clinton Township Public Library',
             'Clinton-Macomb Public Library', 'Coleman Area Library', 'Coloma Public Library', 'Colon Township Library',
             'Columbia Township Library', 'Commerce Township Community Library', 'Community District Library',
             'Comstock Township Library', 'Constantine Township Library', 'Coopersville Area District Library',
             'Crawford County Library', 'Cromaine District Library', 'Crooked Tree District Library',
             'Croton Township Library', 'Crystal Falls District Community Library', 'Curtis Township Library',
             'Darcy Library of Beulah', 'Dearborn Heights City Libraries', 'Dearborn Public Library',
             'Deckerville Public Library', 'Delta Township District Library', 'Delton District Library',
             'Detroit Public Library', 'DeWitt District Library', 'Dexter District Library', 'Dickinson County Library',
             'Dorothy Hull Library - Windsor Township', 'Dorr Township Library', 'Dowagiac District Library',
             'Dowling Public Library', 'Dryden Township Library', 'East Lansing Public Library',
             'Eastpointe Memorial Library', 'Eaton Rapids Area District Library', 'Eau Claire District Library',
             'Ecorse Public Library', 'Elk Rapids District Library', 'Elk Township Library', 'Elsie Public Library',
             'Escanaba Public Library', 'Evart Public Library', 'Fairgrove District Library',
             'Farmington Community Library', 'Fennville District Library', 'Ferndale Area District Library',
             'Fife Lake Public Library', 'Flat River Community Library', 'Flat Rock Public Library',
             'Forsyth Township Public Library', 'Fowlerville District Library',
             'Frankenmuth James E. Wickson District Library', 'Franklin Public Library', 'Fraser Public Library',
             'Freeport District Library', 'Fremont Area District Library', 'Fruitport District Library',
             'Galesburg-Charleston Memorial District Library', 'Galien Township Public Library',
             'Garden City Public Library', 'Gary Byker Memorial Library of Hudsonville', 'Genesee District Library',
             'George W. Spindler Memorial Library', 'Georgetown Township Public Library',
             'Gladstone School & Public Library', 'Gladwin County District Library', 'Glen Lake Community Library',
             'Gloria Coles Flint Public Library', 'Goodland Township Library', 'Grace A. Dow Memorial Library',
             'Grand Ledge Area District Library', 'Grand Rapids Public Library', 'Grant Area District Library',
             'Grosse Pointe Public Library', 'Hackley Public Library', 'Hamburg Township Library',
             'Hamtramck Public Library', 'Harbor Beach Area District Library', 'Harper Woods Public Library',
             'Harrison District Library', 'Harrison Township Public Library', 'Hart Area Public Library',
             'Hartford Public Library', 'Hastings Public Library', 'Hazel Park Memorial District Library',
             'Henika District Library', 'Herrick District Library', 'Hesperia Community Library',
             'Highland Township Public Library', 'Hillsdale Community Library', 'Holly Township Library',
             'Home Township Library', 'Homer Public Library', 'Hopkins District Library',
             'Houghton Lake Public Library', 'Howard Miller Library', 'Howe Memorial Library',
             'Howell Carnegie District Library', 'Hudson Carnegie District Library', 'Huntington Woods Public Library',
             'Indian River Area Library', 'Interlochen Public Library', 'Ionia Community Library',
             'Iosco-Arenac District Library', 'Ironwood Carnegie Library', 'Ishpeming Carnegie Public Library',
             'J. C. Wheeler Public Library', 'Jackson District Library', 'Jacquelin E. Opperman Memorial Library',
             'Jonesville District Library', 'Jordan Valley District Library', 'Kalamazoo Public Library',
             'Kalkaska County Library', 'Kent District Library', 'Laingsburg Public Library',
             'Lake Linden-Hubbell School/Public Library', 'Lake Odessa Community Library',
             "L'Anse Area School-Public Library", 'Lapeer District Library', 'Lawrence Memorial Public Library',
             'Lawton Public Library', 'Leanna Hicks Public Library of Inkster', 'Leelanau Township Library',
             'Leighton Township Library', 'Leland Township Public Library', 'Lenawee District Library',
             'Lenox Township Library', 'LeRoy Community Library', 'Lincoln Park Public Library',
             'Lincoln Township Public Library', 'Litchfield District Library', 'Livonia Public Library',
             'Lois Wagner Memorial Library', 'Loutit District Library', 'Luther Area Public Library',
             'Lyon Township Public Library', 'Lyons Township District Library', 'MacDonald Public Library',
             'Mackinac Island Public Library', 'Mackinaw Area Public Library', 'Madison Heights Public Library',
             'Mancelona Township Library', 'Manchester District Library', 'Manistee County Library',
             'Manistique School & Public Library', 'Maple Rapids Public Library',
             'Marcellus Township Wood Memorial Library', 'Marion Area District Library',
             'Marlette District Library', 'Marshall District Library', 'Mason County District Library',
             'Maud Preston Palenske Memorial Library', 'Mayville District Public Library',
             'McBain Community Library', 'McMillan Township Library', 'Melvindale Public Library',
             'Mendon Township Library', 'Menominee County Library', 'Merrill District Library',
             'Milan Public Library', 'Milford Public Library', 'Millington Arbela District Library',
             'Missaukee District Library', 'Monroe County Library System', 'Montmorency County Public Libraries',
             'Moore Public Library', 'Morton Township Public Library', 'Mount Clemens Public Library',
             'Mulliken District Library', 'Munising School Public Library', 'Muskegon Area District Library',
             'Negaunee Public Library', 'New Buffalo Township Public Library', 'Newaygo Area District Library',
             'Niles District Library', 'North Adams Community Memorial Library', 'North Branch Township Library',
             'Northfield Township Area Library', 'Northville District Library', 'Nottawa Township Library',
             'Novi Public Library', 'Oak Park Public Library', 'Ogemaw District Library', 'Ontonagon Township Library',
             'Orion Township Public Library', 'Osceola Township School Public Library',
             'Oscoda County District Library', 'Otsego County Library', 'Otsego District Public Library',
             'Ovid Public Library', 'Oxford Public Library', 'Parchment Community Library',
             'Pathfinder Community Library', 'Patmos Library', 'Paw Paw District Library',
             'Peninsula Community Library', 'Pentwater Township Library', 'Pere Marquette District Library',
             'Peter White Public Library', 'Petoskey District Library', 'Pigeon District Library',
             'Pinckney Community Public Library', 'Pittsford Public Library', 'Plymouth District Library',
             'Pontiac Public Library', 'Port Austin Township Library', 'Portage District Library',
             'Portage Lake District Library', 'Portland District Library',
             'Potterville-Benton Township District Library', 'Presque Isle District Library',
             'Public Libraries of Saginaw', 'Putnam District Library', 'Rauchholz Memorial Library',
             'Rawson Memorial Library', 'Ray Township Public Library', 'Reading Community Library',
             'Redford Township District Library', 'Reed City Area District Library', 'Reese Unity District Library',
             'Republic-Michigamme Public Library', 'Richfield Township Public Library', 'Richland Community Library',
             'Richland Township Library', 'Richmond Township Library', 'River Rapids District Library',
             'River Rouge Public Library', 'Riverview Veterans Memorial Library', 'Rochester Hills Public Library',
             'Romeo District Library', 'Romulus Public Library', 'Roscommon Area District Library',
             'Roseville Public Library', 'Royal Oak Public Library', 'Ruth Hughes Memorial District Library',
             'Saint Charles District Library', 'Saint Clair County Library System', 'Saint Clair Shores Public Library',
             'Saint Ignace Public Library', 'Salem Township Library', 'Salem-South Lyon District Library',
             'Saline District Library', 'Sandusky District Library', 'Sanilac District Library',
             'Saranac Clarksville District Library', 'Saugatuck-Douglas District Library',
             'Schoolcraft Community Library', 'Schultz-Holmes Memorial Library', 'Sebewaing Township Library',
             'Seville Township Public Library', 'Shelby Area District Library', 'Shelby Township Library',
             'Sherman Township Library', 'Shiawassee District Library', 'Sleeper Public Library',
             'Sodus Township Library', 'South Haven Memorial Library', 'Southfield Public Library',
             'Southgate Veterans Memorial Library', 'Sparta Carnegie Township Library', 'Spies Public Library',
             'Spring Lake District Library', 'Springfield Township Library', 'Stair District Library',
             'Sterling Heights Public Library', 'Sturgis District Library', 'Sunfield District Library',
             'Superior District Library', 'Surrey Township Public Library', 'Suttons Bay-Bingham District Library',
             'Tahquamenon Area Public Library', 'Tamarack District Library', 'Taylor Community Library',
             'Taymouth Township Library', 'Tecumseh District Library', 'Tekonsha Township Public Library',
             'Theodore A. Cutler Memorial Library', 'Thomas E. Fleschner Memorial Library', 'Thomas Township Library',
             'Thompson Home Public Library', 'Thornapple Kellogg School and Community Library',
             'Three Oaks Township Public Library', 'Three Rivers Public Library',
             'Timothy C. Hauenstein Reynolds Township Library', 'Topinabee Public Library',
             'Traverse Area District Library', 'Trenton Veterans Memorial Library', 'Troy Public Library',
             'Utica Public Library', 'Van Buren District Library', 'Vermontville Township Library',
             'Vernon District Public Library', 'Vicksburg District Library', 'Wakefield Public Library',
             'Waldron District Library', 'Walkerville Public/School Library', 'Walled Lake City Library',
             'Walton Erickson Public Library', 'Warren Public Library', 'Waterford Township Public Library',
             'Watertown Township Library', 'Watervliet District Library', 'Wayne Public Library',
             'West Bloomfield Township Public Library', 'West Branch District Library', 'West Iron District Library',
             'Wheatland Township Library', 'White Cloud Community Library', 'White Lake Community Library',
             'White Lake Township Library', 'White Pigeon Township Library', 'White Pine District Library',
             'Whitefish Township Community Library', 'Willard Public Library',
             'William P. Faust Public Library of Westland', 'Wixom Public Library', 'Wolverine Community Library'
]

# setup geocoder
geolocator = Nominatim(
    user_agent="library-mapper",
    ssl_context=ssl.create_default_context(cafile=certifi.where())
)

results = []

for lib in libraries:   # loop through one at a time
    query = f"{lib}, Michigan"
    try:
        loc = geolocator.geocode(query, timeout=10)
        if loc:
            results.append({"Library": lib, "Latitude": loc.latitude, "Longitude": loc.longitude})
            print(f"✅ Found {lib}: {loc.latitude}, {loc.longitude}")
        else:
            results.append({"Library": lib, "Latitude": None, "Longitude": None})
            print(f"⚠️ No result for {lib}")
    except Exception as e:
        results.append({"Library": lib, "Latitude": None, "Longitude": None})
        print(f"❌ Error for {lib}: {e}")

    time.sleep(1)

# save to CSV
pd.DataFrame(results).to_csv("library_coords.csv", index=False)
print("Saved results to library_coords.csv")
