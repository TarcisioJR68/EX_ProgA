def descendentes(arv):
    if arv == []:
        return []
    
    else:
        return [p for p in arv if isinstance(p, str)] + [des for e in arv if isinstance(e, (tuple, list)) for des in descendentes(e)]

arv = ( "Maria", [ ("Joana", [ ("Lucio", []),
                               ("Jõao", [])
                             ]
                   ),
                   ("Pedro",[]),
                   ("Patricia", [ ("Marina", [ ("Marcelo", []),
                                               ("Tomás", [])
                                             ]
                                  )
                                ]
                   ),
                   ("Marcos",[])
                 ]
      )

print(descendentes(arv[1]))