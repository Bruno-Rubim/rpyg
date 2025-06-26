from attack.model import Attack, Stab

class NpcFactory:
    def get_npc(name: str, attacker, reciever) -> Attack:
        match name:
            case 'stab':
                attack = Stab(
                        name = 'stab',
                        attacker = attacker,
                        reciever = reciever
                        )
                return attack
