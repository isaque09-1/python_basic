import asyncio
import time
async def fazer_arroz():
    print('Fazendo arroz...')
    #await asyncio.to_thread(time.sleep(3))
    await asyncio.sleep(3)

    print('Arroz pronto!')
async def fazer_carne():
    print('Fazendo carne...')
    await asyncio.sleep(5)
    print('Carne pronta!')
async def fazer_feijao():
    print('Fazendo feijão...')
    await asyncio.sleep(7)
    print('Feijão pronto!')
async def cozinhar():
    await asyncio.gather(
    fazer_arroz(),
    fazer_carne(),
    fazer_feijao(),
    )
print('Almoço pronto!')
asyncio.run(cozinhar()) 