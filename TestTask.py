import discord
from discord import utils
import time
import config
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Властилин, {0} готова к работе!'.format(self.user))

    async def on_message(self, message):
        print('[log] Сообщение от {0.author}: {0.content}'.format(message))

    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.POST_ID:
            channel = self.get_channel(payload.channel_id)  # получаем объект канала
            message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
            member = utils.get(message.guild.members,
                               id=payload.user_id)  # получаем объект пользователя который поставил реакцию

            try:
                emoji = str(payload.emoji)  # эмоджик который выбрал юзер
                role = utils.get(message.guild.roles, id=config.ROLES[emoji])  # объект выбранной роли (если есть)

                if (len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                    await member.add_roles(role)
                    print('[Успех] Пользователь "{0.display_name}" получил роль: "{1.name}"'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[Ошибка] Пользователь "{0.display_name}" превысил количество ролей '.format(member))

            except KeyError as e:
                print('[Ошибка] Эмоджи нет в списке' + emoji)
            except Exception as e:
                print(repr(e))

    async def on_raw_reaction_remove(self, payload):
        channel = self.get_channel(payload.channel_id)  # получаем объект канала
        message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
        member = utils.get(message.guild.members,
                           id=payload.user_id)  # получаем объект пользователя который поставил реакцию

        try:
            emoji = str(payload.emoji)  # эмоджик который выбрал юзер
            role = utils.get(message.guild.roles, id=config.ROLES[emoji])  # объект выбранной роли (если есть)

            await member.remove_roles(role)
            print('[Успех] Роль "{1.name}" была отобрана у пользователя "{0.display_name}"'.format(member, role))

        except KeyError as e:
            print('[Ошибка] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))

# RUN
client = MyClient()
client.run(config.TOKEN);
