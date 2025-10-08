# Initialize empty sets
subscribers = set()
unsubscribers = set()

# Function to add an email
def add_email(email, set_name):
    set_name.add(email)
    print(f"\nEmail '{email}' added to {'subscribers' if set_name == subscribers else 'unsubscribers'}.")

# Function to remove an email
def remove_email(email, set_name):
    if email in set_name:
        set_name.remove(email)
        print(f"\nEmail '{email}' removed.")
    else:
        print(f"\nEmail '{email}' not found.")

# Function to display emails
def display_emails(set_name):
    print("Emails:")
    for email in set_name:
        print(f"{email}")

# Finding active subscribers
def find_active_subscribers(subscribers, unsubscribers):
    result = subscribers.difference(unsubscribers)
    print("Active Subscribers:")
    print(result)


add_email("user1@example.com", subscribers)
add_email("user8@example.com", unsubscribers)
add_email("user3@example.com", subscribers)
add_email("user10@example.com", subscribers)
add_email("user12@example.com", subscribers)
add_email("user12@example.com", unsubscribers)
print(subscribers)

remove_email("user1@example.com", subscribers)
remove_email("user2@example.com", subscribers)
remove_email("user3@example.com", subscribers)

# Displaying subscribers and unsubscribers
print("\nAll Subscribers:")
display_emails(subscribers)


print("\nAll Unsubscribers:")
display_emails(unsubscribers)


find_active_subscribers(subscribers, unsubscribers)
