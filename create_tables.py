from restaurant import app, db
from restaurant.models import User, Table, Item, Order

with app.app_context():
    db.create_all()
    
    # Add sample tables if none exist
    if Table.query.count() == 0:
        sample_tables = [
            Table(table=1, time="10:00-11:00 AM", date="2024-01-15", accomodation=4),
            Table(table=2, time="11:00-12:00 PM", date="2024-01-15", accomodation=2),
            Table(table=3, time="12:00-01:00 PM", date="2024-01-15", accomodation=6),
            Table(table=4, time="01:00-02:00 PM", date="2024-01-15", accomodation=4),
            Table(table=5, time="02:00-03:00 PM", date="2024-01-15", accomodation=8),
        ]
        for table in sample_tables:
            db.session.add(table)
    
    # Add sample menu items if none exist
    if Item.query.count() == 0:
        sample_items = [
            Item(name="Barbecue Salad", description="Delicious grilled salad", price=200, source="plate1.png"),
            Item(name="Salad with Fish", description="Fresh fish salad", price=150, source="plate2.png"),
            Item(name="Spinach Salad", description="Healthy spinach salad", price=100, source="plate3.png"),
            Item(name="Fresh Salad", description="Garden fresh salad", price=120, source="salad.png"),
            Item(name="Fried Noodles", description="Crispy fried noodles", price=180, source="noodles.png"),
            Item(name="Roasted Chicken", description="Juicy roasted chicken", price=300, source="chicken.png"),
            Item(name="Cheese Pizza", description="Cheesy delicious pizza", price=250, source="pizza.png"),
            Item(name="Burger", description="Classic beef burger", price=220, source="burger.png"),
        ]
        for item in sample_items:
            db.session.add(item)
    
    db.session.commit()
    print("All tables created successfully.")
    print(f"Sample data added: {Table.query.count()} tables, {Item.query.count()} menu items")