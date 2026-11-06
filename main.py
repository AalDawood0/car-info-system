# Car Info System - By Marwan Ahmed Fermawy
# Autotronics Student - Ashmun, Menoufia

print("Welcome to Car Info System")
print("By Marwan - Delta Tech")
print("----------------------------------------")

car = input("Enter car type (toyota, bmw, mercedes): ").lower()

cars_info = {
    "toyota": "Japanese - High Reliability - 1600cc",
    "bmw": "German - Sport Performance - Turbo Engine",
    "mercedes": "German - Luxury - Advanced Tech",
    "hyundai": "Korean - Economic - Low maintenance"
}

if car in cars_info:
    print(f"Info about {car}: {cars_info[car]}")
else:
    print(f"{car} not in database yet, will add soon!")

print("Developed in Ashmun, Menoufia")