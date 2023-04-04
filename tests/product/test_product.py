from inventory_report.inventory.product import Product


def test_cria_produto():

    ID = 1
    PRODUCT_NAME = "T-SHIRT"
    COMPANY_NAME = "VI3 Co."
    CREATE_DATE = "06/06/2006"
    VALIDATE_DATE = "09/09/2009"
    NUM_SERIES = "848737"
    STORAGE_GUIDE = "Guarda-roupa"

    produto = Product(
        ID,
        PRODUCT_NAME,
        COMPANY_NAME,
        CREATE_DATE,
        VALIDATE_DATE,
        NUM_SERIES,
        STORAGE_GUIDE,
    )

    assert produto.id == ID
    assert produto.nome_do_produto == PRODUCT_NAME
    assert produto.nome_da_empresa == COMPANY_NAME
    assert produto.data_de_fabricacao == CREATE_DATE
    assert produto.data_de_validade == VALIDATE_DATE
    assert produto.numero_de_serie == NUM_SERIES
    assert produto.instrucoes_de_armazenamento == STORAGE_GUIDE
