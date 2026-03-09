
categories = input("Выберите категорию: ").lower().strip()

match categories:
    case "напиток":
        print("чай, кофе, сок")
    case "суп":
        print("борщ, щи, суп-пюре")
    case "десерт":
        print("торт, мороженое, фрукты")

bludo = input("Выберите блюдо: ")

match bludo:
    case 'чай':
        print(20)
    case 'кофе':
        print(30)
    case 'сок':
        print(15)
    case 'борщ':
        print(20)
    case 'щи':
        print("30")
    case 'суп-пюре':
        print(15)
    case 'торт':
        print(20)
    case 'мороженое':
        print(30)
    case 'фрукты':
        print(15)
