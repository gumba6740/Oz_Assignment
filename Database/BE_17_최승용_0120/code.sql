CREATE TABLE customers(
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    address TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE pets(
	pet_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    pet_name VARCHAR(50),
    species VARCHAR(50) NOT NULL,    
    breed VARCHAR(50),
    birth_year YEAR NOT NULL,
    weight DECIMAL(5, 2),
    notes TEXT,
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);

CREATE TABLE rooms(
	room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_number INT NOT NULL UNIQUE,
    room_type VARCHAR(20) NOT NULL,
    price_per_night DECIMAL(20, 2)
);
 
CREATE TABLE reservation(
	reservation_id INT PRIMARY KEY AUTO_INCREMENT,
    pet_id INT,
    room_id INT,
    checkin_date DATE NOT NULL,
    checkout_date DATE NOT NULL,
    room_total_price DECIMAL(20, 2) NOT NULL,
    reserv_status ENUM('pending', 'confirmed', 'checkin', 'checkout', 'delay', 'cancel', 'noshow'),
    FOREIGN KEY (pet_id) REFERENCES pets(pet_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id),
	CHECK (checkin_date < checkout_date)
);


CREATE TABLE service_menu(
	service_id INT PRIMARY KEY AUTO_INCREMENT,
    service_name VARCHAR(50) NOT NULL,
    description TEXT,
    price_per_use DECIMAL(20, 2) NOT NULL
);


CREATE TABLE reservation_service(
	rs_id INT PRIMARY KEY AUTO_INCREMENT,
    reservation_id INT,
    service_id INT,
    quantity INT NOT NULL,
    price_per_use DECIMAL(20, 2) NOT NULL,
    FOREIGN KEY (reservation_id) REFERENCES reservation(reservation_id),
    FOREIGN KEY (service_id) REFERENCES service_menu(service_id)
);

CREATE TABLE payment(
	payment_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    reservation_id INT,
    total_amount DECIMAL(20, 2) NOT NULL,
    paid_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50) NOT NULL,
    payment_status ENUM('ready', 'paid', 'canceled', 'failed', 'refunded'),
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (reservation_id) REFERENCES reservation(reservation_id)
);