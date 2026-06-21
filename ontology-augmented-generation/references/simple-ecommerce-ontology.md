# Simple E-Commerce Domain Ontology Example (for prompt injection)

Use this as a template for creating your own task-specific ontologies. This is intentionally minimal and illustrative.

## Classes
- **Product**
  - Properties: sku (string, unique), name (string), price (decimal > 0), category (enum: electronics, clothing, books, home), inStock (boolean), description (string, optional)
- **Customer**
  - Properties: customerId (string, unique), name (string), email (string), tier (enum: bronze, silver, gold, platinum), signupDate (date)
- **Order**
  - Properties: orderId (string, unique), orderDate (date), status (enum: pending, processing, shipped, delivered, cancelled, refunded), totalAmount (decimal)
- **OrderItem** (line item)
  - Properties: quantity (integer >= 1), unitPrice (decimal)

## Relations / Object Properties
- **places** (Customer → Order) : cardinality 1:*
- **contains** (Order → OrderItem) : 1:*
- **refersToProduct** (OrderItem → Product) : exactly 1
- **owns** (Customer → Product) via purchases (derived or via orders)

## Data Properties & Constraints (Axioms)
- Product.price must be > 0
- Order.status must be one of the enumerated values
- Order.totalAmount == sum over its OrderItems of (quantity * unitPrice)
- A Customer can place multiple Orders but each Order belongs to exactly one Customer
- Product.inStock is true only if current inventory > 0 (in real system this would be computed)

## Example Instance Data (for few-shot grounding)
```
Product SKU-42:
  name: "Wireless Headphones Pro"
  price: 129.99
  category: electronics
  inStock: true

Customer CUST-1001:
  name: "Alex Rivera"
  tier: gold

Order ORD-98765:
  orderDate: 2025-06-18
  status: shipped
  totalAmount: 389.97
  contains:
    - OrderItem: qty=3, unitPrice=129.99, refersToProduct=SKU-42
```

## Compact Serialization for Prompt (copy-paste ready)

```
## E-Commerce Ontology (minimal task-relevant subset)

Classes:
- Product (sku, name, price>0, category in {electronics,clothing,books,home}, inStock)
- Customer (customerId, name, email, tier in {bronze,silver,gold,platinum})
- Order (orderId, orderDate, status in {pending,processing,shipped,delivered,cancelled,refunded}, totalAmount)
- OrderItem (quantity>=1, unitPrice)

Relations:
- places: Customer -> Order (1:*)
- contains: Order -> OrderItem (1:*)
- refersToProduct: OrderItem -> Product (exactly 1)

Key Constraints:
- Order.totalAmount must equal sum(quantity * unitPrice) over its items
- Only Products with inStock=true can be ordered
- Order status transitions follow: pending → processing → shipped → delivered (or cancelled/refunded at certain points)

Example grounded fact:
Order ORD-98765 placed by Customer CUST-1001 contains 3x Product SKU-42 (Wireless Headphones Pro) and has status=shipped.
```

## Usage Notes
- When using in a prompt, include the compact version + 1-2 specific instances relevant to the current query.
- For verification prompts, also include the full constraint list.
- Extend this ontology with real attributes and new classes (e.g., Inventory, Promotion, Return) as needed for your use case.
