from atack.model import Atack, Stab, FireBreath, Shoot, PunchHolder

class atackFactory:
    def get_atack(name: str, atacker, reciever) -> Atack:
        match name:
            case 'stab':
                atack = Stab(
                    atacker = atacker,
                    reciever = reciever
                )
                return atack

            case 'fire_breath':
                atack = FireBreath(
                    atacker = atacker,
                    reciever = reciever
                )
                return atack

            case 'shoot':
                atack = Shoot(
                    atacker = atacker,
                    reciever = reciever
                )
                return atack
            
            case 'punch_holder':
                atack = PunchHolder(
                    atacker = atacker,
                    reciever = reciever
                )
                return atack
            
            case _:
                raise(f'attack "{name}" not made yet')