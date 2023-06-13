def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
#reverse the fruit list
    fruit_list.reverse()
    print(f"Reverse: {fruit_list}")

#add a fruit:
    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")
#insert cherry
    index = fruit_list.index("apple")
    fruit_list.insert(index,"cherry")
    print(f"insert cherry: {fruit_list}")
#minion ate the banana
    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")
#pop
    popped = fruit_list.pop()
    print(f"pop list: {fruit_list}")
    print(f"popped fruit: {popped}")

    fruit_list.sort()
    print(f"sorted: {fruit_list}")

    fruit_list.clear()
    print(f"cleared: {fruit_list}")


if __name__ == "__main__":
    main()