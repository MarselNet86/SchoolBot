import psycopg2
from config import host, user, password, db_name, port


class Database:
    def __init__(self, database):
        self.connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        self.connection.autocommit = True

    def create_tables(self):
        """Создать таблицы users и results, если они отсутствуют"""
        with self.connection.cursor() as cursor:
            # Создание таблицы users, если она не существует
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    user_id BIGINT,
                    register_date TIMESTAMP DEFAULT NOW()
                );
            """)

            # Создание таблицы results, если она не существует
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS results (
                    id SERIAL PRIMARY KEY,
                    fk_id INT REFERENCES users(id),
                    tier VARCHAR(10),
                    result_number INT
                );
            """)

        print("Таблицы успешно созданы или уже существуют.")

    def user_exists(self, user_id):
        """Проверить пользователя на существование в таблице"""
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE user_id = %s", [user_id])
            result = cursor.fetchall()
            print(bool(len(result)))
            return bool(len(result))

    def add_user(self, user_id):
        """Добавить нового пользователя в таблицу"""
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO users (user_id) VALUES (%s)", [user_id])

    def update_tier(self, user_id, tier):
        """Добавить результат пользователя в таблицу"""
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT id FROM users WHERE user_id = %s", [user_id]
            )
            fk_id = cursor.fetchone()[0]

            cursor.execute(
                "SELECT * FROM results WHERE fk_id = %s", [fk_id]
            )
            result = cursor.fetchone()

            if result is None:
                cursor.execute(
                    "INSERT INTO results (fk_id, tier) VALUES (%s, %s)",
                    [fk_id, tier]
                )
            else:
                cursor.execute(
                    "UPDATE results SET tier = %s, result_number = %s WHERE fk_id = %s",
                    [tier, 0, fk_id]
                )

    def update_result(self, user_id, result_number):
        """Обновить результат пользователя в таблице"""
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT id FROM users WHERE user_id = %s", [user_id]
            )
            fk_id = cursor.fetchone()[0]

            cursor.execute(
                "UPDATE results SET result_number = %s WHERE fk_id = %s",
                [result_number, fk_id])

    def get_top_three(self, tier):
        """Получить результаты пользовтелей из каждой категории"""
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT users.user_id, results.result_number FROM results
                INNER JOIN users ON users.id = results.fk_id
                WHERE results.tier = %s
                ORDER BY results.result_number DESC
                LIMIT 3
                """,
                [tier]
            )
            return cursor.fetchall()


connection = Database(host, user, password, db_name, port)
connection.create_tables()