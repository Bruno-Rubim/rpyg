from atack.model import Atack, Stab, FireBreath, Shoot, PunchHolder
from entity.model import Entity

class AtackFactory:
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
            
            case _:
                raise(f'attack "{name}" not made yet')
            
        return Atack()