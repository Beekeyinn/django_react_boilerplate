import argparse
import json
import secrets
import string


def generate_secrets(
    chars=string.ascii_letters + string.digits + "!@#$%^&*()", size=50
):
    return "".join([secrets.choice(chars) for i in range(size)])


def main():
    parser = argparse.ArgumentParser(description="Used to generate the env file")
    parser.add_argument(
        "-d",
        "--database",
        type=str,
        action="extend",
        nargs="+",
        help="provide database_host database_name database_port database_username database_password",
    )
    parser.add_argument(
        "-k",
        "--key",
        type=str,
        help="provide OPEN AI key",
    )
    database_host = "localhost"
    database_name = "candybit_openai"
    database_port = 5432
    database_username = "postgres"
    database_password = "postgres"
    args = parser.parse_args()
    if args.database:
        if len(args.database) != 5:
            print("Error while parsing arguments. pleas use --help for further detail.")
        database_host = args.database[0]
        database_name = args.database[1]
        database_port = args.database[2]
        database_username = args.database[3]
        database_password = args.database[4]
    if args.key:
        openai_key = args.key
    else:
        print(" Please provide the key for open api")
        return
    secret_key = generate_secrets()

    with open("config.json", "r", encoding="utf-8") as fle:
        config = json.load(fle)

    with open(".env", "w", encoding="utf-8") as env:
        env.write(f"SECRET_KEY={secret_key}\n\n")
        env.write(f"ALLOWED_HOSTS={config['ALLOWED_HOSTS']}\n")
        env.write(f"TIMEZONE={config['TIMEZONE']}\n")
        env.write(f"ADD_SLASH=False\n")
        env.write(f"DEBUG={config['DEBUG']}\n\n\n\n")
        env.write(f"# ---------------DATABASE-------------\n")
        env.write(f"DATABASE_HOST={database_host}\n")
        env.write(f"DATABASE_NAME={database_name}\n")
        env.write(f"DATABASE_USERNAME={database_username}\n")
        env.write(f"DATABASE_PASSWORD={database_password}\n")
        env.write(f"DATABASE_PORT={database_port}\n\n\n\n")
        env.write(f"# ---------------KEYS-------------\n")
        env.write(f"OPEN_AI_KEY={openai_key}")

    print("completed")


if __name__ == "__main__":
    main()
