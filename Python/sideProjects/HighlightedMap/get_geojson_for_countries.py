import requests
import os

# List of countries and their acronyms (replace with your actual list)
countries = {
    "Algeria": "DZA",
    "American Samoa": "ASM",
    "Angola": "AGO",
    "Anguilla": "AIA",
    "Antarctica": "ATA",
    "Antigua and Barbuda": "ATG",
    "Argentina": "ARG",
    "Armenia": "ARM",
    "Aruba": "ABW",
    "Australia": "AUS",
    "Azerbaijan": "AZE",
    "The Bahamas": "BHS",
    "Bahrain": "BHR",
    "Bangladesh": "BGD",
    "Barbados": "BRB",
    "Belize": "BLZ",
    "Benin": "BEN",
    "Bermuda": "BMU",
    "Bhutan": "BTN",
    "Bolivia": "BOL",
    "Botswana": "BWA",
    "Brazil": "BRA",
    "British Indian Ocean Territory": "IOT",
    "British Virgin Islands": "VGB",
    "Brunei": "BRN",
    "Burkina Faso": "BFA",
    "Burundi": "BDI",
    "Cabo Verde": "CPV",
    "Cambodia": "KHM",
    "Cameroon": "CMR",
    "Canada": "CAN",
    "Caribbean Netherlands": "BES",
    "Cayman Islands": "CYM",
    "Central African Republic": "CAF",
    "Chad": "TCD",
    "Chile": "CHL",
    "Christmas Island": "CXR",
    "Cocos (Keeling) Islands": "CCK",
    "Colombia": "COL",
    "Comoros": "COM",
    "Cook Islands": "COK",
    "Côte d'Ivoire": "CIV",
    "Costa Rica": "CRI",
    "Curaçao": "CUW",
    "Democratic Republic of the Congo": "COD",
    "Djibouti": "DJI",
    "Dominica": "DMA",
    "Dominican Republic": "DOM",
    "Ecuador": "ECU",
    "Egypt": "EGY",
    "El Salvador": "SLV",
    "Equatorial Guinea": "GNQ",
    "Eritrea": "ERI",
    "Eswatini": "SWZ",
    "Ethiopia": "ETH",
    "Falkland Islands (Islas Malvinas)": "FLK",
    "Fiji": "FJI",
    "Gabon": "GAB",
    "The Gambia": "GMB",
    "Georgia": "GEO",
    "Ghana": "GHA",
    "Gibraltar": "GIB",
    "Grenada": "GRD",
    "Guam": "GUM",
    "Guatemala": "GTM",
    "Guernsey": "GGY",
    "Guinea": "GIN",
    "Guinea-Bissau": "GNB",
    "Guyana": "GUY",
    "Haiti": "HTI",
    "Heard Island and McDonald Islands": "HMD",
    "Honduras": "HND",
    "India": "IND",
    "Indonesia": "IDN",
    "Iraq": "IRQ",
    "Isle of Man": "IMN",
    "Israel": "ISR",
    "Jamaica": "JAM",
    "Japan": "JPN",
    "Jersey": "JEY",
    "Jordan": "JOR",
    "Kazakhstan": "KAZ",
    "Kenya": "KEN",
    "Kiribati": "KIR",
    "Kyrgyzstan": "KGZ",
    "Kuwait": "KWT",
    "Laos": "LAO",
    "Lebanon": "LBN",
    "Lesotho": "LSO",
    "Liberia": "LBR",
    "Libya": "LBY",
    "Madagascar": "MDG",
    "Malawi": "MWI",
    "Malaysia": "MYS",
    "Maldives": "MDV",
    "Mali": "MLI",
    "Marshall Islands": "MHL",
    "Mauritania": "MRT",
    "Mauritius": "MUS",
    "Mexico": "MEX",
    "Micronesia": "FSM",
    "Mongolia": "MNG",
    "Montserrat": "MSR",
    "Morocco": "MAR",
}

# Base URL for GeoJSON files (from the link you provided)
base_url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries/"

# Create a directory to store downloaded files (if it doesn't exist)
os.makedirs("geojson_data", exist_ok=True)

# Download GeoJSON files for each country
for country_name, acronym in countries.items():
    url = f"{base_url}{acronym.upper()}.geo.json"  # Construct URL
    filename = f"geojson_data/{acronym.lower()}.geo.json"  # Output filename

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {country_name} ({acronym})")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {country_name}: {e}")