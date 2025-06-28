## Padrões

### Factory
- /npc/factory.py: criação de NPCs, sendo Enemie ou Friend
- /atack/factory.py: criação de Atacks, tendo múltiplas classes de ataques diferentes

### Template pattern
- /atack/model.py: ataques podem implementar seus próprios métodos de cálculo de dano, ou utilizar a base

### Singleton
- /player/model.py: cria a única instância de jogador que será utilizada durante o jogo

### Mediator
- (planejado) /event