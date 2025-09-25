import re
import random
import string

# ------------------ Validation Functions ------------------ #
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    pattern = r'^\d{10}$'
    return re.match(pattern, phone) is not None

def is_valid_aadhaar(aadhaar):
    return aadhaar.isdigit() and len(aadhaar) == 12

# ------------------ Booking ID Generator ------------------ #
def generate_booking_id(length=6):
    return 'TKT-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# ------------------ Ticket Generation ------------------ #
def generate_ticket_text(name, age, aadhaar, num_people, email, phone, booking_id, seat_number):
    return f"""
🎫===== ONLINE TICKET =====🎫
Booking ID: {booking_id}
Seat Number: {seat_number}
Name: {name}
Age: {age}
Aadhaar: {aadhaar}
People accompanying: {num_people}
Email: {email}
Phone: {phone}
============================
"""

# ------------------ Main Program ------------------ #
def main():
    print("🎫 Welcome to the Online Ticket Booking System 🎫")
    
    try:
        total_tickets = int(input("How many tickets do you want to book? "))
        if total_tickets < 1:
            print("❌ Number of tickets must be at least 1.")
            return
    except ValueError:
        print("❌ Invalid input. Must be a number.")
        return
    
    booked_tickets = []
    
    for i in range(1, total_tickets + 1):
        print(f"\n--- Ticket {i} ---")
        name = input("Enter full name: ").strip()
        
        # Age validation
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("❌ Invalid age! Skipping this ticket.")
            continue
        
        # Aadhaar validation
        aadhaar = input("Enter Aadhaar number: ").strip()
        if not is_valid_aadhaar(aadhaar):
            print("❌ Invalid Aadhaar! Must be 12 digits. Skipping this ticket.")
            continue
        
        # Number of accompanying people
        try:
            num_people = int(input("Number of accompanying people: "))
        except ValueError:
            print("❌ Invalid number! Skipping this ticket.")
            continue
        
        # Email validation
        email = input("Enter email: ").strip()
        if not is_valid_email(email):
            print("❌ Invalid email format! Skipping this ticket.")
            continue
        
        # Phone validation
        phone = input("Enter phone number: ").strip()
        if not is_valid_phone(phone):
            print("❌ Invalid phone number! Skipping this ticket.")
            continue
        
        # Generate booking details
        booking_id = generate_booking_id()
        seat_number = f"{random.randint(1,50)}{random.choice(string.ascii_uppercase)}"
        ticket_text = generate_ticket_text(name, age, aadhaar, num_people, email, phone, booking_id, seat_number)
        
        # Display ticket along with confirmation
        print(f"✅ Booking confirmed! Ticket sent to {email} (simulated).")
        print(ticket_text)
        
        # Save ticket info in memory
        booked_tickets.append(ticket_text)
    
    # Save all tickets to a file with UTF-8 encoding
    if booked_tickets:
        with open("all_tickets.txt", "w", encoding="utf-8") as f:
            for t in booked_tickets:
                f.write(t + "\n")
        print(f"\n💾 All tickets saved to all_tickets.txt")

if __name__ == "__main__":
    main()
