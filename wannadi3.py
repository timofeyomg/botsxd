from twitchio.ext import commands
import vk_api
from enum import IntEnum


def captcha_handler(captcha):
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)


class VkUserPermissions(IntEnum):
    STATUS = 2 ** 10


vk_session = vk_api.VkApi(
    login='timofeyomg@mail.ru',
    password='43729487a',
    token='vk1.a.31rthjeuujAsOsxiILGX4ssBFBVY5LZ-HeKgVXt3vpizr36uUilXKmp9iVjNx-K-Jv9XCqKFkVgBLzHsgwY7n-BZlIPrGszpOSVCK8OV-fIo1Ah4IiXtSTKIiiZS0YKJdwqLS63cqLZli_vKvswhscQGtd-ICGXZ4FZr-Lckuy5oD-YsZwLyRzHaE0BEwleV1K9jJuzVk8lbjaKd1JGM9A',
    captcha_handler=captcha_handler)
vk_session.auth()
vk = vk_session.get_api()
bot_name = 'botname'
bot = commands.Bot(
    token="oauth:3iwp50jcm6f8c5v4n4fshlxctnh5m8",  # https://twitchapps.com/tmi/
    nick='timofeyomg_',
    prefix='!',  # you can choose any prefix, now its !song
    initial_channels=['wannadi3']
)


@commands.cooldown(rate=1, per=10)
@bot.command(name='song', aliases=['ыщтп','песня','пiсня','gtcyz','трек','nhtr','трэк','track','music','ьгышс','музыка','vepsrf','сейчасиграет'])
async def test(ctx, status=''):
    with vk_api.VkRequestsPool(vk_session) as pool:
        status = pool.method('status.get', {"user_id": "619942631"})
    audio = status.result ['text']

    if len(status.result) > 1:
        await ctx.channel.send(f'@{ctx.author.name}, сейчас играет: ' + audio)
        print('Done. Now playing: ' + audio)
    else:
        await ctx.channel.send(f'@{ctx.author.name}, сейчас ничего не играет wannad1Dx')
        print('Done. Nothing playing.')


if __name__ == '__main__':
    bot.run()