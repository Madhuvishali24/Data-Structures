families={
          'charley':{'sam':{'boxy','roy'},
                     'nila':{'pepsy'}},
          'devi':{'tommy':{'tony'},
                  'timmy':{'hamster'},
                  'tammy':{'Hamster'}},
          'carlos':{'dirgo':'cat','ferret':'fox'}
        }
for parent,children in families.items():
    print(f"{parent} has {len(children)} kid(s):")
    print(f"{', and '.join([str(child) for child in [*children]])}")
