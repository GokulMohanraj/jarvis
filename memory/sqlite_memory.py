from memory.database import get_connection

def add_message(role, content):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversations(role, content)
        VALUES (?, ?)
        """,
        (role, content)
    )

    conn.commit()
    conn.close()

def get_history(limit=20):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role, content
        FROM conversations
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()

    conn.close()

    rows.reverse()

    return [
        {
            "role": row[0],
            "content": row[1]
        }
        for row in rows
    ]

def clear_history():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM conversations"
    )

    conn.commit()
    conn.close()