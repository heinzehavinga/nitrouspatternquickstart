from pattern.en import tag

for word, pos in tag('Two households, both alike in dignity,In fair Verona, where we lay our scene,From ancient grudge break to new mutiny,Where civil blood makes civil hands unclean.'):
  if pos == "JJ": # Retrieve all adjectives.
    print word

