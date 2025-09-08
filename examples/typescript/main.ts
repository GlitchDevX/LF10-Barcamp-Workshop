abstract class Item {
    abstract getDiscountedPrice(): number;
    abstract exportData(): any; // we don't know the exact return type
}

class Book extends Item {
    constructor(public title: string, public price: number) { super(); }

    getDiscountedPrice() {
        return this.price * 0.85;
    }

    exportData() {
        return { "title": this.title, "price": this.price };
    }
}

class Food extends Item {
    constructor(public name: string, public expiryDate: Date, public price: number) { super(); }

    getDiscountedPrice() {
        return this.price;
    }

    exportData() {
        return { "name": this.name, "expiry_date": this.expiryDate.toISOString(), "price": this.price };
    }
}

class Electronics extends Item {
    constructor(public brand: string, public price: number) { super(); }

    getDiscountedPrice() {
        return this.price * 0.90;
    }

    exportData() {
        return { "brand": this.brand, "price": this.price };
    }
}

const items: Item[] = [
    new Book("Harry Potter", 20),
    new Food("Milk", new Date(), 1.45),
    new Electronics("Samsung", 150)
];

console.log("===DISCOUNTED PRICES===");
for (let item of items) {
    let discountedPrice = item.getDiscountedPrice();
    console.log(`discounted price: ${discountedPrice}`);
}

console.log("===PRODUCTS EXPORT===");
for (let item of items) {
    console.log(item.exportData());
}