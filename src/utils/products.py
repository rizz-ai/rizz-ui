

product_types = """FALL OUTFITS,
NEW,
COATS,
TRENCH COATS,
JACKETS,
BOMBER JACKETS,
BLAZERS,
WAISTCOATS,
DRESSES,
JUMPSUITS,
CARDIGANS,
SWEATERS,
TOPS,
BODYSUITS,
SHIRTS,
BLOUSES,
T-SHIRTS,
HOODIES,
SWEATSHIRTS,
KNITWEAR,
PANTS,
JEANS,
SKIRTS,
SHORTS,
SHOES,
BAGS,
ACCESSORIES,
JEWELRY,
FRAGRANCES,
BEAUTY,
LINGERIE,
PAJAMAS,
SUITS,
CO-ORD SETS,
LOUNGEWEAR,
WORKWEAR,
HOME,
BASICS"""

product_types = product_types.split(',\n')
PRODUCT_TYPES = [s.capitalize() for s in product_types] + ["Skort","Other"]

print(PRODUCT_TYPES)

