#  SISTEMA DE GESTIÓN PARA Electronicos - VERSIÓN FINAL
# Proyecto Integrador Transversal
# Cursos: Fundamentos de Programación + Fundamentos de Gestión de Datos
import sqlite3
import datetime
import csv
import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
from menus import menu_gestor_productos, menu_responsable_compras, menu_administrador_ventas,menu_lider_integracion
from tienda import ElectronicosGestion, TiendaGestorDatabase
from dependencies.container import tienda
warnings.filterwarnings('ignore', category=DeprecationWarning)

# ============================================================================
# MENÚS POR ROL
# ============================================================================
def main():
    """Función principal - Instancia global compartida entre roles."""
    global sistema_elect

    sistema_elect = ElectronicosGestion(tienda)

    while True:
        print("\ SISTEMA DE GESTIÓN Electronicos")
        print("="*60)
        print("\n¿QUIÉN ERES?")
        print("="*60)
        print("1. Gestor de Productos")
        print("2. Responsable de Compras")
        print("3. Administrador de Ventas")
        print("4. Líder de Integración (VE TODO)")
        print("0. Salir")
        print("="*60)

        try:
            opcion = input("\nTu rol (0-4): ").strip()

            if opcion == "1":
                menu_gestor_productos(sistema_elect)
            elif opcion == "2":
                menu_responsable_compras(sistema_elect)
            elif opcion == "3":
                menu_administrador_ventas(sistema_elect)
            elif opcion == "4":
                menu_lider_integracion(sistema_elect)
            elif opcion == "0":
                print("¡Hasta luego! \n")
                break
            else:
                print("❌ Opción inválida")

        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! \n")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


# Ejecutar
if __name__ == "__main__":
    main()
