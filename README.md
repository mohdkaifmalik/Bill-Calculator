# Bill Calculator - Catalogue and Discount

## Overview
This project implements a simple catalog and discount calculator in Python, designed to handle the purchase of three products: Product A, Product B, and Product C. The program prompts the user to enter the quantity of each product and whether they want the items to be wrapped as a gift. Based on the provided input, the program calculates the subtotal, applies various discount rules, and computes additional fees, such as gift wrapping and shipping costs.

## Catalog Information
The catalog consists of the following products with their respective prices:
- Product A: $20
- Product B: $40
- Product C: $50

## Discount Rules
The program applies the following discount rules:
1. **Flat $10 Discount**: If the total cart value exceeds $200, a flat $10 discount is applied.
2. **Bulk 5% Discount**: If the quantity of any single product exceeds 10 units, a 5% discount is applied to that item's total price.
3. **Bulk 10% Discount**: If the total quantity exceeds 20 units, a 10% discount is applied to the entire cart.
4. **Tiered 50% Discount**: If the total quantity exceeds 30 units and any single product quantity is greater than 15, a 50% discount is applied to products with quantities above 15.

Note: Only one discount rule can be applied per purchase. If multiple discounts are applicable, the program calculates the discount amount for each rule and applies the most beneficial one for the customer.

## Fees
- **Gift Wrap Fee**: $1 per unit.
- **Shipping Fee**: 10 units can be packed in one package, and the shipping fee for each package is $5.

## Usage
1. Clone the repository: `git clone https://github.com/your-username/Bill-Calculator.git`
2. Navigate to the project directory: `cd Bill-Calculator`
3. Run the program: `python main.py`
4. Follow the prompts to enter the quantity of each product and specify if you want the items wrapped as a gift.
5. View the detailed bill, including product details, subtotal, discounts, fees, and the grand total.

## Technologies Used
The project is implemented in Python, adhering to the specifications outlined in the task. No external frameworks or libraries are used, and the program provides a command-line interface for user interaction.

## Disclaimer
This project is a solution to a coding task and is intentionally kept simple. It does not aim to create a full-fledged application and is limited to the specific requirements provided in the task description (as mentioned above).

**Note:** AI-generated code was not used in the development of this project to comply with the task requirements.
