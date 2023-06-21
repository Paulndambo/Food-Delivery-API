GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
)

TABLE_STATUS_CHOICES = (
    ("booked", "Booked"),
    ("available", "Available"),
)

BOOKING_STATUS_CHOICES = (
    ("active", "Active"),
    ("cancelled", "Cancelled"),
    ("fullfilled", "Full Filled"),
)

PAYMENT_STATUS_CHOICES = (
    ("pending", "Pending"),
    ("complete", "Complete"),
    ("failed", "Failed"),
)

ORDER_STATUS = (
    ("processing", "Processing"),
    ("cancelled", "Cancelled"),
    ("in_transit", "In Transit"),
    ("delivered", "Delivered"),
)