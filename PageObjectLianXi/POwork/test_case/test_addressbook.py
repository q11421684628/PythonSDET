from PageObjectLianXi.POwork.page.addressbook_page import AddressBook
from PageObjectLianXi.POwork.page.main_page import Main


class TestAddressBook:
    def setup_class(self):
        self.addressbook = Main()
        self.editor = AddressBook()

    def test_add_people(self):
        self.addressbook.add_people().add_people("test_01", "test_01", "13826473849")

    def test_editor_people(self):
        self.editor.editor_people("test02", "13924175992")

    def teardown_class(self):
        self.addressbook.close()
