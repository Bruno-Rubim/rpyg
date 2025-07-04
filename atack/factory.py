from atack.model import Atack, Stab, FireBreath, Shoot, PunchHolder, Spit
from entity.model import Entity

# Factory
# Abstrai a construção de objetos entre várias subclasses

class AtackFactory:
    # a partir de uma variável seletor "name" a factory decide qual
    # classe será construída e retornada
    def get_atack(name: str, atacker: Entity, battle) -> Atack:
        match name:
            case 'stab':
                atack = Stab(
                    atacker = atacker,
                    battle = battle,
                )
                return atack

            case 'fire_breath':
                atack = FireBreath(
                    atacker = atacker,
                    battle = battle,
                )
                return atack

            case 'shoot':
                atack = Shoot(
                    atacker = atacker,
                    battle = battle,
                )
                return atack
            
            case 'punch_holder':
                atack = PunchHolder(
                    atacker = atacker,
                    battle = battle,
                )
                return atack
            
            case 'spit':
                atack = Spit(
                    atacker = atacker,
                    battle = battle,
                )
                return atack
            
            case _:
                raise(f'attack "{name}" not made yet')
            
        return Atack()