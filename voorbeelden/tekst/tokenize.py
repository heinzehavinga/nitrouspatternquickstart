from pattern.en import tokenize

# Zie je hoe tokenize succesvol etc. herkent als afkorting? Dit is het voordeel van een normale string split().
words = tokenize('Two households etc. both alike in dignity,In fair Verona. where we lay our scene,From ancient grudge break to new mutiny,Where civil blood makes civil hands unclean.')
print words