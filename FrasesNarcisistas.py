import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

adjetivos_fuertes = [
    "absolutamente perfecto", "indiscutiblemente talentoso", "deslumbrantemente brillante", "magistral",
    "único en todos los sentidos", "extraordinariamente atractivo", "sobresalientemente inteligente",
    "increíblemente poderoso", "irresistiblemente magnético", "profundamente carismático"
]

adjetivos_suaves = [
    "increíble", "asombroso", "brillante", "espectacular", "excepcional", "notable", "sorprendente",
    "maravilloso", "encantador", "fantástico", "único", "excepcional", "genial", "estupendo"
]

acciones = [
    "Soy la perfección misma", "Domino cualquier situación", "Inspiró a los demás", "Soy un genio creativo",
    "Siempre gano", "Soy imparable", "Logro todo lo que me propongo", "Nunca cometo errores", "Soy irresistible",
    "No hay nadie como yo", "El mundo gira a mi alrededor", "Mi presencia lo cambia todo",
    "Todos me admiran", "Mi inteligencia es superior", "Mi belleza es incomparable", "Soy un líder nato",
    "Todos desean estar a mi lado", "Tengo un magnetismo innegable", "Mi energía es contagiosa",
    "Mi espíritu es inquebrantable", "Soy un ejemplo a seguir", "Mi carisma es único", "Soy una fuerza de la naturaleza",
    "Mi determinación es inspiradora", "Mi empatía es sobresaliente", "Mi valentía es inigualable",
    "Mi creatividad no tiene límites", "Mi visión es extraordinaria", "Mi compasión es excepcional",
    "Mi carácter es impecable", "Mi compromiso es inquebrantable", "Mi sabiduría es inmensurable",
    "Mi honestidad es transparente", "Mi intuición es asombrosa", "Mi pasión es contagiosa", "Mi firmeza es inamovible",
    "Mi tenacidad es legendaria", "Mi alegría es contundente", "Mi humildad es auténtica", "Mi amabilidad es infinita",
    "Mi determinación es inflexible", "Mi optimismo es incansable", "Mi valentía es imponente",
    "Mi integridad es insuperable", "Mi audacia es incomparable", "Mi resiliencia es invencible",
    "Mi generosidad es inigualable", "Mi astucia es indiscutible", "Mi gracia es inimitable",
    "Mi tenacidad es inquebrantable", "Mi entusiasmo es inigualable", "Mi resistencia es incomparable",
    "Mi bondad es indestructible", "Mi empatía es inigualable", "Mi espíritu es inigualable",
    "Mi autenticidad es inigualable", "Mi vitalidad es inigualable", "Mi sinceridad es inquebrantable",
    "Mi motivación es inigualable", "Mi imaginación es incomparable", "Mi vitalidad es inigualable",
    "Mi capacidad es inigualable", "Mi determinación es incansable", "Mi valentía es inquebrantable",
    "Mi resiliencia es inigualable", "Mi gratitud es inagotable", "Mi perseverancia es inquebrantable",
    "Mi optimismo es inigualable", "Mi entusiasmo es inquebrantable", "Mi inspiración es incomparable",
    "Mi comprensión es inagotable", "Mi benevolencia es incomparable", "Mi integridad es inigualable",
    "Mi compasión es inquebrantable", "Mi coraje es inigualable", "Mi confianza es inquebrantable",
    "Mi lealtad es incomparable", "Mi disciplina es inagotable", "Mi gracia es inigualable",
    "Mi creatividad es inquebrantable", "Mi humildad es incomparable", "Mi sabiduría es inagotable",
    "Mi generosidad es inquebrantable", "Mi amabilidad es incomparable", "Mi dedicación es inagotable",
    "Mi paciencia es inquebrantable", "Mi flexibilidad es incomparable", "Mi respeto es inagotable",
    "Mi adaptabilidad es inquebrantable", "Mi perseverancia es incomparable", "Mi perseverancia es inagotable",
    "Mi comprensión es inquebrantable", "Mi disciplina es incomparable", "Mi integridad es inquebrantable",
    "Mi compasión es incomparable", "Mi coraje es inquebrantable", "Mi confianza es inquebrantable",
    "Mi lealtad es inquebrantable", "Mi gracia es incomparable", "Mi creatividad es incomparable",
    "Mi humildad es inquebrantable", "Mi sabiduría es incomparable", "Mi generosidad es incomparable",
    "Mi amabilidad es inquebrantable", "Mi dedicación es incomparable", "Mi paciencia es incomparable",
    "Mi flexibilidad es inquebrantable", "Mi adaptabilidad es incomparable", "Mi respeto es incomparable",
    "Mi determinación es inquebrantable", "Mi coraje es indomable", "Mi comprensión es incomparable",
    "Mi disciplina es inagotable", "Mi generosidad es ilimitada", "Mi empatía es inquebrantable",
    "Mi integridad es inquebrantable", "Mi lealtad es inquebrantable", "Mi carisma es irresistible",
    "Mi influencia es impactante", "Mi humildad es genuina", "Mi paciencia es infinita",
    "Mi intuición es infalible", "Mi astucia es inigualable", "Mi resiliencia es innegable",
    "Mi alegría es contagiosa", "Mi gratitud es profunda", "Mi creatividad es inigualable",
    "Mi resistencia es asombrosa", "Mi ambición es impresionante", "Mi dedicación es incansable",
    "Mi tolerancia es infinita", "Mi sinceridad es inquebrantable", "Mi sabiduría es eterna",
    "Mi optimismo es imparable", "Mi valentía es insuperable", "Mi esfuerzo es inconmensurable",
    "Mi firmeza es inquebrantable", "Mi compasión es inagotable", "Mi confianza es inquebrantable",
    "Mi pasión es apasionante", "Mi vitalidad es inagotable", "Mi curiosidad es insaciable",
    "Mi empatía es inquebrantable", "Mi amabilidad es inigualable", "Mi espíritu es indomable",
    "Mi voluntad es inquebrantable", "Mi disposición es inagotable", "Mi flexibilidad es inigualable",
    "Mi amor es infinito", "Mi benevolencia es inagotable", "Mi ética es incuestionable",
    "Mi modestia es innata", "Mi liderazgo es innegable", "Mi perspectiva es insuperable",
    "Mi enfoque es infalible", "Mi enfoque es inquebrantable", "Mi presencia es inigualable",
    "Mi magnetismo es innato", "Mi magnetismo es innegable", "Mi determinación es insuperable",
    "Mi valentía es inquebrantable", "Mi entusiasmo es inquebrantable", "Mi resistencia es inquebrantable",
    "Mi fuerza es innegable", "Mi generosidad es insuperable", "Mi sabiduría es insuperable",
    "Mi empatía es inagotable", "Mi fuerza es inquebrantable", "Mi ética es inquebrantable",
    "Mi optimismo es inquebrantable", "Mi humildad es insuperable", "Mi capacidad es inigualable",
    "Mi capacidad es inquebrantable", "Mi determinación es inagotable", "Mi integridad es insuperable",
    "Mi carácter es inquebrantable", "Mi influencia es innegable", "Mi comprensión es insuperable",
    "Mi fortaleza es inagotable", "Mi compasión es inagotable", "Mi gratitud es inquebrantable",
    "Mi sinceridad es insuperable", "Mi intuición es inagotable", "Mi resiliencia es inquebrantable",
    "Mi lealtad es inagotable", "Mi liderazgo es insuperable", "Mi generosidad es inquebrantable",
    "Mi pasión es inquebrantable", "Mi flexibilidad es insuperable", "Mi empatía es insuperable",
    "Mi carisma es inagotable", "Mi gratitud es insuperable", "Mi humildad es inquebrantable",
    "Mi sabiduría es inquebrantable", "Mi confianza es insuperable", "Mi paciencia es inagotable",
    "Mi tolerancia es inquebrantable", "Mi creatividad es insuperable", "Mi optimismo es insuperable",
    "Mi ambición es inagotable", "Mi resistencia es insuperable", "Mi determinación es inquebrantable",
    "Mi fuerza es inagotable", "Mi perseverancia es insuperable", "Mi resiliencia es insuperable",
    "Mi integridad es inagotable", "Mi liderazgo es inquebrantable", "Mi ética es insuperable",
    "Mi generosidad es inagotable", "Mi pasión es insuperable", "Mi humildad es inagotable",
    "Mi sabiduría es insuperable", "Mi carisma es inquebrantable", "Mi confianza es inagotable",
    "Mi creatividad es inagotable", "Mi gratitud es inagotable", "Mi paciencia es inquebrantable",
    "Mi optimismo es inagotable", "Mi valentía es inagotable", "Mi resiliencia es inagotable",
    "Mi determinación es insuperable", "Mi empatía es inquebrantable", "Mi bondad es inagotable",
    "Mi lealtad es insuperable", "Mi liderazgo es inagotable", "Mi empatía es insuperable",
    "Mi perseverancia es inquebrantable", "Mi compasión es insuperable", "Mi compromiso es inagotable",
    "Mi fortaleza es inquebrantable", "Mi integridad es inigualable", "Mi sabiduría es insuperable",
    "Mi generosidad es inagotable", "Mi compromiso es inquebrantable", "Mi paciencia es inagotable",
    "Mi comprensión es insuperable", "Mi tolerancia es inagotable", "Mi gratitud es inquebrantable",
    "Mi liderazgo es inigualable", "Mi determinación es inagotable", "Mi resiliencia es insuperable",
    "Mi comprensión es inagotable", "Mi empatía es inagotable", "Mi disciplina es inagotable",
    "Mi compasión es inagotable", "Mi ética es inagotable", "Mi gratitud es insuperable",
    "Mi sinceridad es inquebrantable", "Mi perseverancia es insuperable", "Mi sabiduría es inagotable",
    "Mi generosidad es inigualable", "Mi creatividad es inagotable", "Mi comprensión es inagotable",
    "Mi flexibilidad es inagotable", "Mi adaptabilidad es inigualable", "Mi adaptabilidad es inagotable",
    "Mi respeto es inagotable", "Mi empatía es inagotable", "Mi perseverancia es inagotable",
    "Mi comprensión es inagotable", "Mi disciplina es inagotable", "Mi compasión es inagotable",
    "Mi coraje es inquebrantable", "Mi confianza es inagotable", "Mi lealtad es inquebrantable",
    "Mi humildad es inagotable", "Mi creatividad es inagotable", "Mi sabiduría es inagotable",
    "Mi generosidad es inagotable", "Mi bondad es inagotable", "Mi paciencia es inagotable",
    "Mi compasión es inagotable", "Mi flexibilidad es inagotable", "Mi respeto es inagotable",
    "Mi adaptabilidad es inagotable", "Mi perseverancia es inagotable", "Mi adaptabilidad es inagotable",
    "Mi respeto es inagotable", "Mi empatía es inagotable", "Mi perseverancia es inagotable",
    "Mi comprensión es inagotable", "Mi disciplina es inagotable", "Mi compasión es inagotable",
    "Mi coraje es inquebrantable", "Mi confianza es inagotable", "Mi lealtad es inquebrantable",
    "Mi humildad es inagotable", "Mi creatividad es inagotable", "Mi sabiduría es inagotable",
    "Mi generosidad es inagotable", "Mi bondad es inagotable", "Mi paciencia es inagotable",
    "Mi compasión es inagotable", "Mi flexibilidad es inagotable", "Mi respeto es inagotable",
    "Mi adaptabilidad es inagotable", "Mi perseverancia es inagotable", "Mi adaptabilidad es inagotable",
    "Mi perseverancia es incomparable", "Mi comprensión es incomparable", "Mi disciplina es inquebrantable"
]

def print_text_with_animation(text, color=Fore.WHITE, delay=0.05):
    for char in text:
        print(f"{color}{char}", end='', flush=True)
        time.sleep(delay)
    print()

warning_message = f"¡Advertencia! Recuerda que esto es bajo fines educativos,No intentes dañar a la gente."

print_text_with_animation(warning_message, Fore.RED)
time.sleep(1)

print_text_with_animation("\nOpciones disponibles:", Fore.YELLOW)
print_text_with_animation("1. Frase Fuerte", Fore.YELLOW)
print_text_with_animation("2. Frase Suave\n", Fore.GREEN)

while True:
    opcion_elegida = input(f"{Fore.CYAN}Elige una opción (1 o 2), o cualquier otro número para salir: ")

    if opcion_elegida == '1':
        frase_fuerte = f"Soy {random.choice(adjetivos_fuertes)} y {random.choice(acciones)}"
        print(f"{Fore.YELLOW}{frase_fuerte}")
        input("Presiona Enter para continuar...")
    elif opcion_elegida == '2':
        frase_suave = f"Soy {random.choice(adjetivos_suaves)} y {random.choice(acciones)}"
        print(f"{Fore.GREEN}{frase_suave}")
        input("Presiona Enter para continuar...")
    else:
        print(f"{Fore.GREEN}¡Gracias por usar el Generador de Frases Narcisistas!")
        break