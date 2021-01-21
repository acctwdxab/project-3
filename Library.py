# Dan Wu
# 1/19/2021
# To write a Library simulator involving multiple classes:  the LibraryItem, Patron  Library classes,
# and the three classes that inherit from LibraryItem (Book, Album and Movie).

class LibraryItem:
    """Represents the items in the library"""
    def __init__(self,library_item_id,title):
        """initialize LibraryItem """
        self._library_item_id = library_item_id
        self._title = title
        self._location ="ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = 0

    def get_library_item_id(self):
        """get the item id"""
        return self._library_item_id

    def get_location(self):
        """get the item's location"""
        return self._location

    def get_title (self):
        """get the library item title"""
        return self._title
    def set_localtion(self,location):
        """set the new location"""
        self._location = location

    def get_checked_out_by(self):
        """get the patron iD who checked out the library item"""
        return self._checked_out_by

    def set_checked_out_by(self,patron_id):
        """set the patron id for the item checked out"""
        self._checked_out_by =patron_id

    def get_requested_by(self):
        """get the patron id for the item requested"""
        return self._requested_by

    def set_requested_by(self,patron_id):
        """set the patron id to requested by"""
        self._requested_by = patron_id

    def get_date_checked_out(self):
        """get the date the library item was checked out"""
        return self._date_checked_out

    def set_date_checked_out(self,current_date):
        """set the date the item checked out"""
        self._date_checked_out = current_date



class Book(LibraryItem):
    """inherits aspects of LibraryItem, specific to book item """
    def __init__(self,library_item_id,title,author=""):
        """Initialize attributes of the parent class. Then initialize attributes specific to an book item"""
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._author = author

    def get_author(self):
        """get the author name for the book"""
        return self._author

    def get_check_out_length(self ) :
        """method represents that book item can be checked out for 21 days"""
        return 21

class Album (LibraryItem):
    """Representing aspects of LibraryItem, specific to Album item """

    def __init__(self , library_item_id , title ,  artist="") :
        """Initialize attributes of the parent class. Then initialize attributes specific to an Album item"""
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._artist = artist

    def get_artist(self):
        """get the artist name for the album"""
        return self._artist

    def get_check_out_length(self ) :
        """method represents that the album items can only be checked out for maximum 14 days"""
        return 14

class Movie(LibraryItem) :
    """Representing aspects of LibraryItem, specific to Movie item """

    def __init__(self , library_item_id , title , director="") :
        """Initialize attributes of the parent class. Then initialize attributes specific to an Movie item"""
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._director = director

    def get_director(self):
        """get the director information for the movie"""
        return self._director

    def get_check_out_length(self):
        """method represents that the movie item can only be checked out for a maximum 7 days"""
        return 7



class Patron:
    """represents patron"""
    def __init__(self,patron_id,name):
        """initialize the patron with parameters patron_id and patron name"""
        self._patron_id = patron_id
        self._name = name
        self._fine_amount = 0
        self._checked_out_items = []


    def get_name(self):
        """get method to get the patron name"""
        return self._name

    def get_patron_id(self) :
        """get method to get the patron id"""
        return self._patron_id

    def get_fine_amount(self):
        """get fine amount for the patron"""
        return self._fine_amount

    def get_checked_out_items(self):
        """get method to get the current checked out items"""
        return self._checked_out_items

    def add_library_item(self,library_item_id):
        """method representing the action adding library item to checked out items"""
        self._checked_out_items.append(library_item_id)

    def remove_library_item(self,library_item_id):
        """method representing the action removing the library items from checked out items"""
        self._checked_out_items.remove (library_item_id)

    def amend_fine(self,fine_amount):
        """change fine amount"""
        self._fine_amount+=fine_amount

class Library:
    """represent library """
    def __init__(self):
        """initialize the library with three parameters: holdings- collection of books; members - collection of patrons who are members
         and current date"""
        self._current_date =0
        self._holdings =[]
        self._members =[]


    def get_holdings(self):
        """get current collection of library items"""
        return self._holdings


    def get_members(self) :
        """get current list of patron members"""
        return self._members

    def check_if_in_members(self,patron_id):
        """check if a patron is in the members list"""
        if patron_id in self._members:
            return True
        else:
            return False

    def check_if_in_holdings(self , library_item_id) :
        """check if a item is in the holdings list"""
        if library_item_id in self._holdings :
            return True
        else :
            return False

    def get_library_item(self,library_item_id):
        """if the given ID matches that of an item in the holdings list returns that item, if not returns none"""
        for item in self._holdings:
            if item.get_library_item_id() ==library_item_id:
                return item
            continue
        return None

    def get_patron_id(self , patron_id) :
        """if the given ID matches that of an item in the members list returns that patron, if not returns none"""
        for patron in self._members :
            if patron.get_patron_id() == patron_id :
                return patron
            continue
        return None

    def add_library_item (self,library_item_id):
        """takes a LibraryItem object as a parameter and adds it to the holdings"""
        return self._holdings.append(library_item_id)

    def add_patron (self, patron_id):
        """takes a Patron object as a parameter and adds it to the members"""
        return self._members.append(patron_id)

    def set_checked_out_by (patron_id):
        """represents when you check out the item you set the patron id info"""
        LibraryItem.checked_out_by=patron_id

    def set_date_checked_out(self) :
        """represents setting the date you check out """
        return self._current_date



    def set_location(self) :
          """represents setting the new location to on hold"""
          LibraryItem.get_location = "CHECKED_OUT"

    def check_out_library_item(self,library_item_id,patron_id):
        """update the library item checkout information including date checked and location"""
        for patron in self._members:
            if patron.get_patron_id() ==patron_id:
                for item in self._holdings:
                    if item.get_library_item_id()==library_item_id:
                       if item.get_location() =="CHECKED_OUT":
                           return "item already checked out"
                       elif item.get_location() == "ON_HOLD_SHELF":
                           return "item on hold by other patron"
                       else:
                           item.set_checked_out_by(patron_id)
                           item.set_date_checked_out(self._current_date)
                           item.set_location("CHECKED_OUT")
                           if item.get_requested_by() == patron_id:
                               item.set_requested_by(None)
                           patron_id.add_library_item(item)
                           return "check out successful"
                    continue
                return "item not found"
            continue
        return "patron not found"

    def return_library_item(self,library_item_id):
          """represent the action of returning library item"""
          for item in self._holdings:
               if item.get_library_item_id ==library_item_id:
                   if item.get_location()== "CHECKED_OUT":
                       patron = item.get_checked_out_by()
                       patron.remove_library_item(item)
                       if item.get_requested_by() !=None:
                          item.set_location("ON_HOLD_SHELF")
                          item.set_location("ON_SHELF")
                          item.set_checked_out_by(None)
                       return  "return successful"
                   return "item already in library"
               continue
               return "item not found"



    def request_library_item(self,patron_id,library_item_id):
        """represents the action of requesting library item"""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                for item in self._holdings:
                    if item.get_library_item_id() == library_item_id:
                        if item.get_requested_by() !=None:
                            return "item already on hold"
                        item.set_requested_by(patron)
                        if item.get_location() =="ON_SHELF":
                            item.set_location("ON_HOLD_SHELF")
                            return "request successful"
                        continue
                    return "item not found"
                continue
            return "patron not found"


    def pay_fine(self,patron_id,amount):
        """represents the action of paying fine for passing duedate"""
        for patron in self._members:
            if patron.get_patron_id()== patron_id:
                patron.amend_fine(-amount)
                return "payment successful"
        return "patron not found"

    def increment_current_date(self):
        """increase the patron's fine by 10% for each overdue item checked out"""
        self._current_date +=1
        for patron in self._members:
            for item in patron.get_checked_out_items():
                if (self._current_date - item.get_date_checked_out()) > item.get_check_out_length()+1:
                    patron.amend_fine(0.1)
                    continue

def main():
    b1 = Book ( "345" , "Phantom Tollbooth" , "Juster" )
    a1 = Album ( "456" , "...And His Orchestra" , "The Fastbacks" )
    m1 = Movie ( "567" , "Laputa" , "Miyazaki" )
    print ( b1.get_author () )
    print ( a1.get_artist () )
    print ( m1.get_director () )

    p1 = Patron ( "abc" , "Felicity" )
    p2 = Patron ( "bcd" , "Waldo" )

    lib = Library ()
    lib.add_library_item ( b1 )
    lib.add_library_item ( a1 )
    lib.add_patron ( p1 )
    lib.add_patron ( p2 )

    lib.check_out_library_item ( "bcd" , "456" )
    loc = a1.get_location ()
    lib.request_library_item ( "abc" , "456" )
    for i in range ( 57 ) :
        lib.increment_current_date ()  # 57 days pass
    p2_fine = p2.get_fine_amount ()
    print(lib.pay_fine ( "bcd" , p2_fine ))
    print(lib.return_library_item ( "456" ))
    print(p1.get_fine_amount())
if __name__=="__main__":
    main()





