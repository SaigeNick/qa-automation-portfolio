from pages.inventory_page import InventoryPage

def test_inventory_page(driver, auto_login):
    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    actual_text = inventory_page.get_cart_text()
    assert "1" == actual_text, "Item wasn't added to text"