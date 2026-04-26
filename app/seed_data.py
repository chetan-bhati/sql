import random
from faker import Faker
from sqlalchemy.orm import Session
from app.database import PracticeSessionLocal, practice_engine, BasePractice
from app.models_practice import User, Product, Order, OrderItem, Payment

BasePractice.metadata.create_all(bind=practice_engine)
fake = Faker()

def seed_database():
    db: Session = PracticeSessionLocal()

    # Check if data already exists
    if db.query(User).first():
        print("Data already seeded.")
        db.close()
        return

    print("Seeding Users...")
    users = []
    for _ in range(1000):
        user = User(
            name=fake.name(),
            email=fake.unique.email(),
            age=random.randint(18, 70),
            country=fake.country()
        )
        users.append(user)
        db.add(user)
    db.commit()

    print("Seeding Products...")
    categories = ["Electronics", "Clothing", "Home", "Books", "Toys"]
    products = []
    for _ in range(200):
        product = Product(
            name=fake.catch_phrase(),
            category=random.choice(categories),
            price=round(random.uniform(10.0, 1000.0), 2)
        )
        products.append(product)
        db.add(product)
    db.commit()

    print("Seeding Orders, Payments, and OrderItems in batches...")
    statuses = ["completed", "pending", "cancelled"]
    payment_methods = ["credit_card", "paypal", "cash"]
    payment_statuses = ["success", "failed", "pending"]

    for i in range(1000):
        user = random.choice(users)
        order = Order(
            user_id=user.id,
            amount=0,
            status=random.choice(statuses)
        )
        
        # Add 1 to 5 random items using relationship
        total_amount = 0
        order_items = []
        for _ in range(random.randint(1, 5)):
            product = random.choice(products)
            quantity = random.randint(1, 4)
            total_amount += product.price * quantity
            order_items.append(OrderItem(product=product, quantity=quantity))
            
        order.items = order_items
        order.amount = total_amount

        # Add Payment using relationship
        order.payment = Payment(
            payment_method=random.choice(payment_methods),
            payment_status=random.choice(payment_statuses)
        )
        
        db.add(order)
        
        # Periodic commit every 200 orders to keep memory safe but speed high
        if (i + 1) % 200 == 0:
            db.commit()
            print(f"Committed {i + 1} orders...")
    db.close()
    print("Database seeding completed successfully.")

if __name__ == "__main__":
    seed_database()
