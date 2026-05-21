# Challenge 1

# Demande le mot à l'utilisateur
word = input("Enter a word: ")

# Crée le dictionnaire puis itère sur chaque caractère
result = {}
for idx, ch in enumerate(word):
	if ch in result:
		result[ch].append(idx)
	else:
		result[ch] = [idx]

# Affiche le dictionnaire final
print(result)


# Challenge 2
# pour tous les exemples donnés

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# Nettoyage et conversion du wallet
wallet_amount = int(wallet.replace('$', '').replace(',', ''))

# Parcours des items dans l'ordre de priorité et ajout au panier si possible
basket = []
for item, price_str in items_purchase.items():
	price = int(price_str.replace('$', '').replace(',', ''))
	if price <= wallet_amount:
		basket.append(item)
		wallet_amount -= price

if not basket:
	print("Nothing")
else:
	print(sorted(basket))