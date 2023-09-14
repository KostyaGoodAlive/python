import asyncpg
import asyncio


class Database():
    def __init__(self):
        loop = asyncio.get_event_loop()
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                user='KostyaGoodAlive',
                database='neondb',
                password='TL6XKA4fkVqN',
                host='ep-restless-butterfly-233506.eu-central-1.aws.neon.tech',
                port='5432'
            )
        )


    async def register_user(self, first_name, last_name ,telegram_id, username):
        sql = f"""
        INSERT INTO telegram_user (first_name,last_name, telegram_id,username)
        VALUES ('{first_name}','{last_name}', '{telegram_id}', '{username}')
        """
        await self.pool.execute(sql)
    async def check_user(self, telegram_id):
        sql = f"""
        SELECT * FROM telegram_user WHERE telegram_id = '{telegram_id}'
        """
        result = await self.pool.fetchrow(sql)
        return result    