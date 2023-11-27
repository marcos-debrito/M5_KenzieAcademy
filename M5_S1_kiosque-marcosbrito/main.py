from management.tab_handler import calculate_tab
from menu import products
from management import product_handler


if __name__ == "__main__":
    # Seus prints de teste aqui
    print(product_handler.get_product_by_id(1))
    print(product_handler.get_products_by_type('asdasd'))

    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }

    print(product_handler.add_product(products, **new_product))
    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))
    print(product_handler.menu_report())


# para rodar os testes :
"""
python -m pytest --testdox -vvs tests/tarefas/tarefa_1
python -m pytest --testdox -vvs tests/tarefas/tarefa_2
python -m pytest --testdox -vvs tests/tarefas/tarefa_3

python -m pytest --testdox
"""
