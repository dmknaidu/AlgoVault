from algorithms.catalog import registry


def main():
    print("Registered Algorithms")
    print("=" * 50)

    for algorithm in registry.list_all():
        print(f"ID: {algorithm.id}")
        print(f"Name: {algorithm.name}")
        print(f"Category: {algorithm.category}")
        print(f"Time: {algorithm.time_complexity}")
        print(f"Space: {algorithm.space_complexity}")
        print()


if __name__ == "__main__":
    main()