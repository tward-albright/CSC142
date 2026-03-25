from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_cost(self):
        raise NotImplementedError


class ByWeightItem(Item):
    def __init__(self, name, weight, cost_per_pound):
        self.name = name
        self.weight = weight
        self.cost_per_pound = cost_per_pound

    def calculate_cost(self):
        return self.weight * self.cost_per_pound


class ByQuantityItem(Item):
    def __init__(self, name, quantity, cost_each):
        self.name = name
        self.quantity = quantity
        self.cost_each = cost_each

    def calculate_cost(self):
        return self.quantity * self.cost_each


class Grapes(ByWeightItem):
    def __init__(self, weight):
        new_name = f"Grapes ({weight} lb.)"
        super().__init__(new_name, weight, 1.5)


class Bananas(ByWeightItem):
    def __init__(self, weight):
        new_name = f"Bananas ({weight} lb.)"
        super().__init__(new_name, weight, 2)


class Oranges(ByQuantityItem):
    def __init__(self, quantity):
        new_name = f"{quantity} orange(s)"
        super().__init__(new_name, quantity, 0.75)


class Cantaloupes(ByQuantityItem):
    def __init__(self, quantity):
        new_name = f"{quantity} cantaloupe(s)"
        super().__init__(new_name, quantity, 1.2)


class Order:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_items(self):
        return self._items

    def calculate_total(self):
        return sum([item.calculate_cost() for item in self._items])

    def __len__(self):
        return len(self._items)


def main():
    order = Order()
    order.add_item(Bananas(5))
    order.add_item(Grapes(2))
    order.add_item(Oranges(10))
    order.add_item(Cantaloupes(2))

    print("Reciept: ")
    for item in order.get_items():
        print(f"  {item.name}: ${item.calculate_cost():.2f}")

    print(f"{len(order)} item(s)")
    print(f"Total cost: ${order.calculate_total():.2f}")


if __name__ == "__main__":
    main()
