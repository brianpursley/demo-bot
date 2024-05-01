DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS manufacturer;
DROP TABLE IF EXISTS category;

CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE manufacturer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(100),
    state CHAR(2),
    zip CHAR(5),
    email VARCHAR(100),
    phone CHAR(10)
);

CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL REFERENCES category (id),
    manufacturer_id INTEGER NOT NULL REFERENCES manufacturer (id),
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL
);
CREATE INDEX idx_product_category_id ON product(category_id);
CREATE INDEX idx_product_manufacturer_id ON product(manufacturer_id);

INSERT INTO category (name) VALUES
('Writing Supplies'),
('Paper Products'),
('Office Furniture'),
('Technology'),
('Cleaning Supplies');

INSERT INTO manufacturer (name, address, city, state, zip, email, phone) VALUES
('PenCraft', '1234 Inkwell Ave', 'Scriptown', 'NY', '10001', 'manufacturer1@cinlogic.com', '2125550101'),
('PaperMills Inc.', '2345 Paper Route', 'Sheetville', 'CA', '90001', 'manufacturer2@cinlogic.com', '3105550102'),
('FurniWorks', '3456 Chair Pl', 'Tabletown', 'TX', '75001', 'manufacturer3@cinlogic.com', '2145550103'),
('TechGears', '4567 Circuit Rd', 'Gearville', 'MA', '02101', 'manufacturer4@cinlogic.com', '6175550104'),
('CleanUpNow', '5678 Scrub St', 'Soapcity', 'FL', '33101', 'manufacturer5@cinlogic.com', '3055550105');

INSERT INTO product (name, description, category_id, manufacturer_id, quantity, unit_price) VALUES
('Standard Ballpoint Pen', 'Our smooth-writing ballpoint pens come in various colors, perfect for office notes and memos. They are designed for comfort and long-lasting ink capacity. Great for daily use in any professional setting.', 1, 1, 100, 0.50),
('Smooth Gel Pen', 'Gel pens with quick-dry ink to prevent smears and smudges. Ideal for left-handed writers. The ergonomic grip offers supreme comfort for long writing sessions.', 1, 1, 150, 0.75),
('Mechanical Pencil', 'High-precision mechanical pencils with durable lead for fine, consistent lines. Includes an eraser tip for quick corrections. Perfect for architects and engineers.', 1, 1, 100, 1.25),
('Sticky Notes', 'Brightly colored sticky notes, 3x3 inches, in yellow, pink, and blue. Each pad contains 100 sheets. The adhesive back sticks firmly and removes cleanly.', 2, 2, 200, 1.99),
('Notepad', 'Eco-friendly notepads made from recycled paper. Each pad contains 50 sheets of lined paper, ideal for taking notes in meetings or organizing daily tasks.', 2, 2, 150, 2.50),
('Printer Paper', 'Standard 8.5x11 inch printer paper suitable for all office machines. Bright white, 20 lb, acid-free paper that resists fading and yellowing. Comes in a box of 500 sheets.', 2, 2, 300, 4.99),
('Executive Chair', 'Luxurious leather executive chairs with adjustable height, lumbar support, and tilt mechanism. Provides comfort and elegance to any office environment.', 3, 3, 40, 249.99),
('Ergonomic Keyboard', 'Ergonomic keyboards designed to reduce strain during long typing sessions. Features split keyboard layout, natural arc, and cushioned palm rest.', 4, 4, 30, 89.99),
('Monitor', '24-inch LED monitors with full HD resolution, providing vibrant color display and wide viewing angles. Ideal for designers and professionals who require precise color accuracy.', 4, 4, 40, 199.99),
('Webcam', 'High-definition webcams with 1080p resolution, perfect for video conferencing and online meetings. Features include autofocus and light correction.', 4, 4, 50, 79.99),
('Desk Organizer', 'Wooden desk organizers with multiple compartments to store your office essentials. Keep your stationery, notes, and gadgets neatly arranged and accessible.', 3, 3, 100, 19.99),
('Filing Cabinet', 'Metal filing cabinets with four drawers, designed for letter and legal size files. Each drawer is equipped with a lock for secure storage of confidential documents.', 3, 3, 50, 159.99),
('Highlighter', 'Pocket-sized highlighters in assorted fluorescent colors. Water-based ink resists smearing and is perfect for textbooks and detailed paperwork.', 1, 1, 200, 0.99),
('Envelopes', 'Premium quality white envelopes, perfect for business correspondence. Self-sealing design for quick and secure mailing. Available in standard letter size.', 2, 2, 300, 0.29),
('Binding Machine', 'Compact and efficient binding machines capable of binding up to 300 pages. Ideal for creating professional reports and presentations.', 4, 4, 25, 129.99),
('Whiteboard', 'Large, magnetic whiteboards designed for classroom and business presentations. Easy to clean and includes a marker tray and mounting hardware.', 3, 3, 20, 99.99),
('Projector', 'Portable projectors with HD resolution, suitable for both office presentations and home entertainment. Features include wireless connectivity and built-in speakers.', 4, 4, 15, 349.99),
('Desk Lamp', 'LED desk lamps with adjustable arms and brightness settings. Provides eye-friendly light, perfect for reading and computer work.', 3, 3, 100, 29.99),
('Toner Cartridge', 'High-capacity toner cartridges designed for high-volume printing. Compatible with various models of laser printers. Ensures sharp, professional-quality prints.', 4, 4, 70, 89.99),
('Correction Fluid', 'Fast-drying correction fluid, easy to apply with a brush applicator. Perfect for correcting typing and handwriting errors.', 1, 1, 150, 1.49),
('Fax Machine', 'Compact and reliable fax machines with high-speed transmission capabilities. Includes features like memory storage, speed dial, and automatic document feeder.', 4, 4, 25, 159.99),
('Paper Clips', 'Durable metal paper clips, rust-resistant and non-skid. Available in multiple sizes to hold papers securely without tearing.', 2, 2, 500, 0.99),
('Stamp Pad', 'High-quality stamp pads with long-lasting ink, suitable for office and classroom use. Non-toxic and available in various colors.', 1, 1, 120, 2.99),
('Trash Bin', 'Durable polyethylene trash bins, designed for office use. Lightweight, easy to clean, and comes in several colors to match any office decor.', 5, 5, 100, 14.99),
('Cleaning Wipes', 'Pre-moistened cleaning wipes, effective for sanitizing and cleaning non-porous surfaces. Kills germs and removes stains.', 5, 5, 200, 6.49),
('Multipurpose Cleaner', 'Eco-friendly multipurpose cleaner, safe for all surfaces. Cuts through grease, grime, and dirt, leaving a fresh scent.', 5, 5, 150, 4.99),
('Air Purifier', 'Compact air purifiers with HEPA filters, ideal for maintaining a clean office environment. Reduces allergens, smoke, and dust.', 5, 5, 40, 129.99),
('Conference Table', 'Modern conference tables with built-in charging stations and data ports. Seats up to 10 people comfortably.', 3, 3, 10, 499.99),
('Bulletin Board', 'Cork bulletin boards framed in aluminum, perfect for posting notices, flyers, and photos. Includes mounting hardware.', 3, 3, 50, 19.99),
('Mouse Pad', 'Ergonomic mouse pads with wrist support to enhance comfort during prolonged computer use. Non-slip base and smooth surface.', 4, 4, 200, 12.99),
('Scanner', 'High-speed document scanners with double-sided scanning capability. Connects via USB or Wi-Fi for flexible office setups.', 4, 4, 20, 299.99);
